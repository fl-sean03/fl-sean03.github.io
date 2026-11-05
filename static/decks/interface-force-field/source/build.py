#!/usr/bin/env python3
"""Build the slide story as a self-contained HTML viewer, an editable PowerPoint and presenter notes."""
import argparse
import base64
import html
import json
import mimetypes
import re
import zipfile
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from fontTools.ttLib import TTFont
from lxml import etree as ET
from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from style import ACCENT, BODY, INK, MUTED, TEAL

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
W, H = 1920, 1080
LEFT, WIDTH = 96, 1728  # the content column
LH = 1.28  # line height in font sizes
PROSE_X = 780  # where a figure slide's words start, right of its title


@lru_cache(maxsize=None)
def font_for(size, bold):
    return ImageFont.truetype(str(HERE / 'fonts' / ('Lato-Bold.ttf' if bold else 'Lato-Regular.ttf')), size)


def measure(value, size, bold=False, spacing=0):
    """Width in slide pixels; spacing is CSS letter-spacing in em, which follows every character."""
    return font_for(size, bold).getlength(value) + spacing * size * len(value)


def wrapped(value, width, size, bold=False):
    font = font_for(size, bold)
    lines, line = [], ''
    for word in value.split():
        candidate = f'{line} {word}'.strip()
        if line and font.getlength(candidate) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    return lines + [line]


def shrink(size, minimum, lines):
    return [(s, lines) for s in range(size, minimum - 1, -1)]


def text(elements, value, x, y, width, options, bold=False, color=BODY, lh=LH, **style):
    """Place value at the first (size, most lines) option that fits the width; returns the height used."""
    for size, most in [(options, 1)] if isinstance(options, int) else options:
        rows = wrapped(value, width, size, bold)
        if len(rows) <= most and all(measure(r, size, bold, style.get('spacing', 0)) <= width for r in rows):
            break
    else:
        raise ValueError(f'Text does not fit {width:.0f}px: {value[:90]}')
    for n, row in enumerate(rows):
        elements.append(dict(kind='text', text=row, x=x, y=y + n * size * lh, w=width, h=size * lh,
                             size=size, bold=bold, color=color, lh=lh, **style))
    return len(rows) * size * lh


def shape(elements, x, y, width, height, color):
    elements.append(dict(kind='shape', x=x, y=y, w=width, h=height, color=color))


def picture(elements, slide, x, y, width, height):
    """Fit the slide's figure in the box, centred; returns its size."""
    path = (BUNDLE / slide['figure']).resolve()
    if not path.is_relative_to(BUNDLE) or not path.is_file():
        raise ValueError(f'Missing or invalid figure: {slide["figure"]}')
    with Image.open(path) as image:
        ratio = min(width / image.width, height / image.height)
        iw, ih = image.width * ratio, image.height * ratio
    elements.append(dict(kind='image', file=slide['figure'], alt=slide['alt'], x=x + (width - iw) / 2,
                         y=y + (height - ih) / 2, w=iw, h=ih))
    return iw, ih


def heading(elements, slide, width, sizes, lh=LH):
    text(elements, slide['kicker'].upper(), LEFT, 58, WIDTH, 17, bold=True, color=ACCENT, spacing=.16)
    return 92 + text(elements, slide['title'], LEFT, 92, width, sizes, bold=True, color=INK, lh=lh)


def column(elements, paragraphs, x, y, width, bottom):
    """Set (text, bold, colour) paragraphs at the largest size from 26 to 24 px that ends above `bottom`."""
    gap, lh = 12, 1.37
    for size in (26, 25, 24):
        lines = sum(len(wrapped(value, width, size, bold)) for value, bold, _ in paragraphs)
        if y + lines * size * lh + gap * (len(paragraphs) - 1) <= bottom:
            break
    else:
        raise ValueError(f'The prose runs below {bottom}px; shorten it')
    for value, bold, color in paragraphs:
        y += text(elements, value, x, y, width, [(size, 9)], bold=bold, color=color, lh=lh) + gap


