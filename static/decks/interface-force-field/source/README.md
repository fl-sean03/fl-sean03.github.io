# How the Interface Force Field presentation is made

This folder produces the whole presentation. `source/story.json` holds the words on every slide, the speaker’s notes, the picture descriptions and the sources. The Python scripts beside it draw every picture from open crystal structures, molecules built with RDKit and published numbers, then lay the one story out three ways, as the browser viewer `index.html`, the editable PowerPoint file and the PDF in `downloads/`. Every picture was drawn for this presentation, and none is copied from another presentation or paper. Published results are quoted from their papers with page and figure locators, not rerun.

Paths here are relative to the bundle folder, `static/decks/interface-force-field`, where the commands below run.

## What draws each slide

Each part of the talk has its own module of figures, in slide order from `fig_opening.py` to `fig_close.py`, and `source/figures.py` runs them all or only the ones named. A figure is laid out on the 1920 × 1080 slide grid at the exact size of the box it fills, 1728 × 654 on a figure slide, or 1160 × 654 beside the animation on slide 2, so its labels match the slide’s own text in size.

| Slide | Figure | What it shows and how it is built |
|---|---|---|
| 1 Cover | `fig_opening.cover` | The peptide S7 (SSFPQPN, from Ruan et al. 2013) lying on a platinum (111) surface in liquid water |
| 2 The question | `fig_opening.hook` | The tripeptides TLT and TFT beside an ideal platinum cube and tetrahedron, with a close-up of the atoms on each kind of face. With TLT the crystals grow as cubes, and with TFT they shift toward tetrahedra |
| 2 The question | `fig_opening.growth` | An animation of the idea behind the question, under the rule in `growth.py`. A platinum crystal grows one layer of atoms at a time while TFT on its triangular faces slows their growth, so its square faces shrink and vanish and it ends as an octahedron. It is an illustration, not a simulation |
| 3 Why it matters | `fig_opening.motivation` | A platinum cube and tetrahedron, a gold rod 23 Å across, the peptide SVSVGGK on the flat (001) face of hydroxyapatite, and triethanolamine between two broken faces of tricalcium silicate |
| 4 Why IFF exists | `fig_opening.compat` | A platinum crystal as the metal model and the tripeptide TFT as the molecular model, first built separately with a question mark between them, then joined by the shared rules of IFF |
| 5 The solution | `fig_opening.catalog` | A gold crystal, quartz with OH groups, hydroxyapatite and tricalcium silicate, above a water droplet, the peptide S7 and a polyethylene chain |
| 6 From electrons to rules | `fig_terms.electrons` | Water’s electron density from a density functional calculation (PySCF, PBE functional, 6-31G(d) basis), beside water as balls, springs and charges. The calculation only draws the picture |
| 7 Five kinds of terms | `fig_terms.terms` | One ethanol molecule giving a hydrogen bond to a water molecule, drawn five times, once for each kind of term |
| 8 The Lennard-Jones curve | `fig_pairs.lj` | The rhodium 12-6 curve from Kanhaiya et al. (2021), with the pair drawn at its wall, its well and its tail |
| 9 Coulomb’s law | `fig_pairs.coulomb` | The energy of two opposite and two like unit charges in a vacuum, drawn against the rhodium curve at the same scale |
| 10 Surface energy | `fig_pairs.cleave` | A rhodium (111) block, whole and then pulled apart into two halves with two new faces |
| 11 Example 1, platinum | `fig_examples.platinum` | S7 in water on the triangular (111) and the square (100) platinum faces, its F ring flat on one and upright on the other |
| 12 Example 2, silica | `fig_examples.wetting` | Slices 14 Å thick through water on the (101) face of cristobalite, a form of silica. Covered in OH groups (Q3), the face lets water spread into a film. After heating has joined the OH groups in pairs into Si–O–Si bridges (Q4), marked, water beads up at 42°. The water is drawn to the published contact angles |
| 13 Example 3, bone mineral | `fig_examples.apatites` | The flat (001) face of hydroxyapatite above pH 14, at pH 10 and at pH 5, as hydrogen joins the phosphates and calcium leaves, with dotted rings where calcium left |
| 14 IFF Agent | `fig_close.agent` | Eight small pictures, one for each step of the workflow, all with rhodium’s published values |
| 15 The answer | `fig_close.closing` | The cover scene again, with the F ring marked |

