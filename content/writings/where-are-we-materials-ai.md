---
title: "Where Are We"
subtitle: "Materials AI, and where its training labels come from"
date: 2026-09-03
image: "/images/writings/where-are-we-title.png"
image_alt: 'Title slide of the deck, "Where are we? Foundation models for materials, and where their labels come from," beside a figure from Unke et al. (2021) that arranges systems from small molecules to proteins between ab initio accuracy and force-field efficiency.'
links:
  - label: "Read the slides"
    url: "/decks/where-are-we-materials-ai.html"
  - label: "Download PowerPoint (.pptx)"
    url: "/decks/where-are-we-materials-ai.pptx"
    download: true
  - label: "Download PDF"
    url: "/decks/where-are-we-materials-ai.pdf"
    download: true
---

Talk given in a foundation models and alignment course at CU Boulder, September 2026. The brief was to present the state of practice in your own field, name the methods people actually use, and say where they break.

**[Read the slides in your browser](/decks/where-are-we-materials-ai.html)** (18 slides, arrow keys to move) · [PDF](/decks/where-are-we-materials-ai.pdf) · [PowerPoint](/decks/where-are-we-materials-ai.pptx)

**What is in it.** Machine-learned interatomic potentials as foundation models: MACE, GNoME, MatterSim, UMA. How density functional theory, hand-written force fields and learned potentials each answer the same question, which is what a given arrangement of atoms costs in energy. What scaling the training data bought. How that data gets manufactured in the first place.

Then three limitations.

**Where the labels come from.** Every one is a calculation. A titanium potential accurate to 6 meV per atom against DFT is 24 percent wrong on shear modulus when checked against experiment. The model is not bad. It is faithful to the wrong reference.

**Atoms to parts.** Ten orders of magnitude in length, fifteen in time, and every handoff between levels is fitted by hand. Foundation models occupy the first level only.

**What we optimize.** Energy above hull is a computed stand-in for a question nobody can write down, and pushing hard on it drives the model into the region where its own scorer was never valid.

The deck closes on the companies funding autonomous labs to fix this, and on what they have published so far.
