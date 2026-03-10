---
title: "The Throughput Barrier"
description: "The fundamental barrier to matter compilation is not precision but speed. Even at a million atoms per second, building a macroscopic object takes geological time."
date: 2026-03-09
---


*Research compiled March 2026. This document works through the arithmetic of atomic-scale manufacturing throughput, what has been demonstrated, what has been proposed, and where the gaps are. Confidence labels: Established, Plausible, Speculative.*

---

## 1. The Arithmetic

The throughput problem in matter compilation is not subtle. It is a straightforward arithmetic problem, and the numbers are punishing.

A 1 cm cube of solid matter contains on the order of 10^22 to 10^23 atoms, depending on the material. Diamond (carbon) packs roughly 1.76 x 10^23 atoms per cubic centimeter. Silicon is about 5 x 10^22. Aluminum is about 6 x 10^22. For the calculations that follow, we will use 10^22 as a conservative lower bound.

Now consider current manipulation speeds:

| Method | Rate (atoms/sec) | Time for 1 cm³ (10^22 atoms) | Source |
|--------|------------------|-------------------------------|--------|
| STM research manipulation | ~1 | 10^22 sec (~300 trillion years) | Various, since IBM 1989 |
| Zyvex HDL (hydrogen depassivation) | ~50 | 2 x 10^20 sec (~6 trillion years) | Zyvex Labs |
| Hypothetical 1M atoms/sec | 10^6 | 10^16 sec (~300 million years) | No one has demonstrated this |
| Required for 1 cm³ in 1 hour | 2.8 x 10^18 | 3,600 sec (1 hour) | Target |

The gap between the best demonstrated serial rate (~50 atoms/sec) and the rate needed for practical macroscale manufacturing (~3 x 10^18 atoms/sec) is roughly 17 orders of magnitude. Even granting a hypothetical million-atom-per-second serial manipulator that nobody has built, the gap is still 13 orders of magnitude.

To put this differently: to build 1 cm³ in 1 hour at Zyvex's demonstrated rate, you would need approximately 6 x 10^16 parallel manipulators. At the hypothetical 1M atoms/sec rate, you would need roughly 3 x 10^12 parallel manipulators. That is 3 trillion.

No other engineering challenge that I am aware of has a gap of this magnitude between demonstrated capability and practical requirement. The semiconductor industry faced a gap of perhaps 8 to 10 orders of magnitude between the first transistor (1947) and modern chips with 10^11 to 10^12 transistors. The throughput barrier for matter compilation is roughly twice that large, measured in orders of magnitude.

**Confidence: Established.** This is arithmetic, not speculation.

---

## 2. Serial Approaches and Their Limits

### STM/AFM Manipulation

The scanning tunneling microscope has been used to position individual atoms since Don Eigler's famous IBM logo in 1989. In the 36 years since, STM-based manipulation has progressed from a laboratory stunt to a semi-routine technique, but the fundamental speed has not changed dramatically.

The most significant recent result in serial mechanosynthesis came in December 2025. A team of 54 researchers, including Ralph Merkle, demonstrated inverted-mode STM with 96.4% success rate for covalent mechanosynthesis. The specific reaction was hydrogen abstraction from a silicon surface. This was published as arXiv:2512.24431.

This result is genuinely important. It demonstrates that:

1. Covalent bond breaking under positional control is achievable with high reliability.
2. The success rate is high enough that error correction through repeat attempts is feasible.
3. The approach can be automated.

What it does not demonstrate:

1. Speed beyond single-digit atoms per second.
2. Any chemistry beyond hydrogen abstraction from silicon.
3. Bond formation (only bond breaking was shown).
4. Three-dimensional construction.

Zyvex Labs has pushed hydrogen depassivation lithography (HDL) to approximately 50 atoms per second. This is the fastest demonstrated rate for any form of tip-based atomic manipulation. HDL is a subtractive process: hydrogen atoms are removed from a passivated silicon surface, exposing bare silicon for subsequent chemical processing. It is not additive construction.