def cover(elements, slide, story):
    picture(elements, slide, 820, 0, 1100, 1080)
    y = 236 + text(elements, slide['title'], LEFT, 236, 620, [(96, 2)], bold=True, color=INK, lh=1.08) + 36
    y += text(elements, story['subtitle'], LEFT, y, 560, [(34, 2)]) + 36
    y += text(elements, slide['lede'], LEFT, y, 600, [(26, 6)], lh=1.37) + 52
    text(elements, story['author'], LEFT, y, 600, 27, bold=True, color=INK)


def figure(elements, slide, story):
    """The title on the left, the slide's words on the right, and the figure across the slide below them."""
    heading(elements, slide, PROSE_X - 64 - LEFT, shrink(46, 42, 3), lh=1.14)
    column(elements, [(slide['lede'], False, BODY), (slide['takeaway'], True, INK)], PROSE_X, 92,
           LEFT + WIDTH - PROSE_X, 322)
    width, _ = picture(elements, slide, LEFT, 336, WIDTH, 654)
    if width < .97 * WIDTH:
        raise ValueError(f'The figure shrinks to {width:.0f}px wide; draw it at 1728 × 654')


def bookend(elements, slide, story):
    picture(elements, slide, 820, 0, 1100, 1080)
    y = heading(elements, slide, 760, shrink(52, 46, 2)) + 50
    recap, why = slide['body']
    y += text(elements, recap, LEFT, y, 720, [(30, 5)], color=INK) + 44
    used = text(elements, why, LEFT + 30, y, 690, [(28, 8)])
    shape(elements, LEFT, y + 6, 5, used - 12, TEAL)
    text(elements, slide['signoff'], LEFT, y + used + 64, 720, 48, bold=True, color=ACCENT)


LAYOUTS = {'cover': cover, 'figure': figure, 'bookend': bookend}


def layout(slide, number, story):
    kind = slide.get('layout', 'figure')
    if kind not in LAYOUTS:
        raise ValueError(f'Unknown layout: {kind}')
    elements = []
    LAYOUTS[kind](elements, slide, story)
    refs = slide.get('refs', [])
    picture_right = kind in ('cover', 'bookend')  # the picture runs to the bottom right corner
    if refs:
        text(elements, ' • '.join(story['sources'][ref]['short'] for ref in refs), LEFT, 1018,
             900 if picture_right else 1600, 15, color=MUTED)
    if not picture_right:
        text(elements, str(number), 1700, 1018, 124, 17, bold=True, color=MUTED, align='right')
    for el in elements:
        if el['x'] < 0 or el['y'] < 0 or el['x'] + el['w'] > W + .5 or el['y'] + el['h'] > H + .5:
            raise ValueError(f'Element outside the slide: {el}')
    return elements


def missing_glyphs(story, pages):
    """Characters in visible text that Lato lacks, which a browser or PowerPoint would draw in another font."""
    covered = set.intersection(*(set(TTFont(HERE / 'fonts' / f'Lato-{weight}.ttf').getBestCmap())
                                 for weight in ('Regular', 'Bold')))
    seen = [el['text'] for page in pages for el in page if el['kind'] == 'text']
    seen += [p for slide in story['slides'] for p in slide['notes']] + [s['title'] for s in story['sources'].values()]
    return sorted({ch for value in seen for ch in value if not ch.isspace() and ord(ch) not in covered})


def data_url(path):
    mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def px(value):
    return f'{round(value, 2):g}px'


def element_html(el):
    style = f"left:{px(el['x'])};top:{px(el['y'])};width:{px(el['w'])};height:{px(el['h'])};"
    if el['kind'] == 'image':
        src = data_url(BUNDLE / el['file'])
        return f'<img class="element figure" style="{style}" alt="{html.escape(el["alt"])}" src="{src}">'
    if el['kind'] == 'shape':
        return f'<div class="element" aria-hidden="true" style="{style}background:{el["color"]}"></div>'
    style += f"font-size:{el['size']}px;font-weight:{700 if el['bold'] else 400};color:{el['color']};"
    style += ''.join([f"line-height:{el['lh']};" if el['lh'] != LH else '',
                      f"letter-spacing:{el['spacing']}em;" if el.get('spacing') else '',
                      f"text-align:{el['align']};" if el.get('align') else ''])
    return f'<div class="element text" style="{style}">{html.escape(el["text"])}</div>'


