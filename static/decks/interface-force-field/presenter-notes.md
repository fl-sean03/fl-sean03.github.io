# Presenter notes

## 1. Interface Force Field

I want to connect the atoms in a picture to a result we can check. We'll build the background first, work through rhodium, and then look at published systems where a molecular model helped explain an experiment. Every atomic drawing here is idealized. The plotted pair curves are analytic calculations from published parameters. The material results come from the cited papers and were not rerun for this talk.

Sources: H13, K21

## 2. An atom has a nucleus and electrons

An atom is a unit of an element. Its positive nucleus and negative electrons give it electrical structure. The electron cloud has no hard outer wall, so a sphere is a model of atomic size. A drawing can leave out electronic detail while keeping the atomic positions we need for a material calculation. The size used in a rendering must be stated separately from a claim about electron density.

Sources: DERIVED

## 3. Molecules connect atoms; crystals repeat a pattern

Water is a familiar molecule. A metal crystal is an extended arrangement of atoms rather than a collection of small separate molecules. At an interface, which is where two materials meet, both kinds of structure can be present. We need a model that describes each material and the interactions between them. Lines are omitted from the space-filling drawing so the occupied volume stays visible.

Sources: H13

## 4. Atoms push and pull on one another

Imagine compressing a metal or pulling its surface apart. Work changes how its atoms are arranged. The model assigns an energy to those arrangements and a force to each atom. The touching spheres show an ideal rhodium crystal. Their radius follows the crystal's nearest-neighbor spacing, so the rendering shows a filled solid. It is a structural illustration, with no claim that atoms are rigid billiard balls.

Sources: K21, DERIVED

## 5. Can a short molecule change a metal particle’s shape?

Ruan and colleagues used peptide variants and electron microscopy to study crystal-face recognition. Their model is named CHARMM-METAL in the paper and belongs to the metal-parameter lineage incorporated into IFF. A face is a flat exposed orientation of the crystal. We'll return to the result after introducing energy, water competition and surfaces. Crystal shape is an indirect readout of selective binding, so growth conditions remain part of the evidence.

Sources: R13

## 6. A simulation is a controlled model experiment

An observable is a quantity we can estimate from the calculation and compare with an experiment, such as density or surface energy. A simulation can make a buried interface easier to inspect, or compare candidate molecules before synthesis. Its answer depends on the chemistry included, the mathematical approximation and the configurations explored. Agreement must be assessed for the actual question and conditions.

Sources: H13, K21

## 7. Different methods keep different physical detail

Density functional theory, or DFT, is an electronic-structure method built around electron density. It can address changes in bonding and charge, with results that depend on the chosen approximation. Classical molecular mechanics replaces that electronic calculation with an energy function and parameters. Learned potentials use examples from reference calculations to approximate the energy landscape. More electronic detail usually increases cost, while a useful approximation must retain the physics the question needs.

Sources: HK64, H13, MACE

## 8. Compare the scale and the work actually timed

Wang and colleagues report 21 minutes for a DFT energy evaluation of 281-atom Trp-cage and 0.072 seconds for AI²BMD. Figure 2f compares energy-calculation timings; the accompanying prose calls this a simulation step. This timing benchmark does not report a trajectory duration. Kanhaiya's classical lattice protocol uses five conventional fcc cells along each axis. Four atoms per cell gives 500 atoms. It describes roughly 100 ps before stable behavior followed by 500 ps for averaging, using NPT at 298.15 K. A picosecond is one trillionth of a second. The classical paper does not provide an equivalent wall-clock timing here. Cross-paper differences in hardware, system, solvent and task prevent a universal speed ratio.

Sources: W24, K21, K21SI, DERIVED, W24C

## 9. Molecular mechanics assigns energy to atom positions

A configuration is a list of atomic positions, with a simulation cell when periodic boundaries are used. Molecular mechanics evaluates potential energy for that configuration. A force field supplies the functional forms and coefficients. In the common IFF-compatible form, bonded terms describe internal molecular geometry, while electrostatics and van der Waals terms describe nonbonded interactions. The complete package also needs units and rules for which atom pairs interact.

Sources: H13

## 10. Stretching a bond costs energy

