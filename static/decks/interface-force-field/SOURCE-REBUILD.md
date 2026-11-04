# Rebuilding the Interface Force Field presentation

`source/story.json` holds the public slide text, speaker notes, figure descriptions and source identifiers. `source/build.py` lays out that one story as self-contained browser slides and PowerPoint slides with editable text and notes. Each element uses the same 1920 × 1080 coordinates in both formats. The PowerPoint canvas is 13⅓ × 7½ inches.

Create a Python environment with `source/requirements.txt`. LibreOffice must be on the executable path. Lato must be available to LibreOffice; the exact browser fonts and their notices are included under `source/fonts/`. Install those fonts locally if the system does not already provide Lato. Do not substitute fonts when checking the exported PowerPoint.

From this bundle directory, run the following commands with that environment's Python. Choose a local scratch directory outside the published bundle for the LibreOffice profile and intermediate export.

```sh
python source/plots.py
python source/drawings.py
python source/build.py
python source/export.py --work-dir /absolute/local/scratch/iff-export
```

The outputs are `index.html`, `downloads/iff-visual-showcase.pptx`, `downloads/iff-visual-showcase.pdf` and `presenter-notes.md`. The PDF is exported from the native PowerPoint text through LibreOffice. Its text remains selectable. Public document metadata names Sean Florez as author, leaves lastModifiedBy and creator empty, and retains only LibreOffice's PDF Producer field.

The browser viewer embeds its fonts and figures, so it has no network dependency. Arrow keys move between pages. Digits then Enter jump to a page. Q opens Questions, B then 1–6 opens the appendices, O or G opens the overview, F toggles full screen, and H or ? opens help. URL fragments accept page numbers, Q and B1–B6. The viewer supports edge clicks and horizontal swipes.

`source/plots.py` computes the analytical curves and numeric checks from `source/parameters.json`. It writes plot images and underlying data, including `source/data/science-checks.json`. `source/drawings.py` creates original teaching diagrams. Its fcc lattice uses the four conventional fractional basis sites. Space-filling sphere radii equal half the nearest-neighbour spacing; these are idealized models, not new simulation results. The energy landscape is illustrative.

After rebuilding, inspect every browser slide and the LibreOffice-rendered PowerPoint. Check for clipped labels, missing glyphs and changed line breaks. Check keyboard navigation, overview selection, hash links, downloads and selectable PDF text. The title image on the Writings page must be captured from the actual new first slide. After that capture and all exports, run `python source/manifest.py` to record final artifact and title-image hashes. The artifact manifest excludes itself. Reconcile the source identifiers and slide claims in `citation-license-manifest.json` whenever the story changes.

Published results were not rerun. Analytic pair calculations and ideal structures do not establish model accuracy for a new material. Workflow repeatability does not establish scientific accuracy.

The three `source/data/rh_*.car` files retain the original corrected rhodium cell and surface structures from the supplementary archive for Kanhaiya et al. (2021), including its author correction. They are retained as source evidence, under the cited CC BY 4.0 terms. The new idealized teaching pictures are constructed from the fcc basis rather than rendered from these files.