### AI-Assisted Automation

In 2025, AutoOSS (published in JACS) demonstrated a system that can run scanning probe operations autonomously for more than 25 hours. This is meaningful because the human operator has historically been the bottleneck in SPM experiments. Tip preparation, approach, drift correction, image analysis, and decision-making about where to manipulate all required expert human attention.

AutoOSS and similar systems reduce the human bottleneck. They do not reduce the physics bottleneck. A perfectly automated STM that can run 24/7 without human intervention still operates at roughly 1 atom per second. That converts a 300-trillion-year task into a 300-trillion-year task that does not require anyone to sit at the console.

This distinction matters. AI automation of scanning probe microscopy is valuable for research. It accelerates discovery. It enables experiments that were previously impractical because no human could maintain focus for 25 hours. But it does not address the throughput barrier by any significant factor. Even a 100x speedup from better automation and tip design (which has not been demonstrated) would reduce 300 trillion years to 3 trillion years.

**Confidence: Established.** These are published results with known limitations.

---

## 3. Parallel Approaches

If serial manipulation is too slow by 15 to 20 orders of magnitude, the only path to practical throughput is parallelism. Several approaches have been proposed or partially demonstrated.

### Massively Parallel Tip Arrays

The most direct approach is to build arrays of many tips and operate them simultaneously. Several efforts are underway:

**Cantilever-free parallel AFM.** In 2021, a team published in Nature Communications a cantilever-free parallel AFM architecture with more than 1,000 probes. This system demonstrated parallel imaging, meaning the tips could scan a surface simultaneously. It did not demonstrate parallel manipulation. Imaging is far simpler than manipulation because imaging only requires measuring tip-surface interaction forces, while manipulation requires controlling those forces precisely enough to move or remove individual atoms.

**MEMS-based parallel STM arrays.** Zyvex and collaborators have demonstrated parallel STM-based hydrogen depassivation lithography using MEMS-actuated tip arrays. The demonstrated parallelism is modest: a handful of tips operating simultaneously. Zyvex has projected scaling to 10 parallel tips at 1M atoms/sec each. Neither the 10-tip parallelism nor the 1M atoms/sec rate has been demonstrated.

**DOE AMO project.** The U.S. Department of Energy has funded an Atomically Precise Manufacturing (APM) program that includes development of MEMS-based massively parallel scanning probe systems. The target is a 1000x speedup over current SPM rates. This program is in development and has not published results demonstrating the target speedup.

The fundamental challenges of parallel tip arrays are:

1. **Precision across the array.** Each tip must maintain sub-angstrom positioning accuracy. Across an array of thousands or millions of tips, this requires controlling thermal expansion, mechanical vibration, and drift for every tip independently.

2. **Feedback bandwidth.** Each tip needs its own feedback loop to detect and correct positioning errors. The feedback electronics must operate faster than the manipulation rate. For millions of tips at millions of operations per second each, the total feedback bandwidth becomes enormous.

3. **Thermal drift.** At room temperature, thermal expansion of the supporting structure causes drift that is large compared to atomic spacings. A 1 cm support structure made of silicon expands by roughly 25 pm per millikelvin temperature change. Atomic spacings are roughly 200 to 300 pm. Temperature stability of better than 10 mK is needed across the entire array.

4. **Cross-talk.** Mechanical and electrical coupling between adjacent tips in a dense array can cause one tip's operation to disturb its neighbors. This gets worse as tip density increases.

The honest assessment: nobody has demonstrated even 10 parallel tips doing precise atomic manipulation simultaneously. The requirement is 10^12 to 10^16 parallel tips. That is a gap of 11 to 15 orders of magnitude in parallelism, on top of whatever serial speed improvement is needed.

**Confidence: Established for the challenges. Plausible that tip arrays can scale to thousands. Speculative that they can scale to trillions.**

### Self-Replicating Assemblers

