# Presenter notes

## 1. Interface Force Field

How can a computer tell us which face of a crystal a molecule will stick to, and why should we believe its answer? We build the tools one at a time, from a single pair of atoms up to whole surfaces in water, and then look at three published studies where the Interface Force Field, or IFF, was compared with experiments.

The picture is a peptide called S7 lying on platinum in water; it comes back in the first example and at the end.

The crystal structures come from the Crystallography Open Database or from published lattice sizes, and the surfaces were built from them with ASE and the molecules with RDKit, all open software. The pictures of molecules on surfaces are illustrations, arranged to show the idea rather than taken from a simulation. Every result quoted comes from the cited papers and was not rerun here. Besides the worked arithmetic, the one calculation made for this presentation is the electron cloud of a water molecule, and it only draws a picture.

### Sources

- Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840–846. https://doi.org/10.1021/nl400022g
- Wyckoff (1963). Crystal Structures 1, 7–83. Crystallography Open Database entry 9008480, platinum. https://www.crystallography.net/cod/9008480.html
- RDKit, open-source cheminformatics software. https://www.rdkit.org
- Larsen et al. (2017). The atomic simulation environment, a Python library for working with atoms. Journal of Physics: Condensed Matter 29, 273002. https://doi.org/10.1088/1361-648X/aa680e

## 2. Can one amino acid change the shape of a metal crystal?

Proteins are chains of amino acids, and a peptide is a short chain. Each amino acid has a one-letter code. Here T is threonine, L is leucine and F is phenylalanine, which carries a flat ring of six carbon atoms.

Ruan and colleagues grew platinum crystals in water with each peptide present. With TLT the crystals came out as cubes, whose faces all show a square pattern of atoms. With TFT most came out as tetrahedra, whose faces all show a triangular pattern. Chemists call these the {100} and {111} faces.

A crystal grows by adding atoms to its faces. A molecule that sticks to one kind of face slows growth there, so that face ends up covering the crystal. The question is how a simulation could explain why F prefers the triangular face.

### Sources

- Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840–846. https://doi.org/10.1021/nl400022g
- Wyckoff (1963). Crystal Structures 1, 7–83. Crystallography Open Database entry 9008480, platinum. https://www.crystallography.net/cod/9008480.html
- RDKit, open-source cheminformatics software. https://www.rdkit.org

## 3. Models built separately do not fit together

To simulate a peptide on platinum in water, the computer needs rules for three sets of interactions. Platinum atoms hold the solid together. Water molecules and the peptide interact with each other. And every platinum atom interacts with every nearby atom of water and peptide, and this third set decides which crystal face the peptide sticks to.

Good rules for the first two sets already existed, but separately. Metal models were built to describe metals, and molecular models were built to describe water and proteins. The third set needs both sides described in the same terms.

A popular metal model, the embedded-atom method, uses equations of its own, while protein models such as CHARMM and AMBER use different ones. Nothing in either says how a metal atom should feel a water molecule. Kanhaiya and colleagues also report that metal-only models of this kind give surface energies up to about 50% too low.

IFF describes the metal with the same simple equation the molecular models already use between atoms that are not bonded, the Lennard-Jones curve we meet shortly. Its two numbers per metal are tuned so the simulated metal has the measured density and surface energy, and the metal–molecule pairs then follow from the same rules. For ten metals, Kanhaiya and colleagues report agreement with experiment within 0.1 to 5% for lattice size, surface energy, water interface energy and binding of organic molecules.

### Sources

- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Heinz, Lin, Mishra and Emami (2013). Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 29, 1754–1765. https://doi.org/10.1021/la3038846

## 4. IFF puts solids and molecules in one compatible model

A force-field family is a complete set of rules and numbers for one kind of chemistry, such as AMBER, CHARMM and OPLS-AA for proteins and organic molecules, or PCFF for polymers. IFF adds solids, such as metals, silica, minerals and cement, written in the same style as those families so the two can be used together.