def slide_refs(slide):
    """The sources behind a slide, those in its footer and then those only its notes cite."""
    return slide.get('refs', []) + slide.get('note_refs', [])


def source_items(story, refs):
    items = []
    for ref in refs:
        source = story['sources'][ref]
        title = html.escape(source['title'])
        items.append(f'<li><a href="{html.escape(source["url"])}" target="_blank" rel="noopener">{title}</a></li>'
                     if source['url'] else f'<li>{title}</li>')
    return ''.join(items)


def prose(text):
    """Escaped reading-version text; a no-break space keeps each number on the same line as its unit."""
    return re.sub(r'(?<=\d) (?=Å|°C|GPa|kcal/mol|m?J/m²)', '\u00a0', html.escape(text))


def article_html(story, n, slide):
    """One slide in reading order with its notes and sources, for phones and readers."""
    e, kind = prose, slide.get('layout', 'figure')
    parts = [f'<article id="read-{e(slide["id"])}" data-index="{n}">',
             f'<p class="r-kicker">{e(" · ".join(filter(None, [str(n + 1), slide.get("kicker")])))}</p>',
             f'<h2>{e(slide["title"])}</h2>']
    if kind == 'cover':
        parts.append(f'<p class="r-lede">{e(story["subtitle"])}</p><p class="r-author">{e(story["author"])}</p>')
    if slide.get('lede'):
        parts.append(f'<p class="r-lede">{e(slide["lede"])}</p>')
    if slide.get('figure'):
        with Image.open(BUNDLE / slide['figure']) as image:  # reserves the space before the picture loads
            size = f'width="{image.width}" height="{image.height}"'
        parts.append(f'<figure><img data-slide="{n}" {size} alt="{e(slide["alt"])}"></figure>')
    if slide.get('takeaway'):
        parts.append(f'<p class="r-take">{e(slide["takeaway"])}</p>')
    parts += [f'<p class="r-body">{e(p)}</p>' for p in slide.get('body', [])]
    if slide.get('signoff'):
        parts.append(f'<p class="r-signoff">{e(slide["signoff"])}</p>')
    parts.append('<h3 class="r-label">Notes</h3>' + ''.join(f'<p>{e(p)}</p>' for p in slide['notes']))
    if refs := slide_refs(slide):
        parts.append(f'<h3 class="r-label">Sources</h3><ul class="r-sources">{source_items(story, refs)}</ul>')
    return ''.join(parts) + '</article>'


