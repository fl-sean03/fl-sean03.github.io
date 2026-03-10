---
title: "Building Reality Check: What Has Actually Been Built"
description: "An honest inventory of what has been constructed with atomic or near-atomic precision as of early 2026. What works, what doesn't, and where the gaps are."
date: 2026-03-09
---


---

## The Question

What has actually been BUILT with atomic precision? Not predicted, not simulated, not published in a theoretical paper, but physically constructed and demonstrated. This is a harder question than it sounds, because the field is saturated with computational studies, theoretical designs, and promissory roadmaps. Filtering down to what has been physically realized gives a much shorter and more sobering list.

---

## 1. Silicon Quantum Devices (The Most Commercially Advanced APM)

**Silicon Quantum Computing (SQC), Sydney, Australia** is the most commercially advanced atomically precise manufacturing operation in the world. Their approach uses scanning tunneling microscopy combined with phosphine dosing to place individual phosphorus atoms into a silicon crystal lattice with 0.13 nm accuracy. The process is called PAQMan (Parallel Atomically Quilted Manufacturing), and it is the only method in the world that can image the exact positions of qubits embedded in a solid-state substrate.

What SQC has actually demonstrated:

- November 2025: patterned 250,000 qubit registers in 8 hours, a throughput that would have seemed absurd five years ago
- 99.99% gate fidelity, among the highest reported for any qubit platform
- Real commercial products being sold to paying customers

The products are worth listing explicitly because they represent genuine APM revenue:

- **Quantum Twins**: application-specific quantum simulators. These are custom chips where the arrangement of phosphorus atoms encodes a replica of a physical system the customer wants to simulate. Each chip is a bespoke atomically precise structure built to order.
- **Watermelon**: a quantum machine learning system built on the same atomically precise silicon platform.
- **Customers**: Telstra (Australian telecom) and the Australian Department of Defence, which took delivery of a rack-mounted quantum system deployed in a datacenter in August 2025.

This is real APM being used commercially today. Atoms are being placed with sub-nanometer precision to build functional devices that people pay money for.

**Verdict**: The most commercially advanced APM in the world. Real products, real customers, real revenue. But the scope is narrow: placing one type of atom (phosphorus) in one substrate (silicon) for one application (quantum computing). Extending this to other elements or other substrates is a separate engineering challenge that SQC has not attempted.

