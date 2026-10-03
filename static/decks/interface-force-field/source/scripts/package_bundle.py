"""Assemble the portable presentation and its reproducible public source."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
web = ROOT / 'website-bundle'
source = web / 'source'
(source / 'scripts').mkdir(parents=True, exist_ok=True)
(source / 'data').mkdir(exist_ok=True)
names = [
    'build_assets.py', 'build_deck.py', 'build_browser.py', 'build_manifest.py',
    'render_exports.py', 'sanitize_pdf.py', 'package_bundle.py', 'story.py',
    'requirements-lock.txt', 'production_metadata.json',
]
for name in names:
    shutil.copy2(ROOT / 'scripts' / name, source / 'scripts' / name)
for path in sorted((ROOT / 'data').glob('*')):
    if path.is_file():
        shutil.copy2(path, source / 'data' / path.name)
for name in ['README.md', 'LICENSE-ATTRIBUTION.md', 'SOURCE-REBUILD.md', 'SITE-COPY.md']:
    document = ROOT / name
    if not document.exists():
        document = ROOT.parent / name
    shutil.copy2(document, web / name)
shutil.copy2(ROOT / 'build/iff-visual-showcase.notes.md', web / 'presenter-notes.md')
shutil.copy2(ROOT / 'build/iff-visual-showcase.slides.json', source / 'slides.json')
shutil.copy2(ROOT / 'build/rendered/slide-01.png', web / 'cover.png')
files = []
for path in sorted(web.rglob('*')):
    if path.is_file() and path.name != 'artifact-manifest.json':
        files.append({
            'path': path.relative_to(web).as_posix(),
            'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        })
(web / 'artifact-manifest.json').write_text(json.dumps({
    'schema': 'iff-showcase.artifacts/v1', 'files': files,
}, indent=2) + '\n')
zip_path = ROOT / 'build/iff-website-owner-bundle.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
    for path in sorted(web.rglob('*')):
        if path.is_file():
            info = zipfile.ZipInfo('iff-showcase/' + path.relative_to(web).as_posix(),
                                   date_time=(2026, 10, 3, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
print('Portable bundle:', len(files) + 1, 'files')
print('ZIP SHA-256:', hashlib.sha256(zip_path.read_bytes()).hexdigest())
