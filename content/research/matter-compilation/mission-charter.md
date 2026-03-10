---
title: "Mission Charter"
description: "The mission for matter compilation: build physical structures with atomic precision. The central barrier, the five capability layers, the methodology, and the decision filter."
date: 2026-03-09
---

## Mission

Build physical structures with atomic precision.

The engineering challenge is straightforward to state: make physical fabrication as precise and programmable as digital computation. A modern chip fab places billions of transistors with sub-nanometer registration. We want that level of control for arbitrary physical structures, not just silicon, not just planar, not just in a cleanroom.

## Why This Is Possible

This is not speculation. Biology proves that atomically precise construction works at scale and at speed.

**Existence proofs:**

- **Ribosomes** assemble proteins from amino acids with atomic precision, at rates of ~20 amino acids per second, with error rates below 10^-4. Every cell contains thousands of them running in parallel. Biology solved the throughput problem through massive parallelism of precise molecular machines.

- **DNA replication** copies 3 billion base pairs with error rates around 10^-9 after proofreading. The machinery is atomically precise, self-correcting, and fast (1,000 nucleotides per second in E. coli).

- **DNA origami** (Rothemund, 2006; subsequent work through 2026) achieves sub-nanometer positioning of components in designed 3D structures. Yields above 90% are routine. This is human-designed atomically precise construction, not just biology.

- **STM atom manipulation** (Eigler and Schweizer, IBM, 1989) placed individual xenon atoms on a nickel surface. Since then, hydrogen depassivation lithography (Zyvex Labs) has demonstrated atomically precise patterning at 7.7nm pitch.

- **Atomic layer deposition** builds films one atomic layer at a time, with thickness control at the angstrom level. This is already industrial-scale atomically precise manufacturing, limited to thin films.

The physics of building with atomic precision is settled. No new physical principles are needed. The challenge is entirely engineering: faster, more general, more parallel, more materials, larger structures.

## The Central Barrier

The throughput problem.

The gap between demonstrated serial atomic manipulation (~50 atoms/sec, Zyvex HDL) and the rate needed to build macroscopic objects (~3 x 10^18 atoms/sec for 1 cm^3 in one hour) spans roughly 17 orders of magnitude. Even a hypothetical million-atom-per-second manipulator, which no one has built, still leaves a 13 order-of-magnitude gap.

This is the largest throughput gap in any engineering discipline I am aware of. The semiconductor industry faced a gap of roughly 8 to 10 orders of magnitude between the first transistor and modern chips. The matter compilation throughput barrier is roughly twice that.

The full arithmetic, the survey of serial and parallel approaches, and the analysis of plausible scaling paths are in [The Throughput Barrier]({{< ref "throughput-barrier" >}}).

## The Five Capability Layers

Building physical structures with atomic precision is not one technology. It is a stack of building capabilities, each operating at different scales and with different tools:

| Layer | Domain | Building Capability | Status |
|-------|--------|---------------------|--------|
| **1. Atomic/Molecular Control** | APM, atomic-scale devices, nanoscale assembly | Place atoms and molecules where they need to go. The finest-grain building tools. | Real but narrow (STM, DNA origami, ALD). Precision proven, throughput not. |
| **2. Materials Intelligence** | Foundation models, inverse design, autonomous experimentation | Know what to build and predict whether it will work before building it. | Accelerating now (MatterGen, A-Lab, GNoME). |
| **3. Manufacturing Knowledge** | Process development, recipes, metrology, failure modes | Translate a design into a repeatable fabrication process. The gap where most materials die today. | The critical gap. 141 ANSI standardization gaps documented. |
| **4. Production Systems** | Digital thread, digital twins, robotics workcells, QC | Build reliably at volume, with traceability and quality control. | Emerging (Genesis Mission, NIST digital thread, SMART USA). |
| **5. Infrastructure Assembly** | Modular manufacturing, robotic assembly, digital construction | Assemble components into large-scale functional structures. | Far horizon (NASA metamaterial work, modular construction). |