**Source**: [Silicon Quantum Computing](https://sqc.com.au/)

---

## 2. Hydrogen Depassivation Lithography (The Most Precise Patterning)

**Zyvex Labs** in Richardson, Texas sells a commercial product called ZyvexLitho1 that performs hydrogen depassivation lithography (HDL) on silicon. The process removes individual hydrogen atoms from a passivated Si(100) surface to create atomically precise 2D patterns. Those exposed silicon sites can then be functionalized through selective chemistry.

The numbers:

- Rate: approximately 50 hydrogen atoms per second
- Resolution: 768 picometers (0.768 nm), which is sub-nanometer and below what either EUV or e-beam lithography can achieve
- May 2025: Zyvex demonstrated atomically precise nanoimprint masks at dimensions beyond the capability of any other lithography technology

Their projection (not yet achieved) calls for 10 parallel tips operating at 1 million atoms per second, which would bring the cost down to roughly $2,000 per cubic micrometer of atomically precise material. That projection remains undemonstrated, but the single-tip system is a shipping product.

**Verdict**: Real commercial product. But there are important caveats. HDL removes atoms (subtraction), it does not place them (addition). It creates 2D patterns on silicon surfaces, not 3D structures. And it operates in a single material system. This is atomically precise patterning, not atomically precise construction.

**Source**: [Zyvex Labs](https://www.zyvexlabs.com/)

---

## 3. Covalent Mechanosynthesis (The First Experimental Demonstration)

In December 2025, a team of 54 researchers published an experimental demonstration of deterministic covalent mechanosynthesis using inverted-mode scanning tunneling microscopy (arXiv:2512.24431). The author list includes Ralph Merkle, who has been writing about mechanosynthesis since the 1990s.

What they actually demonstrated:

- 96.4% success rate for single hydrogen atom removal from a silicon surface
- 100% yield in sequential hydrogen abstractions for dangling bond pair formation
- Sub-angstrom positioning precision
- Zero-bias operation (no applied voltage during the mechanosynthetic step)
- The critical innovation was functionalizing both sides of the tunnel junction with characterized matter, meaning both the tip and the surface are known at the atomic level

This is the first published experimental result that can legitimately be called mechanosynthesis: a mechanical tool performing a specific chemical reaction at a specific site with high fidelity and atomic positioning.

**Verdict**: A genuine milestone. The first real experimental mechanosynthesis. But the scope is extremely limited: only hydrogen abstraction from silicon. Only one type of reaction on one substrate. The paper notes that extension to other elements and reaction types "is expected," but that extension has not been demonstrated. There is a large distance between removing hydrogen atoms from silicon and building arbitrary covalent structures from multiple elements.

**Source**: [arXiv:2512.24431](https://arxiv.org/abs/2512.24431)

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

- **GATTAquant** (Braunschweig, Germany): sells DNA nanorulers for super-resolution microscopy calibration. These are atomically precise structures with fluorophores at known separations, used as measurement standards. Real product, real customers, real revenue.
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
- **Polymer assemblers**: the group of David Leigh at the University of Manchester demonstrated a synthetic molecular machine that assembles specific polymer sequences by threading monomers onto a track in a defined order (Nature Communications, 2020).

The Leigh group result is the most relevant because it demonstrates a synthetic machine that actually builds a specific molecular product. But the performance numbers are sobering:

- Speed: approximately 1 amino acid equivalent per 12 hours
- For comparison, a biological ribosome assembles 15 to 20 amino acids per second
- That is a factor of roughly 600,000 to 900,000 times slower than biology

**Verdict**: Proof that synthetic molecular machines CAN build specific molecular products. This is a genuine scientific achievement. But at six orders of magnitude slower than biology, there is no manufacturing application. These are research demonstrations, not manufacturing tools. Closing a factor-of-a-million performance gap is not incremental engineering; it requires fundamentally different approaches.

**Source**: Leigh group polymer assembler: [DOI: 10.1038/s41467-020-18223-5](https://doi.org/10.1038/s41467-020-18223-5)

---

## 7. Diamond Mechanosynthesis (The Theory Without The Practice)

Diamond mechanosynthesis has the most extensive theoretical literature of any proposed APM system. Robert Freitas and Ralph Merkle have published detailed computational studies of tooltip designs, reaction pathways, and theoretical machine architectures for building diamond structures atom by atom.

The track record:

- **CBN Nano Technologies**: holds 24+ mechanosynthesis patents granted between 2021 and 2023. These patents describe tooltip geometries, reaction sequences, and molecular machine designs for diamond construction.
- **Freitas's theoretical framework**: multiple publications describing specific tooltip chemistries, reaction energetics calculated via density functional theory (DFT), and designs for complete molecular assembler systems.
- **Philip Moriarty at the University of Nottingham**: received 1.53 million GBP for a 5-year experimental program to attempt diamond mechanosynthesis, starting in 2008. Moriarty's team found diamond surfaces too difficult to work with experimentally and pivoted to silicon, which is how they contributed to the silicon-based work described in Section 3.

The bottom line: despite more than 20 years of theoretical work, detailed computational modeling, and significant experimental funding, there is zero experimental demonstration of diamond mechanosynthesis. No one has placed a carbon atom onto a diamond surface using a mechanical tool with positional control. The patents describe machines that have never been built.

This does not mean diamond mechanosynthesis is impossible. The theoretical work may be entirely correct. But the gap between "DFT says this reaction should work" and "we did this reaction in a lab" is the gap where most proposed nanotechnologies go to die.

**Verdict**: Extensive theoretical work. Computationally modeled. Patented. But zero experimental demonstrations after two decades. The theory is ahead of experiment by at least a generation.

**Source**: [CBN Nano Technologies](https://www.cbnano.com/)

---

## 8. What This Inventory Reveals

The pattern across all seven categories is consistent: real atomically precise manufacturing exists today, but every demonstrated capability is narrow.

| What works | Material | Scope | Scale |
|---|---|---|---|
| SQC qubit placement | Phosphorus in silicon | Single atom type, single substrate | 250K registers in 8 hours |
| Zyvex HDL | Hydrogen on silicon | Atom removal, not addition | 2D patterns, sub-nm resolution |
| Inverted-mode STM | H abstraction from Si | One reaction type | Single atoms, 96.4% yield |
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

Atomically precise construction works for narrow domains. SQC, Zyvex, and GATTAquant have commercial products generating revenue. The December 2025 inverted-mode STM result is the first legitimate experimental mechanosynthesis. Individual atoms can be placed or removed with sub-nanometer precision on silicon surfaces. DNA origami can build complex 3D nanostructures in aqueous solution. These are facts, not projections.

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
- Leigh group polymer assembler: [DOI: 10.1038/s41467-020-18223-5](https://doi.org/10.1038/s41467-020-18223-5)
