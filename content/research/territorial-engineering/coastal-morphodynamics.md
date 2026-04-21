---
title: "Coastal Morphodynamics"
description: "The science every downstream document inherits: sediment budgets, littoral drift cells, equilibrium profile, storm response, barrier islands, inlet stability, and the limits of numerical modeling."
date: 2026-04-21
image: /images/research/territorial-engineering/coastal-morphodynamics.png
---

Coastal engineering inherits all its boundary conditions from sediment physics. Where sand goes, what makes it move, how it organizes itself into beaches, barriers, and inlets, these are not design variables. They are the constraint set inside which design operates. Every successful reclamation project treats the sediment system as dominant and designs to work with it. The ones that fail tend to fail because they ignored it.

This document is the science base for everything downstream. It establishes the accounting framework (sediment budgets), the transport relations (CERC, Kamphuis, van Rijn), the geometry of equilibrium (beach profile, headland-bay planform, barrier island, inlet cross-section), and the honest limits of current numerical models.

---

## Sediment budgets

The sediment budget is the foundational accounting tool for coastal management. It quantifies inputs, outputs, and storage changes within a defined control volume over a specified time period. Komar's *Beach Processes and Sedimentation* (1998) provides the canonical treatment. A reach of coast receives sediment from rivers, eroding bluffs, offshore bar migration onshore, and longshore drift from adjacent cells. It loses sediment to submarine canyons, tidal inlet ebb deltas, blown-out dunes, and longshore drift out of the cell. Net change in storage equals inputs minus outputs.

For a cross-shore profile integrated over a reference depth (the closure depth h*), the continuity expression is dV/dt = Q_in - Q_out, where V is volumetric storage per unit shoreline width and the Q terms are transport rates in m³/yr per meter of coast.

The USACE Coastal Engineering Manual, Part V (EM 1110-2-1810, 2002) systematizes this into a national framework for beach nourishment and inlet management. It recognizes three categories of sediment budget components:

- **Natural processes**: wave-driven longshore drift, aeolian transport, riverine input, biogenic carbonate production
- **Anthropogenic**: dredged material placement, dam impoundment reducing river sediment, beach nourishment, sand mining
- **Tectonic and sea-level vertical components**: subsidence, isostatic rebound, relative sea-level rise

A closing sediment budget resolves all three. Failure to account for river-load reduction by upstream damming is the most common source of chronic budget deficit in developed coastlines. The Mississippi River's sediment discharge dropped by half between 1950 and 2000 through dam construction in the Missouri basin, and the Louisiana coast has lost approximately 4,900 km² of land since 1932 in large part because of this deficit.

---

## Littoral drift cells

Littoral drift cells are semi-enclosed compartments bounded by headlands, submarine canyons, or major inlets, within which sediment circulates with minimal exchange to adjacent cells. Bowen and Inman (1966) formalized the cell concept in the Point Arguello sediment budget study for CERC. Cell boundaries are identified using sediment tracer studies, heavy-mineral sourcing, wave-flux divergence analysis, and bathymetric breaks.

The cell concept matters for reclamation because fill placed in one cell does not feed adjacent cells, and shoreline works that interrupt longshore drift cause predictable downdrift erosion. Every serious reclamation project begins with delineation of the drift cell it sits in and a mass balance within that cell.

### CERC equation

The Shore Protection Manual formula, universally called the CERC equation, links immersed-weight longshore sediment flux I_l to breaking wave energy flux:

**I_l = K · P_ls**

where P_ls = (ρ_s g H_b² C_gb sin 2α_b)/16 is the breaking wave energy flux per unit width, H_b is significant breaking wave height, C_gb is group velocity at breaking, α_b is breaker angle, and K is a dimensionless transport coefficient near 0.77 for bulk transport, adjusted for grain size. Volumetric transport Q_l = I_l / [(ρ_s - ρ)(1 - p) g], with p near 0.4 for typical beach sand porosity.

CERC overpredicts transport on coarse-grained beaches and is insensitive to wave period and beach slope. It remains the most widely used bulk formula in US practice and appears throughout the CEM Part III-2.

### Kamphuis formula

Kamphuis (1991) developed a physically richer formula from 3D laboratory experiments, incorporating wave period, beach slope, and grain size explicitly:

**I_m = 2.27 · H_{s,b}² · T_p^{1.5} · (tan α_b)^{0.75} · D_50^{-0.25} · (sin 2φ_b)^{0.6}**

where I_m is immersed-mass transport rate (kg/s·m), T_p is spectral peak period (s), tan α_b is beach slope from breaker line to shore, and D_50 is median grain size (m). Kamphuis rates run approximately one-third of CERC predictions and match field measurements more closely. Most recent process-based modeling favors Kamphuis or the van Rijn formulations for design work where grain size or wave period deviates from SPM calibration conditions.

### van Rijn formulations

Leo van Rijn's formula set (van Rijn 1993, updated through 2016) separates bed-load and suspended-load transport using non-dimensional parameters. The TRANSPOR2004 model integrates these for cross-shore and longshore directions, accounting for wave asymmetry and undertow. van Rijn's framework is the default transport engine in Delft3D and is increasingly used for nourishment design.

---

## Equilibrium beach profile

The equilibrium beach profile (EBP) concept asserts that a beach exposed to stationary wave conditions asymptotically approaches a stable cross-shore form. Bruun (1954) first described this empirically. Dean (1977) derived the canonical power-law expression:

**h = A x^(2/3)**

where h is water depth (m), x is cross-shore distance from shoreline (m), and A is a sediment scale parameter in m^(1/3). A is a function of sediment fall velocity: A ≈ 0.067 w_s^{0.44} (Dean 1987). For fine sand with D_50 = 0.2 mm, A ≈ 0.10. For coarse sand with D_50 = 0.5 mm, A ≈ 0.15.

The 2/3 exponent follows from the assumption of uniform wave-energy dissipation per unit volume across the surf zone. Dean and Dalrymple (2002), *Coastal Processes with Engineering Applications*, remains the definitive pedagogical treatment, including nourishment volume calculations derived from EBP geometry.

The EBP defines the active profile from berm crest to the closure depth h*, beyond which annual wave-driven sediment exchange is negligible. Hallermeier (1981) provides the canonical closure-depth estimator using annual wave statistics; USACE uses this to set the seaward limit of nourishment volume calculations.

The EBP has known limits: it assumes stationary wave conditions, ignores longshore gradients, and represents gravel beaches and hard-substrate coasts poorly. For reclamation design, the EBP is useful for setting fill geometry targets and nourishment sacrificial volumes, but not for site selection or multi-decade evolution forecasts.

---

## Bruun rule and its discontents

Bruun (1962) proposed that as sea level rises by ΔS, the equilibrium profile translates upward and landward, causing shoreline recession R:

**R = (L* · ΔS) / (h* + B)**

where L* is horizontal active-profile extent, h* is closure depth, and B is berm crest height. The ratio L*/(h* + B) is typically 50 to 100, so 1 m of sea-level rise produces 50 to 100 m of shoreline recession under Bruun assumptions.

The Bruun Rule has been under sustained critique since the early 1990s. Cooper and Pilkey's 2004 *Geomorphology* paper, titled "Sea-level rise and shoreline retreat: time to abandon the Bruun Rule," is the reference attack. They argue the rule is inapplicable in most real-world settings because it assumes:

1. A closed sediment budget with no longshore gradients
2. A clearly defined closure depth
3. No coastal structures
4. No sediment input from rivers, inlets, or the nearshore
5. Steady-state wave climate

Most coastlines violate multiple assumptions simultaneously. Ranasinghe et al. (2012) synthesize alternatives including the coastal volumetric approach and process-based models that reproduce SLR shoreline response without the Bruun assumption set. Their review confirms that Bruun predictions bracket observed recession rates but are unreliable for specific-site planning.

The Davidson-Arnott relaxed-budget model (R-DA) allows exchange between upper and lower shoreface, acknowledging that lower-shoreface erosion can contribute sediment to maintain the upper profile under SLR. This more nearly matches observed shoreline behavior on barrier coasts.

For reclamation design, the honest treatment is to use Bruun as a screening tool for relative site comparison and to use process-based models with explicit sediment budgets for actual design work. Using Bruun as the sole basis for SLR adaptation planning is not defensible in 2026.

