---
title: "Building Reality Check: What Has Actually Been Built"
description: "An honest inventory of what has been constructed with atomic or near-atomic precision as of early 2026. What works, what doesn't, and where the gaps are."
date: 2026-03-09
---


---

## The Question

What has actually been BUILT with atomic precision? Not predicted, not simulated, not published in a theoretical paper, but physically constructed and demonstrated. This is a harder question than it sounds, because the field is saturated with computational studies, theoretical designs, and promissory roadmaps. Filtering down to what has been physically realized gives a much shorter and more sobering list.

---

## 1. Silicon Quantum Devices (Commercial Atom-Precise Manufacturing) {#1-silicon-quantum-devices-the-most-commercially-advanced-apm}

**Silicon Quantum Computing (SQC), Sydney, Australia** is an atomically precise manufacturing operation with commercial products. Their approach uses scanning tunneling microscopy combined with phosphine dosing to place individual phosphorus atoms into a silicon crystal lattice with 0.13 nm accuracy. The process is called PAQMan (Precision Atom Qubit Manufacturing), and SQC says it is the only company worldwide that can manufacture quantum processors at atomic scale.

What SQC has actually demonstrated:

- November 2025: SQC reports patterning 250,000 qubit registers in 8 hours, a throughput that would have seemed absurd five years ago
- An 11-qubit atom processor with gate fidelities from 99.10% to 99.99%, and Bell-state fidelities of up to 99.5% that the Nature paper calls state-of-the-art (December 2025)
- Commercial products on offer, with an Australian Defence contract to deliver one

The products are worth listing explicitly because they show APM on offer commercially:

- **Quantum Twins**: application-specific quantum simulators. These are custom chips where the arrangement of phosphorus atoms encodes a replica of a physical system the customer wants to simulate. Each chip is a bespoke atomically precise structure built to order.
- **Watermelon**: a quantum machine learning system built on the same atomically precise silicon platform.
- **Customers and partners**: Telstra (Australian telecom) ran a 12-month collaboration with SQC on Watermelon, and Australian Defence awarded SQC a contract in August 2025 to deliver a Watermelon system. SQC offers these systems as turnkey hardware for a customer's datacenter or as remote access to machines hosted at SQC.

This is real APM with a commercial offering today. Atoms are being placed with sub-nanometer precision to build functional devices that SQC offers to customers.

**Verdict**: Real products on offer, with a government contract and a telecom collaboration behind them. But the scope is narrow: placing one type of atom (phosphorus) in one substrate (silicon) for one application (quantum computing). Extending this to other elements or other substrates is a separate engineering challenge that SQC has not attempted.