The surfaces are built to match the real ones, including the OH groups on silica and the way a mineral surface changes with acidity. One simulation can then hold a solid, water and a molecule together, and its results can be compared with experiments.

### Sources

- Heinz, Lin, Mishra and Emami (2013). Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 29, 1754–1765. https://doi.org/10.1021/la3038846
- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Wyckoff (1963). Crystal Structures 1, 7–83. Crystallography Open Database entry 9008463, gold. https://www.crystallography.net/cod/9008463.html
- Levien, Prewitt and Weidner (1980). Structure and elastic properties of quartz at pressure. American Mineralogist 65, 920–930. Crystallography Open Database entry 9000775. https://www.crystallography.net/cod/9000775.html
- Sudarsanan and Young (1969). Significant precision in crystal structural details: Holly Springs hydroxyapatite. Acta Crystallographica B 25, 1534–1543. Crystallography Open Database entry 9011091. https://www.crystallography.net/cod/9011091.html
- Mumme (1995). Crystal structure of tricalcium silicate from a Portland cement clinker and its application to quantitative XRD analysis. Neues Jahrbuch für Mineralogie, Monatshefte 4, 145–160. Crystallography Open Database entry 1540704. https://www.crystallography.net/cod/1540704.html
- RDKit, open-source cheminformatics software. https://www.rdkit.org

## 5. A force field replaces the electron cloud with simple rules

Every atom has a small, heavy nucleus made of protons and, in most atoms, neutrons, surrounded by a cloud of electrons. Where atoms sit and how they hold together is decided by these electrons.

Quantum chemistry computes the electron cloud directly. The most common method is density functional theory, or DFT, which uses an approximate formula called a functional to describe how electrons affect each other. It is accurate but slow, so it is usually limited to hundreds or a few thousand atoms.

A force field skips the electrons. Atoms become balls, bonds become springs, and each atom carries a fixed partial charge, a fraction of an electron’s charge, written δ− or δ+. In water the oxygen pulls electrons towards itself, so it is slightly negative and the hydrogens slightly positive.

Machine-learned force fields sit in between. A model such as MACE or AI²BMD is trained to reproduce quantum results on many example structures, and it is reliable only for structures like the ones it was trained on. A classical force field such as IFF uses fixed rules, so it is the fastest of these methods and reaches millions of atoms, but a standard one never breaks or forms bonds. It suits questions about surfaces, binding and water, where bonds stay intact.

The cloud on the left is a real calculation of one water molecule, made with the PySCF program and the PBE functional. The balls and springs on the right are a drawing of the same molecule.

### Sources

- Hohenberg and Kohn (1964). Inhomogeneous Electron Gas. Physical Review 136, B864–B871. https://doi.org/10.1103/PhysRev.136.B864
- Heinz and Suter (2004). Atomic Charges for Classical Simulations of Polar Systems. Journal of Physical Chemistry B 108, 18341–18352. https://doi.org/10.1021/jp048142t
- PySCF, the Python-based Simulations of Chemistry Framework. https://pyscf.org
- Batatia et al. (2022). MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields. arXiv 2206.07697. https://arxiv.org/abs/2206.07697
- Wang et al. (2024). Ab initio characterization of protein molecular dynamics with AI²BMD. Nature 635, 1019–1027. https://doi.org/10.1038/s41586-024-08127-z
- Wang et al. (2025). Author Correction to Ab initio characterization of protein molecular dynamics with AI²BMD. Nature. https://doi.org/10.1038/s41586-024-08556-w

## 6. The energy is a sum of five kinds of terms

Molecular mechanics adds up the energy of a whole system from simple pieces. Bond stretching, angle bending and twisting act along the chemical bonds inside a molecule. Van der Waals and charge interactions act between atoms that are not bonded to each other, including atoms in different molecules, and between a molecule and a solid.