def write_html(story, pages):
    fonts = ''.join(f"@font-face{{font-family:{f['family']};font-weight:{f['weight']};font-style:{f['style']};"
                    f"src:url({data_url(HERE / 'fonts' / f['file'])}) format('truetype');}}"
                    for f in json.loads((HERE / 'fonts/fonts.json').read_text()))
    sections = []
    for n, (slide, elements) in enumerate(zip(story['slides'], pages), 1):
        attrs = {'id': f'slide-{slide["id"]}', 'data-id': slide['id'], 'data-page': str(n),
                 'data-qa': 'true' if slide.get('qa') else 'false', 'aria-label': slide['title'], 'aria-hidden': 'true'}
        at = ' '.join(f'{k}="{html.escape(v)}"' for k, v in attrs.items())
        sections.append(f'<section class="slide" role="group" aria-roledescription="slide" {at}>'
                        + ''.join(element_html(el) for el in elements) + '</section>')
    reader = (f'<div id="reader" role="region" aria-label="Reading version with notes" hidden>'
              f'<header class="r-head"><h1>{html.escape(story["title"])}</h1>'
              f'<button type="button" id="to-slides">Slides</button></header>'
              f'<p class="r-intro">The reading version shows every slide with what the speaker says about it.</p>'
              + ''.join(article_html(story, n, slide) for n, slide in enumerate(story['slides'])) + '</div>')
    title, subtitle = html.escape(story['title']), html.escape(story['subtitle'])
    css = fonts + (HERE / 'deck.css').read_text()
    notices = (HERE / 'fonts/NOTICES.txt').read_text()  # verbatim, as browsers keep entities in script text
    output = (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
              f'<meta name="viewport" content="width=device-width,initial-scale=1">'
              f'<title>{title} · {html.escape(story["author"])}</title><meta name="description" content="{subtitle}">'
              f'<style>{css}</style><script type="text/plain" id="font-notices">{notices}</script></head>'
              f'<body><main id="stage" aria-label="Presentation"><div id="deck">{"".join(sections)}</div></main>'
              f'{reader}<script>{(HERE / "viewer.js").read_text()}</script></body></html>')
    (BUNDLE / 'index.html').write_text('\n'.join(line.rstrip() for line in output.splitlines()) + '\n')


def notes_text(story, slide):
    sources = [story['sources'][ref] for ref in slide_refs(slide)]
    listed = '\n'.join(' '.join(filter(None, (s['title'], s['url']))) for s in sources)
    return '\n\n'.join(slide['notes']) + (f'\n\nSources\n{listed}' if listed else '')


def write_pptx(story, pages):
    deck = Presentation()
    deck.slide_width, deck.slide_height = Inches(40 / 3), Inches(7.5)
    deck._element.sldSz.set('type', 'screen16x9')
    props = deck.core_properties
    props.title, props.subject, props.author = story['title'], story['subtitle'], story['author']
    props.last_modified_by = props.comments = props.keywords = ''
    props.created = props.modified = datetime.now(timezone.utc)
    for source, elements in zip(story['slides'], pages):
        slide = deck.slides.add_slide(deck.slide_layouts[6])
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = RGBColor(255, 255, 255)
        for el in elements:
            x, y, w, h = (Inches(el[key] / 144) for key in ('x', 'y', 'w', 'h'))
            if el['kind'] == 'image':
                image = slide.shapes.add_picture(str(BUNDLE / el['file']), x, y, w, h)
                image._element.nvPicPr.cNvPr.set('descr', el['alt'])
                continue
            if el['kind'] == 'shape':
                box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
                box.fill.solid()
                box.fill.fore_color.rgb = RGBColor.from_string(el['color'][1:])
                box.line.fill.background()
                for effect in box._element.xpath('./p:style/a:effectRef'):
                    effect.set('idx', '0')
                continue
            frame = slide.shapes.add_textbox(x, y, w, h).text_frame
            frame.margin_top = frame.margin_bottom = frame.margin_left = frame.margin_right = 0
            frame.word_wrap = False
            frame.vertical_anchor = MSO_ANCHOR.TOP
            para = frame.paragraphs[0]
            para.space_before = para.space_after = Pt(0)
            para.line_spacing = 1.0
            para.alignment = PP_ALIGN.RIGHT if el.get('align') == 'right' else PP_ALIGN.LEFT
            run = para.add_run()
            run.text = el['text']
            run.font.name, run.font.size, run.font.bold = 'Lato', Pt(el['size'] / 2), el['bold']
            run.font.color.rgb = RGBColor.from_string(el['color'][1:])
            if el.get('spacing'):
                run._r.get_or_add_rPr().set('spc', str(round(el['spacing'] * el['size'] / 2 * 100)))
        slide.notes_slide.notes_text_frame.text = notes_text(story, source)
    (BUNDLE / 'downloads').mkdir(exist_ok=True)
    destination = BUNDLE / 'downloads/iff-visual-showcase.pptx'
    deck.save(destination)
    clean_pptx(destination, len(pages))