`draw.py` holds what the figures share. That is the slide-pixel canvas, the numbered markers, arrows, panels and charts, the camera views, and the scenes several figures reuse, such as S7 on platinum and the ideal platinum crystals. `style.py` holds the colours and the file locations shared by the pictures, the science checks and the slide builder.

## Where the atoms come from

- Quartz, cristobalite, hydroxyapatite and tricalcium silicate come from the Crystallography Open Database, whose entries are public domain (CC0). The files in `source/data/structures/` are entry 9000775 for quartz (Levien, Prewitt and Weidner 1980), 9009686 for α-cristobalite at room temperature (Pluth, Smith and Faber 1985), 9011091 for hydroxyapatite (Sudarsanan and Young 1969) and 1540704 for tricalcium silicate (Mumme 1995). ASE reads them, and `structures.py` repeats each cell and cuts out a block, keeping every SiO₄ and PO₄ group whole.
- Platinum and gold are ideal face-centred cubic crystals built from the lattice sizes in database entries 9008480 (a = 3.9231 Å) and 9008463 (a = 4.07825 Å). Rhodium uses a = 3.8032 Å, the five-cell length in Kanhaiya et al. (2021), Table 2, divided by five. ASE builds the flat (111) and (100) surfaces, and the cube and the tetrahedron are cut from the ideal crystal along its {100} and {111} faces. The growing crystal in the animation sits on the same platinum lattice.
- Cut surfaces are finished as the chemistry requires. Each oxygen on silica that lost its second silicon gets a hydrogen, which makes the surface’s silanol (SiOH) groups, and the hydroxide columns of hydroxyapatite all point the same way.
- The two silica surfaces on slide 12 are cut from cristobalite along its (101) face, through the widest gap between layers of silicon, so each silicon on the face loses one bond. A hydrogen on each oxygen left with one silicon gives the OH-covered surface, Q3 in Emami et al. (2014), with 4.7 OH groups per nm². For the heated surface, Q4, the silanols on the top face pair up, each with its nearest neighbour, and each pair condenses as 2 Si–OH → Si–O–Si + H₂O. Every silicon on the face then has four bridging oxygens and none carries OH. Each new bridge closes a small, strained ring of three silicons, so every atom more than 3 Å above the bottom of the slab is relaxed with springs that pull the bonds toward Si–O 1.60 Å and the angles toward O–Si–O 109.47° and Si–O–Si 146.7°, the values in cristobalite.
- Molecules are built with RDKit from SMILES strings or peptide sequences, embedded in three dimensions and relaxed with the MMFF force field. The peptides S7, TLT, TFT and SVSVGGK are the ones in the cited papers. Ethanol, triethanolamine and a 20-carbon polyethylene chain complete the set.
- Water has the standard geometry, with O–H 0.9572 Å and an angle of 104.52°. It is placed at random at the density of liquid water, 0.0334 molecules per Å³, with no two oxygens closer than 2.75 Å.
- A molecule on a surface is arranged to show the idea. It is relaxed with MMFF while each atom is held within a band of heights over the surface, so the pose is plausible, but it is not a simulation snapshot.

## How the pictures are drawn

`render.py` is a small ray tracer written for this presentation. Its camera is orthographic, so equal sizes look equal anywhere in a picture. It traces spheres, cylinders and triangles exactly at three times the output resolution, then shades them with a key light from the upper left, a weak fill light from the right, a small highlight and a faint rim. Contact shading computed from the depth of each pixel darkens the hollows between atoms, distant atoms fade slightly toward the background, and outlines are drawn where the depth jumps or one object meets another. The renderer returns the mapping from ångströms to pixels, so markers, arrows and labels land exactly on the atoms they point at. `draw.py` places each render on the canvas at 1.25 pixels per slide pixel without resampling it. The animation on slide 2 is 81 renders from the same ray tracer, described in the next section.

