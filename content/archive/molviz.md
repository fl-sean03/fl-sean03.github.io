---
title: "MolViz"
description: "Browser-native molecular visualization for computational workflows"
date: 2025-11-01
---

Every computational chemist has a dozen visualization tools open — VMD for trajectories, OVITO for defects, PyMOL for proteins, a notebook for plots. Nothing talks to anything else. Context switching eats hours per day.

**The thesis:** Visualization should live next to the computation, in the browser, wired to the same data stream the job outputs. One viewer, one URL, real-time trajectory streaming, no local install.

**Why it's parked:** The right wedge turned out to be the agentic science worker, not the viewer. Once an agent is running the simulations, you don't need the human-optimized UI — you need machine-readable outputs and an occasional publication figure. MolViz becomes a thin render layer on top, not a product.