The concept is straightforward: instead of building trillions of assemblers with some external manufacturing process, you build one assembler and have it build copies of itself. This is the approach Drexler proposed in *Engines of Creation* (1986) and analyzed in detail in *Nanosystems* (1992).

The theoretical foundation is solid. John von Neumann proved in the 1940s that a universal constructor (a machine that can build any machine, including copies of itself) is mathematically possible. The proof is constructive: von Neumann described the architecture such a machine would require, including a description tape, a constructor mechanism, and a copy mechanism for the description tape.

Biology demonstrates that molecular-scale self-replication works. Every cell on Earth is a self-replicating molecular machine. E. coli divides every 20 minutes under optimal conditions, meaning it roughly doubles its molecular machinery (including ribosomes, polymerases, membrane components, and everything else) in 20 minutes.

However:

1. **No synthetic nanoscale self-replicator has ever been demonstrated.** The simplest known self-replicating biological system, Mycoplasma mycoides JCVI-syn3.0, has 473 genes encoding roughly 500,000 atoms' worth of molecular machinery. We cannot build anything of comparable complexity from scratch.

2. **The chicken-and-egg problem.** You need a working assembler to build the first self-replicating assembler. If you had a working assembler, you might not need self-replication (you could just build more assemblers with it). The bootstrap problem is real: how do you get from zero assemblers to one?

3. **Error accumulation.** Copies degrade without error correction. A photocopier-of-photocopier chain degrades rapidly. Biological replication solves this with proofreading enzymes that achieve error rates of roughly 1 per 10^9 nucleotides. These proofreading systems are themselves complex molecular machines that must be replicated accurately.

4. **Environmental requirements.** Biological self-replication requires a rich chemical environment: specific substrates, energy carriers (ATP), cofactors, water, temperature control, and pH buffering. A synthetic self-replicating assembler would either need similar environmental support or would need to be far more self-sufficient than any biological system.

**Confidence: Speculative.** The physics allows it. Biology proves it is possible in principle. Engineering it from scratch is beyond current capability by a wide margin.

### Convergent Assembly

Drexler's convergent assembly concept proposes a hierarchical manufacturing chain: nanoscale assemblers build small components, which are assembled into larger components by larger machines, continuing through roughly 30 stages from nanometers to meters. At each stage, the assembly operations are appropriate to the scale: molecular manipulation at the bottom, pick-and-place robotics at the top.

The mathematics is favorable. A binary convergent assembly tree with N stages produces components of size roughly 2^N times the base component size. Starting from 1 nm components, 30 stages gets you to approximately 1 meter (2^30 nm is about 1 m). At each stage, the number of assembly operations is halved (each operation combines two components from the previous stage), so the total work scales linearly with the number of atoms rather than requiring each atom to be handled individually at the final scale.

The unsolved problems:

1. **Interface compatibility.** At each stage boundary, the components from stage N must be compatible with the assembly process at stage N+1. A 100 nm component assembled by molecular machines must have features that a 1 micrometer-scale pick-and-place system can grip, orient, and bond. These interface requirements propagate through all 30 stages.

2. **No complete chain demonstrated.** Nobody has demonstrated a convergent assembly chain from nanometer to even millimeter scale. Individual stages have been demonstrated in isolation (molecular self-assembly at the nanoscale, MEMS assembly at the microscale, robotic assembly at the macroscale), but the complete integrated chain does not exist.

3. **Error propagation.** Defects at early stages propagate through the hierarchy. If a nanoscale component has a defect, the micrometer-scale component containing it is defective, and so on up. Error rates must be extremely low at every stage, or inspection and rejection systems must be built into every stage.

**Confidence: Plausible math, zero engineering demonstration.**

---

## 4. Self-Assembly: The Partial Bypass

Self-assembly sidesteps the throughput problem entirely. Instead of placing each atom individually, you design components that assemble themselves through thermodynamic driving forces. All copies assemble in parallel, simultaneously, because the process is driven by free energy minimization rather than by a serial manipulator.

