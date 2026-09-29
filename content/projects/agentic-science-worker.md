---
title: "Agentic Science Worker"
description: "Autonomous AI infrastructure for computational materials research"
date: 2026-01-15
status: "Past"
period: "2026"
role: "Creator"
thread: "loop"
links:
  - label: "Repository"
    url: "https://github.com/fl-sean03/agentic-science-worker"
image: "/images/projects/agentic-science-worker.png"
image_alt: "Bar plot of an experimental X-ray diffraction pattern for LiNiO2 (black, above the axis) against the calculated R-3m pattern (blue, below), from 10 to 70 degrees 2θ, with the main reflections labeled."
---

Most discoveries die between the lab and the real world. But there's an earlier bottleneck. Before you can translate a discovery, you have to make it. And the rate of discovery in computational materials science is throttled not by compute, not by theory, but by the human overhead of running the loop.

Find the paper, extract the parameters, configure the simulation, submit the job, wait, parse the output, check it against what's known, decide what to run next. Each step is trivial. Together, they determine how many questions actually get asked.

Agentic Science Worker was my attempt to remove that overhead. Built on Claude Code, it operated as an autonomous computational scientist that handled the full execution loop while the researcher stayed in control of direction.

It ran molecular dynamics in LAMMPS with parameters taken from the literature, and density functional theory calculations in Quantum ESPRESSO. It queried materials databases, extracted information from the literature, submitted and orchestrated HPC jobs, and validated results against published benchmarks.

The system didn't guess. It validated against published results. It documented its reasoning. It maintained scientific standards while removing the friction that makes those standards expensive to uphold.

I built an 11-tier benchmark framework to evaluate it, from single-tool tasks through frontier HPC+ML hybrid workflows. Full logging, full reproducibility. If it couldn't be verified, it didn't count.

This project applied the same thesis I hold for materials. Work dies from friction, not from being wrong. The value is in removing that friction, whether between lab and deployment or between question and answer.

[github.com/fl-sean03/agentic-science-worker](https://github.com/fl-sean03/agentic-science-worker)
