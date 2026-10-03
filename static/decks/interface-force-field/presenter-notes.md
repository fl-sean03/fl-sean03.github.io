# Presenter notes and citations

## 01. Interface Force Field

This deck explains Interface Force Field (IFF) as a classical molecular-mechanics framework. The running example is face-centered cubic rhodium, with source-grounded ideal structures and numerical results from Kanhaiya et al. (2021). Camera motion and analytical two-atom illustrations explain concepts; they are not recorded material trajectories. Published predictions are replotted and are not newly rerun simulations. The aim is to understand how an atomic model becomes a claim that can be tested against experiment, including where the claim should be restricted. Pure-metal, alloy and agent-workflow examples have separate evidence boundaries.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)

## 02. Begin with the decision

Surface energy matters when evaluating exposed crystal faces, cleavage and interface formation. This is a narrow pedagogical material question, not a prediction of a complete product or catalyst. The paper parameterizes metal models using lattice and surface evidence at standard conditions. A surface energy should not be confused with adsorption free energy, liquid interface tension, reaction barrier or corrosion rate. Changing the decision usually changes the required estimator, conditions and validation evidence. We begin with pure fcc Rh to avoid introducing unsupported alloy or reaction generality.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 03. Keep every link in the chain visible

Coordinates and a cell specify a configuration. A Hamiltonian and parameter package specify how the model assigns energy to that configuration. Forces follow from derivatives. A numerical operation then explores configurations or time evolution. An observable is an estimator applied to the resulting configurations. Only comparison under a suitable evidence contract supports a qualified material claim. Each transformation requires enough provenance to reproduce it. The IFF Agent is meant to preserve that evidence chain rather than collapse a successful file export or calculation into scientific acceptance.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- IFF Agent workflow documentation (2026)

## 04. Start with a real periodic crystal

The corrected public supplementary archive supplies rh_unit_cell_Fm3m.car. Its cubic cell has a=b=c=3.8032 Å and an Rh site at the origin under Fm-3m symmetry. This source is expanded into the four conventional fcc sites: (0,0,0), (0,1/2,1/2), (1/2,0,1/2), and (1/2,1/2,0). The illustration includes periodic equivalents on the cell boundary, so visible sphere count is not a cell atom count. The geometry is an ideal source-grounded construction, not a relaxed measured snapshot. The conventional-cell length agrees with the Rh five-cell reference in Table 2: 19.016 Å / 5.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)

## 05. A supercell changes scale, not chemistry

The visual supercell is built by repeating the source-derived conventional cell three times in each direction. It contains 108 atoms because 4 × 3³ = 108. It is smaller than the 500-atom, 5 × 5 × 5 fcc supercells used in the paper to calculate lattice parameters. Replication changes the finite model size without changing the element or ideal phase. Atom count alone does not establish convergence: long-wavelength modes, defects, correlations, cutoffs and periodic image effects can all change the required size. This image is a reproducible structural illustration, not a claim about simulation accuracy.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)

## 06. A surface introduces a physical boundary

The display slab is constructed with ASE fcc111 from the corrected Rh lattice constant. It has 144 atoms, six layers and 7 Å vacuum on either side, and is not the research slab used to produce the published results. Bulk periodicity and surface boundary conditions answer different physical questions. In an ionic material, termination, stoichiometry and charge neutrality can make a surface construction substantially more consequential; the neutral elemental-metal example avoids those issues but does not make them optional elsewhere. The source archive also supplies oriented Rh surface cells, which we retain for geometry provenance. Playback shows only camera and construction-stage changes.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)

## 07. Coordinates do not define the model

A coordinate file does not determine atomic charges, which interaction terms apply or the coefficients in those terms. In the published pure-metal example, Rh is modeled by charge-neutral atoms with Lennard–Jones interactions. An alloy or mineral can require physically justified charge assignments and different conventions. Combining packages also requires compatible functional forms, cross interactions, units and exclusion rules. A renderer can show a plausible crystal while the actual Hamiltonian is wrong, so structure and parameter provenance must be checked separately. The current IFF Agent workflow explicitly maintains these distinctions and separates model-family branches.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- IFF Agent workflow documentation (2026)

## 08. IFF is classical molecular mechanics

