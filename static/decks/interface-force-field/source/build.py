#!/usr/bin/env python3
"""Build one slide story as self-contained HTML and editable PowerPoint."""
import argparse
import base64
import html
import json
import mimetypes
from pathlib import Path
from functools import lru_cache
from datetime import datetime, timezone
import zipfile
from lxml import etree as ET

from PIL import Image, ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
INK, BODY, MUTED = '#15191F', '#2E3440', '#5C6573'
ACCENT, TEAL, BLUE, TINT = '#B3263E', '#1D7F79', '#3474B8', '#F4F5F7'
W, H = 1920, 1080


@lru_cache(maxsize=128)
def font_for(size, bold):
    return ImageFont.truetype(str(HERE / 'fonts' / ('Lato-Bold.ttf' if bold else 'Lato-Regular.ttf')), size)


def wrapped(text, width, size, bold=False):
    font = font_for(size,bold)
    lines = []
    for paragraph in str(text).split('\n'):
        line = ''
        for word in paragraph.split():
            candidate = f'{line} {word}'.strip()
            if line and font.getlength(candidate) > width:
                lines.append(line)
                line = word
            else:
                line = candidate
        lines.append(line)
    return lines


def textbox(elements, text, x, y, width, height, size=30, bold=False, color=BODY, minimum=24):
    for fitted in range(size, minimum - 1, -1):
        lines = wrapped(text, width, fitted, bold)
        if len(lines) * fitted * 1.28 <= height and all(font_for(fitted,bold).getlength(line) <= width for line in lines):
            break
    else:
        raise ValueError(f'Text exceeds {width}×{height}: {text[:100]}')
    for n, line in enumerate(lines):
        elements.append(dict(kind='text', text=line, x=x, y=y + n * fitted * 1.28,
                             w=width, h=fitted * 1.28, size=fitted, bold=bold, color=color))
    return len(lines) * fitted * 1.28


def shape(elements, x, y, width, height, color=TINT):
    elements.append(dict(kind='shape', x=x, y=y, w=width, h=height, color=color))


def picture(elements, filename, alt, x, y, width, height):
    path = (BUNDLE / filename).resolve()
    if not path.is_relative_to(BUNDLE) or not path.is_file():
        raise ValueError(f'Missing or invalid figure: {filename}')
    with Image.open(path) as image:
        ratio = min(width / image.width, height / image.height)
        iw, ih = image.width * ratio, image.height * ratio
    elements.append(dict(kind='image', file=filename, alt=alt, x=x + (width-iw)/2,
                         y=y + (height-ih)/2, w=iw, h=ih))


def paragraphs(elements, items, x, y, width, height, size=32):
    if not items:
        return
    gap = 25
    for fitted in range(size, 23, -1):
        heights = [len(wrapped(t, width - 30, fitted)) * fitted * 1.28 for t in items]
        if sum(heights) + gap * (len(items) - 1) <= height:
            break
    else:
        raise ValueError('Body text exceeds its slide area')
    for text, block_h in zip(items, heights):
        shape(elements, x, y + 8, 5, 26, ACCENT)
        textbox(elements, text, x + 28, y, width - 28, block_h + 1, fitted, minimum=fitted)
        y += block_h + gap


