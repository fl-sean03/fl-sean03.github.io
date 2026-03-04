---
title: "Heinz Lab Agent"
description: "Autonomous AI infrastructure for a computational materials science research lab"
date: 2026-02-20
---

Every research lab runs the same loop. Read the literature. Set up the experiment. Run it. Analyze the results. Decide what to run next. The science is in the decisions. Everything else is overhead, and it consumes most of the day. In a computational materials science lab, that overhead is configuration files, job submission, convergence checks, parameter extraction from papers, data reformatting between tools. Each step is trivial. Together, they determine how many questions the lab actually asks.

The Heinz Lab Agent is a persistent autonomous agent running on the [Seed Fleet](/projects/private-agent-network/) that handles research execution for my PI's computational materials science group. It inherits its scientific capabilities from the [Agentic Science Worker](/projects/agentic-science-worker/) toolkit and runs them as always-on infrastructure rather than tools you invoke. It wakes when work arrives, executes, and goes quiet. The lab doesn't interact with it like a chatbot. It operates like a system.

**What it does:**
- Molecular dynamics via LAMMPS and density functional theory via Quantum ESPRESSO
- Literature extraction: pulls parameters, methods, and benchmarks from papers
- Simulation setup: writes input files, configures jobs, submits to HPC clusters
- Result validation against published data, with full documentation of reasoning
- Slack integration for the research group: status updates, result summaries, question handling
- Custom tooling: building an atomic structure viewer and other lab-specific utilities

The agent completed a seven-phase, publication-ready research workflow autonomously. Hypothesis formulation through simulation execution through analysis to a formatted manuscript. Full logging, full reproducibility. It validates against known results at every step because in computational science, a wrong answer that looks right is worse than no answer at all.

What makes this different from a one-off script or a ChatGPT session is persistence. The agent accumulates context over weeks and months. It remembers which parameters work for which systems, which simulation approaches failed and why, which papers matter for which questions. When a new student joins the lab, that knowledge is structured, searchable, and connected to the tools where the work happens. It doesn't leave when a senior student graduates.

Another research group saw the Slack integration and wanted their own version. Spun one up for them. The pattern is replicable because the underlying infrastructure is general: a persistent agent with domain knowledge, connected to the tools a specific lab actually uses. The scientific capabilities come from the Agentic Science Worker repo. The runtime comes from the Seed Fleet. The domain knowledge is what makes it useful for a specific group.

The lab doesn't need to change how it works. The agent fits into the existing workflow and removes the overhead that prevents results from compounding. The researchers set direction. The infrastructure handles the rest.
