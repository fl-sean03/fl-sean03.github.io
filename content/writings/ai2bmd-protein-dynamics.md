---
title: "Learning Protein Dynamics from Quantum Fragments"
subtitle: "A talk on a 2024 Nature paper that simulates proteins with quantum-trained AI"
date: 2026-10-21
image: "/images/writings/ai2bmd-protein-dynamics-title.png"
image_alt: 'Title slide of the deck, "Learning protein dynamics from quantum fragments," with the paper title, "Ab initio characterization of protein molecular dynamics with AI²BMD," beside Fig. 1 from Wang et al. (2024), which follows proteins split into small units through DFT datasets and the AI²BMD potential to simulated trajectories, ending in panels on ab initio accuracy, kinetics, thermodynamics and agreement with wet-lab experiments.'
links:
  - label: "Read the slides"
    url: "/decks/ai2bmd-protein-dynamics.html"
  - label: "Download PowerPoint (.pptx)"
    url: "/decks/ai2bmd-protein-dynamics.pptx"
    download: true
  - label: "Download PDF"
    url: "/decks/ai2bmd-protein-dynamics.pdf"
    download: true
---

Talk given in a foundation models and alignment course at CU Boulder, September 28, 2026. It covers Wang et al., "[Ab initio characterization of protein molecular dynamics with AI²BMD](https://doi.org/10.1038/s41586-024-08127-z)," *Nature* 635, 1019–1027 (2024). Quantum calculations like density functional theory (DFT), which works out where the electrons sit, are accurate but far too slow for whole proteins. Classical force fields, which treat atoms as charged balls on springs, are fast but approximate. AI²BMD learns from DFT on small fragments and reuses that across whole proteins.

**[Read the slides in your browser](/decks/ai2bmd-protein-dynamics.html)** (23 slides including backups, arrow keys to move) · [PDF](/decks/ai2bmd-protein-dynamics.pdf) · [PowerPoint](/decks/ai2bmd-protein-dynamics.pptx)

---

## From fragments to a whole protein

The authors cut a protein into overlapping fragments, one per amino acid, with small chemical caps at the cuts. Twenty kinds of amino acid plus a shared cap piece make 21 fragment types. DFT computed energy and atomic forces for 20.88 million fragment snapshots in different shapes. The dataset took about 12.93 million CPU core-hours.

Every fragment type gets its own learned potential, a geometry-aware neural network that turns atom positions and elements into an energy. Each atom's force is the downhill slope of that energy, so the two always agree. A new protein reuses the same 21 models.

AI²BMD adds up the fragment energies and subtracts the overlapping caps so nothing counts twice. Classical terms connect atoms in separate fragments, and a polarizable force field, whose charges shift with their surroundings, handles the water. The paper's simulation results describe this whole hybrid.

---

## What the paper shows

Against whole-protein DFT on five smaller proteins, AI²BMD's average force error was 1.974 kcal/mol per ångström, about a quarter of the classical force field's 8.094. (kcal/mol is an energy unit, and an ångström is 0.1 nanometers.) Four larger proteins, up to 13,728 atoms, were checked against fragmented DFT. These short tests measure agreement with DFT, not with experiment.

For Trp-cage, a 281-atom protein, one energy calculation took 0.072 seconds with AI²BMD and 21 minutes with DFT, about 17,500 times longer. DFT times for large proteins are extrapolated. Full simulation steps in water take more work, and conventional classical simulation still runs those faster.

Nuclear magnetic resonance (NMR), the physics behind MRI, measures J couplings, values in hertz tied to backbone twist angles. Couplings predicted from simulated angles correlated with experimental ones at 0.924 for AI²BMD and 0.543 for the classical force field, where 1 is a perfect straight-line match. That covers one aspect of backbone shape. Other measurements and systems would test the model further.

Chignolin, a protein only 10 amino acids long, folded and unfolded in selected AI²BMD runs of up to 10 nanoseconds. These examples leave open how much time chignolin spends folded and how fast it switches.

For two proteins, barnase and CI2, AI²BMD recomputed the energies of shapes sampled with a classical force field. The unfolding enthalpy, the heat it takes to unfold the protein, came out at 116.5 kcal/mol for barnase, against 110.4 classical and 118.7 measured. For CI2 it was 73.0, against 57.1 and 78.4. Recomputing energies can't add shapes the sampling missed.

---

## What I make of it

Accuracy depends on the reference, the chemistry and the sampling.

The reference is one chosen version of DFT, applied in fragments and joined by classical terms. Matching it shows the model is faithful to that setup, which is why the experimental checks matter. My earlier talk, [Where Are We with Materials AI](/writings/where-are-we-materials-ai/), makes the same point.

The chemistry is the vocabulary of 21 fragment types. Molecules bound to the protein, unusual amino acids, changed charge states and chemical reactions need evidence this study doesn't provide.

The sampling has to reach the shapes that matter for each property. For the recomputed energies, I didn't find checks that the classical samples cover the shapes AI²BMD favors.

I see the main contribution as the combination of the fragment split, quantum dataset, geometry-aware network and experimental checks. Extending it to materials or other chemistry would need its own vocabulary, training references and checks against measured properties.

For the course, I tied the paper to reuse and to choosing training targets and evaluation. My takeaway is that trustworthy reuse depends on the whole system of models and sampling. The alignment connection is my interpretation. What a model optimizes should match what users care about.

What evidence would we require before reusing a potential like this in unfamiliar chemistry?

---

## Credits

Figures in the slides are reproduced or adapted from Wang et al., *Nature* (2024), under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). [The authors' code](https://github.com/microsoft/AI2BMD) is public.