def layout(slide, number, total, story):
    elements = []
    footer_elements = []
    kind = slide.get('layout', 'text')
    if kind not in ('cover','figure','cards','comparison','table','text'):
        raise ValueError(f'Unknown layout: {kind}')
    body = slide.get('body', [])
    textbox(elements, slide.get('chapter', 'Interface Force Field').upper(), 96, 58, 1728, 28,
            size=17, bold=True, color=ACCENT, minimum=17)
    footer = ' · '.join(story.get('sources',{}).get(ref,{}).get('short',ref) for ref in slide.get('refs',[]))
    if len(wrapped(footer,1540,15)) > 1:
        footer = ' · '.join(slide.get('refs',[]))
    textbox(footer_elements, footer, 96, 1018, 1540, 22, size=15, color=MUTED, minimum=15)
    textbox(footer_elements, f'{number:02} / {total}', 1700, 1018, 124, 22, size=17, bold=True,
            color=MUTED, minimum=17)
    if kind == 'cover':
        textbox(elements, slide['title'], 96, 220, 850, 230, size=70, bold=True, color=INK, minimum=58)
        textbox(elements, slide.get('lead', story.get('subtitle', '')), 96, 485, 800, 210, size=34)
        textbox(elements, story.get('author', 'Sean Florez'), 96, 790, 820, 50, size=27, bold=True)
        if slide.get('figure'):
            picture(elements, slide['figure'], slide.get('alt', ''), 960, 180, 864, 690)
        return elements+footer_elements
    textbox(elements, slide['title'], 96, 92, 1728, 138, size=52, bold=True, color=INK, minimum=46)
    title_lines = len(wrapped(slide['title'], 1728, 52, True))
    top = 186 + max(0, title_lines - 1) * 60
    if slide.get('lead'):
        top += textbox(elements, slide['lead'], 96, top, 1728, 126, size=30) + 30
    available = 970 - top
    if kind == 'figure':
        if body:
            paragraphs(elements, body, 96, top + 28, 520, available - 28, 30)
            picture(elements, slide['figure'], slide.get('alt', ''), 660, top, 1164, available)
        else:
            picture(elements, slide['figure'], slide.get('alt', ''), 96, top, 1728, available)
    elif kind in ('cards', 'comparison'):
        count = len(body)
        columns = 3 if count == 3 else 2
        rows = (count + columns - 1) // columns
        cell_w, cell_h = (1728 - 36 * (columns - 1)) / columns, (available - 30 * (rows - 1)) / max(1, rows)
        for n, text in enumerate(body):
            x, y = 96 + (n % columns) * (cell_w + 36), top + (n // columns) * (cell_h + 30)
            shape(elements, x, y, cell_w, cell_h)
            shape(elements, x, y, cell_w, 6, [ACCENT, TEAL, BLUE][n % 3])
            heading, separator, detail = text.partition('|')
            if separator:
                used = textbox(elements, heading.strip(), x+30, y+30, cell_w-60, 140, 36, True, INK)
                textbox(elements, detail.strip(), x+30, y+used+50, cell_w-60, cell_h-used-75, 29)
            else:
                textbox(elements, text, x+30, y+36, cell_w-60, cell_h-72, 32)
    elif kind == 'table':
        table = slide['table']
        rows = [table['headers']] + table['rows']
        cell_w, cell_h = 1728 / len(rows[0]), min(110, available / len(rows))
        for row_n, row in enumerate(rows):
            if len(row) != len(rows[0]):
                raise ValueError('Table rows must match header length')
            for col_n, text in enumerate(row):
                x, y = 96 + cell_w * col_n, top + cell_h * row_n
                if row_n % 2 == 0:
                    shape(elements, x, y, cell_w, cell_h)
                textbox(elements, text, x+18, y+18, cell_w-36, cell_h-24,
                        24 if row_n else 23, bold=not row_n, minimum=18)
        if body:
            paragraphs(elements, body, 96, top+cell_h*len(rows)+30, 1728,
                       available-cell_h*len(rows)-30, 27)
    else:
        paragraphs(elements, body, 96, top+20, 1650, available-20, 36)
    elements += footer_elements
    for el in elements:
        assert el['x'] >= 0 and el['y'] >= 0 and el['x']+el['w'] <= W+1 and el['y']+el['h'] <= H, el
    return elements


def data_url(path):
    mime = mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def write_html(story, pages):
    fonts = []
    for font in json.loads((HERE/'fonts/fonts.json').read_text()):
        fmt = 'truetype' if font['file'].endswith('.ttf') else 'opentype'
        fonts.append(f"@font-face{{font-family:{font['family']};font-weight:{font['weight']};font-style:{font['style']};src:url({data_url(HERE/'fonts'/font['file'])}) format('{fmt}');}}")
    chunks = []
    for n, (slide, elements) in enumerate(zip(story['slides'], pages), 1):
        attrs = dict(id=f'slide-{slide["id"]}', **{'data-id':slide['id'], 'data-page':str(n),
                     'data-section':'backup' if slide['id'].startswith('B') else 'main',
                     'data-qa':str(slide.get('qa', slide['title'].lower().startswith('questions'))).lower(),
                     'aria-label':slide['title'], 'aria-hidden':'true'})
        at = ' '.join(f'{k}="{html.escape(v, quote=True)}"' for k,v in attrs.items())
        content = []
        for el in elements:
            style = f"left:{el['x']}px;top:{el['y']}px;width:{el['w']}px;height:{el['h']}px;"
            if el['kind'] == 'text':
                style += f"font-size:{el['size']}px;font-weight:{700 if el['bold'] else 400};color:{el['color']};"
                content.append(f'<div class="element text" style="{style}">{html.escape(el["text"])}</div>')
            elif el['kind'] == 'shape':
                content.append(f'<div class="element" aria-hidden="true" style="{style}background:{el["color"]}"></div>')
            else:
                content.append(f'<img class="element figure" style="{style}" alt="{html.escape(el["alt"], quote=True)}" src="{data_url(BUNDLE/el["file"])}">')
        chunks.append(f'<section class="slide" role="group" aria-roledescription="slide" {at}>'+''.join(content)+'</section>')
    title = html.escape(story['title'])
    css = ''.join(fonts) + (HERE/'deck.css').read_text()
    notices = html.escape((HERE/'fonts/NOTICES.txt').read_text())
    script = (HERE/'viewer.js').read_text()
    output = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Sean Florez</title><style>{css}</style><script type="text/plain" id="font-notices">{notices}</script></head><body><main id="stage" aria-label="Presentation"><div id="deck">'+''.join(chunks)+f'</div></main><script>{script}</script></body></html>'
    (BUNDLE/'index.html').write_text('\n'.join(line.rstrip() for line in output.splitlines())+'\n')


def write_pptx(story, pages):
    deck = Presentation()
    deck.slide_width, deck.slide_height = Inches(40/3), Inches(7.5)
    deck._element.sldSz.set('type','screen16x9')
    props = deck.core_properties
    props.title, props.subject, props.author = story['title'], story.get('subtitle', ''), 'Sean Florez'
    props.last_modified_by = ''
    props.comments = ''
    props.keywords = ''
    props.created = props.modified = datetime.now(timezone.utc)
    for source, elements in zip(story['slides'], pages):
        slide = deck.slides.add_slide(deck.slide_layouts[6])
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = RGBColor(255,255,255)
        for el in elements:
            x,y,w,h = [Inches(el[key]/144) for key in ('x','y','w','h')]
            if el['kind'] == 'image':
                picture_shape = slide.shapes.add_picture(str(BUNDLE/el['file']),x,y,w,h)
                picture_shape._element.nvPicPr.cNvPr.set('descr',el['alt'])
                continue
            if el['kind'] == 'shape':
                box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,x,y,w,h)
                box.fill.solid()
                box.fill.fore_color.rgb = RGBColor.from_string(el['color'][1:])
                box.line.fill.background()
                for effect in box._element.xpath('./p:style/a:effectRef'):
                    effect.set('idx','0')
                continue
            box = slide.shapes.add_textbox(x,y,w,h)
            frame = box.text_frame
            frame.clear()
            frame.margin_top = frame.margin_bottom = frame.margin_left = frame.margin_right = 0
            frame.word_wrap = False
            frame.vertical_anchor = MSO_ANCHOR.TOP
            para = frame.paragraphs[0]
            para.space_before = para.space_after = Pt(0)
            para.line_spacing = 1.0
            run = para.add_run()
            run.text = el['text']
            run.font.name, run.font.size, run.font.bold = 'Lato', Pt(el['size']/2), el['bold']
            run.font.color.rgb = RGBColor.from_string(el['color'][1:])
        notes = source.get('notes', '')
        if isinstance(notes,list):
            notes = '\n\n'.join(notes)
        full_refs = [ref+': '+story.get('sources',{}).get(ref,{}).get('title',ref)+' '+
                     (story.get('sources',{}).get(ref,{}).get('url') or '') for ref in source.get('refs',[])]
        slide.notes_slide.notes_text_frame.text = notes + '\n\nSources:\n' + '\n'.join(full_refs)
    (BUNDLE/'downloads').mkdir(exist_ok=True)
    destination = BUNDLE/'downloads/iff-visual-showcase.pptx'
    deck.save(destination)
    clean_pptx(destination,len(pages))