Each layer represents a class of building problem. Layer 1 is about precision. Layer 5 is about scale. Advancing matter compilation means pushing capability forward across all five layers simultaneously, because a breakthrough in atomic control without manufacturing knowledge to exploit it does not produce buildable structures.

## The Loop as Methodology

The design-make-measure-learn loop is how we advance building capability:

```
    Design --> Simulate --> Make --> Measure
       ^                                |
       +------------ Learn ------------+
```

Every revolution of the loop produces a physical result, generates knowledge, and makes the next revolution faster. Today this loop takes 10-20 years for a new material. Self-driving labs are compressing it to months for narrow material systems.

The loop is a powerful methodology for systematic progress, but it is a tool, not the mission. The mission is building. The loop is how we get better at building. Compressing the loop is valuable precisely because it accelerates our ability to construct physical structures with greater precision and broader material scope.

## Near-Term Focus

Advance atomically precise fabrication from narrow demonstrated domains toward broader material systems and larger scales.

Today, atomically precise construction works in isolated domains: silicon qubits via hydrogen depassivation lithography, DNA nanostructures via programmed self-assembly, thin films via atomic layer deposition, molecular machines designed in simulation. These capabilities are fragmented across different research communities, different tools, different materials, and different scales.

The near-term work is to:

1. **Map the landscape**: Catalog what has been demonstrated, at what precision, in what materials, at what throughput. (Begun in the [APM Deep Dive]({{< ref "apm-deep-dive" >}}) and [Feasibility Assessment]({{< ref "feasibility-assessment" >}}).)
2. **Identify bridgeable gaps**: Find places where two demonstrated capabilities, connected, would unlock a new class of buildable structures.
3. **Advance throughput**: The throughput barrier is the central problem. Any work that credibly moves the needle on parallel, precise fabrication is high priority.
4. **Build manufacturing knowledge**: Capture process recipes, failure modes, and characterization methods so that demonstrated fabrication results become repeatable and transferable.

## Non-Goals

We are not:

- A generic AI lab.
- An AI materials discovery company. (AI-driven discovery is a tool, not the mission. See [AI in Materials Science]({{< ref "ai-materials-honest" >}}) for why discovery alone does not produce buildable structures.)
- A materials-screening company that proposes candidates without fabricating them.
- A lab-automation company that speeds up experiments without advancing fabrication precision.
- A consultancy.
- A point-solution MES vendor.

## Decision Filter

Every project gets judged by one question: **Does this advance our ability to build physical structures with greater precision, at larger scale, or from more diverse materials?**

- Advances precision: do it.
- Advances scale: do it.
- Expands material scope: do it.
- None of the above: cut it, defer it, or treat it as cash-flow support.

---

## How This Relates to Other Documents

- **[Vision]({{< ref "vision" >}})**: The north star narrative (why, what changes, the end state).
- **This document**: The mission (what we build, how we decide, what we are not).
- **[Ontology]({{< ref "ontology" >}})**: Hard definitions to prevent semantic drift.
- **[The Throughput Barrier]({{< ref "throughput-barrier" >}})**: Full treatment of the central engineering problem.
- **[Technology Roadmap]({{< ref "technology-roadmap" >}})**: Technical milestones across the five layers.
- **[Ecosystem Plan]({{< ref "ecosystem-plan" >}})**: Multi-venture architecture and phasing.
- **[AI in Materials Science]({{< ref "ai-materials-honest" >}})**: Honest assessment of what AI discovery can and cannot do.

Sources: [Eigler & Schweizer, Nature 1990](https://doi.org/10.1038/344524a0), [Rothemund, Nature 2006](https://doi.org/10.1038/nature04586), [Zyvex Labs](https://www.zyvexlabs.com/), [MatterGen](https://www.nature.com/articles/s41586-025-08628-5), [White House Genesis Mission](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/), [NIST Digital Thread](https://www.nist.gov/programs-projects/digital-thread-manufacturing), [MGI Autonomous Experimentation Workshop](https://www.mgi.gov/sites/mgi/files/MGI_Autonomous_Materials_Innovation_Infrastructure_Workshop_Report.pdf)