### What Works

**DNA origami.** DNA nanotechnology can produce three-dimensional structures with sub-nanometer precision and near-100% yield. A single reaction tube can produce billions of identical copies in hours. The design space is enormous: arbitrary 3D shapes can be programmed through base-pair sequence design. This is the most mature atomic-precision fabrication technology that operates at practical throughput. Key results from the Dietz group (TU Munich) and Rothemund (Caltech) have demonstrated structures from simple 2D tiles to complex 3D objects with moving parts.

**Block copolymer self-assembly.** Block copolymers (polymers with two or more chemically distinct segments) spontaneously form regular patterns with feature sizes of 5 to 50 nm. These patterns include lamellae, cylinders, and spheres in regular arrays. The patterns are determined by the polymer chemistry and processing conditions.

**Directed self-assembly (DSA).** The hybrid approach: use top-down lithography to create templates (guide patterns), then let block copolymers or DNA origami self-assemble within those templates. This combines the arbitrary pattern capability of lithography with the resolution of self-assembly. DSA is under active development for semiconductor manufacturing, with IMEC and several chipmakers evaluating it for sub-5 nm features.

### What Does Not Work

**Arbitrary structure generation.** Self-assembly produces structures that minimize free energy. You can influence which structures form by choosing chemistry and conditions, but you cannot force arbitrary atomic arrangements. Thermodynamics chooses the structure. You choose the menu of options through materials selection, but you do not have atom-by-atom control.

**Long-range order control.** Self-assembled structures tend to have defects at domain boundaries. Maintaining perfect order across centimeters or meters is not achievable with current self-assembly techniques. Grain boundaries, dislocations, and other defects are thermodynamically inevitable at finite temperature.

**Multi-material integration.** Self-assembly works well within a single material system (DNA with DNA, block copolymers with block copolymers). Integrating multiple materials with different chemistries into a single self-assembled structure is extremely challenging. Biology does this (cells contain proteins, lipids, nucleic acids, and polysaccharides in integrated structures), but only after 4 billion years of evolutionary optimization.

**Rapid design iteration.** DNA origami requires synthesizing new DNA sequences for each new design. Block copolymer self-assembly requires synthesizing new polymers. The turnaround time from design to physical structure is days to weeks. This is fast by chemistry standards but slow by software standards.

### Verdict

Self-assembly is a powerful complement to directed assembly, not a replacement. It solves the throughput problem for a restricted class of structures (those near thermodynamic equilibrium) but cannot produce arbitrary structures with atomic precision. The most likely path to practical matter compilation involves self-assembly for bulk structure formation combined with directed assembly (tip-based or otherwise) for critical features that must be atomically precise.

**Confidence: Established for the capabilities. Established for the limitations.**

---

## 5. The Biological Precedent

Biology is the existence proof that molecular-scale manufacturing at practical throughput is physically possible. Understanding exactly what biology demonstrates (and what it does not) is essential to assessing the throughput barrier.

### What Biology Demonstrates

**Massively parallel molecular machines.** A typical mammalian cell contains roughly 10 million ribosomes. Each ribosome synthesizes protein at a rate of 15 to 20 amino acids per second. The total protein synthesis rate per cell is therefore on the order of 10^8 amino acid additions per second. This is massively parallel molecular manufacturing, running continuously, at room temperature (well, 310 K), in water.

**Self-replication at scale.** A human body contains approximately 37 trillion cells (3.7 x 10^13), all descended from a single fertilized egg. The entire construction process takes about 9 months. This is convergent assembly in action: one cell becomes two, two become four, continuing through roughly 47 doublings to reach the final cell count. Along the way, cells differentiate into roughly 200 distinct types and organize into tissues and organs.