The spring analogy describes the shape of the energy close to equilibrium. A common harmonic form is U = (k/2)(r-r_eq)^2, with k the stiffness and r_eq the preferred bond length. Force-field families sometimes absorb the factor of one half into k, so the coefficient convention matters. A fixed harmonic bond model has a limited range and does not describe bond breaking. The drawing uses touching spheres and a separate energy diagram.

Sources: H13, DERIVED

## 11. Bending an angle also costs energy

Take two bonds that meet at the same atom. The angle between them is another coordinate of the molecule. A simple harmonic bending term rises quadratically with displacement from the preferred angle. Its stiffness affects vibrations and mechanical response. This term is distinct from an interaction between two separate molecules. The pictured arrangement is an illustrative geometry rather than a fit to a specific compound.

Sources: H13, DERIVED

## 12. A torsion describes a twist along a bond

A dihedral angle compares the planes formed by two overlapping sets of three atoms. Rotating around the central bond can bring atoms closer together or change favorable electronic arrangements. Force fields represent the resulting energy variation with periodic terms. In a long molecule these preferences influence the shapes it can sample. Other terms, including nonbonded interactions, also contribute to the total cost of rotation.

Sources: H13, DERIVED

## 13. Atoms interact across a gap, too

Nonbonded interactions act between atoms that are not directly joined by the relevant covalent bonds. An effective repulsive term prevents unrealistic overlap, while an attractive term can help produce cohesion. Electrostatics accounts for charges and polarity. The force field specifies exclusions and scaling for atoms connected through short bond paths, so these terms are not blindly added for every possible pair in a molecule.

Sources: H13, R13

## 14. The Lennard-Jones curve has a wall and a well

Lennard-Jones, abbreviated LJ, is a simple effective pair potential. The exponents identify a functional form, not a full electronic calculation. Here the original plot evaluates Kanhaiya's rhodium coefficients. The isolated pair is a teaching device. A metal crystal contains many interacting neighbors, so this curve alone does not give the total binding or elastic behavior of a solid.

Sources: K21, DERIVED

## 15. Read the zero crossing, minimum and well depth

An angstrom, Å, is one ten-billionth of a meter. Energy is reported per mole of pairs, which scales a microscopic pair energy by Avogadro's number. Our equation is U=epsilon[(r0/r)^12-2(r0/r)^6]. Kanhaiya calls the minimum-length parameter sigma; we call it r0 to distinguish it from the zero-crossing sigma in U=4epsilon[(sigma/r)^12-(sigma/r)^6]. The curves are identical when sigma=r0/2^(1/6). At r0 the pair energy is -epsilon.

Sources: K21, LJ, DERIVED

## 16. Force is the negative slope of energy

The radial force is F_r=-dU/dr. For this minimum-length 12-6 form, F_r=(12epsilon/r)[(r0/r)^12-(r0/r)^6]. The sign convention takes increasing separation as positive. Energy below zero can still have a repulsive slope. The plot is the analytic derivative of the same published pair potential, and its units are kcal per mole per angstrom. It is not a measured force trace.

Sources: K21, DERIVED

## 17. Work the rhodium numbers

These rounded values come from direct analytic evaluation of the published 12-6 rhodium parameters. At 2.500 Å, the energy is negative while the force is positive because the separation is shorter than the minimum. At 2.757 Å the energy is -7.84 and the force vanishes. At 3.000 Å the force is attractive. The table's force unit is kcal/(mol Å), and energy is kcal/mol of pairs. Extra digits in the check file document arithmetic, not higher physical precision.

Sources: K21, DERIVED

## 18. Changing the metal changes the pair curve

Kanhaiya Table 1 gives Rh r0=2.757 Å and epsilon=7.84 kcal/mol; Ir 2.785 and 9.20; alpha-Ca 4.025 and 3.36; alpha-Sr 4.379 and 3.40. These are elemental fcc model parameters. They do not establish that a material remains chemically stable in every environment. For example, reactivity in water needs an appropriate model. The original plots compare the specified pair functions at their published values.

Sources: K21, DERIVED

## 19. A solid adds interactions with many neighbors

The pair sum runs over each distinct unordered atom pair. A solid's equilibrium spacing balances interactions with multiple neighbor shells. Cleaving a solid changes many terms and allows atoms to relax. Surface energy is reported in joules per square meter, whereas epsilon has energy units. Fitting a surface target therefore requires an actual surface calculation, a normalization and stated conditions. There is no universal unit conversion from epsilon to gamma.