Bonds and angles act like springs. A bond has a natural length, and stretching or squeezing it costs energy that grows with the square of the change, E = k (r − r₀)², so twice the stretch costs four times the energy. An angle works the same way, E = k (θ − θ₀)². Water’s O–H bond rests at about 0.96 ångström, where one ångström is a ten-billionth of a metre, and its H–O–H angle rests at about 104.5 degrees. Each family tunes the stiffness k so that molecules vibrate at their measured frequencies. The springs never break, so a standard force field cannot describe chemical reactions, in which bonds form or break.

Twisting around a bond has favourite angles. Ethane is two carbon atoms, each carrying three hydrogens. Looking along the bond between the carbons, the back hydrogens can sit between the front ones, called staggered, or behind them, called eclipsed, which costs a little more energy. The energy repeats every 120°, and a force field describes it with a smooth wave, E = k [1 + cos(nφ − δ)], where φ is the twist angle, n is the number of repeats in a full turn, three for ethane, and δ shifts where the lowest points fall. The height k is tuned to measurements or to quantum chemistry. Twisting terms like this decide how flexible molecules such as peptides and polymers fold and bend.

Each force-field family writes these pieces in its own way and with its own numbers. Some write the spring energy with a factor of one half and some leave it out, so stiffness numbers cannot be copied from one family into another without checking. Some, such as PCFF, add extra terms that couple stretching and bending and use a softer van der Waals curve, but all of them build the energy from these five pieces. Families also differ in how they treat atoms close together in one molecule. Pairs joined by one or two bonds are usually left out of the van der Waals and charge sums, and pairs three bonds apart are counted in full or scaled down, depending on the family.

A simulation then moves the atoms. Molecular dynamics adds up the force on every atom, moves every atom a tiny step according to those forces, and repeats. Each step is typically one femtosecond, a millionth of a billionth of a second, so a million steps make one nanosecond. Averages over many steps give measurable quantities such as density, energy or binding. Energy minimization, a related method, skips the motion and moves the atoms straight downhill to the nearest low-energy arrangement.

### Sources

- Heinz, Lin, Mishra and Emami (2013). Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 29, 1754–1765. https://doi.org/10.1021/la3038846

## 7. Two atoms attract until they get too close

Even neutral atoms attract each other weakly, because their electron clouds flicker and pull on each other. This is the van der Waals attraction. When the atoms get too close, their electron clouds overlap and they push apart strongly.

Energies here are in kilocalories per mole, the energy of one mole of such pairs, about 6 × 10²³ of them. The rhodium curve has its lowest point at r₀ = 2.757 Å with a depth ε of 7.84 kcal/mol. These two numbers were tuned so that simulated rhodium has the measured density and surface energy.

The curve is called 12-6 because its push grows as the twelfth power of one over the distance and its pull as the sixth power. Written with the lowest point, it is E = ε [(r₀/r)¹² − 2 (r₀/r)⁶].

The force on the atoms is the slope of the curve with its sign flipped. At 2.5 Å the energy is still negative, about −2.8 kcal/mol, yet the slope is steep and the atoms push apart with a force of about 54 kcal/mol per ångström. At 3.0 Å the slope is gentle and the atoms pull together with about 7.5. At 2.757 Å the curve is flat and the force is zero. A simulation moves atoms using these forces, so the shape of the curve matters as much as its depth.

Each metal gets its own pair of numbers. In the same study iridium has r₀ = 2.785 Å and ε = 9.20 kcal/mol, calcium 4.025 Å and 3.36, and strontium 4.379 Å and 3.40. Calcium and strontium are larger atoms, so their lowest points sit further out. A deeper well means the atoms hold on to each other more strongly, which goes with a higher surface energy. The study gives values like these for ten metals and for stainless steel.

Pairs of unlike atoms come from a mixing rule. A simulation with 10 kinds of atoms has 55 different pairs, too many to fit one by one, so the rule builds every unlike pair from the two like ones. The rule used here takes the geometric mean, the square root of the product. For rhodium with calcium, r₀ = √(2.757 × 4.025) = 3.331 Å and ε = √(7.84 × 3.36) = 5.13 kcal/mol. Families such as CHARMM and AMBER use the ordinary average for r₀ instead, so the rule must match the family the numbers are used with. This is a worked example of the rule, not a claim about real rhodium–calcium alloys.

