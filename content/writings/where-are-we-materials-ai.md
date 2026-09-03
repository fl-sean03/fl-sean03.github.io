---
title: "Where Are We"
subtitle: "Materials AI, and where its training labels come from"
date: 2026-09-03
image: "/images/writings/where-are-we-title.png"
---

I gave this talk in a foundation models and alignment course at CU Boulder. The assignment was to present the state of practice in your own field, name the methods people actually use, and say where they break.

My field trains machine-learned interatomic potentials. MACE, GNoME, MatterSim, UMA. They are foundation models by any working definition: train once on one broad corpus, then run zero-shot on systems the model never saw. They work, and the scaling curves hold. One of them covers platinum surfaces, which is my own system, and I did not train it.

Every label they learn from is a calculation. Density functional theory approximates quantum mechanics, and a model that reproduces it perfectly inherits its disagreements with measurement too. Here is the number that stuck with me: a titanium potential accurate to 6 meV per atom against DFT is 24 percent wrong on shear modulus when you check it against experiment. The model is not bad. It is faithful to the wrong reference.

The rest of the deck is about three places that shows up. Where the labels come from and what a measurement would change. Why nothing connects a prediction about atoms to a property anyone would buy. And what happens when you optimize hard against a number that a model computed, which is the closest thing this field has to an alignment problem, and it behaves differently from the version people argue about in language models.

[Download the slides](/decks/where-are-we-materials-ai.pptx) (PowerPoint, 18 slides)