Sources: K21, K21SI, DERIVED

## 20. A mixed pair needs an explicit combining rule

A combining rule generates a cross interaction from the two like-atom parameters. This example uses geometric means for both minimum lengths and well depths, following the selected CVFF family convention. Other families use different length rules. The arithmetic is an illustration of how a rule is consumed. It supplies no evidence that a Rh-Ca alloy is accurately represented. Alloy charge, phase stability and electronic effects need their own evidence.

Sources: K21, K21SI, DERIVED

## 21. Charges add electrical attraction or repulsion

The symbol e is the magnitude of the elementary charge. Using k=332.064 kcal Å/(mol e²), the point-charge calculation is U=k(+1)(-1)/3. These are illustrative charges in vacuum and are not the charges on rhodium atoms. Real ions also have size and other interactions. In water, solvent orientation, screening and polarization affect the result, so the vacuum value cannot be used as an ion-pair energy in solution.

Sources: CODATA, H13, DERIVED

## 22. A small cluster counts each pair once

The pairs are atom 1 with 2, atom 1 with 3, and atom 2 with 3. Summing each once gives three times -7.84. The sphere diameter equals the isolated-pair minimum in this deliberately simple illustration. This is not a fragment cut from the equilibrium fcc crystal. No relaxation, long-time stability or preference over other cluster shapes has been calculated. A larger system uses the same counting idea while boundary and cutoff rules also matter.

Sources: K21, DERIVED

## 23. Molecular mechanics makes repeated sampling practical

A single low-energy structure may miss the many arrangements present at a finite temperature. The lower cost of classical interactions makes repeated energy and force evaluation practical. This helps sample molecular conformations, water exchange and surface binding. The benefit depends on the model and workload. A fast trajectory can still sample too little time or use the wrong surface chemistry.

Sources: H13, K21

## 24. Parameters connect equations to physical measurements

Parameterization chooses coefficients so the model reflects the material of interest. Structural data constrain packing and bonding geometry. Surface and immersion measurements constrain interactions across material boundaries. Dipole moments and other electrical data help constrain charge assignments. These effects are coupled. Several parameters may affect the same observable, and a fitted coefficient is not necessarily a uniquely measured atom property.

Sources: H13, C04

## 25. Fitting and testing answer different questions

For the rhodium example, density or lattice size and surface energy are calibration targets. The elastic properties are predictions beyond those targets. This separation lets us ask whether a useful surface model also reproduces mechanical response. A reserved test loses independence if its outcome is used to tune a parameter, choose a model family or adjust a fitting weight. The published paper is not described here as a prospectively blinded campaign.

Sources: K21, AGENT

## 26. A parameter should have a defensible physical role

Physically interpretable means we can explain why a parameter is present and how it relates to the modeled chemistry. For example, a length parameter changes the distance scale while an energy parameter changes cohesion. Interpretation does not make the fit unique or guarantee transfer to a new compound. The rhodium mechanical limit will show why a sensible parameter set can still be restricted by its functional form.

Sources: H13, K21

## 27. IFF connects inorganic surfaces with molecules

IFF stands for Interface Force Field. The 2013 paper establishes a framework for combining inorganic and molecular components while retaining chemically interpretable parameters and thermodynamic comparisons. Its purpose includes the boundary where a biomolecule or polymer meets a solid. Coverage is compound-specific. A supported force-field family still needs suitable parameters, charge assignments and surface models for the proposed system.

Sources: H13

## 28. Compatibility is an equation-level requirement

IFF has been integrated with common molecular force-field families, including CHARMM, AMBER, CVFF, OPLS and PCFF in the supported contexts described by the papers. These families do not share every convention. A valid export must preserve the intended interactions, including the treatment of short bond paths and unlike atom types. Reading exported coefficients is useful, but a numerical energy and force comparison checks the consumed interpretation.

Sources: H13, K21, K21SI, AGENT

## 29. A silica surface changes its chemistry in water

A silanol is a silicon-oxygen-hydrogen group at the surface. Losing its proton leaves a negatively charged siloxide group. The particle size, solution and preparation influence the extent of this change. The silica papers show why a surface labeled only SiO2 is incomplete. We use their published chemical and adsorption evidence here. The later correction to the 2014 paper changes density-profile plots, which this deck does not reproduce.

