---
title: "Core Ontology and Glossary"
description: "Hard definitions to prevent semantic drift: the loop, core terms, system terms, the scale ladder, confidence labels, and anti-patterns."
date: 2026-03-09
---

Hard definitions to prevent semantic drift. Every document should use these terms consistently.

---

## The Loop

The matter compiler is a loop, not a pipeline. Every term below exists within this cycle:

```
    Design ──→ Simulate ──→ Make ──→ Measure
       ↑                                 │
       └──────────── Learn ──────────────┘
```

| Step | What Happens | Key Terms |
|------|-------------|-----------|
| **Design** | Specify what you want, propose how to achieve it | Intent, functional target, structure, composition, architecture |
| **Simulate** | Predict whether the design will work before building it | DFT, molecular dynamics, multi-scale modeling |
| **Make** | Physically produce the design | Process, recipe, synthesis, fabrication, assembly |
| **Measure** | Characterize what you actually got | Metrology, characterization, qualification, validation |
| **Learn** | Feed results back to improve the next revolution | Knowledge capture, model updating, process refinement |

## Core Terms

| Term | Definition |
|------|-----------|
| **Intent** | A human-specified functional goal with constraints (e.g., "a battery cathode with >250 mAh/g capacity that survives 1000 cycles at 45C") |
| **Functional Target** | Quantified performance requirements derived from intent |
| **Structure** | The atomic/molecular/microstructural arrangement that achieves the functional target |
| **Composition** | The elemental makeup of the structure |
| **Architecture** | The multi-scale spatial organization (grain boundaries, interfaces, porosity, layering) |
| **Process** | The sequence of physical/chemical operations that produces the structure (synthesis route, thermal history, deposition parameters) |
| **Recipe** | A fully specified, reproducible process with all parameters, tolerances, and equipment requirements |
| **Qualification** | Formal demonstration that a material/process/product meets specified requirements through testing and analysis |
| **Validation** | Confirmation that the qualified product actually performs as intended in its use environment |
| **Digital Thread** | Bidirectional data flow connecting design, manufacturing, quality, and measurement across the product lifecycle |
| **Digital Twin** | A computational model that mirrors a physical system, updated with real-time data, used for prediction and optimization |

## System Terms

| Term | Definition |
|------|-----------|
| **Matter Compilation** | Closing the design-make-measure-learn loop for physical things with increasing speed, autonomy, and scale |
| **The Loop** | The core cycle: design, simulate, make, measure, learn, repeat. Everything we build serves to compress the loop or expand its scope. |
| **Loop Compression** | Making each revolution faster, more autonomous, and more reliable |
| **Scope Expansion** | Making the loop work for more materials, more complex structures, and larger scales |
| **Manufacturing Knowledge** | The accumulated understanding of how to go from a design to a repeatable, qualified manufacturing outcome, the gap that breaks most loops today |
| **Module** | A validated, reusable building block (physical or informational) that can be composed into larger systems |
| **Convergent Assembly** | Hierarchical manufacturing where each stage assembles components from the previous stage, scaling from nm to m in ~30 stages |
| **Mechanosynthesis** | Using precisely positioned molecular tools to form chemical bonds at specific locations |

## Scale Ladder

Compilation changes character by scale. At small scales: precise synthesis and patterning. At large scales: modular orchestration, process control, and validated assembly.

| Scale | Size Range | Control Variables | Dominant Tools Today |
|-------|-----------|-------------------|---------------------|
| **Atomic** | <1 nm | Bond formation, electronic structure | STM, DFT simulation |
| **Molecular** | 1-10 nm | Molecular geometry, conformations | DNA origami, molecular synthesis, MD simulation |
| **Nanoscale Architecture** | 10-100 nm | Self-assembly, directed assembly | Block copolymers, ALD, colloidal assembly |
| **Microstructure** | 100 nm - 100 um | Grain size, phase distribution, texture | Heat treatment, additive mfg, lithography |
| **Part / Device** | 100 um - 10 cm | Geometry, tolerances, interfaces | CNC, 3D printing, semiconductor fab |
| **Assembly / Package** | 1 cm - 1 m | Integration, interconnects, packaging | Pick-and-place, wire bonding, soldering |
| **Workcell / Line** | 1-10 m | Process flow, scheduling, QC | Robotics, MES, PLC |
| **Factory** | 10-100 m | Production planning, digital twins, logistics | ERP, SCADA, digital thread |
| **Site / Infrastructure** | 100 m - 1 km | Modular construction, utilities, logistics | Modular building, heavy civil |
| **City / Civil System** | >1 km | Urban planning, systems integration | Policy, infrastructure planning |

## Confidence Labels

Use these when making claims:

| Label | Meaning |
|-------|---------|
| **Established** | Published, reproduced, widely accepted. Multiple independent sources. |
| **Plausible** | Consistent with known science/engineering. Some evidence but not yet demonstrated at required scale. |
| **Speculative** | Theoretically possible but no experimental evidence. Depends on breakthroughs. |

---

## Anti-Patterns (What These Terms Are NOT)

- **Matter compilation is not "print anything from atoms"**: Too imprecise, points toward sci-fi demos. It's about closing the loop.
- **Compiler is not just AI/ML**: The compiler includes make + measure + learn, not just design + simulate
- **Discovery is not compilation**: Proposing a candidate is one step. Closing the full loop is compilation.
- **The loop is not a pipeline**: It's not sequential stages. It's iterative, concurrent, and every revolution improves the next.
- **Qualification is not bureaucracy**: Measurement and validation are part of the loop, not downstream paperwork
- **Digital thread is not a database**: It's bidirectional flow between design and production, not just data storage