**High-speed polymer synthesis with error correction.** DNA polymerase III in E. coli synthesizes DNA at roughly 1,000 nucleotides per second per replication fork. The raw error rate is about 1 per 10^5 nucleotides, but proofreading and mismatch repair reduce this to about 1 per 10^9 to 10^10 nucleotides. This is an error rate of roughly one part per billion, at a synthesis rate of 1,000 monomers per second. No synthetic system comes close.

### What Biology Does Not Demonstrate

**Arbitrary elemental composition.** Biology builds almost exclusively from six elements: carbon, hydrogen, oxygen, nitrogen, phosphorus, and sulfur. It uses about 20 amino acids and 4 nucleotide bases as building blocks. It does not build with metals (except as trace cofactors), ceramics, semiconductors, or most of the periodic table. A general matter compiler needs to handle dozens of elements. Biology does not show how to do this.

**Operation outside aqueous conditions.** Biological molecular machines operate in water at temperatures near 310 K and pH near 7.4. They fail outside these narrow conditions. A matter compiler that can only work in warm salt water is severely limited in what it can build and where it can operate.

**Bootstrapping from scratch.** Every biological self-replicating system is descended from a 4-billion-year chain of inheritance. No biological system was engineered from raw materials. The first self-replicating molecular system arose through processes we do not fully understand (the origin of life remains an open problem). Biology does not provide a recipe for building a self-replicating molecular machine from non-biological feedstock.

### The Synthetic Biology Gap

The gap between biological molecular machines and synthetic ones is enormous. The most instructive comparison is the ribosome versus synthetic molecular assemblers:

| Property | Ribosome | Leigh Assembler (2013) |
|----------|----------|----------------------|
| Rate | 15-20 amino acids/sec | ~1 amino acid per 12 hours |
| Speed ratio | 1x | 1/648,000 to 1/864,000 |
| Error rate | ~1 per 10^4 (before proofreading) | Not characterized at scale |
| Parallelism | ~10^7 per cell | Single molecule |
| Energy source | GTP hydrolysis | Chemical fuel |
| Self-replicating | Yes (indirectly, via cell division) | No |

The Leigh group's molecular assembler (University of Manchester) was a landmark achievement in synthetic chemistry. It demonstrated that a synthetic molecular machine could pick up amino acids in sequence and link them together. But the rate gap is a factor of roughly 600,000 to 900,000. This is the current state of synthetic molecular machinery compared to the biological version that evolution produced.

**Confidence: Established.** These are measured quantities.

---

## 6. What Would It Take?

Let us work through the requirements for a practical matter compiler that can build 1 cm³ of arbitrary material in 1 hour.

**Target throughput:** 10^22 atoms in 3,600 seconds = 2.8 x 10^18 atomic operations per second.

**Scenario: Ribosome-speed assemblers.**

If each assembler operates at ribosome speed (roughly 20 operations per second), you need:

- 2.8 x 10^18 / 20 = 1.4 x 10^17 assemblers

A ribosome has a mass of approximately 2.5 x 10^6 daltons, or about 4.2 x 10^-21 kg. For 1.4 x 10^17 assemblers:

- Total assembler mass: 1.4 x 10^17 x 4.2 x 10^-21 kg = 5.9 x 10^-4 kg, or about 0.6 grams.

This is a physically plausible mass. Less than a gram of molecular machinery could, in principle, provide sufficient throughput for macroscale manufacturing. The volume would be roughly 0.6 cm³ (assuming density near water). You could hold the entire assembler fleet in a thimble.

**The bootstrap problem.**

But building 1.4 x 10^17 assemblers requires either:

1. An existing manufacturing system capable of producing 10^17 molecular machines (which is the problem we are trying to solve), or
2. Self-replication.

If assemblers can self-replicate with a doubling time of 1 hour (E. coli manages 20 minutes, so this is conservative), then starting from a single assembler:

- 1 assembler to 1.4 x 10^17 assemblers requires log2(1.4 x 10^17) = approximately 57 doublings.
- At 1 hour per doubling: 57 hours, or about 2.4 days.