Sources: P12, E14, E14C

## 30. Rhodium begins with a repeating fcc cell

A unit cell is a building block that can reproduce the crystal by translation. A conventional fcc cell contains four independent atomic sites after sharing corner and face sites with neighboring cells. The corrected source cell has cubic edge 3.8032 Å. Boundary spheres in a drawing can show copies of shared atoms, so their visible count is not the count of independent atoms. Crystal-contact spheres have radius a/(2sqrt(2)), consistent with touching nearest neighbors.

Sources: K21, K21C, DERIVED

## 31. Repeat the cell to build a supercell

Five cells in each of three directions gives 125 conventional cells. Multiplying by four atoms per fcc cell gives 500 atoms, the lattice-protocol size described in the paper's SI. A smaller drawing may be used to show the pattern clearly. Periodic boundaries mimic extended material through copies; surfaces and isolated molecules require appropriate extra space and boundary treatment. Convergence checks assess whether a larger box changes the observable.

Sources: K21SI, DERIVED

## 32. Expose a surface by cleaving the solid

Miller indices such as (111) label an orientation in a crystal. The cut shown here creates equivalent parallel faces. Atoms at those faces have fewer neighbors across the missing solid, and their positions can adjust. The pictured slab is idealized and constructed for explanation. It is not a reconstruction of an experimental surface or a newly simulated rhodium trajectory.

Sources: K21, K21SI

## 33. Two new faces require a factor of two

The angle brackets denote an average over sampled configurations. If two equivalent faces of area A are created, the total newly exposed area is 2A. Kanhaiya's metal method compares matched unified and cleaved boxes. The full free-energy expression includes entropy; the SI estimates a small correction for the metal conditions studied. This approximation needs to be reassessed for a different interface, temperature or molecular adsorption process.

Sources: K21, K21SI, DERIVED

## 34. Excellent agreement can be a calibration result

Kanhaiya Table 2 reports a five-cell length, 5a, rather than a single cell edge. The published 12-6 model gives the same rounded value as the reference. Table 3 reports Rh(111) surface energy 2.643 J/m² for both LJ families versus reference 2.64±0.02. These comparisons test reproduction of calibration data. The SI discusses experimental face mixtures and the approximation between surface free energy and the energy-difference method. Published values are reproduced here as facts and were not rerun.

Sources: K21, K21SI

## 35. Minimization finds a nearby low-energy arrangement

Energy minimization uses forces or gradients to reduce the potential energy. It is useful for removing unrealistic close contacts and relaxing a structure before dynamics. It does not assign a physical time to the movement down the landscape. A minimizer can stop in a local basin, so several starting configurations or broader sampling may be needed. The landscape is an original explanatory sketch.

Sources: MD, H13, DERIVED

## 36. Molecular dynamics advances motion in short steps

Newton's equation connects acceleration to force through atomic mass. A molecular-dynamics integrator repeatedly updates positions and velocities using that relationship. A femtosecond, fs, is one quadrillionth of a second. Temperature and pressure controls set the intended statistical conditions, and their settings affect sampling. A successful short run does not prove convergence. Any motion in our diagrams is illustrative and does not represent a new material trajectory.

Sources: K21, MD, DERIVED

## 37. A trajectory becomes evidence through an observable

A trajectory is a time-ordered series of atomic configurations. Turning it into a material result requires an estimator with a reference state and conditions. Neighboring time samples are correlated, so a large frame count does not automatically mean many independent observations. Block averages, repeated runs and convergence checks help assess sampling. Experimental uncertainty and model error are separate sources of disagreement.

Sources: H13, K21SI

## 38. Rhodium mechanics exposes the pair model’s limit

Moduli describe stiffness under different deformations. K is the bulk modulus for volume compression, E is Young's modulus for uniaxial stretching, and G is the shear modulus. This table uses the selected experimental reference d in Kanhaiya Table 5; other reference values are listed in the paper. The 12-6 bulk modulus is about 6.5% lower than 276 GPa, but its Young's and shear moduli differ much more. The Cauchy-type central-force restriction limits independent elastic behavior. The examples are published predictions beyond the lattice and surface calibration, not newly rerun measurements.

Sources: K21, K21SI

## 39. An alloy needs evidence beyond a mixing rule

