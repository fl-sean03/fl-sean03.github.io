---
title: "Heinz Lab Agent"
description: "Autonomous research infrastructure for the Heinz Interfaces Laboratory at CU Boulder"
date: 2026-02-20
status: "Past"
period: "2026"
role: "Creator"
thread: "loop"
links:
  - label: "GitHub"
    url: "https://github.com/Heinz-Laboratory"
---

Autonomous research agent for the [Heinz Interfaces Laboratory](https://bionanostructures.com/), a computational materials science group at CU Boulder focused on interfacial force fields, hybrid organic-inorganic perovskites, and MXenes. Ran on the [Seed Fleet](/projects/seed-fleet/) with scientific capabilities inherited from the [Agentic Science Worker](/projects/agentic-science-worker/) toolkit. Persistent, always-on, integrated into the lab's Slack. The fleet has since been retired.

Day to day, it automated IFF parameterization, taking a CIF structure in and returning classified atom types and force field parameters as JSON and PDF reports. It was validated on NaCl and applied to 2D perovskite systems like (2-BrPEA)2PbI4.

It ran weekly arXiv literature scans filtered to the lab's research areas (MLIPs, MXenes, halide perovskites, force fields, interfaces). By March 2026 it had produced 17+ structured deep paper analyses, covering MACE fine-tuning benchmarks, MXene MLIP gaps, and uncertainty quantification calibration.

In Slack it posted status updates and result summaries, shared files, and held threaded conversations with lab members. Its structure utilities, built on ASE, handled CIF and POSCAR input and output, supercell generation, and analysis. Its persistent memory held 37 knowledge files as of March 2026, covering people, projects, infrastructure, research themes, and lessons learned.

The lab agent spawned dedicated project agents for long-running complex work. The axiom-agent built a production molecular visualization tool across 72 hours of continuous autonomous development (React/TypeScript frontend, direct WebGL renderer, CIF/XYZ/PDB parsing, PNG/PDB/CIF export). Other project agents were scoped for MLIP validation, trajectory analysis automation, and experimental data pipelines connecting DFT predictions to XRD, DSC, and other characterization measurements.

The lab agent shipped three projects.

- [axiom-gui](https://github.com/Heinz-Laboratory/axiom-gui) is a high-performance web-based tool for molecular structure visualization, with a production-grade WebGL renderer and multi-format support.
- perovskite-iff-autoparameterization is an automated IFF parameterization pipeline for hybrid organic-inorganic perovskites, from CIF input to validated force field output.
- lab-agent-infrastructure backs up the agent's full system state and provides disaster recovery, covering memory, scripts, config, and conversation history.

The lab agent completed a seven-phase, publication-ready research workflow autonomously, from hypothesis formulation through literature review, simulation configuration, execution, result validation against published benchmarks, and analysis to a formatted manuscript. Every step was fully logged and reproducible.

The roadmap included autonomous materials screening (hundreds of candidates evaluated against target properties), active learning loops for training lab-specific interatomic potentials, and a searchable data warehouse for every simulation the group has run.

[github.com/Heinz-Laboratory](https://github.com/Heinz-Laboratory)
