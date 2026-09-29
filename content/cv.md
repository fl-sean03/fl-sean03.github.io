---
title: "CV"
description: "Education, research, research automation, manufacturing and national-security experience, with the full CV and resumes to download."
layout: cv
aliases: ["/resume/"]
resume_pdf: "/Sean_Florez_Resume.pdf"
cv_pdf: "/Sean_Florez_CV.pdf"
variants:
  - label: "Machine learning and research computing"
    url: "/ML_Resume.pdf"
  - label: "National security"
    url: "/NS_Resume.pdf"
---

## Education

### Ph.D., Materials Science and Engineering

University of Colorado Boulder · expected May 2028

- Advised by Prof. Hendrik Heinz in the Heinz Interfaces Laboratory.
- Atomistic simulation of interfaces; experiment-calibrated force fields; autonomous-laboratory infrastructure.

### B.S., Materials Science and Engineering

University of Florida · May 2024

- Minor in Chemistry.

## Research

### Graduate Research Assistant, MXene interlayer shear

University of Colorado Boulder, Heinz Interfaces Laboratory · Oct 2024–present

- Lead-author manuscript in preparation.
- Ran the production shear campaign for OH-, F-, and mixed-terminated Ti₃C₂ bilayers in LAMMPS, running 780 NVT shear trajectories across six termination and geometry cells on CU Boulder's Alpine cluster, ten seeds per stress, zero failed runs.
- Froze the protocol before production and had the campaign audited read-only afterward. The audit re-derived every reported critical stress from raw trajectories using an independent re-implementation of the slip classifier, and caught an inflated trajectory count in our own reporting before it reached the manuscript.
- Surface termination sets interlayer shear resistance across roughly a threefold range (τ<sub>0.5</sub> 42–135 MPa), OH > mixed > F.

### Graduate Research Assistant, hydrogen release from N-ethylcarbazole on Pt nanocrystals

University of Colorado Boulder, Heinz Interfaces Laboratory · Oct 2024–present

- Lead-author manuscript in preparation.
- Designed and ran the MD campaign behind the manuscript, 60 slab production runs across three Pt facets plus cuboctahedral nanoparticle ensembles, zero production job failures.
- Found that dehydrogenation-reactive configurations concentrate at low-coordination sites. Vertices carry 5.4× the per-atom contact density of {100} terraces and 2.9× that of {111}, so local coordination, rather than facet identity, sets where release happens.
- Built the per-area normalization methodology that makes facets, edges, and vertices comparable, and validated the finite nanoparticle against infinite slabs facet by facet.
- Wrote the technical narrative for the ALCF Director's Discretionary allocation that funds the next campaign.

### Graduate Research Assistant, copper-oxide force fields for INTERFACE FF

University of Colorado Boulder, Heinz Interfaces Laboratory · Oct 2024–present

- Parameterized INTERFACE force-field models for copper oxides as the first-year university deliverable of an industry-funded program, calibrated exclusively against experimental data, including lattice constants, elastic constants, surface energies, and vibrational spectra.
- Delivered a validated Cu₂O parameter family in bonded 9-6 and 12-6 forms, anchored to experimental lattice constants and within ±5% of both independent experimental elastic references. Shipped as a distribution bundle (LAMMPS data files and run decks, an .frc for msi2lmp, a CHARMM/NAMD .prm), with all 52 configurations run-verified.

### Graduate Research Assistant, retrieval over the force-field corpus

University of Colorado Boulder, Heinz Interfaces Laboratory · Oct 2024–present

- Built a SOAP-embedding retrieval index over the group's 3,009-structure, 6.7M-atom corpus so a new atom's type and parameters can be proposed from its nearest structural neighbors behind a confidence gate. The same index maps coverage gaps and audits type consistency.

### High-Performance Computing Intern

Air Force Research Laboratory, Materials & Manufacturing Directorate, Wright-Patterson AFB · May–Aug 2025

- Built the LAMMPS shear-testing workflow for OH-terminated Ti₃C₂ bilayers under controlled hydration and ran the stress sweeps on DoD HPC.
- Fit slip probability against applied shear stress with logistic models. Hydration turns out to be non-monotonic. Dry bilayers hold to 103 MPa, a quarter monolayer of water drops them to 8 MPa, and full coverage recovers to 39 MPa as water rebuilds bridging hydrogen bonds.
- First MD evidence that hydration tunes MXene interlayer shear strength by an order of magnitude, with the stress windows that follow for EM-shielding composite design.