Liu's SI states that alloy charges were obtained using pure-metal pair potentials and experimental formation energies, with extended-Born reasoning to interpret chemical trends. The AlNi base assignment is +0.39e for Al and -0.39e for Ni. These are model partial charges. They are not a unique experimental partition of electrons. A neutral elemental metal model cannot simply be copied into every alloy without examining polarity, phase and structure.

Sources: L18, L18SI

## 40. Defects and polarization change the model question

A defect is a departure from the ideal crystal, such as a missing atom. L18SI Table S2 varies how charge left by an AlNi vacancy is assigned among nearby atoms. Its raw molecular-mechanics energies depend on that hypothesis and are not measured formation free energies. A fixed neutral LJ model also lacks an explicit responding electron cloud. Geada's gold extension adds a charged core-shell response. Many-body models such as EAM can address other metal-specific behavior, with their own scope and interface limitations.

Sources: L18SI, G18, K21

## 41. Real systems test different parts of a model

We have enough background to return to real questions. These six published examples use related interface modeling ideas across different chemistry. Some establish a mechanism through matched trends, while others compare a numerical surface property. Their evidential strength differs. A success on one interface does not validate all supported compounds or every property of the same material.

Sources: R13, P12, E14, L16, M13, G18

## 42. Peptide chemistry steers platinum crystal shape

Ruan et al., Nano Letters 2013, pp. 842-844, Figures 2-3. The CHARMM-METAL model, an IFF metal-model predecessor, describes competition between water and peptides. Phenylalanine's ring can lie on (111) but has an unfavorable geometry on (100), reducing adsorption there. Strong binding to (111) alone did not correlate with tetrahedral yield; contrast between faces mattered. The TLT-to-TFT substitution and microscopy provided an experimental test of the proposed recognition principle. The calculations did not simulate the complete synthesis reaction.

Sources: R13

## 43. A silica-binding peptide must fit the surface

Patwardhan et al., JACS 2012, Figure 10 and Table 3, pp. 6251-6253. Replacing histidine at one position relieved conformational strain and allowed better contacts. Replacing a terminal histidine removed useful contacts and weakened binding. Adsorption assays and zeta-potential data supported the computed relative trends. A hydrogen bond is an attractive interaction involving a hydrogen-bearing group and a suitable electronegative site. Zeta potential measures an electrical property of the particle's moving liquid boundary, rather than a direct image of individual charges.

Sources: P12

## 44. Surface groups change how water wets silica

Emami et al., Chemistry of Materials 2014, section 4.1 and Figure 5, pp. 2653-2654. Heat of immersion is the energy released when a dry surface enters water; values here are its positive magnitude. The SPC, TIP3P and PCFF water models gave 167, 160 and 157 mJ/m² respectively, so the selected comparison explicitly names TIP3P. Section 4.2 and Figure 6 also compare wetting as surface chemistry changes. The 2016 correction revises density-profile Figures 8-9; it leaves the immersion and contact-angle data used here unchanged. These comparisons support a specified surface/water model and are not a universal held-out accuracy score. The paper states that hydration energies of Q3 surfaces were among the quantities used to refine nonbonded parameters, so this numerical agreement is a calibration check.

Sources: E14, E14C

## 45. Bone mineral presents a pH-dependent surface

Lin and Heinz, JPCC 2016, Table 7 and discussion, pp. 4986-4987. Hydroxyapatite contains calcium, phosphate and hydroxide. Changing pH changes surface protonation and calcium content in the constructed models. The work compares immersion energies and hydration-stabilized crystal shapes with experimental data. Dry-sample calorimetry reports values around 600-700 mJ/m², while broader literature values depend on preparation. The paper explains how facet weighting and hydration history affect comparisons. This evidence concerns mineral surfaces; it establishes no drug efficacy or clinical prediction.

Sources: L16

## 46. Grinding aids reduce attraction between cement grains

Mishra, Flatt and Heinz, JPCC 2013, Figure 6 and section 6, pp. 10426-10427. The model compares reconstructed dry, hydroxylated and organically covered surfaces. MDIPA and TIPA show greater reductions in attraction than the weaker aids, in the same qualitative order as grinding observations. The comparison is a trend across additives, rather than a direct measurement of each atomistic agglomeration energy. Direct C3S cleavage data are limited and some calibration checks use related phases. Fracture, roughness, coverage and processing conditions also influence milling performance.

Sources: M13

