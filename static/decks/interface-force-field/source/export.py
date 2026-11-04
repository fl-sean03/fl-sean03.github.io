#!/usr/bin/env python3
"""Export native editable slides to a selectable-text PDF with clean metadata."""
import argparse
import hashlib
from pathlib import Path
import shutil
import subprocess

import pymupdf
from pptx import Presentation

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work-dir', type=Path, required=True, help='Private local export directory')
    args = parser.parse_args()
    work = args.work_dir.resolve()
    work.mkdir(parents=True,exist_ok=True)
    original = work/'iff-visual-showcase.pdf'
    if original.exists():
        raise ValueError('Use a new work directory; an earlier PDF export is already present.')
    presentation = BUNDLE/'downloads/iff-visual-showcase.pptx'
    expected_pages = len(Presentation(presentation).slides)
    source_hash = hashlib.sha256(presentation.read_bytes()).digest()
    subprocess.run(['libreoffice','-env:UserInstallation='+ (work/'lo-profile').as_uri(),
                    '--headless','--convert-to','pdf','--outdir',str(work),str(presentation)],check=True)
    document = pymupdf.open(original)
    producer = document.metadata.get('producer','')
    document.del_xml_metadata()
    document.set_metadata({'title':'Interface Force Field','author':'Sean Florez',
                           'subject':'From atoms to material predictions and evidence',
                           'creator':'','keywords':'',
                           'producer':producer if 'LibreOffice' in producer else ''})
    destination = BUNDLE/'downloads/iff-visual-showcase.pdf'
    candidate = work/'checked.pdf'
    document.save(candidate,garbage=4,deflate=True)
    with pymupdf.open(candidate) as checked:
        assert len(checked) == expected_pages and all(page.get_text().strip() for page in checked)
    if hashlib.sha256(presentation.read_bytes()).digest() != source_hash:
        raise ValueError('PowerPoint changed during export; rebuild into a new work directory.')
    temporary = destination.with_suffix('.new.pdf')
    shutil.copyfile(candidate,temporary)
    temporary.replace(destination)
    print(f'Exported {len(document)} selectable-text PDF pages. Author Sean Florez; creator empty.')


if __name__=='__main__':
    main()