The same curve is often written with σ, the distance where the energy crosses zero, which is shorter than r₀ by a factor of 1.1225. Programs such as LAMMPS expect σ. The 2021 paper calls its 2.757 Å σ but means the lowest point, which earlier IFF papers called r₀. If 2.757 Å is typed in as a zero crossing, the lowest point moves out to 3.095 Å, 12% too far. Five cells of rhodium would then measure about 21.3 Å instead of 19.0, and the surface energy would be wrong, all without any error message.

The fix is σ = 2.757 / 1.1225 = 2.456 Å. A force-field file can load without errors and still describe a different material, so after converting, check the curve family and the units the program expects, then compute one pair by hand. Its energy at 2.757 Å should read −7.84 kcal/mol, not 0, and its force should be zero. A 2021 correction to the paper added missing supplementary files and changed none of its tables.

### Sources

- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Kanhaiya, Kim, Im and Heinz (2021). Author Correction to Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials. https://doi.org/10.1038/s41524-021-00576-8
- Kanhaiya, Kim, Im and Heinz (2021). Supplementary Information for Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. https://static-content.springer.com/esm/art%3A10.1038%2Fs41524-020-00478-1/MediaObjects/41524_2020_478_MOESM1_ESM.pdf
- LAMMPS documentation, pair style lj/cut. https://docs.lammps.org/pair_lj.html
- Calculations and illustrations made for this presentation.

## 8. Charges reach much further than van der Waals

Coulomb’s law says the energy of two charges falls off only as one over the distance, E = 332.064 q₁q₂ / r. The number converts the energy to kcal/mol when r is in ångströms and the charges q₁ and q₂ are in elementary charges, the charge of one proton. Two opposite unit charges in a vacuum, such as a sodium ion and a chloride ion, have −110.7 kcal/mol at 3 Å and still −33.2 at 10 Å. The rhodium van der Waals pull at 10 Å is about −0.007.

In water the pull between ions is about 80 times weaker, because water molecules turn so that their opposite partial charge faces each ion, which screens it. A force field does not add this screening by hand. It comes out of the partial charges on the water molecules themselves.

### Sources

- NIST (2022). CODATA recommended values of the fundamental physical constants. https://physics.nist.gov/cuu/Constants/Table/allascii.txt
- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Calculations and illustrations made for this presentation.

## 9. IFF tunes each solid to its measured surface energy

Atoms at a surface have lost some of their neighbours, so a surface costs energy. Splitting a block makes two new faces, so the surface energy is the energy needed to pull the halves apart divided by twice the area of one face. It is measured in joules per square metre.

The energy of the block is the sum over every pair of atoms in it. Three rhodium atoms at the lowest-energy distance make three pairs, so their total is 3 × (−7.84) = −23.52 kcal/mol. Inside the crystal each atom has 12 nearest neighbours, each 2.689 Å away. That is closer than r₀ because the farther neighbours also pull, squeezing the nearest ones a little closer than a lone pair would sit. In practice a simulation adds up pairs out to a cutoff distance, beyond which the van der Waals pull is too weak to matter.

Rhodium is a face-centred cubic, or fcc, metal. Its repeating cell is a cube 3.803 Å on a side with an atom at each corner and one in the middle of each face. Each corner atom is shared by eight cells and each face atom by two, so one cell holds 8 × ⅛ + 6 × ½ = 4 atoms. Five cells in each direction give 500 atoms, and the simulation box repeats in every direction, called periodic boundaries, so the block behaves like part of an endless crystal. The two rhodium numbers were tuned to give this block its measured size, 19.016 Å along each edge, so that agreement is a calibration rather than a test.

For rhodium’s triangular face the measured surface energy is 2.64 ± 0.02 J/m² and the model gives 2.643. Like the crystal size, this was a tuning target, so it confirms the tuning rather than tests the model. Two small differences remain. The measurements may come from samples with mixed faces and read 1 to 2% high. The simulation gives an energy, while the measurement gives a free energy, which also counts entropy, a measure of how many ways the atoms can move and arrange themselves. The authors estimate that these two differences partly cancel.

