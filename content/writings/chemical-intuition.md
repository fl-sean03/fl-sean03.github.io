---
title: "Chemical Intuition Through Physics Practice"
subtitle: "A research proposal to train language models on simulated crystal stability"
date: 2026-10-07
image: "/images/writings/chemical-intuition-title.png"
image_alt: "Title slide showing NaCl, silicon, strontium titanate and zinc oxide crystals feeding a simulated stability reward, which updates a language model. The proposed tests cover withheld crystals and chemistry questions in words."
links:
  - label: "Read the slides"
    url: "/decks/chemical-intuition.html"
  - label: "Download PowerPoint (.pptx)"
    url: "/decks/chemical-intuition.pptx"
    download: true
  - label: "Download PDF"
    url: "/decks/chemical-intuition.pdf"
    download: true
---

Presentation 3 for CSCI 7000, a foundation models and alignment course at CU Boulder, October 7, 2026. I propose training a language model to generate crystal structures, using simulated stability as its reward. The question is whether that practice could teach chemical intuition that carries over to unfamiliar chemistry and to questions written in words.

**[Read the slides in your browser](/decks/chemical-intuition.html)** (27 slides including supplements, arrow keys to move) · [PDF](/decks/chemical-intuition.pdf) · [PowerPoint](/decks/chemical-intuition.pptx)

---

## Practicing with a physics reward

The model writes a crystal as text. After basic checks on its format, composition and atom spacing, a learned interatomic potential relaxes the structure and estimates its stability. Reinforcement learning uses that score to update the language model.

The scorer also has limits. It's trained on quantum calculations, and its errors can become a training target of their own. The proposal uses uncertainty estimates to send questionable structures for more expensive density functional theory (DFT) checks.

## What would count as learning

I'd compare the original model, supervised fine-tuning alone, and supervised fine-tuning followed by reinforcement learning. Independent checks would test whether the proposed crystals improve, whether the model handles chemistry withheld from fine-tuning and reinforcement learning, and whether any gains carry over to chemistry in words. The main comparison would also account for extra sampling. The supplementary slides discuss ordinary relaxation as a baseline for a later refinement task.

These are proposed experiments. Better simulated rewards would need independent evidence before I'd call them chemical intuition.

This follows [Where Are We with Materials AI](/writings/where-are-we-materials-ai/) and [Learning Protein Dynamics from Quantum Fragments](/writings/ai2bmd-protein-dynamics/). The slides include the research plan, supplementary derivations and source credits.