**Sources**: [Silicon Quantum Computing](https://sqc.com.au/), [Technology](https://sqc.com/technology), [SQC Launches Quantum Twins™ Enabling Simulation of Quantum Physics and Chemistry](https://sqc.com/news/sqc-launches-quantum-twins), [An 11-qubit atom processor in silicon](https://www.nature.com/articles/s41586-025-09827-w), [SQC and Australian Defence Partner to Deliver Quantum Machine Learning](https://sqc.com/news/silicon-quantum-computing-and-australian-defence-partner-up-to-deliver-quantum-enhanced-machine-learning), and [Telstra And SQC Explore Smarter Network Prediction](https://thequantuminsider.com/2025/10/13/telstra-and-sqc-explore-smarter-network-prediction/)

---

## 2. Hydrogen Depassivation Lithography (The Most Precise Patterning)

**Zyvex Labs** in Richardson, Texas sells a commercial product called ZyvexLitho1 that performs hydrogen depassivation lithography (HDL) on silicon. The process removes individual hydrogen atoms from a passivated Si(100) surface to create atomically precise 2D patterns. Those exposed silicon sites can then be functionalized through selective chemistry.

The numbers:

- The rate is 50 hydrogen atoms per second, the figure Zyvex reported in 2010. Its 2025 conference abstract on nanoimprint masks says the throughput of this STM-based lithography is "severely limited compared to other direct write techniques such as E-beam Lithography".
- The resolution is 768 picometers (0.768 nm), the width of a Si(100) 2×1 dimer row. That is sub-nanometer and below what either EUV or e-beam lithography can achieve.
- In May 2025 Zyvex presented a route to nanoimprint templates written with HDL and reported sub-10 nm features and gratings with a feature radius of curvature down to 1.5 nm. Transfer of the template into quartz was listed as the next step.

The projection that goes with these numbers is also from 2010. Zyvex said then that within seven years it would be selling tools that remove more than a million hydrogen atoms a second using 10 parallel tips, at a cost of about $2,000 per cubic micrometer of added silicon. Those seven years have passed and the projection remains undemonstrated, but the single-tip system is a shipping product.

**Verdict**: Real commercial product. But there are important caveats. HDL removes atoms (subtraction), it does not place them (addition). It creates 2D patterns on silicon surfaces, not 3D structures. And it operates in a single material system. This is atomically precise patterning, not atomically precise construction.

**Sources**: [Zyvex Labs](https://www.zyvexlabs.com/). For the 2010 rate and projection, [Atomic-level manufacturing](https://www.eurekalert.org/news-releases/738776) (American Institute of Physics, 19 October 2010). For the 2025 work, the conference abstracts [Atomically Precise Lithography for Nanoimprint masks](https://eipbn.org/abstracts/2025/papers/4C-2.pdf) and [Fabrication of Atomically-precise Nanoimprint Masks by STM Lithography](https://eipbn.org/abstracts/2025/papers/6A-4.pdf). For the resolution, [Zyvex Labs Announces Sub-Nanometer Resolution Lithography System](https://thequantuminsider.com/2022/09/28/zyvex-labs-announces-sub-nanometer-resolution-lithography-system-2/).

---

## 3. Covalent Mechanosynthesis (An Experimental Demonstration) {#3-covalent-mechanosynthesis-the-first-experimental-demonstration}

In December 2025, a team of 60 authors, all listed with CBN Nano Technologies, posted a preprint demonstrating what they call mechanosynthesis, using inverted-mode scanning tunneling microscopy (arXiv:2512.24431). The author list includes Ralph Merkle, who has been writing about mechanosynthesis since the 1990s.

What they actually demonstrated:

- A single hydrogen atom removed from the silicon probe in 27 of 28 trials (96.4%), with 20 of the 27 at the targeted atom
- A second hydrogen atom removed in 24 of 24 attempts to form a pair of dangling bonds, with 21 of the 24 producing the intended pair
- Sub-angstrom positioning precision
- Zero-bias operation (no applied voltage during the mechanosynthetic step)
- The key idea is control of both sides of the tunnel junction: tailored molecules on the sample surface image the probe apex and also act as the reagents, so the probe's atomic structure is known

The authors call this mechanosynthesis: a specific chemical reaction driven by mechanical control of where the reagents sit, with no applied bias.

**Verdict**: A genuine milestone. But the scope is extremely limited: only hydrogen abstraction from silicon. Only one type of reaction on one substrate. The paper says the approach "is expected to extend to other elements and moieties," but that extension is not shown in it. There is a large distance between removing hydrogen atoms from silicon and building arbitrary covalent structures from multiple elements.

**Source**: [Inverted-Mode Scanning Tunneling Microscopy for Atomically Precise Fabrication (arXiv:2512.24431)](https://arxiv.org/abs/2512.24431), a preprint. The trial counts are in its main text and supplement.

---

## 4. DNA Origami (The Most Versatile Nanoscale Construction)

DNA origami is the most versatile method currently available for building complex nanoscale structures. The technique folds a long single-stranded DNA scaffold into arbitrary 2D and 3D shapes using hundreds of short "staple" strands that hold the scaffold in the desired configuration. Attachment points on the structure can be positioned with sub-nanometer precision.

What has actually been built and demonstrated:

- Arbitrary 2D and 3D shapes at approximately 100 nm scale, with attachment points placed to sub-nm accuracy
- Drug delivery vehicles: doxorubicin-loaded DNA origami structures that showed antitumor efficacy in nude mice
- Metal oxide nanostructures fabricated via atomic layer deposition (ALD) on DNA origami crystal templates (2025)
- Self-assembling swarm molecular robots demonstrated by a collaboration between Tohoku University and Kyoto University (2024)
- DNA nanorulers for microscopy calibration, used to validate super-resolution microscopy systems

Commercial products actually being sold today:

- **GATTAquant** (Braunschweig, Germany): sells DNA nanorulers for super-resolution microscopy calibration. These are atomically precise structures with fluorophores at known separations, used as measurement standards. It is a real product on sale.
- **tilibit nanosystems** (Munich, Germany): sells modular DNA origami kits for research laboratories. Pre-designed scaffold and staple sets for building specific nanostructures.

**Verdict**: The most versatile nanoscale construction method available today. Real commercial products exist and are being sold. But the limitations are significant: DNA origami operates in aqueous environments only, at approximately 100 nm scale, producing structures that are soft and not mechanically robust. The chemistry is limited to what is compatible with DNA. This is a powerful research tool and a real commercial product category, but it is not a path to general-purpose manufacturing of hard, dry, mechanically strong structures.

**Sources**: [GATTAquant](https://www.gattaquant.com/), [tilibit nanosystems](https://www.tilibit.com/)

---

## 5. Atomically Precise Metal Nanoclusters

Wet chemistry methods can produce metal nanoclusters with exact, crystallographically determined compositions. The most studied examples are gold clusters: Au25, Au38, Au144, and others. Each cluster contains a specific number of metal atoms in a specific geometric arrangement, confirmed by X-ray crystallography.

What has been demonstrated:

- Exact-composition clusters with known crystal structures for gold, silver, and copper
- Catalytic applications: selective hydrogenation reactions where the cluster composition determines selectivity
- Electrocatalysis for energy applications
- Early commercial deployment in water decontamination and chemical processing

**Verdict**: These are genuinely atomically precise products. Every cluster in a batch has the same number of atoms in the same arrangement. But they are self-assembled via thermodynamically driven wet chemistry, not positionally assembled by a tool. You do not choose where each atom goes; the chemistry determines the structure. The range of accessible compositions is limited to what thermodynamics and kinetics allow. This is atomically precise manufacturing in the sense that the products are atomically precise, but not in the sense that you have arbitrary control over the arrangement.

---

## 6. Molecular Machines (The Earliest Stage Building Blocks)

Synthetic molecular machines that can perform mechanical work at the molecular scale have been demonstrated by several research groups. The most relevant question for matter compilation is whether any of them can actually build things.

What has been demonstrated:

- **Molecular motors**: rotational speeds of 10 million revolutions per second (Ben Feringa's group, University of Groningen). These are light-driven or chemically driven molecular rotors.
- **Light-activated artificial muscles**: macroscopic actuation from molecular-level photochemical switching (Nature Communications, 2025).
- **Polymer assemblers**: the group of David Leigh at the University of Manchester demonstrated a synthetic molecular machine that moves along a track and joins building blocks in a defined order, forming a single-sequence oligomer with a carbon-carbon backbone (Chem, 2020).

The Leigh group work is the most relevant because it demonstrates a synthetic machine that actually builds a specific molecular product. But the performance numbers are sobering. The group's 2013 peptide machine took 36 hours to link three amino acids:

- Speed: approximately 1 amino acid per 12 hours
- For comparison, a biological ribosome assembles 15 to 20 amino acids per second
- That is a factor of roughly 600,000 to 900,000 times slower than biology

**Verdict**: Proof that synthetic molecular machines CAN build specific molecular products. This is a genuine scientific achievement. But at six orders of magnitude slower than biology, there is no manufacturing application. These are research demonstrations, not manufacturing tools. Closing a factor-of-a-million performance gap is not incremental engineering; it requires fundamentally different approaches.

**Sources**: McTernan, De Bo and Leigh, [A Track-Based Molecular Synthesizer that Builds a Single-Sequence Oligomer through Iterative Carbon-Carbon Bond Formation](https://doi.org/10.1016/j.chempr.2020.09.021) (Chem, 2020). For the 2013 machine, Lewandowski et al., [Sequence-Specific Peptide Synthesis by an Artificial Small-Molecule Machine](https://doi.org/10.1126/science.1229753) (Science, 2013), and the 36 hours in [Rotaxane mimics ribosome to spin out peptides](https://www.chemistryworld.com/news/rotaxane-mimics-ribosome-to-spin-out-peptides/5793.article) (Chemistry World).

---

## 7. Diamond Mechanosynthesis (The Theory Without The Practice)

Diamond mechanosynthesis has the most extensive theoretical literature of any proposed APM system. Robert Freitas and Ralph Merkle have published detailed computational studies of tooltip designs, reaction pathways, and theoretical machine architectures for building diamond structures atom by atom.

The track record:

- **CBN Nano Technologies**: holds mechanosynthesis patents, among them [US 11,180,514](https://patents.google.com/patent/US11180514B2/en) (granted 2021) and [US 11,708,384](https://patents.google.com/patent/US11708384B2/en) (granted 2023). These patents describe tooltip geometries, reaction sequences, and molecular machine designs for diamond construction.
- **Freitas's theoretical framework**: multiple publications describing specific tooltip chemistries, reaction energetics calculated via density functional theory (DFT), and designs for complete molecular assembler systems.
- **Philip Moriarty at the University of Nottingham**: received 1.53 million GBP for a 5-year experimental program to attempt diamond mechanosynthesis, starting in 2008. In a 2011 interview Moriarty said diamond is "a very difficult material to work with" and that his group had "a parallel effort focused on silicon, which is much, much easier to work with than diamond."

The bottom line: despite more than 20 years of theoretical work, detailed computational modeling, and significant experimental funding, there is zero experimental demonstration of diamond mechanosynthesis. No one has placed a carbon atom onto a diamond surface using a mechanical tool with positional control. The patents describe machines that no one has reported building.

This does not mean diamond mechanosynthesis is impossible. The theoretical work may be entirely correct. But the gap between "DFT says this reaction should work" and "we did this reaction in a lab" is the gap where most proposed nanotechnologies go to die.

**Verdict**: Extensive theoretical work. Computationally modeled. Patented. But zero experimental demonstrations of diamond mechanosynthesis after two decades. The theory is ahead of experiment by at least a generation.

**Sources**: [CBN Nano Technologies](https://www.cbnano.com/). The two patents are both titled "Systems and methods for mechanosynthesis". The Nottingham grant is in [Diamond mechanosynthesis for atomically precise nanotechnology to be explored experimentally](https://events.foresight.org/diamond-mechanosynthesis-for-atomically-precise-nanotechnology-to-be-explored-experimentally/) (Foresight Institute), and the 2011 interview is [Philip Moriarty discusses mechanosynthesis with Sander Olson](https://www.nextbigfuture.com/2011/03/philip-moriarty-discusses.html) (NextBigFuture).

---

## 8. What This Inventory Reveals

The pattern across all seven categories is consistent: real atomically precise manufacturing exists today, but every demonstrated capability is narrow.

| What works | Material | Scope | Scale |
|---|---|---|---|
| SQC qubit placement | Phosphorus in silicon | Single atom type, single substrate | 250K registers in 8 hours |
| Zyvex HDL | Hydrogen on silicon | Atom removal, not addition | 2D patterns, sub-nm resolution |
| Inverted-mode STM | H abstraction from Si | One reaction type | Single atoms, 27 of 28 trials |
| DNA origami | DNA | Aqueous, soft, ~100 nm | Billions of copies per batch |
| Metal nanoclusters | Au, Ag, Cu clusters | Self-assembled, specific compositions | Sub-2 nm clusters |
| Molecular machines | Organic molecules | Extremely slow | Single molecules |
| Diamond mechanosynth | Carbon on diamond | Theory only | Zero experimental demos |

Several observations emerge:

**Silicon dominates.** Three of the six experimentally demonstrated categories (SQC, Zyvex, inverted-mode STM) work on silicon. This is not because silicon is the ideal substrate for matter compilation. It is because silicon surface science is the most mature field in nanotechnology, with decades of STM expertise, well-characterized surfaces, and a huge installed base of equipment. The demonstrated capabilities reflect where the tools are, not where the applications need to be.

**Subtraction is easier than addition.** Zyvex removes hydrogen. The December 2025 STM result removes hydrogen. SQC deposits phosphorus, but only one atom type. Removing an atom from a known surface is a much more tractable problem than placing a specific atom at a specific site on a partially-built structure of mixed composition. The hardest part of matter compilation (multi-element positional assembly) has the least experimental support.

**Self-assembly scales, positional assembly doesn't.** DNA origami and metal nanoclusters can produce billions of identical copies because they rely on thermodynamic self-assembly. Every positional method (STM-based) operates on one site at a time. The throughput problem is fundamental: you need parallelism to scale, and parallelism for positional assembly requires arrays of independently controlled tips, which nobody has demonstrated at scale.

**The gap is in the middle.** We can place single atoms (bottom) and we can manufacture macroscopic objects (top). The gap is in the mesoscale: building structures from thousands to millions of precisely placed atoms of multiple element types. This is where convergent assembly is supposed to work, but convergent assembly from atomically precise components has not been experimentally demonstrated at any scale.

---

## 9. Confidence Assessment

**Established** (high confidence, experimentally demonstrated):

Atomically precise construction works for narrow domains. SQC, Zyvex, and GATTAquant have commercial products. The December 2025 inverted-mode STM preprint reports experimental mechanosynthesis of one reaction type. Individual atoms can be placed or removed with sub-nanometer precision on silicon surfaces. DNA origami can build complex 3D nanostructures in aqueous solution. These are facts, not projections.

**Plausible** (reasonable extrapolation, not yet demonstrated):

These narrow capabilities will expand to more materials, more reaction types, and larger scales over the next 10 to 20 years. The inverted-mode STM technique will be extended beyond hydrogen abstraction to other reactions. Tip arrays will achieve modest parallelism (tens to hundreds of tips). DNA origami will be used as scaffolding for inorganic materials with increasing sophistication. SQC-style placement will extend to other dopant atoms. This is plausible because the underlying physics does not prohibit it and because there are funded research programs pursuing each extension.

**Speculative** (possible but undemonstrated, requires breakthroughs):

These individual capabilities will converge into a general-purpose matter compilation capability within a generation. Multi-element positional assembly will achieve the throughput needed for practical manufacturing. Convergent assembly from atomically precise blocks will be demonstrated and scaled. Diamond or other hard covalent materials will be built by mechanosynthesis. The speculative label is warranted because every step in this chain requires solving problems that nobody has solved yet, and several of them (multi-element positional assembly, massively parallel tip control, convergent assembly at scale) may turn out to be much harder than the optimistic projections suggest.

---

## 10. What To Watch

The developments that would change this assessment most dramatically:

1. **Multi-element mechanosynthesis**: any experimental demonstration of positionally placing two or more different element types to build a defined covalent structure. This has never been done.
2. **Parallel tip arrays**: any demonstration of more than 10 independently controlled STM tips performing coordinated mechanosynthetic operations. Zyvex has projected this but not demonstrated it.
3. **Convergent assembly**: any demonstration of assembling atomically precise sub-components into a larger atomically precise structure through mechanical means. This is the core claim of the Drexlerian manufacturing pathway and it has zero experimental support.
4. **SQC expansion**: if SQC extends their PAQMan process to elements beyond phosphorus or substrates beyond silicon, that would demonstrate the generalizability of their approach.
5. **Molecular machine speed**: any synthetic molecular machine operating within two orders of magnitude of ribosomal speed (so, 0.1 to 1 operations per second or faster). Current synthetic machines are six orders of magnitude too slow.

Until at least two of these five milestones are achieved, the gap between "narrow APM works" and "general-purpose matter compilation" remains firmly in the speculative category.

---

## Sources

- Silicon Quantum Computing: [https://sqc.com.au/](https://sqc.com.au/)
- Zyvex Labs: [https://www.zyvexlabs.com/](https://www.zyvexlabs.com/)
- Inverted-mode STM mechanosynthesis: [arXiv:2512.24431](https://arxiv.org/abs/2512.24431)
- GATTAquant DNA nanorulers: [https://www.gattaquant.com/](https://www.gattaquant.com/)
- tilibit nanosystems: [https://www.tilibit.com/](https://www.tilibit.com/)
- CBN Nano Technologies: [https://www.cbnano.com/](https://www.cbnano.com/)
- Leigh group polymer assembler: [DOI: 10.1016/j.chempr.2020.09.021](https://doi.org/10.1016/j.chempr.2020.09.021)