This is the exponential growth argument for self-replicating assemblers. The numbers are seductive. But every step after step 1 (building the first assembler) is undemonstrated. Step 1 itself is undemonstrated.

**Energy requirements.**

At 10 to 100 kT per atomic operation (Drexler's estimate from *Nanosystems*):

- 10^22 operations x 100 x 4.1 x 10^-21 J = 4.1 x 10^3 J = 4.1 kJ per cm³
- Over 1 hour: 4.1 kJ / 3600 s = 1.1 W

About one watt. This is negligibly small. Even at 1000 kT per operation, you need about 11 watts. The energy cost of matter compilation is not the bottleneck. The throughput is.

**Confidence: The mass and energy calculations are Established. The bootstrap scenario is Speculative.**

---

## 7. Is This Solvable?

### Arguments for Yes

**Biology proves it works.** Massively parallel molecular manufacturing is not a theoretical possibility. It is happening inside every living cell. The physics allows it. The thermodynamics allows it. The error rates are manageable. Biology is proof that the throughput barrier is not a fundamental physical limit.

**The energy costs are modest.** At 10 to 100 kT per operation, matter compilation is energetically cheap. There is no thermodynamic wall. The energy per kilogram of compiled matter would be on the order of kilojoules, comparable to the energy in a few grams of sugar.

**Computing overcame a similar scale gap.** The semiconductor industry went from 1 transistor (1947) to 10^12 transistors on a single chip (2020s) in roughly 70 years. That is 12 orders of magnitude. Matter compilation needs 15 to 20 orders of magnitude of improvement. The scale is larger, but the computing precedent shows that sustained exponential improvement over decades is possible when there are strong economic incentives and no fundamental physical barriers.

### Arguments for Not in Our Lifetime

**Biology had 4 billion years.** Evolution explored an astronomically large design space over billions of generations to arrive at ribosomes, polymerases, and the rest of the molecular machinery that makes cellular life work. We are attempting to engineer equivalent systems from scratch, in decades. The gap between "physics allows it" and "engineers can build it" can be very large.

**The simplest self-replicating system is still enormously complex.** JCVI-syn3.0, the simplest known self-replicating cell, has 473 genes and roughly 500,000 atoms of essential molecular machinery. We cannot yet build a system of this complexity from scratch. We can modify existing biological systems (synthetic biology), but we cannot design and construct a self-replicating molecular machine de novo.

**The semiconductor analogy is misleading.** Semiconductor manufacturing parallelizes 2D patterning through projection lithography: a single light exposure patterns billions of transistors simultaneously. This works because transistors are essentially flat and the patterning is done with photons, not mechanical probes. Matter compilation requires 3D atomic construction, which is a fundamentally different problem. Photolithography's parallelism does not transfer to 3D molecular assembly.

### Arguments for Domain-Specific Solutions

The most pragmatic assessment may be that the throughput barrier is solvable for specific high-value, small-volume applications, but not for general-purpose macroscale manufacturing in the foreseeable future.

**Quantum computing components.** Silicon Quantum Computing (SQC) in Sydney is already using STM-based atomic precision manufacturing to build quantum computing devices. Each device contains millions of atoms, not 10^23. At current SPM rates, building a device with 10^6 precisely placed atoms takes hours to days, not geological time. For a $10 million quantum computer, spending a week on atomic-precision fabrication of the critical qubit layer is commercially viable.

**Catalysts and molecular sieves.** A catalyst particle might contain 10^8 to 10^12 atoms. At 50 atoms/sec, 10^10 atoms takes about 6 years. Too slow for serial production, but potentially viable with modest parallelism (1,000 tips reduces it to 2 days).

**The hybrid approach.** Use atomic precision for the critical features (active sites, quantum dots, molecular recognition surfaces) and conventional manufacturing for bulk structure. This avoids the throughput barrier entirely for the bulk material while achieving atomic precision where it matters. This is likely the first commercially viable path.

**Confidence: The domain-specific approach is Plausible and partially demonstrated (SQC). General-purpose macroscale matter compilation remains Speculative.**

---

## 8. Confidence Assessment

| Claim | Confidence | Basis |
|-------|-----------|-------|
| The throughput gap is 15-20 orders of magnitude | **Established** | Arithmetic from known atomic densities and demonstrated manipulation rates |
| No existing serial technology can bridge this gap | **Established** | Even 10^6 atoms/sec (undemonstrated) leaves 13 orders of magnitude |
| Massively parallel molecular assemblers could theoretically bridge it | **Plausible** | Biology proves the physics works; engineering path unclear |
| Self-replicating assemblers could bootstrap the fleet | **Speculative** | No synthetic nanoscale self-replicator has been demonstrated |
| Convergent assembly provides a viable architecture | **Plausible** | Math is sound; no complete chain demonstrated |
| Self-assembly can complement directed assembly | **Established** | DNA origami, DSA are working technologies |
| Domain-specific APM is viable now | **Established** | SQC, Zyvex are operating |
| General-purpose macroscale matter compilation in 20 years | **Speculative** | Requires multiple undemonstrated breakthroughs in sequence |
| General-purpose macroscale matter compilation ever | **Plausible** | No physical law forbids it; biology proves it is possible in principle |

The throughput barrier is the central unsolved problem of matter compilation. Precision is advancing steadily (the December 2025 inverted-mode STM result is a genuine milestone). Control is improving (AI-assisted automation is real). But speed? Speed is stuck. The gap between what we can do and what we need to do is 15 to 20 orders of magnitude, and no demonstrated technology reduces it by more than 2 or 3 orders of magnitude.

This does not mean matter compilation is impossible. It means matter compilation is hard in a specific, quantifiable way, and that honest roadmaps must account for this gap rather than waving it away.

---

## Sources

1. **Inverted-mode STM mechanosynthesis.** Rashidi, M. et al. (2025). "Covalent mechanosynthesis with an inverted scanning tunneling microscope." arXiv:2512.24431. [https://arxiv.org/abs/2512.24431](https://arxiv.org/abs/2512.24431)

2. **Cantilever-free parallel AFM.** Sarioglu, A.F. et al. (2021). "Cantilever-free scanning probe microscopy with massively parallel probes." Nature Communications. [https://www.nature.com/articles/s41467-021-22266-3](https://www.nature.com/articles/s41467-021-22266-3)

3. **Zyvex Labs.** Hydrogen depassivation lithography and atomically precise manufacturing. [https://www.zyvexlabs.com/](https://www.zyvexlabs.com/)

4. **AutoOSS.** Gordon, O. et al. (2025). "Autonomous on-surface synthesis." Journal of the American Chemical Society. [https://pubs.acs.org/journal/jacsat](https://pubs.acs.org/journal/jacsat)

5. **DOE Atomically Precise Manufacturing program.** U.S. Department of Energy, Office of Science. [https://science.osti.gov/bes/Community-Resources/Reports](https://science.osti.gov/bes/Community-Resources/Reports)

6. **Drexler, K.E.** *Nanosystems: Molecular Machinery, Manufacturing, and Computation.* Wiley, 1992. Energy and throughput analysis in Chapters 13-14.

7. **JCVI-syn3.0.** Hutchison, C.A. et al. (2016). "Design and synthesis of a minimal bacterial genome." Science 351(6280). [https://www.science.org/doi/10.1126/science.aad6253](https://www.science.org/doi/10.1126/science.aad6253)

8. **Leigh assembler.** Lewandowski, B. et al. (2013). "Sequence-specific peptide synthesis by an artificial small-molecule machine." Science 339(6116). [https://www.science.org/doi/10.1126/science.1229753](https://www.science.org/doi/10.1126/science.1229753)

9. **Silicon Quantum Computing (SQC).** STM-based atomically precise fabrication of silicon quantum devices. [https://sqc.com.au/](https://sqc.com.au/)
