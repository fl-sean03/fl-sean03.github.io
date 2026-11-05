# Rebuilding the Interface Force Field presentation

`source/story.json` holds the slide text, speaker notes, picture descriptions and source identifiers. `source/build.py` lays out that one story as browser slides with a reading version, as PowerPoint slides with editable text and notes, and as `presenter-notes.md`. Each element uses the same 1920 × 1080 coordinates in the browser and in PowerPoint, whose canvas is 13⅓ × 7½ inches.

Create a Python 3.12 environment from `source/requirements.txt`. The PDF export needs LibreOffice on the executable path, and LibreOffice needs Lato. The font files and their notices are in `source/fonts/`, so install them if the system lacks Lato, and do not let another font stand in when checking the export.

From this bundle directory, run these commands with that environment’s Python. The export needs a new scratch directory outside the bundle for the LibreOffice profile and the intermediate PDF.

```sh
python source/science.py
python source/figures.py
python source/build.py
python source/export.py --work-dir /absolute/local/scratch/iff-export
python source/manifest.py
```

`science.py` computes the worked numbers from the published parameters in `source/parameters.json` and checks them, writing `source/data/science-checks.json` and `source/data/lj-curves.csv`. The checks cover the arithmetic and algebra, not the accuracy of a model.

`figures.py` draws every picture into `assets/`, or only the ones named, as in `python source/figures.py cover lj`. Each part of the talk has its own module of pictures, in slide order from `fig_opening.py` to `fig_close.py`, and `draw.py` holds the slide-pixel canvas, the labels, arrows and charts, and the scenes that several pictures share. `structures.py` builds the atoms from the Crystallography Open Database files in `source/data/structures/`, from published lattice constants and from RDKit molecules. `render.py` is a small ray tracer for the atoms, and `style.py` holds the colours and file locations that the pictures, the science checks and the slide builder share. The water electron cloud is a PySCF calculation with the PBE functional, and it only draws a picture. Molecules on surfaces are arranged to show the idea and are not simulation snapshots.

`build.py` writes `index.html`, `downloads/iff-visual-showcase.pptx`, `presenter-notes.md` and `citation-license-manifest.json`, and it stops if a source is cited but not listed, or listed but not cited, or if Lato lacks a character on a slide. A slide’s `refs` appear in its footer, and its `note_refs` are sources that only its notes cite. `export.py` turns the PowerPoint into `downloads/iff-visual-showcase.pdf` through LibreOffice, so the PDF text stays selectable. Both files name Sean Florez as author. The PowerPoint leaves lastModifiedBy empty, and the PDF takes its title and subject from the PowerPoint and leaves its creator empty.

The viewer embeds its fonts and pictures, so it needs no network. Arrow keys, edge clicks and swipes move between pages. Digits then Enter jump to a page, Q opens the questions slide, O or G opens the overview, F toggles full screen, and H or ? opens help. T opens the reading version, every slide in order with its notes, and T or Esc returns to the slides. Clicking or tapping a picture in the reading version enlarges it. The address accepts page numbers, slide names such as `#lj`, and `#read`, and the reading version opens by itself on a phone held upright.

After rebuilding, look at every slide in the browser and in the PDF, on a laptop and on a phone 390 pixels wide, including the reading version and an enlarged picture. Check for clipped labels, changed line breaks, the keyboard and touch controls, the downloads and the selectable PDF text. Before running `manifest.py`, capture the Writings page title image, `static/images/writings/interface-force-field-title.png`, from the actual first slide at 1920 × 1080; `manifest.py` then records the final hashes of the bundle and that image, leaving itself out. `build.py` rewrites `citation-license-manifest.json` from the story, so reconcile its sources with the slide claims whenever the story changes.

Published results were not rerun. The worked pair calculations and ideal structures do not show that a model is accurate for a new material.
