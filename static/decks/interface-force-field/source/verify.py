#!/usr/bin/env python3
"""Check that the viewer, the PowerPoint and the PDF tell the same story, with clean metadata and checked wording.

`python source/verify.py` prints one line per check and exits non-zero if any fails. `main()` returns every public
text in the bundle (data URIs stripped, this file left out), so a further scan can reuse them.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

import pymupdf
from pptx import Presentation

BUNDLE = Path(__file__).resolve().parent.parent
TARGET = ('IFF supplies compatible interaction equations and material parameters so a classical simulation can '
          'describe a solid together with water, polymers or biological molecules. It addresses inconsistent '
          'material/surface descriptions and the difficulty of combining separately developed models, allowing '
          'supported interface structures, binding and energies to be calculated and compared with experiments.')
FACTS = ('protons and, in most atoms, neutrons', '160 ± 5', '533', '600 to 700', 'His-11', 'C-terminal', 'KSLSRHDHIHHH',
         'CHARMM-METAL', 'PCFF-SILICA', '−13.0 ± 0.1', '−15.5', 'EP2527307A1', 'Figures 10 and 11',
         'gold made of many small crystals', 'glycine', 'osteoporosis', 'SVSVGGK', 'photothermal cancer therapy',
         'Thank you. Questions?')
fails = []


def check(name, ok, detail=''):
    print('PASS' if ok else 'FAIL', name, detail if not ok else '')
    if not ok:
        fails.append(name)


def absent(texts, name, pattern, flags=re.I):
    hits = [(k, m.group(0)) for k, t in texts.items() for m in re.finditer(pattern, t, flags)]
    check(name, not hits, hits[:6])


def main(bundle=BUNDLE):
    story = json.loads((bundle / 'source/story.json').read_text())
    n = len(story['slides'])
    check('at most 15 slides', n <= 15, n)
    deck = Presentation(bundle / 'downloads/iff-visual-showcase.pptx')
    props = deck.core_properties
    check('pptx slide count', len(deck.slides) == n, len(deck.slides))
    check('pptx author', props.author == 'Sean Florez', props.author)
    check('pptx lastModifiedBy blank', not props.last_modified_by, props.last_modified_by)
    check('pptx title', props.title == 'Interface Force Field', props.title)
    with zipfile.ZipFile(bundle / 'downloads/iff-visual-showcase.pptx') as z:
        xml = z.read('docProps/core.xml').decode() + z.read('docProps/app.xml').decode()
    check('pptx metadata names no generator', 'python-pptx' not in xml)
    pdf = pymupdf.open(bundle / 'downloads/iff-visual-showcase.pdf')
    check('pdf page count', len(pdf) == n, len(pdf))
    meta = pdf.metadata
    check('pdf metadata', meta['author'] == 'Sean Florez' and meta['title'] == props.title
          and meta['subject'] == props.subject and not meta['creator'] and not meta['keywords'], meta)
    html = (bundle / 'index.html').read_text()
    for i, (slide, page) in enumerate(zip(story['slides'], deck.slides), 1):
        joined = ' '.join(s.text_frame.text for s in page.shapes if s.has_text_frame and s.text_frame.text.strip())
        pdf_text = ' '.join(pdf[i - 1].get_text().split())
        title = slide['title']
        check(f'{i} editable title', title in joined, joined[:120])
        check(f'{i} pdf selectable title', ' '.join(title.split()) in pdf_text, pdf_text[:120])
        for key in ('lede', 'takeaway'):
            if slide.get(key):
                check(f'{i} {key} in pptx and pdf',
                      slide[key] in joined and ' '.join(slide[key].split()) in pdf_text, slide[key][:60])
        notes = page.notes_slide.notes_text_frame.text if page.has_notes_slide else ''
        check(f'{i} notes', all(p in notes for p in slide['notes']), notes[:80])
        cited = slide.get('refs', []) + slide.get('note_refs', [])
        if cited:
            check(f'{i} notes end with all {len(cited)} sources', '\nSources\n' in notes
                  and all(story['sources'][r]['title'] in notes for r in cited))
        check(f'{i} html title', title in html)
    catalog = next(s for s in story['slides'] if s['id'] == 'catalog')
    check('target in the catalog notes', any(TARGET in p for p in catalog['notes']))
    check('target on the bookend', any(TARGET in json.dumps(s, ensure_ascii=False) for s in story['slides']
                                       if s.get('layout') == 'bookend'))
    examples = [s['title'] for s in story['slides'] if s['title'].startswith('Example')]
    check('example titles numbered in order', [t.split(':')[0] for t in examples] == ['Example 1', 'Example 2',
                                                                                       'Example 3'], examples)
    check('kickers keep only the topic', not any('Example' in s.get('kicker', '') for s in story['slides']))
    notes_md = (bundle / 'presenter-notes.md').read_text()
    check('notes headings carry the titles', all(f'## {k}. {s["title"]}' in notes_md
                                                 for k, s in enumerate(story['slides'], 1)))
    check('every figure slide has words', all(s.get('lede') and s.get('takeaway') for s in story['slides']
                                              if s.get('layout', 'figure') == 'figure'))

    texts = {}
    for path in sorted(bundle.rglob('*')):
        if path.is_file() and path != Path(__file__).resolve() and path.suffix in {
                '.html', '.md', '.json', '.py', '.js', '.css', '.txt', '.csv', '.cif', '.xyz'}:
            texts[str(path.relative_to(bundle))] = re.sub(r'data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+', '',
                                                          path.read_text())
    texts['pdf'] = ' '.join(page.get_text() for page in pdf)
    texts['pptx'] = ' '.join(s.text_frame.text for page in deck.slides for s in page.shapes if s.has_text_frame)
    texts['pptx notes'] = ' '.join(page.notes_slide.notes_text_frame.text for page in deck.slides
                                   if page.has_notes_slide)
    texts['pptx xml'] = xml
    words = '\n'.join(texts.values())
    absent(texts, 'no em dash', '—', 0)
    for fact in FACTS:
        check(f'fact present: {fact}', fact in words)
    check('softened crystal-shape wording', 'shifted platinum crystals from cubes toward tetrahedra' in words)
    print(len(texts), 'public texts checked')
    return texts


if __name__ == '__main__':
    main()
    print(len(fails), 'failures')
    sys.exit(bool(fails))