Stiffness was not a tuning target, so it tests the model. It is measured in gigapascals, and one gigapascal is about ten thousand times the pressure of the atmosphere. For squeezing from all sides, the bulk modulus, the model gives 258 GPa against a measured 276, 6.5% low. For stretching, Young’s modulus, it gives 209 against 379, and for sliding one layer over another, the shear modulus, 77 against 147. Other measurements give 269 to 271 GPa for squeezing, 319 and 378 for stretching and 150 for shearing.

Curves that act only between pairs of atoms force two of the crystal’s stiffness constants to be equal, and real rhodium does not follow that rule. So the model is good for surfaces and interfaces, but its stiffness is a known weakness.

Force fields such as PCFF, COMPASS and CFF use a softer 9-6 curve, E = ε [2 (r₀/r)⁹ − 3 (r₀/r)⁶], whose push grows as the ninth power instead of the twelfth, while CHARMM, AMBER, OPLS-AA and CVFF use the 12-6 curve. Because the shapes differ, IFF publishes separate rhodium values for each. The 9-6 values are r₀ = 2.807 Å and ε = 6.38 kcal/mol. Both sets reproduce the crystal size and the surface energy, 2.643 J/m², but the 9-6 crystal is softer still, 175 GPa against 276 measured for squeezing. Using 12-6 numbers in a 9-6 force field, or the reverse, gives a different material without any error message.

### Sources

- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Kanhaiya, Kim, Im and Heinz (2021). Supplementary Information for Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. https://static-content.springer.com/esm/art%3A10.1038%2Fs41524-020-00478-1/MediaObjects/41524_2020_478_MOESM1_ESM.pdf
- Calculations and illustrations made for this presentation.

## 10. The F ring lies flat on platinum’s triangular face

S7 is a seven-amino-acid peptide, SSFPQPN, found by screening many peptides for ones that bind platinum. Ruan and colleagues simulated it on both faces in water with CHARMM-METAL, IFF’s early model for metals, which combines the CHARMM protein model with metal parameters written the same way.

On the triangular face the F ring lies flat, because its six carbons fit the triangular pattern of platinum atoms. On the square face the ring stands up instead, and the computed binding energy of +3 kcal/mol means the peptide does not stick, so water keeps that surface covered.

In the lab, every version of the peptide that contained F grew many tetrahedra, crystals with only triangular faces, and versions without F grew mainly cuboctahedra. One version, S7-G, with F replaced by glycine, G, still binds the triangular face strongly, at about −52 kcal/mol, but it also binds the square face, so it gives few tetrahedra. Versions with tyrosine in place of F lie flat on both faces. What matters is the contrast between the faces. The same idea explains the TLT to TFT switch from the opening.

The pictures are illustrations of these poses, not snapshots from the simulations.

### Sources

- Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840–846. https://doi.org/10.1021/nl400022g
- Wyckoff (1963). Crystal Structures 1, 7–83. Crystallography Open Database entry 9008480, platinum. https://www.crystallography.net/cod/9008480.html
- RDKit, open-source cheminformatics software. https://www.rdkit.org

## 11. Water spreads or beads up depending on the silica surface

Heating silica to between 200 and 1000 °C drives off its OH groups. On the fully covered surface water spreads flat, with a contact angle of 0°, and on the most heated surface it beads up at about 42°. The contact angle is the angle between the surface and the edge of a droplet, so a small angle means the water spreads.

Emami and colleagues built silica models with 4.7, 2.35, 1.2 and 0 OH groups per square nanometre to match these samples. The simulated angles came within 3° of the measured ones.

With a standard water model called TIP3P, the model also releases 160 mJ/m² of heat when dry silica with 4.7 OH groups per square nanometre is dipped in water, against 160 ± 5 measured. The paper lists both matches as features of the model, not as independent tests. A 2016 correction to the paper changed only two density plots, not these results.

