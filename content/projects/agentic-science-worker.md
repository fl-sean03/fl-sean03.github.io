---
title: "Agentic Science Worker"
description: "Autonomous AI infrastructure for computational materials research"
date: 2026-01-15
---

Most discoveries die between the lab and the real world. But there's an earlier bottleneck: before you can translate a discovery, you have to make it. And the rate of discovery in computational materials science is throttled not by compute, not by theory, but by the human overhead of running the loop.

Find the paper, extract the parameters, configure the simulation, submit the job, wait, parse the output, check it against what's known, decide what to run next. Each step is trivial. Together, they determine how many questions actually get asked.

Agentic Science Worker is my attempt to remove that overhead. Built on Claude Code, it operates as an autonomous computational scientist that handles the full execution loop while the researcher stays in control of direction.

**What it does:**
- Molecular dynamics via LAMMPS with literature-derived parameters
- Density functional theory calculations via Quantum ESPRESSO
- Materials database queries and literature extraction
- HPC job submission and orchestration
- Result validation against published benchmarks

The system doesn't guess. It validates against published results. It documents its reasoning. It maintains scientific standards while removing the friction that makes those standards expensive to uphold.

I built an 11-tier benchmark framework to evaluate it, from single-tool tasks through frontier HPC+ML hybrid workflows. Full logging, full reproducibility. If it can't be verified, it doesn't count.

This project applies the same thesis I hold for materials: work dies from friction, not from being wrong. The value is in removing that friction, whether between lab and deployment or between question and answer.

[github.com/fl-sean03/agentic-science-worker](https://github.com/fl-sean03/agentic-science-worker)