### Undergraduate Research Assistant

Hennig Group, University of Florida · Oct 2021–May 2024

- Benchmarked the VASPsol implicit solvation model against experimental energies from the Minnesota Solvation Database for neutral and charged solutes in water.
- Optimized cavity and screening parameters by grid search and Nelder–Mead across a large DFT campaign, and outlined a surrogate-model strategy that replaces high-count parameter sweeps for future calibrations.

### Materials Modeling Intern

Air Force Research Laboratory · May–Dec 2023

- Built and validated an automated DFT workflow (Quantum ESPRESSO with Python, ASE, and pymatgen) for high-throughput screening of low-work-function emitters, giving the group a reproducible selection path for field-emission candidates.

## Research automation and compute infrastructure

### OpenSDL, computational and autonomous laboratory framework

[github.com/fl-sean03/OpenSDL](https://github.com/fl-sean03/OpenSDL) · 2026–present

- An open foundation for building computational and autonomous laboratories, released under Apache-2.0. Declare what a laboratory can do, execute those declarations as reproducible workflows, preserve the evidence, and feed the result back into the choice of the next experiment. Roughly 26,000 non-test lines of Python, about 600 test functions, CI, and a [published documentation site](https://seanflorez.com/OpenSDL/).
- A durable runtime with DAG execution, retries, timeouts, resource leases, restart reconciliation, and policy checks, over SQLite metadata and content-addressed artifact storage. Adapters for a simulated lab, local compute, and human tasks, with Slurm and hardware integration in progress; a CLI, Python SDK, HTTP API, and MCP hook; portable run export.
- Implemented campaign scoring and next-round selection. A reference three-dye formulation search matched an unseen target recipe within 0.5 percentage points, evaluating 96 candidates per round.

### agent-fleet, persistent research automation

[github.com/fl-sean03/agent-fleet](https://github.com/fl-sean03/agent-fleet) · 2026–present

- Built a research harness based on a 15-agent fleet operating for months, with isolated workspaces, persistent conversations, and inter-agent messaging.
- Ran multi-day computational campaigns with recovery after reboots, credential expiry, and preemption.

### HPC and cloud throughput infrastructure

2025–present

- [subjob](https://github.com/fl-sean03/subjob) runs many heterogeneous tasks inside one HPC allocation, so a hundred short jobs cost one queue wait instead of a hundred. Shared task pool, workers spanning nodes and partitions, event journaling, per-task walltime enforcement, and heartbeat-driven recovery of a dead worker's claims. Built for the per-snapshot analysis fan-outs behind the Pt campaign.
- [CloudComputeManager](https://github.com/fl-sean03/cloudcomputemanager) (MIT) manages GPU-cloud lifecycles for scientific workloads on spot instances, covering provisioning, environment setup, multi-stage pipelines, checkpoint and preemption recovery, batch sweeps, and cost tracking. Workload-agnostic, with 368 tests. Used for LAMMPS shear campaigns.

## Manufacturing

### Engineering Contractor

Rocky Mountain Scientific Laboratory · Jun–Aug 2026

- Worked in the Automation and Robotics embed, June to August 2026, on the quality system for a client affiliate's new energetic-materials production line.
- Developed lot-release records covering inspections, approval authority, hold criteria, and nonconformance disposition, with item-level traceability to the governing military specification.
- Built a controlled, single-source document set with 10 client-format instructions, 20 test-specific quality-control packets, manufacturing procedures, and inspections.
- Automated checks for process-route isolation, link validity, terminology, and consistency between released documents and their source.
- Built a program tracker that generates the Kanban board, decision log, requirements traceability matrix, and design-review record.
- Supported quality, packaging, labeling, on-site commissioning, and hazard and failure-mode analysis.

## National security

### S&T Scouting Intern

The Joint Staff, J7 / Future Technology Office · Aug–Oct 2025

- Prioritized propulsion and energy concepts and produced eight technical briefs assessing readiness, risk, and experimentation paths for TRL 3–5 technologies.
- Coordinated with Service laboratories and DoD R&D organizations to connect emerging academic research to operational experimentation and transition pipelines.

### Technology Commercialization Intern

Idaho National Laboratory (DOE) · May–Aug 2024

- Ran 20 customer-discovery interviews under Energy I-Corps and authored the commercialization plan for a laboratory-origin technology.
- Built AI and natural-language tooling for the technology-transfer team, and supported a DOE proposal that was awarded $2M.

## Leadership and service

### Co-Founder, LabLink Initiative

[lablinkinitiative.org](https://www.lablinkinitiative.org) · Aug 2024–present

- Nonprofit moving community college students into national-laboratory research internships, principally the DOE Office of Science CCI and SULI programs. Partnerships with three Sacramento-area community colleges, and a webinar delivered across Phi Theta Kappa, the honor society for two-year colleges, that drew more than 250 students.
- Built the matching pipeline and the tooling behind it.

## Publications and outputs

### Co-author

[arXiv:2601.12570](https://arxiv.org/abs/2601.12570) · 2026 preprint

- INTERFACE Force Field for Alumina with Validated Bulk Phases and a pH-Resolved Surface Model Database for Electrolyte and Organic Interfaces.

### Lead author

Two manuscripts in preparation

- Modeling of MXene Shear Properties via Atomistic Molecular Dynamics Simulations, with AFRL Materials & Manufacturing Directorate co-authors.
- Understanding Hydrogen Release Mechanisms of N-Ethylcarbazole on Pt Nano-Crystal Catalysts.

### Open-source releases

[github.com/fl-sean03](https://github.com/fl-sean03)

- [MolSAIC](https://github.com/fl-sean03/MolSAICV4), a code-first MD system builder for atomistic model construction and force-field assignment.
- [pdb2msi](https://github.com/fl-sean03/pdb2msi), a PDB to Materials Studio structure converter.

### Computing allocations

ALCF, CU Boulder Alpine, and DoD HPC

- Argonne Leadership Computing Facility Director's Discretionary award *HydrogenStorage*, approximately 26,150 node-hours across Polaris, Crux, Sophia, and Graphcore, awarded May 2026.
- CU Boulder Research Computing (Alpine) and DoD HPC allocations supporting production MD campaigns, including 480-job Slurm arrays with checkpoint-restart.

### Quantum-chemical property prediction on QM9

[github.com/fl-sean03/qm9-smiles-predictor](https://github.com/fl-sean03/qm9-smiles-predictor)

- Four reproducible pipelines (single-task, multitask, autoencoder, hybrid Mordred + ECFP4) predicting nine quantum-chemical properties across roughly 130k molecules.
- Reproduced and critiqued published SMILES-FNN baselines, showing where multitask learning underperforms and where hybrid descriptors reduce MAE relative to Mordred-only models, for dipole moment and polarizability in particular.

### Automated phase identification in experimental powder XRD

[github.com/fl-sean03/opxrd-ml-binary-phase](https://github.com/fl-sean03/opxrd-ml-binary-phase)

- Ingested the roughly 92k-pattern opXRD archive (about 2.4% labeled) and formulated binary classification for a rare phase, with an interpolated 2θ grid and normalized intensities.
- Trained logistic-regression and random-forest classifiers with SMOTE for extreme class imbalance, reaching a 0.80 minority-phase F1 with balanced precision and recall on held-out data. A prototype for automated pXRD analysis in self-driving laboratories.

## Skills

### Molecular dynamics

LAMMPS, NAMD, Materials Studio/Discover

- Model building, equilibration protocol design, shear and deformation workflows, trajectory analysis at multi-GB scale.

### Electronic structure

VASP, VASPsol, Quantum ESPRESSO

- Automated high-throughput workflows via ASE and pymatgen.

### Force fields

INTERFACE FF, CVFF, CHARMM, PCFF, COMB3, EAM

- Parameterization against experimental data, transferability testing, elastic and surface-energy validation.

### Machine learning

scikit-learn, TensorFlow, imbalanced-learn, RDKit, Mordred, SOAP descriptors

- Regression, classification, class-imbalance handling, surrogate modeling, uncertainty and error analysis.

### Python

NumPy, SciPy, pandas, MDAnalysis, matplotlib

- Package design, CLI tooling, pytest, ruff, pyright.

### HPC and systems

Slurm and PBS Pro, job arrays, checkpoint-restart, throughput benchmarking, GPU and CPU-MPI builds

- Linux, bash, git, systemd, SQLite, Docker, GitHub Actions, MCP.

### Quality and manufacturing

Lot-release record and human-factors document design, military-specification traceability

- Requirements traceability matrices, PDR/CDR stage gates, FMEA and process hazard analysis, BOM development, vendor qualification, labeling compliance.
