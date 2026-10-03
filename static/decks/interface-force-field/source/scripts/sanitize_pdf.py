"""Remove PDF multimedia and attachments, including non-page references."""
from pathlib import Path
import re
import sys

import pymupdf as fitz

ROOT = Path(__file__).resolve().parents[1]
MEDIA_SUBTYPES = {"/Screen", "/RichMedia", "/Movie", "/Sound", "/FileAttachment"}
MEDIA_TYPES = {"/EmbeddedFile", "/Rendition", "/MediaClip"}
MEDIA_ACTIONS = {"/Rendition", "/Movie", "/Sound", "/RichMediaExecute", "/GoToE"}
PDF_TOKENS = re.compile(
    r"\s+|%[^\r\n]*|<<|>>|\[|\]|[+-]?(?:\d+\.\d*|\.\d+|\d+)|[^\s()<>\[\]{}/%]+|/[^\s()<>\[\]{}/%]*"
)


def object_tokens(text):
    """Locate syntax tokens without interpreting strings or hexadecimal data."""
    tokens = []
    pos = 0
    while pos < len(text):
        if text[pos] == "(":
            pos += 1
            depth = 1
            while pos < len(text) and depth:
                char = text[pos]
                if char == "\\":
                    pos += 2
                    continue
                if char == "(":
                    depth += 1
                elif char == ")":
                    depth -= 1
                pos += 1
            tokens.append(("string", -1, -1))
            continue
        if text[pos] == "<" and not text.startswith("<<", pos):
            end = text.find(">", pos + 1)
            pos = len(text) if end < 0 else end + 1
            tokens.append(("string", -1, -1))
            continue
        match = PDF_TOKENS.match(text, pos)
        if not match:
            pos += 1
            continue
        value = match.group()
        if not value.isspace() and not value.startswith("%"):
            tokens.append((value, match.start(), match.end()))
        pos = match.end()
    return tokens


def remove_references(text, removed):
    tokens = object_tokens(text)
    spans = []
    for index in range(len(tokens) - 2):
        a, b, c = tokens[index:index + 3]
        if a[0].isdigit() and b[0].isdigit() and c[0] == "R" and int(a[0]) in removed:
            spans.append((a[1], c[2]))
    for start, end in reversed(spans):
        text = text[:start] + "null" + text[end:]
    return text


def key_value(document, xref, name):
    try:
        return document.xref_get_key(xref, name)[1]
    except (ValueError, RuntimeError):
        return "null"


def scrub(document):
    """Scrub the entire object graph, including structure-tree annotation links."""
    removed_annotations = 0
    for page in document:
        for annotation in list(page.annots() or []):
            subtype = key_value(document, annotation.xref, "Subtype")
            if subtype in MEDIA_SUBTYPES:
                page.delete_annot(annotation)
                removed_annotations += 1
    attachment_names = list(document.embfile_names())
    for name in attachment_names:
        document.embfile_del(name)

    blocked = set()
    for xref in range(1, document.xref_length()):
        subtype = key_value(document, xref, "Subtype")
        obj_type = key_value(document, xref, "Type")
        action = key_value(document, xref, "S")
        embedded = key_value(document, xref, "EF")
        if subtype in MEDIA_SUBTYPES or obj_type in MEDIA_TYPES or action in MEDIA_ACTIONS:
            blocked.add(xref)
        elif obj_type == "/Filespec" and embedded != "null":
            blocked.add(xref)

    # An OBJR can retain an annotation after its page Annots entry is removed.
    for xref in range(1, document.xref_length()):
        if key_value(document, xref, "Type") != "/OBJR":
            continue
        obj = key_value(document, xref, "Obj")
        if re.fullmatch(r"\d+\s+\d+\s+R", obj) and int(obj.split()[0]) in blocked:
            blocked.add(xref)

    rewritten = 0
    for xref in range(1, document.xref_length()):
        if xref in blocked:
            document.update_object(xref, "null")
            continue
        text = document.xref_object(xref, compressed=False)
        cleaned = remove_references(text, blocked)
        if cleaned != text:
            document.update_object(xref, cleaned)
            rewritten += 1
        # Associated files can also appear outside the embedded-file name tree.
        if key_value(document, xref, "AF") != "null":
            document.xref_set_key(xref, "AF", "null")

    metadata = document.metadata
    metadata.update({
        "title": "Interface Force Field: From atoms to evidence",
        "author": "Sean Florez", "creator": "", "keywords": "IFF, molecular mechanics, calibration, validation",
        "subject": "Interface Force Field and the experimental evidence workflow",
    })
    document.set_metadata(metadata)
    document.del_xml_metadata()
    return {"page_annotations_removed": removed_annotations,
            "embedded_files_removed": len(attachment_names),
            "media_objects_removed": len(blocked), "objects_rewritten": rewritten}


def check_static(document):
    if document.embfile_names():
        raise ValueError("PDF still contains embedded files")
    for xref in range(1, document.xref_length()):
        if (key_value(document, xref, "Subtype") in MEDIA_SUBTYPES
                or key_value(document, xref, "Type") in MEDIA_TYPES
                or key_value(document, xref, "S") in MEDIA_ACTIONS
                or key_value(document, xref, "EF") != "null"):
            raise ValueError("PDF still contains a media or attachment object")


def sanitize(path):
    with fitz.open(path) as document:
        stats = scrub(document)
        temporary = path.with_suffix(".static.pdf")
        document.save(temporary, garbage=4, deflate=True, clean=True)
    try:
        with fitz.open(temporary) as document:
            check_static(document)
        temporary.replace(path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    print(path.name, stats)


if __name__ == "__main__":
    files = sys.argv[1:] or ["build/iff-visual-showcase.pdf"]
    for filename in files:
        path = Path(filename)
        sanitize(path if path.is_absolute() else ROOT / path)