## 47. Gold’s electrons respond to nearby charges

Geada et al., Nature Communications 2018, Table 2 p. 6 and Figure 5 p. 7. A harmonically coupled charged core-shell pair on each metal atom models polarization. The water-monolayer comparison above is for the polarizable (111) model, with experimental reference differences and surface mismatch retained. The nonpolarizable model already gives similar liquid-water energetics; induced charges matter differently for ion contact. The interfacial-tension experimental entry is an upper bound, so it must not be treated as an exact measurement. The extension does not give a general model of chemical reactions or arbitrary electrode conditions.

Sources: G18

## 48. Choose the observable before judging the result

Across the examples, the strongest conclusion follows the actual measured quantity. A morphology trend, an adsorption assay and a calorimetric energy are different tests. Keep conditions attached to the result. A model that explains one trend may still have important numerical errors elsewhere, as the rhodium mechanical table shows. New chemistry or an altered surface calls for renewed evidence.

Sources: R13, P12, E14, L16, M13, G18

## 49. The IFF Agent carries evidence through eight steps

The approved public workflow has eight steps: Intake, References, Model, Contract, Run and fit, Validate, Export readback, and Review and disposition. The workflow aims to carry decisions and evidence through a calculation without losing their context. Implementing this workflow does not establish that any new material package has passed fitting, independent validation or scientific adoption.

Sources: AGENT

## 50. Define the question before running the fit

A fit/test contract is a plan for assessing a bounded model, including which measurements may tune it and which are reserved. The model assignment must include the chosen family conventions. Changing the chemistry, references or intended use can change which model and tests are appropriate. Keeping these choices inspectable lets a reviewer reconstruct why a coefficient set was considered suitable.

Sources: AGENT

## 51. Run, test, read back, then review

An export can be syntactically valid while changing units, mixing or length conventions. Readback compares the consumed model against the intended one, including energy and forces where relevant. Validation also needs numerical convergence and suitable scientific comparisons. A final review can accept a bounded use, narrow it or withhold a material claim. Execution receipts prove that operations happened; scientific evidence determines what their results establish.

Sources: AGENT

## 52. A repeatable answer can still be inaccurate

If every input, coefficient and numerical setting is preserved, rerunning a calculation should produce consistent behavior within its statistical and numerical variability. That is useful evidence about execution. A physical model can reproduce the same wrong answer. Rhodium's elastic mismatch illustrates this distinction even when its density and surface targets are reproduced well.

Sources: K21, AGENT

## 53. Use DFT when electron rearrangement matters

DFT evaluates electronic energy using an electron-density framework. It is useful when a fixed-chemistry model cannot represent the event being studied, such as a chemical reaction or changing electronic distribution. Results depend on the functional, electronic setup and sampled structures. DFT is an approximation with property-specific errors. A more detailed method still needs evidence for the target observable.

Sources: HK64, K21

## 54. Use classical IFF for supported interface sampling

Classical IFF is useful when its effective interactions and surface models are appropriate and the need is to explore molecular configurations or interface behavior. Fixed-topology bonded models do not automatically form and break bonds. A fixed neutral metal model also lacks explicit changing charge. The published example papers support defined uses. They do not grant blanket transfer to untested compounds, defects or reaction pathways.

Sources: H13, K21, G18

## 55. Use a learned potential within its supported data domain

A learned potential estimates an energy function from data. MACE is one primary example of this approach; AI²BMD applies a learned quantum-based strategy to biomolecular simulation. Architecture alone does not determine transfer. A model trained around one set of structures can make unreliable predictions when bonding, composition or configuration changes beyond its coverage. Its reference method also contributes uncertainty.

Sources: MACE, W24

## 56. Compare methods against the same physical question

This comparison describes tendencies rather than a universal ranking. A fair performance claim specifies the same observable, system, target error and workload, with hardware and sampling costs. Hybrid approaches can combine methods when needed. Learned and classical models both require suitable validation; quantum calculations also need convergence and a defensible reference approximation. The method name alone cannot settle accuracy.

Sources: HK64, H13, MACE, W24

## 57. What these figures establish

The new curves can be rebuilt from the public source scripts and parameter table. Reproducing their arithmetic establishes correct evaluation of the equation. It does not independently validate the equation as a model of rhodium. The surface, mechanics and application examples refer to published studies. No new fit, material trajectory, experiment or adopted parameter package is presented in this deck.