The droplets are drawn to these angles and are not simulation snapshots.

### Sources

- Emami et al. (2014). Force Field and a Surface Model Database for Silica to Simulate Interfacial Properties in Atomic Resolution. Chemistry of Materials 26, 2647–2658. https://doi.org/10.1021/cm500365c
- Emami et al. (2016). Correction to Force Field and a Surface Model Database for Silica to Simulate Interfacial Properties in Atomic Resolution. Chemistry of Materials 28, 406–407. https://doi.org/10.1021/acs.chemmater.5b04760
- Levien, Prewitt and Weidner (1980). Structure and elastic properties of quartz at pressure. American Mineralogist 65, 920–930. Crystallography Open Database entry 9000775. https://www.crystallography.net/cod/9000775.html
- Jorgensen, Chandrasekhar, Madura, Impey and Klein (1983). Comparison of simple potential functions for simulating liquid water. Journal of Chemical Physics 79, 926–935. https://doi.org/10.1063/1.445869

## 12. Bone mineral changes its surface with pH

Hydroxyapatite is made of calcium ions, phosphate groups and hydroxide ions. pH measures how acidic water is, with 7 neutral and lower numbers more acidic. Protonation means a hydrogen ion, H⁺, attaching to a group such as phosphate.

Lin and Heinz built surface models for different pH. The bare crystal surface is stable only above pH 14, which almost never occurs in water around living things. By about pH 10 each surface phosphate has gained one hydrogen and the hydroxide and some calcium have left. By about pH 5 each has gained two, and more calcium has gone. Near pH 7 the surface carries a mix, and an infrared measurement found 31% with one hydrogen and 69% with two.

When dry hydroxyapatite meets water it gives off heat, the immersion energy, measured in millijoules per square metre. Weighting the model faces by how much of a real crystal each one covers gives 619 mJ/m² at pH 7, and counting all faces equally gives 533. Heat measurements on perfectly dried crystals give 600 to 700. The comparison depends on how the faces are weighted and on how dry the real samples were, since a sample that has already taken up water from the air gives off less heat.

The slices are cut from the measured crystal structure, with hydrogens added and calcium removed by hand to show each step. They are illustrations, not simulation results.

### Sources

- Lin and Heinz (2016). Accurate Force Field Parameters and pH Resolved Surface Models for Hydroxyapatite to Understand Structure, Mechanics, Hydration, and Biological Interfaces. Journal of Physical Chemistry C 120, 4975–4992. https://doi.org/10.1021/acs.jpcc.5b12504
- Sudarsanan and Young (1969). Significant precision in crystal structural details: Holly Springs hydroxyapatite. Acta Crystallographica B 25, 1534–1543. Crystallography Open Database entry 9011091. https://www.crystallography.net/cod/9011091.html

## 13. The IFF Agent carries one material through eight steps

The IFF Agent is a workflow described by the author for building and checking IFF models step by step. It sits around the force field and is not part of it. This presentation describes the workflow only and claims no implementation or results from it.

Its eight steps are named intake, references, model, contract, run and fit, validate, export readback, and review and disposition. The first four decide what the result must show before anything is computed. The contract fixes in advance which measurements may be used for tuning and which are kept back as tests.

Rhodium shows the steps with the published numbers. The question is rhodium faces in water. The references are the measured size, surface energy and stiffness. The model is a 12-6 pair curve. The contract tunes the size and surface energy and keeps stiffness as a test. The fit gives r₀ = 2.757 Å and ε = 7.84 kcal/mol. The test finds a stretching stiffness of 209 GPa against 379 measured. The readback checks that the exported file gives −7.84 kcal/mol at r₀, not 0, which catches the mix-up between r₀ and σ described with the Lennard-Jones curve. The review approves the model for surfaces and flags its stiffness.

Every number comes from the 2021 rhodium paper; none is a new fit or result.

### Sources

