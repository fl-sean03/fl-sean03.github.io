---
title: "Heinz Lab Agent"
description: "Autonomous research infrastructure for the Heinz Interfaces Laboratory at CU Boulder"
date: 2026-02-20
---

Autonomous research agent for the Heinz Interfaces Laboratory, a computational materials science group at CU Boulder focused on interfacial force fields, hybrid organic-inorganic perovskites, and MXenes. Runs on the [Seed Fleet](/projects/private-agent-network/) with scientific capabilities inherited from the [Agentic Science Worker](/projects/agentic-science-worker/) toolkit. Persistent, always-on, integrated into the lab's Slack.

**Day-to-day capabilities:**
- Automated IFF parameterization: CIF structure in, classified atom types and force field parameters out (JSON + PDF reports). Validated on NaCl, applied to 2D perovskite systems like (2-BrPEA)2PbI4
- Weekly arXiv literature scans filtered to lab research areas (MLIPs, MXenes, halide perovskites, force fields, interfaces)
- Deep paper analysis: 17+ structured analyses to date, covering MACE fine-tuning benchmarks, MXene MLIP gaps, uncertainty quantification calibration
- Slack integration: status updates, result summaries, file sharing, threaded conversations with lab members
- Structure utilities: CIF/POSCAR I/O, supercell generation, analysis (ASE-based)
- Persistent memory: 37 knowledge files covering people, projects, infrastructure, research themes, lessons learned

&nbsp;

**Multi-agent delegation.** The lab agent spawns dedicated project agents for long-running complex work. The axiom-agent built a production molecular visualization tool across 72 hours of continuous autonomous development (React/TypeScript frontend, direct WebGL renderer, CIF/XYZ/PDB parsing, PNG/PDB/CIF export). Other project agents are scoped for MLIP validation, trajectory analysis automation, and experimental data pipelines connecting DFT predictions to XRD, DSC, and other characterization measurements.

**What it's shipped:**
- [axiom-gui](https://github.com/Heinz-Laboratory/axiom-gui): High-performance web-based molecular structure visualization. Production-grade WebGL renderer with multi-format support.
- perovskite-iff-autoparameterization: Automated IFF parameterization pipeline for hybrid organic-inorganic perovskites. CIF input to validated force field output.
- lab-agent-infrastructure: Full system state backup and disaster recovery for the agent. Memory, scripts, config, conversation history.
- [heinz-lab-website](https://heinzlab.org): Lab website built in Astro.

&nbsp;

**Completed a seven-phase publication-ready research workflow autonomously.** Hypothesis formulation through literature review, simulation configuration, execution, result validation against published benchmarks, analysis, and formatted manuscript. Full logging and reproducibility at every step.

The roadmap includes autonomous materials screening (hundreds of candidates evaluated against target properties), active learning loops for training lab-specific interatomic potentials, and a searchable data warehouse for every simulation the group has run. Another research group has already adopted the pattern for their own lab.

[github.com/Heinz-Laboratory](https://github.com/Heinz-Laboratory)