Sources: DERIVED, K21

## 58. Ask what would change your confidence

For a peptide, check which face and solution were used. For bone mineral, check the protonation and hydration history. For a force-field export, check the consumed equation and units. For rhodium mechanics, keep the deformation mode visible. These checks make the claim reviewable and help decide when a more detailed or different model is required.

Sources: H13, K21, P12, L16, AGENT

## 59. IFF makes an interface a testable atomic model

The Interface Force Field provides a framework for supported inorganic and molecular interactions in one compatible description. Its papers show how chemical assignment, surface models and property comparisons can make interface simulations useful. The examples span several types of evidence. The size of a claimed success should remain tied to the actual tested system and observable.

Sources: H13

## 60. Some questions require a different model

An ordinary fixed-topology IFF model has a stated set of atoms, terms and charges. Reactive extensions and polarizable models expand particular capabilities, with separate parameterization and validation. The gold extension is one such bounded example. A model should be selected by the physical question and tested within the proposed conditions. An unfamiliar system can fall outside several available models at once.

Sources: H13, K21, G18, L18SI

## 61. Read the primary evidence

The citation manifest lists source titles, DOI links, precise use and reuse status. Presenter notes keep the context of each comparison. Original plots and drawings avoid redistributing paper figures. The source rebuild instructions identify how the deck and analytic curves were made. The appendix defines equation conventions and retains the rhodium evidence table and experimental qualifications.

Sources: H13, K21, R13, P12, E14, L16, M13, G18

## 62. Questions

I would start with the observable we need to trust. The method, parameter choices and checks follow from that question. A useful next experiment or calculation distinguishes plausible explanations and can change the decision. The appendix is available for equations, conventions and the numerical evidence behind the worked examples.

Sources: DERIVED

## B1. Equations and units

Bond, angle and torsion functions depend on the chosen family, as do exclusions and scale factors for short bond paths. The written radial force is positive for increasing separation. The constants and coefficient meanings must be consistent with the unit system. The analytic plots sum explicitly defined pair interactions and do not replace a complete periodic simulation with its cutoff and electrostatic choices.

Sources: H13, K21, CODATA, DERIVED

## B2. The paper’s sigma is a minimum-length parameter

The symbol sigma alone is ambiguous across sources. Kanhaiya Equation 1 uses it at the energy minimum, while the common lj/cut form uses it at the zero crossing. Epsilon remains the well depth for this algebraic conversion. Entering 2.757 Å as the zero-crossing sigma would define a different pair potential. Preserve the equation with the number and verify the consumed energy curve.

Sources: K21, LJ, DERIVED

## B3. The 9-6 and 12-6 wells are different functions

The different repulsive exponents change the shape and curvature of the well. Their fitted coefficients are not interchangeable. The 12-6 conversion between zero crossing and minimum length is an exact rewriting of one function. Moving from a 12-6 function to a 9-6 function changes the model. Kanhaiya reports separate rhodium coefficients for both forms in Table 1. Host-family combination rules must also be retained.

Sources: H13, K21, DERIVED

## B4. Parameters and worked-number checks

All four elemental-metal rows come from Kanhaiya Table 1 and are the 12-6 family. The zero-crossing sigma is derived from the minimum-length r0. The public science-checks file contains unrounded values and algebraic assertions at the minimum and for the derivative. The Coulomb and cluster examples use the deliberately restricted geometries stated on their slides. These computations verify arithmetic and convention handling, rather than new material accuracy.

Sources: K21, CODATA, DERIVED

## B5. Rhodium evidence and uncertainty

Kanhaiya Tables 2, 3 and 5 provide these values. The lattice and surface rows were calibration targets. The elastic rows are predictions beyond those targets. Selected E and G references are listed in the main mechanical slide; Poisson ratio appears in this appendix, and other reference values remain in the paper. The Rh-water table gives an experimental upper bound, so it is excluded as a direct accuracy benchmark. L18SI's AlNi vacancy comparisons separately report raw MM energies of 5.49, 4.57 and 2.59 eV for first/second-shell charge partitions 100/0, 67/33 and 0/100. Those hypotheses are not measured formation free energies.

Sources: K21, K21SI, L18SI

## B6. References and visual provenance