IFF belongs within classical molecular mechanics, so IFF versus molecular mechanics is a category error. Useful comparisons are between specific models for a defined chemistry, state and observable. The cited metal work uses simple pair potentials, while other classical models such as EAM include many-body metallic effects and reactive families serve different purposes. Compatibility with an organic or biomolecular host force field does not guarantee every mixed interface is accurate; the host parameters and cross-interaction rules still affect the result. The presentation avoids the paper’s broad speed or accuracy slogans and instead uses observable-specific numerical evidence.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)

## 09. Sum only the applicable interactions

A generic classical Hamiltonian may contain bonded, electrostatic and nonbonded terms, with additional cross terms or many-body terms depending on the family. This is a menu rather than a prescription that all IFF systems use all listed terms. The pure Rh example in Kanhaiya et al. uses neutral atoms and the applicable Lennard–Jones form. Electrostatics becomes chemically important in the alloy example later in the deck. A model can hold topology or electronic response fixed, which limits phenomena such as bond breaking, polarization or changing oxidation state unless a suitable extension is explicitly included and validated.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)
- Original derivation / explicitly illustrative visual

## 10. Two parameters have physical meaning

Table 1 gives separate 12–6 and 9–6 Rh parameters. In the paper’s equations, the symbol sigma denotes the equilibrium nonbond distance, which this deck calls Rmin to avoid confusing it with the conventional LAMMPS lj/cut sigma. Epsilon is the energy well depth. Lattice and surface properties are coupled functions of both parameters, even though their dominant interpretations are length and cohesion. The 9–6 set is not obtained by copying the 12–6 values into a different formula, and it is not a demonstrated later revision of the 12–6 model. These values are reproduced for explanation, not adopted as a newly reviewed package.

Readable equations and values:
Rh 12-6: Rmin = 2.757 angstrom; epsilon = 7.84 kcal/mol. Rh 9-6: Rmin = 2.807 angstrom; epsilon = 6.38 kcal/mol.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 11. Check the engine’s parameter convention

A convention mismatch changes the potential even if a coefficient file appears syntactically valid. The paper’s 12–6 potential has its minimum at Rmin. LAMMPS lj/cut defines sigma at the zero crossing, with the minimum at 2^(1/6) sigma. Converting Rh therefore gives sigma approximately 2.4562 Å. The 9–6 expression in the paper has its own coefficient and mixing conventions and must not be converted using this 12–6 rule. Unit systems, cutoff handling, long-range corrections and mixing rules also matter. Export readback should compare energies, forces and affected observables from the exact consumed files.

