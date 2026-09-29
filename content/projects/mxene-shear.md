---
title: "MXene Interlayer Shear"
description: "Molecular dynamics on what sets the shear resistance between MXene layers, from hydration to surface termination."
date: 2026-09-28
status: "In preparation"
period: "2025–present"
role: "Lead author"
thread: "models"
weight: 2
---

MXenes are conductive two-dimensional materials, and they're promising for electromagnetic shielding in composites. Each layer's surface carries chemical groups such as OH and F, its termination. To use them you need to understand how the layers hold together and slide apart.

At the Air Force Research Laboratory in summer 2025 I built a LAMMPS workflow that shears OH-terminated Ti<sub>3</sub>C<sub>2</sub> bilayers under controlled hydration, and I ran the stress sweeps on DoD HPC. Fitting slip probability against applied shear stress showed that hydration is non-monotonic. A little water lubricates the interface, and full coverage rebuilds strength as water forms bridging hydrogen bonds. Water is a knob that moves shear strength by an order of magnitude, which gives stress windows for EM-shielding composite design.

The production campaign at CU Boulder varies the termination. I sheared bilayers capped with OH, with F, and with a mix in LAMMPS on the Alpine cluster, and termination sets the shear resistance across roughly a threefold range. The geometry dependence is chemistry-specific, since the two box geometries differ for F and mixed terminations and coincide for OH.

- Dry bilayers hold to 103 MPa. A quarter monolayer of water drops that to 8 MPa, and full coverage recovers to 39 MPa.
- The shear resistance, τ<sub>0.5</sub>, runs from 42 to 135 MPa across terminations, OH above mixed above F.
- The campaign is 780 NVT shear trajectories across six termination and geometry cells, ten seeds per stress, and zero failed runs.

A persistent disagreement with published reference values traced back to the NPT equilibration step, so the protocol moved to minimize-only plus NVT shear. I froze the protocol before production and had the campaign audited afterward. The audit re-derived every reported critical stress from raw trajectories with an independent re-implementation of the slip classifier, and it caught an inflated trajectory count in the campaign's own reporting before it reached the manuscript.

Understanding why hydration and termination matter at the molecular level lets you predict which processing conditions will reach target properties. That's what connects atomic-scale physics to manufacturing guidance.

Manuscript in preparation, with me as lead author and co-authors at the AFRL Materials & Manufacturing Directorate and CU Boulder. I've also run a molecular dynamics campaign on [hydrogen release from N-ethylcarbazole on platinum nanocrystals](/projects/pt-hydrogen-release/).