Each kind of matter has the form that shows it best.

- Molecules are balls and sticks, with each bond coloured half by each of its atoms, so their bonds and shapes show.
- Metals and ions are touching spheres at their metallic or ionic radii, because how they pack is the point. A dark floor under a metal slab keeps the background from showing through the hollows.
- Silica, hydroxyapatite and tricalcium silicate are SiO₄ and PO₄ tetrahedra with calcium as balls, which shows the building blocks they are made of.
- In a picture about one interaction, the atoms involved keep their full colour and the others fade toward white.
- A picture with water renders the solid with its molecule and the water separately and stacks them, so the pale water casts no shadow on the molecule.

Text is ink `#15191F` and body grey `#2E3440`, with muted grey `#5C6573` for secondary labels and a pale tint `#F4F5F7` behind panels. Red `#B3263E` is the accent for IFF and for what a slide points at, and blue `#3474B8` and teal `#1D7F79` tell two cases apart. Hydrogen is white, carbon slate grey, nitrogen blue, oxygen red, silicon sand, phosphorus orange, calcium green, platinum silver, gold yellow and rhodium teal. Lato is the only typeface, in the figures and on the slides. Figures that are mostly one shaded scene are saved as JPEG, and the rest as PNG, which keeps their lines and text sharp.

## The rule behind the animation

The animation on slide 2 illustrates the idea behind the opening question, that the faces molecules stick to grow slowest and end up covering the crystal. It is not a simulation from the paper or from anywhere else, and `source/growth.py` writes out the whole rule.

- Platinum atoms sit on the sites of the ideal platinum lattice. The crystal starts as a cuboctahedron, with 10 layers of atoms from its centre to each of its six square faces and to each of its eight triangular faces.
- Every face grows one layer of atoms at a time. Each layer starts as an island around a random point on its face, clear of the peptides, and spreads until it covers the face, with up to 2.9 Å of random extra distance roughening its edge. Each face starts at a random point in its first layer, so the faces do not keep step.
- A square face adds one layer per unit of time and a triangular face, where TFT lies, adds a quarter of a layer. If every face grew at the same rate, the crystal would keep its shape, because both kinds of face would move out in proportion to their distance from the centre. At these rates the square faces shrink and vanish at 20 units, and the crystal is then an octahedron, which has only triangular faces. The first frame has 4,460 atoms and the last 22,588, counting the layers still spreading.
- TFT lies flat on the triangular faces with its phenylalanine ring down, posed the same way as S7 lying flat on the platinum slides. One copy sits at the centre of each triangular face from the start. More copies arrive, falling the last 10 Å onto the face, wherever one fits with every atom at least 1 Å inside the face’s edges and 3 Å from every other copy, 58 copies in all. Each copy steps up onto a new layer just before the layer’s spreading edge reaches it.
- The atoms in the outer layer of a square face are tinted blue, so the square faces can be seen shrinking. The 81 frames run evenly from 0 to 20 units, each 600 pixels square. The GIF holds its first frame for 1 second and its last for 1.5 and loops every 8.8 seconds. All frames share one palette of 255 colours without dithering, so what does not change between frames stays still and the file stays under 3 MB. The last frame is also saved as `assets/growth-end.jpg`, the still shown in the PDF and to readers who ask for reduced motion.
- One random seed fixes the islands, the timings and the peptides, so every rebuild draws the same animation.

The octahedron is not the shape the experiments found. With F they found tetrahedra, which also have only triangular faces, and the rule cannot say why one formed rather than the other. The notes on slide 2 say so.

## The numbers behind the plots

`source/parameters.json` holds every published parameter with its source and page. It has the 12-6 values for rhodium, iridium, calcium and strontium and the 9-6 values for rhodium from Kanhaiya et al. (2021), Table 1, the mixing rule that paper uses for unlike pairs, the measured and computed size, surface energy and stiffness of rhodium from its Tables 2, 3 and 5, and the Coulomb constant 332.064 kcal Å mol⁻¹ e⁻², derived from the 2022 CODATA constants.