---

## Storm response: the Sallenger scale

Storm response and post-storm recovery occur on different time scales and by different physical mechanisms. Sallenger (2000) proposed a four-regime impact scale linking storm water levels to dune morphology:

| Regime | Condition | Net Sediment Motion |
|---|---|---|
| **Swash** | R_high < D_low | Foreshore erosion only; recovers post-storm |
| **Collision** | D_low < R_high < D_high | Dune scarping; net sand loss from dune |
| **Overwash** | R_high > D_high | Landward sand transport; barrier narrowing |
| **Inundation** | Surge > D_high continuously | Massive landward transport; potential breaching |

R_high is the run-up exceedance elevation (tide plus surge plus wave setup plus swash). D_high is dune crest, D_low is dune toe. USGS applies this scale operationally for pre-landfall hurricane impact forecasting across the US Atlantic and Gulf coasts.

Recovery rates scale with residual berm volume, wave energy climate, and sediment availability. Swash-regime beaches typically recover within a single swell season. Overwash-regime recovery takes years and depends on aeolian dune rebuilding. Inundation-breached barriers may not recover without intervention.

For reclamation design, the Sallenger scale provides the framework for sizing the outer dune and the initial fill freeboard. The design objective is typically to keep the 100-year event in the collision regime and the 500-year event in the overwash regime. Lynetteholm's +2.5 m initial perimeter, rising to +5.5 m at final build, reflects this logic under projected 22nd-century Baltic sea levels.

---

## Headland-bay beach geometry

Headland-bay (or embayed) beaches form in the lee of rocky headlands. Two geometric models describe their planshape equilibrium.

**Parabolic bay shape** (Hsu and Evans 1989) parameterizes the shoreline as a parabola with focus at the dominant wave diffraction point at the headland tip. The form is widely used for beach stability assessments in Australia and Southeast Asia and appears in USACE coastal engineering practice.

**Log-spiral shape** (Silvester 1970, Silvester and Hsu 1993) uses r = r_0 · e^{aθ}, a constant-growth-rate spiral. Both models predict a static equilibrium when headland control is complete. Beaches matching neither template are dynamically unstable and erode toward one of the equilibria.

Headland-bay geometry matters for reclamation because it predicts where placed sand will remain stable. Fill placed inside a static-bay planform is retained. Fill outside the equilibrium will migrate toward it, typically alongshore toward the headland. Pocket-beach nourishments that ignore this geometry suffer rapid loss; those that align with it hold for decades.

---

## Barrier islands

Barriers are elongate sand bodies fronting lagoons and estuaries. They are overwhelmingly Holocene features, produced over the last 7,000 years as sea-level rise drowned low-gradient coastal plains.

Hayes (1979) established the controlling classification in terms of wave-to-tide energy ratio. Barrier islands are elongate in wave-dominated coasts (mean tidal range under 1 m) and take drumstick shapes with large inlets in mixed-energy coasts (tidal range 1 to 4 m). Barriers are effectively absent where tidal range exceeds 4 m, because tidal prism dominates and longshore drift cannot close inlets.

Oertel (1985) systematized the barrier island system as an integrated sediment-sharing system including main-barrier, inlet, flood delta, and ebb delta subsystems. Stutz and Pilkey (2011) provide a global census: approximately 2,149 open-ocean barriers distributed across nine of ten continental sedimentary coasts.

Barrier migration modes are dominated by overwash during sea-level rise, moving the barrier landward while maintaining freeboard, and by aeolian dune progradation during stillstands or sediment-abundant intervals. Undeveloped barriers under SLR typically evolve by rollover, preserving planform while translating landward. Developed barriers with infrastructure and hard-shoreline control cannot roll over; under continued SLR they either require continuous nourishment, rebuild inland, or drown.

For reclamation design on a barrier coast, the key insight is that natural barriers are not fixed features. Reclamation-produced extensions operate as engineered barriers whose stability must be affirmatively maintained through nourishment cycles set by the local sediment budget, or through hard-perimeter design that does not rely on cross-shore sediment exchange for survival.

---

## Tidal prism and inlet stability

Inlet cross-sectional area is governed by tidal prism through the empirical relation first derived by O'Brien (1931):

