# Rebuild the presentation

The `source/` directory contains the public authoring scripts, numerical tables and source-derived structures. Rebuilding creates the 35-slide editable PowerPoint, static PDF, SVG slides, scientific illustrations, three silent animations and a portable browser presentation. It does not run a materials simulation or fit new parameters.

Install Python, FFmpeg, LibreOffice Impress and the Lato and DejaVu Sans fonts. Python package versions are recorded in `source/scripts/requirements-lock.txt`. You can reuse an existing compatible Python environment and skip environment creation and package installation. Once dependencies are installed, the build uses the included data without network access. If you reuse an environment, replace `.venv/bin/python` below with its Python executable. From the bundle directory:

```sh
cd source
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-lock.txt
.venv/bin/python scripts/build_assets.py
.venv/bin/python scripts/build_deck.py
libreoffice --headless --convert-to pdf --outdir build build/iff-visual-showcase.pptx
.venv/bin/python scripts/sanitize_pdf.py
.venv/bin/python scripts/render_exports.py
.venv/bin/python scripts/build_browser.py
.venv/bin/python scripts/build_manifest.py
.venv/bin/python scripts/package_bundle.py
```

`build/` contains the PowerPoint, PDF, cover image, rendered PNG previews and SVG slides. `media/` contains the original illustrations and MP4, GIF and PNG animation alternatives. `website-bundle/` contains the browser viewer, downloads, media, citations, presenter notes and reproducible source.

The PDF sanitizer removes multimedia and attachments from every PDF object, including references retained by the structure tree. Text, vector artwork and web links remain in the static export. The PowerPoint retains its three embedded videos; the browser viewer offers video playback with static alternatives.

Inspect the rebuilt presentation before sharing it. Fonts, LibreOffice and rendering-library versions can change text metrics or PDF/SVG bytes. The citation manifest records asset sizes and SHA-256 hashes for the current rebuild, while the bundle manifest records the packaged files. Source-derived structures and illustrative motion remain distinct from simulation evidence; published numerical results are reproduced without rerunning them.