`science.py` computes the worked numbers from those parameters and checks them. It covers the pair energies and forces, the mixed rhodium–calcium pair, the curve a program draws when r₀ is mistaken for σ, the Coulomb energies, three rhodium atoms in a triangle, the atoms in a face-centred cubic cell and the gap between the computed and measured stiffness. The force must equal minus the slope of the energy, the 12-6 curve must match the textbook 4ε form with σ = r₀/2^(1/6), each curve’s lowest energy must be −ε at r₀, and each number quoted on the slides and in the notes must come out to the digits shown. It writes `source/data/science-checks.json` and `source/data/lj-curves.csv`, and the plots on slides 8, 9 and 14 call the same functions. These checks confirm the algebra and the arithmetic, not that a model is accurate for a new material. Results from the published examples are quoted from the papers, with page and figure locators in `citation-license-manifest.json`.

## How the slides are laid out

`source/story.json` gives each slide a name, a layout (cover, figure or bookend), a kicker, a title, two to four plain sentences of explanation (`lede`, or `body` on the answer slide), a closing line (`takeaway`), its figure and alt text, the speaker’s notes and its sources. The answer slide adds `signoff`, its last line, and `qa`, which makes it the page the Q key opens. Slide 2 adds `animation`, `animation_still`, `animation_alt` and `animation_caption`, which put the animation in a 540-pixel square at the right of the figure row with its caption under it, beside a narrower figure. A slide’s `refs` appear in its footer, and its `note_refs` are sources only its notes cite. `build.py` places every element at the same coordinates in the viewer and in the PowerPoint file, whose page is 13⅓ × 7½ inches. On a figure slide the title takes a left column, the explanation a right column, and the figure fills the box below them. The build stops if any text overflows its box, if a figure would have to shrink to fit its box, if a source is cited but not listed or listed but not cited, or if Lato lacks a character used on a slide. It also writes `presenter-notes.md` and rewrites `citation-license-manifest.json` from the story, so check those sources against the slide claims whenever the story changes. The PowerPoint file carries the animated GIF itself, which PowerPoint plays in a slide show. `export.py` turns the PowerPoint file into the PDF through LibreOffice, which keeps the PDF text selectable, and gives the PDF the animation’s still in its place. Both files name Sean Florez as author. The PowerPoint file leaves lastModifiedBy empty, and the PDF takes its title and subject from the PowerPoint file and leaves its creator empty.

The viewer embeds its fonts and pictures, so it needs no network. The animation is the one file it loads from `assets/` beside it, and a reader whose system asks for reduced motion sees its still instead. Arrow keys, edge clicks and swipes move between pages. Digits then Enter jump to a page, Q opens the answer slide for questions, O or G opens the overview, F toggles full screen, and H or ? opens help. T opens the reading version, every slide in order with its notes, and T or Esc returns to the slides. Clicking or tapping a picture in the reading version enlarges it, except the animation, which plays at its own size. The address accepts page numbers, slide names such as `#lj`, and `#read`, and the reading version opens by itself on a phone held upright.

## Rebuilding and checking

Use Python 3.12 with the versions pinned in `source/requirements.txt`, in an environment kept outside the site folder because Hugo publishes everything under `static/`, and install the test browser with `python -m playwright install chromium`, or set `CHROME` to an existing Chromium. The PDF needs LibreOffice 26.2 on the path, and LibreOffice needs Lato. The font files and their notices are in `source/fonts/`, so install them if the system lacks Lato, and do not let another font stand in when checking the export. The site check needs Hugo 0.140.2 extended.

Run these in order. The export needs a new folder outside the bundle each time.

```sh
python source/science.py
python source/figures.py
python source/build.py
python source/export.py --work-dir /tmp/iff-export-1
python source/title.py index.html ../../images/writings/interface-force-field-title.png
python source/verify.py
python source/interact.py index.html /tmp/iff-viewer
python source/manifest.py
hugo --source ../../.. --destination /tmp/iff-site --minify
```

