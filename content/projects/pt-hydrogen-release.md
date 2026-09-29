---
title: "Hydrogen Release on Pt Nanocrystals"
description: "How N-ethylcarbazole, a liquid organic hydrogen carrier, gives up its hydrogen on platinum nanocrystals, and which surface sites do the work."
date: 2026-09-28
status: "In preparation"
role: "Lead author"
thread: "models"
weight: 3
---

[Liquid organic hydrogen carriers](https://en.wikipedia.org/wiki/Liquid_organic_hydrogen_carrier) are organic compounds that store hydrogen chemically, and N-ethylcarbazole is one of them. Getting the hydrogen back out takes heat and a catalyst, and it's generally seen as the main drawback of the approach. Platinum nanocrystals can do the job. The question is how the release happens on their surface, and which sites do the work.

I designed and ran the molecular dynamics campaign behind the first paper. It simulates slabs, flat platinum surfaces that isolate one facet at a time, and cuboctahedral nanoparticles, which have flat faces, edges and vertices. Dehydrogenation-reactive configurations concentrate at low-coordination sites, the surface atoms with the fewest neighbors, so local coordination rather than facet identity sets where release happens.

- 60 slab production runs across three Pt facets, plus cuboctahedral nanoparticle ensembles, with zero production job failures.
- Vertices carry 5.4× the per-atom contact density of {100} terraces and 2.9× that of {111}.
- A per-area normalization makes facets, edges and vertices comparable, and the finite nanoparticle is validated against infinite slabs facet by facet.

A slab isolates one facet, so it can't show that a vertex carries several times the per-atom contact density of a terrace.

I also wrote the technical narrative for the allocation that funds the next campaign, a Director's Discretionary award at the Argonne Leadership Computing Facility of about 26,150 node-hours, awarded in May 2026. [The program](https://www.alcf.anl.gov/science/directors-discretionary-allocation-program) gives start-up awards to researchers preparing for a major allocation.

Manuscript in preparation, with me as lead author. Another simulation campaign of mine is [MXene interlayer shear](/projects/mxene-shear/).