- Author’s description of the IFF Agent workflow (2026).
- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1

## 14. A flat ring on a triangular face explains the crystal shape

Back to the opening question. Swapping one amino acid, L for F, turned platinum cubes into tetrahedra. The simulations showed why. The F ring lies flat on the triangular face and sticks, while on the square face the ring stands up and the peptide does not stick. Crystals grow slowest on the faces that are covered, so the triangular faces end up covering the crystal, and a crystal with only triangular faces is a tetrahedron.

That answer needed all three sets of interactions in one model, which is what IFF provides. IFF supplies compatible interaction equations and material parameters so a classical simulation can describe a solid together with water, polymers or biological molecules. It addresses inconsistent material/surface descriptions and the difficulty of combining separately developed models, allowing supported interface structures, binding and energies to be calculated and compared with experiments.

The three examples each compared a different kind of result with experiment, the face a peptide prefers on platinum, how water wets silica, and the heat given off as water meets bone mineral. In each, it matters which measurements tuned the model and which were left to test it, and a standard model still cannot describe reactions.

Other published studies tested IFF in other ways. On silica, simulations with PCFF-SILICA, IFF’s silica model, compared the twelve-amino-acid peptide KSLSRHDHIHHH with two versions of it. In the experiments, swapping the histidine at position 6 for alanine made the peptide stick more, and the same swap at position 11, near the C-terminal end of the chain, made it stick less. The simulations ranked the three in the same order, but only on the surface model that matched the experiment, with about 4.7 OH groups per square nanometre. With twice as many, 9.4, the order changed.

For cement, Mishra, Flatt and Heinz computed the energy needed to pull two broken faces of tricalcium silicate apart at 90 °C, close to the conditions in a working mill. Bare faces needed 240 to 450 mJ/m², depending on whether water had reached them, and less than one layer of grinding additive cut that to between 50 and 110. These results are in section 4.3 and Figures 10 and 11 of their paper. Mill tests reported in a patent ranked three amine additives in the same order as the simulation. That is a ranking only, and glycerine, the fourth additive, was not in those tests.

For gold, a polarizable model, in which each gold atom’s electrons can shift towards or away from a nearby ion, gives −13.0 ± 0.1 kcal/mol per water molecule in a layer on gold’s triangular face, and the plain model −12.8 ± 0.1. Measurements on gold made of many small crystals give −13 and −15.5. The shift matters most for ions close to the metal; for water the plain model is nearly as good.

### Sources

- Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840–846. https://doi.org/10.1021/nl400022g
- Heinz, Lin, Mishra and Emami (2013). Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 29, 1754–1765. https://doi.org/10.1021/la3038846
- Kanhaiya, Kim, Im and Heinz (2021). Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard-Jones potentials. npj Computational Materials 7, 17. https://doi.org/10.1038/s41524-020-00478-1
- Patwardhan et al. (2012). Chemistry of Aqueous Silica Nanoparticle Surfaces and the Mechanism of Selective Peptide Adsorption. Journal of the American Chemical Society 134, 6244–6256. https://doi.org/10.1021/ja211307u
- Mishra, Flatt and Heinz (2013). Force Field for Tricalcium Silicate and Insight into Nanoscale Properties: Cleavage, Initial Hydration, and Adsorption of Organic Molecules. Journal of Physical Chemistry C 117, 10417–10432. https://doi.org/10.1021/jp312815g
- Patent EP2527307A1 (2012, in German), clinker grinding tests with amine additives. https://data.epo.org/publication-server/rest/v1.0/publication-dates/20121128/patents/EP2527307NWA1/document.pdf
- Geada et al. (2018). Insight into induced charges at metal surfaces and biointerfaces using a polarizable Lennard-Jones potential. Nature Communications 9, 716. https://doi.org/10.1038/s41467-018-03137-8

## 15. Thank you

Thank you. The notes for each slide hold the equations, the worked numbers and the sources behind it, and the reading version shows them with every slide.

### Sources

- Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840–846. https://doi.org/10.1021/nl400022g