1. `science.py` writes `source/data/science-checks.json` and `source/data/lj-curves.csv`, and stops if a check fails.
2. `figures.py` draws every picture into `assets/`, or only those named, as in `python source/figures.py cover lj`. The name `growth` draws the animation `assets/growth.gif` and its still `assets/growth-end.jpg`, which takes about two minutes.
3. `build.py` writes `index.html`, `downloads/iff-visual-showcase.pptx`, `presenter-notes.md` and `citation-license-manifest.json`.
4. `export.py` writes `downloads/iff-visual-showcase.pdf`, keeping its LibreOffice profile and the intermediate files in the work folder. It converts a copy of the PowerPoint file with the animation’s still in place of the GIF, because a PDF page cannot move.
5. `title.py` captures the title image for the Writings page, the site’s `static/images/writings/interface-force-field-title.png`, from the viewer’s actual first slide at 1920 × 1080.
6. `verify.py` checks that the viewer, the PowerPoint file and the PDF agree. Every title, explanation and closing line must be editable in the PowerPoint file and selectable in the PDF, every note and source must be in the PowerPoint notes, the metadata must be clean, and the corrected facts and wordings must be present. The animation must appear on its slide and in the reading version, each with its still, and as one animated GIF in the PowerPoint file, its caption must be in the PowerPoint file and the PDF, and the GIF must loop in 6 to 12 seconds within 3 MB. It exits with an error if any check fails.
7. `interact.py` opens the viewer in a headless browser on a 1440 × 900 laptop, a 390 × 844 phone held upright and the same phone on its side. It checks the reading version, the keys, the buttons and the enlarged pictures, confirms that the animation loads and moves on the laptop’s slide 2 and in the phone’s reading version and that reduced motion shows its still, confirms that the reading version never scrolls sideways and that the console shows no errors, and saves a screenshot of each state in the folder given.
8. `manifest.py` records the size and SHA-256 hash of every file in the bundle and of the title image in `artifact-manifest.json`, leaving out the manifest itself. Run it last, and again after any change to the bundle.
9. The Hugo build must finish without errors. In its output, `writings/interface-force-field/` must link the viewer and both downloads, `projects/interface-force-field/` must redirect to it, and the published viewer, PowerPoint file and PDF must match the bundle byte for byte.

The scripted checks do not replace looking. After a rebuild, look at every slide at full size in the browser and in the PDF, then at the reading version on a phone 390 pixels wide and on a laptop, including an enlarged picture. Check for clipped labels, changed line breaks, pictures that no longer match their words, the downloads and the selectable PDF text.

## How the presentation was revised

This bundle replaced a 35-slide version from 3 October 2026. The dates below are in Mountain Time.

### 3 November 2026, a 68-slide rebuild

The talk was rebuilt for a reader with high-school science and no background in simulation, and its Writings page was made to match the site’s other two talks. It gained a section on molecular mechanics with the real Lennard-Jones and Coulomb plots, the worked numbers for rhodium, and six published examples. Its pictures drew atoms as large space-filling spheres, as requested at the time, and many slides were grids of four text cards.

### 4 November 2026, an independent review

A review of all 68 slides and their notes judged 36 clear, 28 in need of work and 4 likely to lose a newcomer. It confirmed the science, including the equations, the rhodium tables and all 2,800 rows of curve data, and it found that all 23 sources resolve. It ranked eight changes.

1. State the problem IFF solves, and its answer, near the start.
2. Replace decorative atom pictures with diagrams that mark the distance, angle or rotation and show a second state.
3. Make each published example visible and specific, with its mechanism and one measured or calculated result.
4. Fix five factual points. Most atoms, not all, have neutrons. A label called a simulation an experiment. A residue’s position was misstated. A cement result needed its locator and the scope of its patent comparison. An uncertainty that could not be verified was dropped.
5. Remove a vendor name everywhere it appeared.
6. Shorten the detours and explain each remaining term where it first appears.
7. Give a reader without the speaker a way to read the notes, with text readable on a phone.
8. Rebuild and recheck every export.