def clean_pptx(destination,slide_count):
    replacement = destination.with_suffix('.clean.pptx')
    with zipfile.ZipFile(destination) as source, zipfile.ZipFile(replacement,'w',zipfile.ZIP_DEFLATED) as target:
        for entry in source.infolist():
            data = source.read(entry.filename)
            if entry.filename == 'docProps/app.xml':
                root = ET.fromstring(data)
                for tag in ('Application','Company','Manager','AppVersion'):
                    for el in root.findall('{*}'+tag):
                        el.text = ''
                for el in list(root):
                    tag = ET.QName(el).localname
                    if tag in ('HeadingPairs','TitlesOfParts'):
                        root.remove(el)
                    elif tag in ('Slides','Notes'):
                        el.text = str(slide_count)
                    elif tag == 'PresentationFormat':
                        el.text = 'On-screen Show (16:9)'
                data = ET.tostring(root,encoding='utf-8',xml_declaration=True)
            if entry.filename.startswith('docProps/thumbnail.'):
                continue
            if entry.filename == '_rels/.rels':
                root = ET.fromstring(data)
                for el in list(root):
                    if el.get('Type','').endswith('/thumbnail'):
                        root.remove(el)
                data = ET.tostring(root,encoding='utf-8',xml_declaration=True)
            if entry.filename == '[Content_Types].xml':
                root = ET.fromstring(data)
                for el in list(root):
                    if 'thumbnail' in el.get('PartName',''):
                        root.remove(el)
                data = ET.tostring(root,encoding='utf-8',xml_declaration=True)
            target.writestr(entry,data)
    replacement.replace(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--story', type=Path, default=HERE/'story.json')
    args = parser.parse_args()
    story = json.loads(args.story.read_text())
    missing = {ref for slide in story['slides'] for ref in slide.get('refs',[]) if ref not in story['sources']}
    assert not missing, f'Unknown source identifiers: {missing}'
    ids = [slide['id'] for slide in story['slides']]
    assert len(ids) == len(set(ids)), 'Slide IDs must be unique'
    pages = []
    for n, slide in enumerate(story['slides'],1):
        try:
            pages.append(layout(slide,n,len(ids),story))
        except (ValueError, AssertionError) as exc:
            raise ValueError(f'Slide {slide["id"]}: {exc}') from exc
    write_html(story,pages)
    write_pptx(story,pages)
    notes = '\n\n'.join(f'## {s["id"]}. {s["title"]}\n\n'+ ('\n\n'.join(s.get('notes',[])) if isinstance(s.get('notes'),list) else s.get('notes',''))+'\n\nSources: '+', '.join(s.get('refs',[])) for s in story['slides'])
    notes += '\n\n# References\n\n'+'\n\n'.join(f'{key}. {source["title"]}\n\n'+(source.get('url') or '') for key,source in story['sources'].items())
    (BUNDLE/'presenter-notes.md').write_text('# Presenter notes\n\n'+notes+'\n')
    manifest = {'schema':'iff-presentation.citation-license/v2','prepared':'2026-11-03',
                'scientific_status':'Published results were not rerun. Analytic calculations and idealized structures are educational.',
                'sources':story['sources'],
                'figure_provenance':'All presentation figures are original computed plots or teaching diagrams. No private lecture image or wording is reproduced.',
                'slides':[{'id':s['id'],'page':n,'title':s['title'],'lead':s.get('lead',''),
                           'claims':s.get('body',[]),'source_ids':s.get('refs',[]),
                           'notes':s.get('notes',''),'figure':s.get('figure'),
                           'figure_alt':s.get('alt'), 'table':s.get('table')} for n,s in enumerate(story['slides'],1)]}
    (BUNDLE/'citation-license-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(f'Built {len(ids)} slides as HTML, editable PowerPoint and presenter notes.')


if __name__ == '__main__':
    main()
