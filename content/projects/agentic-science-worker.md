---
title: "Agentic Science Worker"
description: "Autonomous AI infrastructure for computational materials research"
date: 2026-01-15
---

## The bottleneck before the bottleneck.

My [thesis](/writings/thesis/) argues that materials translation is the binding constraint. Most discoveries die between the lab and the real world because no one builds the bridge.

But there's an earlier problem. Before you can translate a discovery, you have to make it. And the rate of discovery in computational materials science is throttled not by compute, not by theory, but by the human overhead of running the loop: find the paper, extract the parameters, configure the simulation, submit the job, wait, parse the output, check it against what's known, decide what to run next.

Each step is trivial. Together, they determine how many questions actually get asked.

## The vision.

What if the execution layer of computational science was infrastructure, not labor?

Not AI that does science. AI that handles the mechanics so scientists can focus on direction. The researcher decides what matters. The system handles the how: literature search, parameter extraction, simulation configuration, job submission, result validation. Rigorous. Reproducible. Fast.

This changes the rate of iteration. And in research, iteration rate is everything. The person who can test ten hypotheses while someone else tests one doesn't just move faster. They learn faster. They find things others miss.

## The project.

Agentic Science Worker is my implementation of this vision. Built on Claude Code, it operates as an autonomous computational scientist: molecular dynamics via LAMMPS, density functional theory via Quantum ESPRESSO, materials database queries, literature extraction, HPC job orchestration.

The system doesn't guess. It validates against published results. It documents its reasoning. It maintains scientific standards while removing the friction that makes those standards expensive to uphold.

I built an 11-tier benchmark framework to evaluate it, from single-tool tasks through frontier HPC+ML hybrid workflows. Full logging, full reproducibility. If it can't be verified, it doesn't count.

## The connection.

This is the same thesis applied earlier in the pipeline. Translation matters between lab and deployment. It also matters between question and answer. Both are places where good work dies from friction, not from being wrong.

I'm building infrastructure for both.

[github.com/fl-sean03/agentic-science-worker](https://github.com/fl-sean03/agentic-science-worker)