Readable equations and values:
Paper 12-6: U = epsilon * ((Rmin/r)^12 - 2*(Rmin/r)^6).
LAMMPS lj/cut: U = 4*epsilon * ((sigma/r)^12 - (sigma/r)^6).
sigma = Rmin / 2^(1/6) = 2.4562077659 angstrom for Rh; epsilon unchanged.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [LAMMPS documentation: lj/cut interaction convention](https://docs.lammps.org/pair_lj.html)

## 12. Forces are the slope of energy

For a two-atom separation r, the radial force is minus dU/dr. Under the Rmin convention the illustrative pair force is 12ε/Rmin[(Rmin/r)^13 − (Rmin/r)^7]. Positive radial force on the atom at positive r points outward; negative force points inward. A solid contains many interacting neighbors, so its equilibrium lattice spacing is determined by the total energy, not by a single pair minimum alone. The plotted curve is analytical in reduced units and is not an experimental result, a fitted force curve or an IFF trajectory. A finite-difference check of the derivative is included in validation.

Readable equations and values:
Force on atom i = minus the gradient of total potential energy with respect to its position.
Radial pair force = (12*epsilon/Rmin) * ((Rmin/r)^13 - (Rmin/r)^7). Positive points outward, negative inward.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- Original derivation / explicitly illustrative visual

## 13. Minimization searches a local basin

Energy minimization changes coordinates, and sometimes cell degrees of freedom, to seek a local energy minimum. Convergence criteria can include energy changes and force thresholds. The result depends on the initial basin, constraints and algorithm; it need not be the global minimum. A converged minimizer can still be solving an inappropriate physical model or a wrongly terminated slab. Temperature-dependent observables generally require more than a static minimum. The schematic basin on this slide is an explanatory drawing with no numerical material trajectory behind it.

- [LAMMPS documentation: fix nve and minimize](https://docs.lammps.org/fix_nve.html)
- Original derivation / explicitly illustrative visual

## 14. MD follows a time evolution

Molecular dynamics numerically integrates equations of motion. A common classical integrator is velocity Verlet. NVE, NVT and NPT ensembles address different constraints; thermostats and barostats affect how a target temperature and pressure are maintained. The FCC-metal paper used 1 fs steps and property-specific ensembles, described in its methods and SI. The embedded movie is prescribed analytical two-atom motion designed to show the force sign and different simulation operations. It does not integrate a Rh material trajectory, report a physical oscillation period or support a thermal prediction. Arrow direction follows the force sign; arrow length is clipped for display and is not a quantitative vector scale. A static poster remains visible if a presentation viewer cannot play the MP4.

Readable equations and values:
Mass of atom i times its second time derivative of position equals force on atom i: mi * d^2(ri)/dt^2 = Fi.

- [LAMMPS documentation: fix nve and minimize](https://docs.lammps.org/fix_nve.html)
- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 15. An observable needs a defined estimator

These formulas illustrate distinct measurement contracts. Density depends on composition and volume; a distribution such as g(r) requires normalization; the isothermal bulk modulus requires an appropriate pressure-volume derivative; a diffusion estimate requires a diffusive long-time regime and correct unwrapping. The MSD expression here assumes three-dimensional isotropic diffusion and must be adjusted for other settings. Static elastic constants, finite-temperature isothermal moduli and measured acoustic adiabatic moduli are not automatically interchangeable. No transport or g(r) result is generated for this deck. Report units, state, estimator, sampling and uncertainty with every actual number.

Readable equations and values:
Density = total mass / volume.
Isothermal bulk modulus K = -V * (partial P / partial V) at fixed temperature.
Three-dimensional isotropic diffusion D = long-time mean squared displacement / (6*t), in a diffusive regime.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- Original derivation / explicitly illustrative visual

## 16. Cleave, then normalize the energy

The paper compares unified and separated metal slabs with matched total atom counts and box dimensions using NVT simulations at 298.15 K. The energy difference is divided by the area of two newly created surfaces. The SI estimates the omitted entropy contribution to be small for these elemental-metal examples, within the stated experimental uncertainty. That approximation cannot be applied to every interface, adsorbate or temperature without justification. The display slab is an explanatory reconstruction rather than the actual research slab. Other geometries need their actual number of interfaces and area normalization, not a memorized universal factor of two.

Readable equations and values:
Surface energy gamma approximately equals (cleaved energy - unified energy) / (2*surface area), for two equivalent new surfaces under the stated assumptions.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 17. Match the experimental state

A careful comparison reconciles experimental specimen, method, state and uncertainty with the model and estimator. The metal SI discusses the difference between polycrystalline experimental surface references and an ideal (111) face, and the small energy-versus-free-energy approximation. Table 5 includes multiple experimental mechanical references, so the deck identifies the selected ones instead of disguising them as a single definitive average. In the current IFF Agent workflow, primary-reference adoption precedes fitting and includes unresolved derivation rules or state definitions. An unexplained secondary number or a published model coefficient is not itself a primary experimental reference.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- IFF Agent workflow documentation (2026)

## 18. Published fit: Rh matches its targets

The paper assigns parameters from experimental density/lattice and surface-energy evidence. The Rh agreement shown here is therefore calibration agreement, not an independent validation score. The chart also shows Ca(alpha) and Sr(alpha) from Table 3 to make the published surface fits inspectable; all references and uncertainties are exactly transcribed. Table 2 contains five-cell lengths, so those lengths should not be misreported as single-cell lattice constants. The paper’s conditions are 298 K and atmospheric pressure for lattice calculations, with surface methods explained in the SI. These are published calculations; the deck does not claim a new rerun or fit.

Readable equations and values:
Rh five-cell lattice reference 19.016 angstrom; 12-6 result 19.016; 9-6 result 19.014.
Rh (111) surface reference 2.64 +/- 0.02 J/m^2; both model results 2.643 J/m^2. These are calibration comparisons.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 19. Independent predictions reveal the limits

Kanhaiya et al. report Rh bulk modulus predictions of 258 GPa and 175 GPa for the two LJ families. We use the 276 GPa experimental entry marked reference d in Table 5; the same table also lists 270, 271 and 269 GPa from other references. Percent deviations on this slide are calculated against the selected 276 GPa reference, not copied from a universal benchmark. These mechanical properties were not the density/surface calibration targets. The paper explains limits of central-force pair models, including the elastic relation C12/C44=1 for the pair framework and material-dependent performance. Do not describe this as a formal blinded campaign or universal IFF validation. Kanhaiya et al. SI S7-S8 reports approximately ±3% reproducibility of calculated elastic moduli and agreement of small-strain Discover and LAMMPS E/K protocols within 0% to ±3% (strain 0.001-0.01). This is computational protocol repeatability, not accuracy against experiment, a statistical confidence interval or the error of a reserved-property prediction. The Rh deviations from the selected 276 GPa experimental entry remain -6.5% and -36.6%.

Readable equations and values:
Rh bulk modulus: selected experiment 276 GPa; 12-6 model 258 GPa (-6.5%); 9-6 model 175 GPa (-36.6%).

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 20. Alloys can add chemical polarity

The original supporting information explains charge assignments using pure-metal pair potentials and experimentally measured alloy formation evidence. Table S2 uses ±0.39e base charges for AlNi. The SI’s extended-Born discussion also reports a feasible Al charge range of approximately +0.39e to +0.5e under its assumptions, so a single charge value must not be presented as a uniquely measured electron population. The topology diagram is schematic, not a source coordinate file or a fitted lattice reconstruction. The original SI supports this binary-alloy example. No numerical main-paper defect comparison, universal alloy predictor or high-entropy-alloy performance is inferred.

- [Liu et al. (2018), Understanding Chemical Bonding in Alloys and the Representation in Atomistic Simulations](https://doi.org/10.1021/acs.jpcc.8b01891)
- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)

## 21. A defect changes its local environment

The three plotted values are from Table S2 for a Ni vacancy. They correspond to redistribution into the first neighbor shell (100/0), into first and second shells (67/33), and into the second shell (0/100). The table describes the first option as most likely and lists the others as alternative charge hypotheses. Its heading explicitly calls the numbers raw defect formation energy in MM. A final thermodynamic defect quantity needs appropriate reservoirs, charge-state terms and conditions; this chart is not a fresh validation or a final vacancy-formation-energy benchmark. It shows why a chemically justified local assignment is consequential. The plot is newly drawn from table facts and reproduces no source figure.

Readable equations and values:
AlNi Ni-vacancy raw defect energies in eV: first/second-shell redistribution 100/0 -> 5.49; 67/33 -> 4.57; 0/100 -> 2.59.

- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)

## 22. Calibration and validation take different paths

The implemented crystalline/ionic workflow separates primary reference selection, branch-specific fitting and independent evidence. Its fitting sequence adjusts the minimum-distance parameter to an adopted lattice reference and a common well-depth scale to adopted surface evidence, revisiting their coupling. Bulk modulus is reserved: it must not influence fit objectives, weights, parameter bounds, family selection or tuning. A failed reserved-property comparison restricts the claim. The FCC-metal literature example is separate from this implemented workflow; its non-fitted mechanical predictions were not rerun here.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- IFF Agent workflow documentation (2026)

## 23. A revised model needs fresh evidence

Changing model parameters, chemistry or functional form creates a new candidate. Test data that inform that change become development evidence; a fresh independent claim requires fresh evidence. The published 12-6 and 9-6 models are alternatives, not a temporal revision. The evidence movie reveals published comparisons before illustrating a possible new evidence contract. The implemented workflow reserves bulk modulus from fitting and family selection. No completed new revision or independent validation is claimed.

- IFF Agent workflow documentation (2026)
- Original derivation / explicitly illustrative visual

## 24. The IFF Agent carries the evidence chain

The IFF Agent implementation connects intake, primary references, model assignment, a bounded fit/test contract, calculation and fitting, independent checks, exact export readback, and scientific review. It keeps CHARMM/AMBER, CVFF/OPLS, PCFF and PCFF-HQ as distinct model-family branches, preserving the potential of each family, coefficients, radius, mixing and export conventions. Runnable software and numerical execution do not establish correct chemical assignment or acceptance of a new scientific package.

- IFF Agent workflow documentation (2026)

## 25. Scientific decisions define the scope

The implemented workflow records reference selection, consequential charge/model choices, bounded fit/test rules and scientific adoption of an exact reviewed export. Family-specific conventions and neutrality remain explicit. Changes to references, chemistry or scientific scope require the relevant decision to be revisited. This explains the workflow design and implementation; it does not establish that a new material package has completed fitting, independent validation or adoption.

- IFF Agent workflow documentation (2026)

## 26. Inputs become a reproducible dossier

An illustrative input brief names composition, phase, interface, thermodynamic state, intended observable, primary references and structural origin. The expected dossier contains family-specific coefficients and conventions, source-grounded geometry, runnable inputs, calibration lineage, independent predictions, uncertainty, export readback and supported scope. It describes the implemented input/output contract and does not present a completed new scientific package.

- IFF Agent workflow documentation (2026)

## 27. Acceptance is more than execution

Numerical execution and engineering checks do not establish scientific acceptance. A package needs adopted references and model choices, calibration evidence, independent validation, convergence, exact export readback and scientific review. The resulting claim may be qualified, limited or withheld. This describes an evidence standard and establishes no new accepted package.

- IFF Agent workflow documentation (2026)

## 28. Choose the method for the decision

Classical potentials, DFT and MLIPs are useful for different questions. IFF is a classical framework with specific supported chemistry and conventions. DFT provides electronic-structure calculations but depends on the chosen functional and numerical setup; it is not an infallible experiment. An MLIP learns from data and can provide a rich potential representation, but coverage, extrapolation and calibration to the intended observable remain consequential. MACE is cited as a primary learned-potential example, not a claim that a particular released model is suitable for Rh or a general alloy. No unmatched atom-count, hardware, time-to-solution or accuracy benchmark is presented.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Batatia et al. (2022), MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields](https://arxiv.org/abs/2206.07697)

## 29. Connect methods to an experimental loop

A full loop should be authored around the actual material question rather than require every available method. Electronic calculations may inform a charge or chemical hypothesis; classical models or MLIPs may enable larger sampling; experiments define and test a physically meaningful target. Each method enters only if it can change a decision and can be checked against a credible baseline. Data used to improve a model are development evidence, while a fresh test supports the next independent claim.

- IFF Agent workflow documentation (2026)
- Original derivation / explicitly illustrative visual

## 30. Make the first question narrow and testable

A useful material brief identifies composition, phase, interface, the decision to be changed, an observable, primary experimental evidence and a defined state. After fitting and independent scientific qualification, a dossier should identify the exact model, reproducible predictions, uncertainty, failures and restrictions. This is an evidence standard, with educational literature examples in this presentation; it is not a promise of a currently accepted new parameterization.

- IFF Agent workflow documentation (2026)
- Original derivation / explicitly illustrative visual

## 31. Appendix · equations and conventions

The two Lennard–Jones expressions follow Kanhaiya et al. equations 1 and 2 after renaming their equilibrium-distance sigma to Rmin. Both have minimum −epsilon at Rmin, but their curvature and repulsive shape differ. The Coulomb expression is a generic pair expression; periodic electrostatics requires the actual summation and boundary convention, and a dielectric factor must not be inserted without defining it. Bonded terms, cross terms, mixing rules, exclusions, units and cutoffs depend on the chosen force-field family. These equations alone do not define a runnable or qualified parameter package.

Readable equations and values:
12-6: U = epsilon * ((Rmin/r)^12 - 2*(Rmin/r)^6).
9-6: U = epsilon * (2*(Rmin/r)^9 - 3*(Rmin/r)^6).
Electrostatic pair energy Uij = qi*qj / (4*pi*epsilon0*epsilon_r*rij); actual long-range convention must be defined.
Force Fi = -gradient_i(U); mass mi * acceleration_i = Fi.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [LAMMPS documentation: lj/cut interaction convention](https://docs.lammps.org/pair_lj.html)
- Original derivation / explicitly illustrative visual

## 32. Appendix · the published data remain visible

This appendix reproduces the selected Ca, Rh and Sr table entries in a native editable table and bar chart. Lattice values are lengths for five conventional unit cells (5a), not single-cell constants. Surface-energy references and uncertainties come from Table 3. Bulk moduli use the explicitly selected Table 5 experimental entries: Ca 20 GPa (reference b), Rh 276 GPa (reference d), Sr 12.0 GPa (references c,d). Additional experimental entries are retained in the article; the deck does not average or discard them. Table 5 predictions use the authors’ mechanical procedure, so protocol and state equivalence need scrutiny before a new material claim. No new model tuning or simulation occurred. Kanhaiya et al. SI S7-S8 reports approximately ±3% reproducibility of calculated elastic moduli and agreement of small-strain Discover and LAMMPS E/K protocols within 0% to ±3% (strain 0.001-0.01). This is computational protocol repeatability, not accuracy against experiment, a statistical confidence interval or the error of a reserved-property prediction. The Rh deviations from the selected 276 GPa experimental entry remain -6.5% and -36.6%.

Readable equations and values:
Ca (α): five-cell lattice, experiment / 12-6 / 9-6 = 27.942 / 27.947 / 27.953 angstrom; surface energy, experiment +/- uncertainty / 12-6 / 9-6 = 0.492 +/- 0.01 / 0.49 / 0.49 J/m^2; bulk modulus, selected experiment / 12-6 / 9-6 = 20 / 30 / 21 GPa.
Rh: five-cell lattice, experiment / 12-6 / 9-6 = 19.016 / 19.016 / 19.014 angstrom; surface energy, experiment +/- uncertainty / 12-6 / 9-6 = 2.64 +/- 0.02 / 2.643 / 2.643 J/m^2; bulk modulus, selected experiment / 12-6 / 9-6 = 276 / 258 / 175 GPa.
Sr (α): five-cell lattice, experiment / 12-6 / 9-6 = 30.42 / 30.423 / 30.421 angstrom; surface energy, experiment +/- uncertainty / 12-6 / 9-6 = 0.41 +/- 0.01 / 0.411 / 0.41 J/m^2; bulk modulus, selected experiment / 12-6 / 9-6 = 12 / 24 / 16 GPa.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)

## 33. Appendix · what uncertainty must include

A plotted error bar can represent experimental uncertainty, sampling variation or a confidence interval; label which one it is. The calibration chart uses only the source-reported experimental uncertainties. It does not invent simulation error bars from rounded table values. Published model predictions are transcribed at their reported precision. Numerical convergence and systematic model error are different from statistical repeatability. For the ideal geometry and explanatory animations in this bundle, there is no sampling uncertainty because they are constructions rather than a measured simulation campaign. A held-out error does not become less important because a run is reproducible. Kanhaiya et al. SI S7-S8 reports approximately ±3% reproducibility of calculated elastic moduli and agreement of small-strain Discover and LAMMPS E/K protocols within 0% to ±3% (strain 0.001-0.01). This is computational protocol repeatability, not accuracy against experiment, a statistical confidence interval or the error of a reserved-property prediction. The Rh deviations from the selected 276 GPa experimental entry remain -6.5% and -36.6%.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- IFF Agent workflow documentation (2026)
- Original derivation / explicitly illustrative visual

## 34. Appendix · primary references

The manifest retains primary source locators and evidence classifications. Kanhaiya et al., current SI and corrected supplementary geometry support the metal example. The author correction restored missing geometry and scripts. The original Liu SI supports the binary-alloy example; only its numerical results are used, with no copied figures. LAMMPS supports engine conventions, MACE the learned-potential role. The IFF Agent section explains its implemented workflow; it supplies no new package validation.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)
- [Liu et al. (2018), Understanding Chemical Bonding in Alloys and the Representation in Atomistic Simulations](https://doi.org/10.1021/acs.jpcc.8b01891)
- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)
- [LAMMPS documentation: lj/cut interaction convention](https://docs.lammps.org/pair_lj.html)
- [LAMMPS documentation: fix nve and minimize](https://docs.lammps.org/fix_nve.html)
- [Batatia et al. (2022), MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate Force Fields](https://arxiv.org/abs/2206.07697)
- IFF Agent workflow documentation (2026)

## 35. Appendix · reuse and scientific limits

No additional reuse license is granted for original visuals, media, prose or authoring code. Third-party material retains its actual license and source attribution. The corrected Rh source CAR files and Kanhaiya article are CC BY 4.0; Liu SI is CC BY-NC 4.0 and is linked rather than distributed. The plots redraw attributed numerical facts and reproduce no source figures. Source-derived ideal geometry and prescribed motion are educational constructions. Published results were not rerun, and this presentation establishes no new materials trajectory, fitted parameter package or scientific adoption. Native Microsoft PowerPoint playback, other browser engines and remote delivery remain unverified.

- [Kanhaiya, Kim, Im & Heinz (2021), Accurate simulation of surfaces and interfaces of ten FCC metals and steel using Lennard–Jones potentials](https://doi.org/10.1038/s41524-020-00478-1)
- [Kanhaiya et al. (2021), Author Correction](https://doi.org/10.1038/s41524-021-00576-8)
- [Liu et al. (2018), original Supporting Information, Tables S1–S2 and discussion S18–S19](https://acs.figshare.com/articles/journal_contribution/Understanding_Chemical_Bonding_in_Alloys_and_the_Representation_in_Atomistic_Simulations/6531197)
- IFF Agent workflow documentation (2026)
- Original derivation / explicitly illustrative visual