The full bibliography is in citation-license-manifest.json and this story source. Public facts were checked against the cited papers. No third-party scientific figure is reproduced. Original structures and analytic plots state their assumptions and do not claim newly simulated material results. The source files preserve the values, equation conventions and method needed to reconstruct the authoring assets.

Sources: H13, K21, K21C, DERIVED

# References

K21. Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials

https://doi.org/10.1038/s41524-020-00478-1

K21C. Kanhaiya et al. (2021), Author Correction

https://doi.org/10.1038/s41524-021-00576-8

L18. Liu et al. (2018), Understanding Chemical Bonding in Alloys and the Representation in Atomistic Simulations

https://doi.org/10.1021/acs.jpcc.8b01891

L18SI. Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19

https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197

LJ. LAMMPS documentation: lj/cut interaction convention

https://docs.lammps.org/pair_lj.html

MD. LAMMPS documentation: fix nve and minimize

https://docs.lammps.org/fix_nve.html

MACE. Batatia et al. (2022), MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields

https://arxiv.org/abs/2206.07697

AGENT. IFF Agent workflow documentation (2026)



DERIVED. Original derivation / explicitly illustrative visual



H13. Heinz, Lin, Mishra and Emami (2013). Thermodynamically Consistent Force Fields for the Assembly of Inorganic, Organic, and Biological Nanostructures: The INTERFACE Force Field. Langmuir 29, 1754-1765.

https://doi.org/10.1021/la3038846

C04. Heinz and Suter (2004). Atomic Charges for Classical Simulations of Polar Systems. J. Phys. Chem. B 108, 18341-18352.

https://doi.org/10.1021/jp048142t

R13. Ruan et al. (2013). Tailoring Molecular Specificity Toward a Crystal Facet: a Lesson From Biorecognition Toward Pt{111}. Nano Letters 13, 840-846.

https://doi.org/10.1021/nl400022g

P12. Patwardhan et al. (2012). Chemistry of Aqueous Silica Nanoparticle Surfaces and the Mechanism of Selective Peptide Adsorption. JACS 134, 6244-6256.

https://doi.org/10.1021/ja211307u

E14. Emami et al. (2014). Force Field and a Surface Model Database for Silica to Simulate Interfacial Properties in Atomic Resolution. Chemistry of Materials 26, 2647-2658.

https://doi.org/10.1021/cm500365c

E14C. Emami et al. (2016). Correction to Force Field and a Surface Model Database for Silica to Simulate Interfacial Properties in Atomic Resolution. Chemistry of Materials 28, 406-407.

https://doi.org/10.1021/acs.chemmater.5b04760

L16. Lin and Heinz (2016). Accurate Force Field Parameters and pH Resolved Surface Models for Hydroxyapatite to Understand Structure, Mechanics, Hydration, and Biological Interfaces. J. Phys. Chem. C 120, 4975-4992.

https://doi.org/10.1021/acs.jpcc.5b12504

M13. Mishra, Flatt and Heinz (2013). Force Field for Tricalcium Silicate and Insight into Nanoscale Properties: Cleavage, Initial Hydration, and Adsorption of Organic Molecules. J. Phys. Chem. C 117, 10417-10432.

https://doi.org/10.1021/jp312815g

G18. Geada et al. (2018). Insight into induced charges at metal surfaces and biointerfaces using a polarizable Lennard-Jones potential. Nature Communications 9, 716.

https://doi.org/10.1038/s41467-018-03137-8

W24. Wang et al. (2024). Ab initio characterization of protein molecular dynamics with AI2BMD. Nature.

https://doi.org/10.1038/s41586-024-08127-z

W24C. Wang et al. (2025). Author Correction to Ab initio characterization of protein molecular dynamics with AI2BMD. Nature.

https://doi.org/10.1038/s41586-024-08556-w

HK64. Hohenberg and Kohn (1964). Inhomogeneous Electron Gas. Physical Review 136, B864-B871.

https://doi.org/10.1103/PhysRev.136.B864

K21SI. Kanhaiya et al. (2021), original Supplementary Information

https://static-content.springer.com/esm/art%3A10.1038%2Fs41524-020-00478-1/MediaObjects/41524_2020_478_MOESM1_ESM.pdf

CODATA. NIST, 2022 CODATA recommended values of fundamental physical constants

https://physics.nist.gov/cuu/Constants/Table/allascii.txt