def clean_pptx(destination, slide_count):
    replacement = destination.with_suffix('.clean.pptx')
    with zipfile.ZipFile(destination) as source, zipfile.ZipFile(replacement, 'w', zipfile.ZIP_DEFLATED) as target:
        for entry in source.infolist():
            data = source.read(entry.filename)
            if entry.filename == 'docProps/app.xml':
                root = ET.fromstring(data)
                for tag in ('Application', 'Company', 'Manager', 'AppVersion'):
                    for el in root.findall('{*}' + tag):
                        el.text = ''
                for el in list(root):
                    tag = ET.QName(el).localname
                    if tag in ('HeadingPairs', 'TitlesOfParts'):
                        root.remove(el)
                    elif tag in ('Slides', 'Notes'):
                        el.text = str(slide_count)
                    elif tag == 'PresentationFormat':
                        el.text = 'On-screen Show (16:9)'
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            if entry.filename.startswith('docProps/thumbnail.'):
                continue
            if entry.filename == '_rels/.rels':
                root = ET.fromstring(data)
                for el in list(root):
                    if el.get('Type', '').endswith('/thumbnail'):
                        root.remove(el)
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            if entry.filename == '[Content_Types].xml':
                root = ET.fromstring(data)
                for el in list(root):
                    if 'thumbnail' in el.get('PartName', ''):
                        root.remove(el)
                data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
            target.writestr(entry, data)
    replacement.replace(destination)


def write_notes(story):
    chunks = ['# Presenter notes']
    for n, slide in enumerate(story['slides'], 1):
        chunks += [f'## {n}. {slide["title"]}', *slide['notes']]
        sources = [story['sources'][ref] for ref in slide_refs(slide)]
        if sources:
            chunks.append('### Sources\n\n' + '\n'.join('- ' + ' '.join(filter(None, (s['title'], s['url'])))
                                                       for s in sources))
    (BUNDLE / 'presenter-notes.md').write_text('\n\n'.join(chunks) + '\n')


def write_manifest(story):
    fields = ('kicker', 'lede', 'takeaway', 'body', 'figure', 'alt', 'refs', 'note_refs', 'notes')
    manifest = {
        'schema': 'iff-presentation.citation-license/v3', 'prepared': '2026-11-05',
        'scientific_status': 'Published results are quoted from the cited papers and were not rerun. The PySCF '
                             'electron cloud of one water molecule was computed only to draw a picture and is not '
                             'evidence.',
        'figure_provenance': 'Every figure was drawn for this presentation from open crystal structures, published '
                             'parameters and molecules built with RDKit. Pictures of molecules on surfaces are '
                             'illustrations, not simulation snapshots. No third-party figure or text is reproduced.',
        'sources': story['sources'],
        'slides': [{'id': s['id'], 'page': n, 'title': s['title'], **{k: s[k] for k in fields if k in s}}
                   for n, s in enumerate(story['slides'], 1)]}
    (BUNDLE / 'citation-license-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--story', type=Path, default=HERE / 'story.json')
    story = json.loads(parser.parse_args().story.read_text())
    ids = [slide['id'] for slide in story['slides']]
    assert len(ids) == len(set(ids)), 'Slide IDs must be unique'
    cited = {ref for slide in story['slides'] for ref in slide_refs(slide)}
    assert cited == set(story['sources']), f'Unknown or unused sources: {cited ^ set(story["sources"])}'
    pages = []
    for n, slide in enumerate(story['slides'], 1):
        try:
            pages.append(layout(slide, n, story))
        except (KeyError, ValueError) as exc:
            raise SystemExit(f'Slide {slide["id"]}: {exc!r}') from exc
    missing = missing_glyphs(story, pages)
    assert not missing, f'Lato lacks these characters: {missing}'
    write_html(story, pages)
    write_pptx(story, pages)
    write_notes(story)
    write_manifest(story)
    print(f'Built {len(ids)} slides as HTML with a reading version, editable PowerPoint and presenter notes.')


if __name__ == '__main__':
    main()