The review also asked to keep the space-filling spheres. The next round’s feedback overtook that request.

### 4 November 2026, real structures

The next round asked for real molecules, surfaces and polymers, said space filling was no longer a constraint and the best visuals were the goal, and asked for each idea to be shown in whatever form explains it best, with or without spheres. Every picture was redrawn from the crystal files, lattice sizes and molecules described above. General 3D renderers were considered, but a small ray tracer was written instead, so the pictures need nothing beyond the pinned Python packages and every label can be placed from the same projection as its atoms. Spheres stayed only for metals and ions, where packing matters. Molecules became balls and sticks so their bonds and shapes show. Minerals first drawn as balls and sticks looked like scattered beads, so they show their SiO₄ and PO₄ building blocks instead. The text-card grids were cut or turned into pictures, and the viewer gained the reading version with the notes and a layout for phones. That pass came to 31 main slides and 6 backup slides.

### 4 November 2026, 15 slides

Thirty-one main slides were too many, and the limit became 15 slides in all. Sixteen main slides and all six backups were cut, and their content moved into the speaker’s notes of the slides that kept those topics, with `note_refs` keeping their sources. The notes now carry the springs, twists and slopes behind the energy terms, the mixing rules, the unit cell, stiffness, the 9-6 curve and three of the six examples (peptides on silica, cement grinding and gold). Three examples stayed on slides, each on a different kind of surface.

### 5 November 2026, the five kinds of energy term

The slide on the five kinds of energy term drew all five on one picture, and its arrows were confusing and sat away from the atoms they meant. It became five panels of the same ethanol and water. Each panel keeps only the atoms involved in colour and draws its motion on the real geometry. A two-way arrow runs beside the O–H bond and parallel to it, an arc sits round the oxygen between its two bonds, an arrow turns round the C–C bond in front of the methyl hydrogens, a dotted line joins two ringed hydrogens for van der Waals, and δ+ and δ− mark the hydroxyl hydrogen and the water oxygen for the charges. Eight versions were drawn and compared at full size. Dimension lines with end dots were too heavy, a view from below turned the water edge-on, and arrowheads with white halos looked fussy, so those were dropped. One arrowhead covered a carbon atom until its arc moved outward.

### 5 November 2026, words on every slide

The pictures were clear but hard to follow without a speaker, so each slide gained two to four plain sentences on what is shown, what happened and why it matters, and the notes kept the detail and citations. The title moved into a left column and the words into a right column, above a fixed figure box, and the figures that did not fit that box were laid out again. Three other layouts were tried and dropped. A column of words beside a narrower figure would have shrunk the labels inside the figures, a band across the full width made the lines too long to read, and two labelled columns read like the old text cards.

The same round made five more changes.

- The crystal-shape result now says that one amino acid “shifted platinum crystals from cubes toward tetrahedra”, the wording the cited paper supports, and the arrow on slide 2 reads “shifts toward” to match.
- The three example slides are titled “Example 1:” to “Example 3:”, and their kickers name only the topic.
- The IFF Agent slide, which listed its eight steps in words, became eight small pictures in the style of the other figures. They run from the rhodium face in water through the papers and measurements, the pair curve, the crystal’s repeating cube, the fitted curve, the stretching test (209 against 379 GPa) and the check of the exported numbers, to the decision. Flow arrows were left out, because the numbered markers and the two groups already give the order.
- A slide on why this matters follows the opening question. It shows four places where molecules meeting a surface matter (platinum catalysts, gold rods studied for cancer treatment, the mineral of bones and teeth, and the grinding of cement), each from a cited paper or patent. Claims the sources do not support, such as bone implants or a figure for faster grinding, were left out.
- The thank-you slide joined the answer slide, which now ties the story back to what the model lets researchers test on a computer before anything is made.

### 5 November 2026, a second review

A second independent review read the 15 slides as a newcomer would and checked each new or reworded claim against its source. It ranked seven fixes, and all seven were made.