**A_c = C · P^n**

where A_c is minimum gorge cross-section (m²), P is the tidal prism through the inlet (m³), C is approximately 6.25 × 10⁻⁵, and n is near 1.0 per O'Brien (1969). Jarrett (1976) revised the constants for regional coasts; the exponent ranges from 0.85 to 1.1 depending on jetty configuration.

A large tidal prism scours and maintains a large inlet. Reduction of tidal prism by bay filling or inlet shoaling causes the inlet to close progressively. Escoffier (1940) provided the first stability theory: an inlet is in stable equilibrium when maximum tidal-cycle velocity equals the equilibrium velocity needed to balance littoral sediment deposition. Below this threshold, the inlet shoals and closes. Above, it scours. The resulting Escoffier stability curve has two equilibria (a stable large inlet and an unstable small inlet) separated by an unstable saddle.

USACE EM 1110-2-1810 Chapter 4 provides operational guidance for inlet management using these relationships. The implication for reclamation is direct: any project that reduces tidal prism materially will destabilize downdrift inlets and may require compensating measures (flood shoal dredging, jetty extension, or direct inlet scour augmentation).

---

## Numerical modeling: what works, what does not

| Model | Developer | Type | Best Use | Known Limits |
|---|---|---|---|---|
| **XBeach** | TU Delft / Deltares | Process-based, 2DH | Storm dune erosion, overwash, surf beat | Depth-averaged; computational cost high; unreliable beyond weeks |
| **Delft3D** | Deltares | Modular hydrodynamic + morphodynamic | Tidal inlet evolution, nourishment spreading, Sand Motor | Requires MORFAC for multi-year runs; calibration-intensive |
| **MIKE21** | DHI | Commercial modular suite | Wave climate, operational surge forecasting, port design | Commercial license; computational limits similar to Delft3D at decadal scale |
| **GENESIS / UNIBEST** | USACE / Deltares | 1-line shoreline models | Long-term planshape, nourishment evolution | Cannot resolve cross-shore profile change |

XBeach was developed specifically for barrier island storm response at UNESCO-IHE by Roelvink and colleagues. It resolves infragravity (surf beat) waves and predicts dune scarping, overwash flux, and breach formation. Its storm impact predictions have been validated against Hurricane Ike and Hurricane Ivan post-storm surveys.

Delft3D has been the primary simulation platform for the Sand Motor mega-nourishment studies and is widely used in inlet management. The morphological acceleration factor technique allows tidal-timescale simulations to represent years of morphological change.

All three process-based models share the same fundamental limit: they cannot reliably simulate decadal-to-century-scale coastal evolution without accumulating numerical errors, and they require site-specific calibration against measured bathymetry and transport rates. For this reason, long-horizon reclamation design combines process-based models for storm and near-term response with empirical approaches (sediment budget, equilibrium profile, Bruun-relaxed budget) for long-term evolution. No single tool covers the full design envelope.

---

## Implications for reclamation design

The morphodynamic framework imposes five operational constraints on any serious reclamation project.

First, the project must close its own sediment budget within the drift cell it occupies. Fill must be sourced from within or explicitly supplemented from out-of-cell imports. Adjacent cells cannot be assumed to supply or accept sediment.

Second, the cross-shore profile must be designed to Dean's form for the local grain size, or the profile will reshape itself and shoreline position will retreat until equilibrium is reached. Over-steep initial placements are common, expensive, and unnecessary.

Third, the storm-design freeboard must keep the design event in the collision or overwash regime, not inundation. Dune elevation, sacrificial berm volume, and back-barrier elevation must be coordinated.

Fourth, any alteration of tidal prism must be compensated in inlet management. Large fill projects close to existing inlets require independent inlet stability analysis and often active management.

Fifth, numerical models are decision-support tools, not design oracles. Long-horizon projections use the sediment budget. Short-horizon storm response uses process-based models. The combination is more defensible than either in isolation.

The morphodynamic constraints do not prohibit reclamation at any scale that has been built to date. They define the design envelope inside which the engineering in [reclamation-methods](/research/territorial-engineering/reclamation-methods/) operates, and the ecological integration options covered in [engineering-with-nature](/research/territorial-engineering/engineering-with-nature/).