1. The heated silica on slide 12 had been drawn by deleting the hydrogens of the OH groups, which left oxygens bonded to a single silicon. Both surfaces are now cut from cristobalite and built as described above, following the Q3 and Q4 definitions of Emami et al. (2014), and the new bridges are marked. A count of the structures confirmed that every silicon has four oxygens, that every oxygen joins two silicons or a silicon and a hydrogen, that the OH-covered face carries 4.7 groups per nm², and that heating removes exactly 8 water molecules per cell. The slide explains what an OH group is, and its notes give the reaction.
2. Slide 4 no longer gives one percentage for how well IFF agrees with experiment. It says that IFF is calibrated to the measured lattice size and surface energy, which are targets rather than tests, and that selected interfaces were tested separately. Its notes add that some metal–water values are known only as upper limits and that binding of organic molecules agrees to about 5 to 10%, and the 50% shortfall is now attributed only to some of the metal-only models compared.
3. The platinum slides keep the result, that one amino acid shifted the crystals from cubes toward tetrahedra, for the peptide versions tested. On the square face adsorption is now called less favourable, computed at +3 kcal/mol, rather than ruled out. The step from a crystal with only triangular faces to a tetrahedron was removed, and the answer slide’s notes point out that an octahedron also has only triangular faces.
4. The twisting term’s k is described as a coefficient that sets a wave rising from 0 to 2k. The 12-6 and 9-6 powers are named as those of the energy, with the powers of the force beside them. The Coulomb slide plots interaction energies, and the factor of 80 for water is the value for bulk water treated as a smooth background, with explicit water molecules needed close to the ions. Slide 4 now says, as its notes do, that nothing set how a metal atom and a water molecule should interact.
5. Broad claims were narrowed. Quantum chemistry is now compared with force fields by typical cost and size, on slide 6 and in its figure’s captions, and its accuracy is said to depend on the method. Energy minimization finds a nearby local minimum. The σ convention is tied to LAMMPS’s lj/cut and lj/class2 styles, and the 21.3 Å crystal is labelled a scaling estimate. The cutoff note explains how many weak pairs beyond the cutoff can add up. Slide 10’s title is about rhodium, and the cover’s notes list every calculation made for the pictures.
6. The gold rods’ caption on slide 3 now says that their surfaces interact with water and biomolecules. The answer slide’s notes call PCFF-SILICA an early silica model in the IFF lineage and describe the gold measurement as water adsorbed from vapour onto gold made of many small crystals.
7. Comments with file paths and user names were removed from the crystal files, keeping their data and attribution, and the revision history above now speaks of molecules without naming the software that built them. The manifest was refreshed.

### 5 November 2026, a growth animation

Slide 2 gained an animation of a platinum crystal growing with peptides on its triangular faces, so a reader can watch the faces that grow slowest end up covering the crystal. Its rule is described above. Two earlier versions were dropped. Atoms added one at a time at random places on the surface grew rough, rounded crystals with no clear faces, and the seven-amino-acid peptide S7 did not fit on the faces of a crystal small enough to show its atoms clearly, so the shorter TFT from the opening question took its place. A fade from the last frame back to the first was also dropped, and the frames were drawn at 600 pixels rather than 675, to keep the file under 3 MB. The figure on slide 2 was laid out again at 1160 pixels wide to make room, with its crystals and labels a little smaller. The caption and the notes say that the animation is an illustration of the idea, not a simulation from the paper, and the notes add that the experiments found tetrahedra rather than octahedra.

## How the pictures were checked

Every figure was opened at full size, and close crops confirmed that labels, arrows and atoms line up and that nothing overlaps or is clipped. Every slide was captured in the browser at 1920 × 1080, and every page of the reading version on a 390-pixel phone and a 1440-pixel laptop. Contact sheets of all the slides from the browser and from the PDF were compared side by side. The animation was watched on slide 2 and in the reading version on both screens, and a contact sheet of its frames confirmed that the square faces shrink and vanish, that no blue appears on a triangular face and that every peptide stays on its face. The scripted checks above confirmed that the three formats agree, that the notes and sources are complete, and that the viewer works with keys, clicks and touch.
