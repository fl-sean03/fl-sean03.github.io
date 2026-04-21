---
title: "Engineering With Nature"
description: "Ecology as engineering substrate: living shorelines, oyster reef and mangrove performance, thin-layer marsh, Dutch Building with Nature, and honest envelopes of application."
date: 2026-04-21
image: /images/research/territorial-engineering/engineering-with-nature.png
---

Ecology and civil engineering occupy adjacent budget lines on most coastal projects. Mitigation for one is offset against the other. The USACE Engineering With Nature program, launched in 2010, proposes a different frame: that natural and nature-based features can deliver engineering functions, and that projects designed to work with biological and sedimentary processes produce better outcomes than projects designed to minimize them. The proposition is partly demonstrated, partly plausible, and requires precision about which parts are which.

This document covers what the performance data show for each class of nature-based feature, where the data are thin, and what conditions determine whether a living shoreline or hybrid approach is sufficient or whether hard structure is the only answer. It does not argue for ecology over engineering or engineering over ecology. It describes what is known.

---

## The EWN framework

USACE's Engineering With Nature initiative was launched in 2010 under Dr. Todd Bridges at the Engineer Research and Development Center (ERDC). Congressional funding arrived in 2019 at $12 million, growing to $21 million by 2021. The program operates through the Network for Engineering with Nature (N-EWN, launched 2019) and has produced three Atlas volumes (2018, 2021, 2024) documenting 118 constructed projects globally.

The operational term is Natural and Nature-Based Features (NNBF): landscape elements engineered to provide flood risk management functions while producing co-benefits in ecology, water quality, recreation, and carbon storage. NNBF categories include oyster reefs, coral reefs, submerged aquatic vegetation, marshes, mangroves, beach-dune systems, maritime forests, and hybrid combinations with structural elements.

Congressional mandate has formalized the requirement. The 2016 Water Resources Development Act requires NNBF consideration in flood risk projects. The 2018 WRDA requires feasibility reports to compare traditional and natural infrastructure options. In 2021, USACE led the International Guidelines on Natural and Nature-Based Features for Flood Risk Management, a five-year effort involving USACE, Netherlands Rijkswaterstaat, UK Environment Agency, NOAA, the World Bank, and 180 practitioners from 77 organizations.

The policy framework is ahead of the performance data in some areas, particularly at large scale. The document that follows works from measured data toward application regimes, not the other direction.

---

## Oyster reef performance

Constructed oyster reefs (COR) function as low-profile breakwaters in estuarine systems. The primary mechanism is bed friction and wave energy dissipation as water passes over the reef crest. The leeward side accumulates sediment, providing secondary stabilization to backing marsh or shoreline fill.

Performance is controlled by a single variable: inundation duration. Morris et al. (2021, *Ecological Applications*) conducted a multi-site comparison across US Atlantic and Gulf coast living shoreline installations and found:

| Inundation regime | Reef crest condition | Average wave height reduction |
|---|---|---|
| Low inundation (reef crest above water more than 50% of time) | Freeboard positive | 68% |
| High inundation (reef crest below water more than 50% of time) | Freeboard near zero or negative | ~5% (not statistically distinguishable from no reef) |

The 68% attenuation figure is an average with site-to-site variation. The ~5% figure for high inundation is the functional floor: a submerged reef provides negligible wave attenuation relative to a bare bottom.

The inundation threshold also determines ecology. Eastern oysters (*Crassostrea virginica*) require aerial exposure for more than half the tidal cycle to maintain population viability. Reef structure that maximizes wave attenuation by sitting higher in the tidal frame is also reef structure that limits oyster establishment and self-repair. This is not a solvable conflict. It is a design tradeoff: engineering performance requires low inundation; ecological function requires high inundation. The two regimes are mutually exclusive at any given tidal elevation.

Time to maximum attenuation is approximately nine years post-construction. As oyster populations establish, grow vertically, and densify the structure, wave dissipation increases. A newly constructed oyster reef underperforms its nine-year equilibrium state significantly, a fact relevant to project performance claims made shortly after installation.

Sea level rise vulnerability follows directly from the inundation relationship. As water levels rise relative to reef crest elevation, any reef transitions from low-inundation (high attenuation) toward high-inundation (low attenuation). Oysters can accrete vertically if substrate and water quality support growth, but accretion rates are not guaranteed to track projected sea level rise. Projects in locations where SLR is proceeding faster than biological accretion will lose attenuation performance over the design life.

The demonstrated application regime for oyster reef living shorelines is estuarine, fetch-limited, low-wave-energy settings. At small to site scale (see [ontology](/research/territorial-engineering/ontology/) scale ladder), constructed oyster reef is a well-documented shoreline stabilization tool. At larger scale, or in exposed wave environments, the geometry required to produce meaningful attenuation becomes structurally incompatible with oyster biology.

---

## Salt marsh attenuation

Salt marsh wave attenuation is the best-documented of the nature-based categories in quantitative terms. Shepard et al. (2011, *PLoS ONE*) conducted a systematic review and meta-analysis establishing:

- Wave height reduction: 0.64 to 0.65% per meter of marsh width.
- A 250 m marsh attenuates approximately 50% of incident wave height.
- Storm surge attenuation: 5 to 10 cm per 100 m of marsh width; 50 to 100 cm per 1,000 m of marsh width.

The surge attenuation figure is highly sensitive to inundation depth during the storm. When surge overtops marsh vegetation and marsh surface is deeply flooded, stem resistance is reduced and the 5 to 10 cm per 100 m rate does not hold. Surge attenuation at high inundation is less than at moderate inundation, mirroring the oyster reef inundation relationship.

Marshes also accumulate sediment through biogenic accretion as suspended material settles in calm conditions behind the vegetated edge. In sediment-rich environments, accretion rates of 2 to 8 mm per year are documented, providing some capacity to track gradual sea level rise. Where sediment supply is low, as in Louisiana where Mississippi River levees cut the sediment flux to the delta, marshes cannot keep pace with relative sea level rise and transition to open water. Louisiana has lost approximately 4,900 km² of coastal wetland since the 1930s through this mechanism. Marsh wave attenuation is only useful on marsh that exists.

Cross-link: marsh loss context, sediment deficits, and subsidence rates are covered in [coastal-morphodynamics](/research/territorial-engineering/coastal-morphodynamics/) and [sediment-as-infrastructure](/research/territorial-engineering/sediment-as-infrastructure/).

---

## Mangrove scaffolds

Mangroves attenuate waves through drag on prop roots, pneumatophores, and trunks. The decay follows an exponential form:

**H(x) = H_0 x e^{-k x}**

where H(x) is wave height at distance x across the mangrove belt, H_0 is incident wave height, and k is an attenuation coefficient. Measured k values range from 0.01 to 0.15 per meter depending on species, stem density, and root architecture. A 200 m dense mangrove stand attenuates 50 to 75% of incident wave height under moderate wave conditions. Wider ranges of k reflect the biological variability; a stand of sparse juvenile mangroves at low density will perform near the lower bound, a mature dense stand at the upper bound.

Mangrove scaffolding deploys bamboo or other permeable structures seaward of degraded mangrove edges where erosion has exposed bare mud. The structure dissipates wave energy enough to allow sediment to settle and mangrove propagules to recruit and establish. Once established, mangrove roots bind the new sediment and become the wave attenuation mechanism themselves. This technique has been deployed at field scale in Vietnam, Indonesia, and Bangladesh where mangrove loss has exposed formerly protected shorelines.

The application regime is tropical and subtropical coasts with sufficient sediment supply and water quality to support mangrove growth. Mangroves cannot be transplanted into cold climates, exposed high-energy coasts, or locations where turbidity or pollution prevent establishment. In Florida, the northern range limit for red mangrove (*Rhizophora mangle*) is roughly latitude 29 to 30 degrees north; freeze events in 2010 and earlier decades killed mangrove stands along the upper Gulf coast. The relevant ESA Section 7 consultation context for any engineered mangrove work adjacent to listed species habitat is covered in [institutions-and-permitting](/research/territorial-engineering/institutions-and-permitting/).

---

## Coral reef attenuation

Ferrario et al. (2014, *Nature Communications*) synthesized global wave dissipation data for coral reefs and found that reefs dissipate 97% of incident wave energy on average. Reef crest depth and rugosity (structural roughness) are the primary controls. A 1 m rise in mean water level over a shallow reef crest roughly doubles wave energy transmission to the shoreline behind it, because the dissipation mechanism depends on the breaking of waves on the shallow crest.

Coral reef restoration does not currently offer a near-term substitute for engineered breakwaters at project scale. Mote Marine Laboratory in Sarasota operates micro-fragmentation propagation of *Acropora cervicornis* and *A. palmata* (both ESA-listed as Threatened) at rates 25 to 50 times conventional propagation. The Coral Restoration Consortium coordinates multi-institution outplanting across the Florida reef tract, with survival rates of 65 to 85% at one year for well-matched genotypes. Over 100,000 coral fragments have been outplanted on Florida reefs since 2012.

The structural limitation is time. Reef crest development to engineering-relevant depths requires decades to centuries. Marine heatwaves bleach and kill reefs at temperatures above approximately 1 degree Celsius over the local maximum monthly mean; many Indo-Pacific reefs are at or above this threshold. Restoration restores ecological function in locally favorable conditions. It does not rebuild wave attenuation at the multi-year timescale relevant to coastal engineering design.

The honest framing: coral reefs provide real coastal protection where they exist. Restoration is worth doing for ecological and co-benefit reasons. But reef restoration is not a shoreline protection tool on the timescale of infrastructure planning.

---

## Thin-layer marsh restoration

Thin-layer placement (TLP) raises subsided marsh surface elevations by depositing dredged material at 5 to 30 cm lift thickness. The lift is thick enough to counter recent subsidence, thin enough to allow existing marsh vegetation to survive through the fill and recolonize from below-ground organic matter. The technique is most useful where marsh has dropped below optimal inundation depth for vegetation but the vegetation community is still present and the substrate is not yet converted to open water.

The Poplar Island Environmental Restoration Project in Chesapeake Bay, Maryland has placed approximately 1 million cubic meters per year of material from Baltimore Harbor maintenance dredging since 1998, restoring over 170 acres of tidal marsh and upland habitat. The project converts dredge disposal cost into ecological restoration, a beneficial use arrangement described in the ontology.

In Louisiana, where subsidence rates run 5 to 25 mm per year and the Mississippi River delivers little sediment to the delta because of upstream levees, TLP performance is explicitly time-limited. A 15 cm placement provides 6 to 30 years of elevation benefit before re-treatment is needed, depending on local subsidence rate. The Louisiana Coastal Master Plan allocates $1.5 billion for sand-moving projects over 50 years specifically because this maintenance cycle is indefinite. The program has placed 193 million cubic yards of sediment since CPRA's founding in 2005. The state loses a football field of land every 100 minutes. TLP is ameliorating the trajectory, not reversing it.

---

## Barrier island restoration

Louisiana has the most extensive active barrier island restoration program in the United States. CWPPRA (the 1990 Coastal Wetlands Planning, Protection and Restoration Act, funded at $40 to 85 million annually) has authorized 214 projects restoring 97,000 net acres at a total cost of $1.8 billion. CPRA has restored 71.6 miles of barrier islands in its cumulative program.

The construction method is conventional hydraulic fill: trailing suction hopper dredgers (TSHDs) pull sediment from offshore borrow areas, typically Ship Shoal located 15 miles offshore, and hydraulically place it to rebuild beach and dune templates. Marsh grass plugs are planted on back-barrier surfaces and sand fences promote aeolian dune growth.

From 2008 to 2016, 17 barrier island restoration projects across Terrebonne Bay, Barataria Bay, and the Chandeleur Islands produced a net gain of approximately 2,200 acres of land. This net gain occurred despite one tropical storm and two hurricanes impacting the restored areas during the measurement period. The largest single project created approximately 1,257 acres of marsh, dune, and beach from 9.2 million cubic yards of sediment, restoring over 7 miles of shoreline.

The Chandeleur Islands lost approximately 85% of their pre-Katrina area to Hurricanes Katrina and Rita in 2005. The most recent CWPPRA restoration placed 5.85 million cubic yards of sand in 47,000 linear feet of berm. An approved future plan with a $362 million budget targets 2,400 acres of dune, beach, and back-barrier marsh using $237 million from Deepwater Horizon settlement funds, with construction expected to begin in 2026.

Half-life is the honest measure of barrier island nourishment performance. Projects in Louisiana have a practical half-life of 10 to 20 years before material losses from storms, longshore drift, and subsidence require major re-nourishment. CPRA explicitly accepts this in its planning documents; the Master Plan is designed for perpetual maintenance cycles.

The Louisiana case applies to other Gulf and Atlantic barrier systems in sediment-deficient settings. Natural barrier rollover, the mechanism by which undeveloped barriers maintain freeboard during sea level rise by migrating landward, is unavailable to developed or restored barriers with fixed infrastructure. Engineered barrier restoration requires active maintenance or it reverts toward open water. The sediment budget context for this is in [coastal-morphodynamics](/research/territorial-engineering/coastal-morphodynamics/).

---

## Netherlands Building with Nature: EcoShape and the Sand Motor

The Dutch Building with Nature (BwN) program operates through EcoShape, a public-private consortium formed in 2008 involving Van Oord, DEME, Boskalis, Deltares, Royal HaskoningDHV, and Rijkswaterstaat. The program's first decade executed approximately EUR 70 million of projects and generated the international BwN design guideline framework.

The BwN philosophy moves through three levels: building in nature (minimize impact), building of nature (use natural materials), and building with nature (harness natural processes as the engineering mechanism itself). The third level is the design innovation: rather than engineering against natural forces, identify natural processes that do useful work and design structures that direct and amplify them.

The Zandmotor (Sand Motor), completed in 2011 at Ter Heijde on the Delfland coast of the Netherlands, is the program's flagship application. Instead of conventional nourishment that distributes sand across 30 km of coast every five years, creating repeated ecological disturbance, 21.5 million cubic meters of sand were placed at one location as a 128-hectare hook-shaped peninsula at a cost of EUR 70 million. Natural wave and tidal forcing then redistribute the sand downdrift over a 10 to 20 year design period, feeding approximately 20 km of coastline without repeated intervention.

The ten-year evaluation in 2021 confirmed coastal protection, dune growth, habitat creation, and recreational use. Sand has migrated as predicted. The intervention effectively pre-placed multiple nourishment cycles' worth of material in one construction event, reducing total disturbance frequency.

The Sand Motor is an accretion intervention by the ontology definitions: it builds on existing substrate, directing natural processes to produce the desired shoreline geometry. It does not produce new substrate that did not previously exist. The distinction matters for jurisdictional and permitting purposes.

Maasvlakte 2, the 1,000-hectare port expansion completed in 2013 on the same Dutch coastline, incorporated BwN principles in a different way. The offshore borrow pit was designed with sloped rather than vertical walls to allow oxygenated seawater circulation and benthic recolonization. The extracted seabed was excluded from clay-rich zones to minimize turbidity plumes. Post-construction monitoring found a 20-fold increase in demersal fish biomass within the deep pit relative to surrounding shallower areas, an unintended ecological benefit from the construction geometry. The deep pit created a low-energy sediment trap with high organic input that functions as an artificial reef.

The Maasvlakte 2 result is a cross-cutting finding: ecological compensation and ecological benefit can diverge from what was planned. The 25,000-hectare Voordelta seabed protection zone established as formal compensation for the 2,455 hectares of Natura 2000 habitat eliminated by the reclamation failed to deliver as designed. Shrimp fishing with gear lighter than the banned beam trawls increased fourfold within the protection zone between 2008 and 2022, sustaining seabed disturbance. A 2022 district court ruling found the compensation inadequate; the Council of State overturned that ruling on narrow legal grounds in subsequent proceedings. The ecological conditions in the Voordelta remain poor as of 2026. The lesson is that regulatory compensation accounting and actual ecological outcomes are not the same thing, and that monitoring the difference matters.

---

## Performance summary

The table below consolidates the quantitative attenuation data from primary literature. Numbers for each habitat reflect the conditions under which they were measured; extrapolating outside those conditions requires explicit justification.

| Habitat or feature | Performance metric | Value | Conditions | Source |
|---|---|---|---|---|
| Oyster reef (constructed) | Wave height reduction | 68% | Low inundation (<50% submerged) | Morris et al. 2021 |
| Oyster reef (constructed) | Wave height reduction | ~5% | High inundation (>50% submerged) | Morris et al. 2021 |
| Oyster reef (constructed) | Time to maximum attenuation | ~9 years | Post-construction establishment | Frontiers 2022 |
| Salt marsh | Wave height reduction per meter width | 0.64 to 0.65% per m | Moderate inundation | Shepard et al. 2011 |
| Salt marsh (250 m width) | Wave height reduction | ~50% | Moderate inundation | Shepard et al. 2011 |
| Salt marsh | Surge attenuation | 5 to 10 cm per 100 m | Moderate inundation | Shepard et al. 2011 |
| Mangrove belt (200 m, dense) | Wave height reduction | 50 to 75% | k = 0.01 to 0.15 m⁻¹ | Literature range |
| Coral reef (intact, global average) | Wave energy dissipation | 97% | Shallow reef crest present | Ferrario et al. 2014 |
| Thin-layer marsh placement | Elevation benefit lifespan | 6 to 30 years per application | Louisiana; subsidence 5 to 25 mm/yr | CPRA |
| Barrier island nourishment | Practical half-life before re-nourishment | 10 to 20 years | Louisiana Gulf coast | CPRA experience |
| Sand Motor mega-nourishment | Coastal benefit period | 10 to 20 year design life | Delfland coast, Netherlands | Rijkswaterstaat 2021 |
| Louisiana barrier island program (2008 to 2016) | Net land gain across 17 projects | ~2,200 acres | Storms occurred during measurement period | CPRA annual data |

---

## When living shorelines are sufficient, when they are not

Nature-based features have documented performance envelopes. They also have hard limits. The engineering question is which regime applies to a given site and function.

**Living shorelines are the right answer** where: the shoreline is estuarine or fetch-limited with low to moderate incident wave energy; the function required is sediment retention and shoreline stabilization rather than surge exclusion; ecological co-benefits are valued; and the site's tidal regime keeps oyster reef or marsh features in their productive inundation range. At lot and site scale, these conditions apply at thousands of US East and Gulf coast locations. The CWPPRA program has demonstrated this at program scale in Louisiana.

**Hybrid structure is the right answer** where: wave energy is too high for living features to survive unaided, but a hard structure placed seaward can reduce energy enough to allow natural features to establish in its lee; or where the living feature has documented attenuation capacity but insufficient surge resistance on its own. Hybrid designs in practice combine a low-profile rock sill or breakwater at the waterward edge with oyster reef, marsh, or beach habitat in the protected zone behind it. The sill keeps incident energy below the biological threshold for habitat establishment; the habitat contributes attenuation and ecological function. At site and district scale, hybrid designs represent the current state of practice for moderate-wave estuarine and open-coast applications.

**Hard structure is the right answer** where: design wave conditions exceed any biological threshold for habitat persistence; surge protection requires a specific crest elevation and overtopping rate that cannot be achieved with soft features; the project life and maintenance budget do not support periodic biological re-establishment; or the consequence of failure is catastrophic and irreversible. Port perimeters, major surge barriers, and flood control levees serving dense urban areas belong here. The Maasvlakte 2 perimeter and the authorized Galveston Bay Barrier System (Ike Dike) are hard-structure answers to hard-structure engineering problems. No combination of marsh, oyster reef, or sand motor would substitute.

The EWN program's 118 documented projects are distributed across a range of scales and functions. The honest characterization of where the data sit: living shorelines at site scale are demonstrated and broadly applicable. Hybrid approaches at district scale are engineered and increasingly standard. Nature-based contributions at megaproject scale are plausible in specific roles (borrow pit habitat design, leeward-of-hard-structure revegetation, beneficial use placement for marsh restoration) but are not substitutes for the hard perimeter that makes the megaproject structurally viable.

That distinction matters for how EWN is applied. The program is not an argument that ecology replaces structure. It is an argument that the two can be integrated where conditions permit, that integration often produces better outcomes than mitigation-as-afterthought, and that the conditions permitting integration need to be evaluated honestly against performance data rather than assumed from ecological optimism.

---

## Monitoring gaps and honest uncertainty

The EWN Atlas documents 118 projects, but performance monitoring across those projects is uneven. The best-monitored features are the ones with the longest track records: Louisiana barrier island nourishment (decades of CWPPRA monitoring), Poplar Island TLP (ongoing since 1998), and the Zandmotor (systematic annual monitoring since 2011 as a designed experiment). Constructed oyster reef performance is better characterized than it was a decade ago, largely through the Morris et al. (2021) multi-site synthesis.

Gaps are concentrated at the large-scale and long-horizon end. How hybrid shoreline designs perform over 20 to 50 year time horizons under projected sea level rise is not well characterized by field data; projections rely on models calibrated against short observation periods. How mangrove scaffold installations perform in high-energy settings when the scaffold fails or degrades has not been systematically documented. Coral reef restoration success at multi-kilometer scale has not been demonstrated.

The nine-year time to maximum oyster reef performance has a practical implication for infrastructure investment: a project permitted and constructed today will not reach its design performance state for nearly a decade. Projects whose cost-benefit analysis assumes day-one performance are using the wrong baseline.

Louisiana's subsidence rate compounds every monitoring challenge in that setting. A project performing well at installation can be losing performance within five years as the surface subsides into higher inundation. Performance monitoring must account for vertical change, not just planform area.

Sea level rise interacts with these dynamics in ways that are directionally understood but not precisely quantified at site level. The NOAA 2022 SLR scenarios span from 0.3 m (low) to 2.0 m (high) by 2100 at the global mean, with regional adjustments for subsidence, GIA, and ocean dynamics. For Louisiana, where relative sea level rise already exceeds 1 inch per year in some locations, even the low scenario further compresses the performance window of nature-based features. Planning with NOAA Intermediate-High (1.5 m global by 2100) as the design scenario, as USACE currently does for most coastal project analysis, is appropriate for long-lived infrastructure.

The performance data in this document, combined with the morphodynamic framework in [coastal-morphodynamics](/research/territorial-engineering/coastal-morphodynamics/), provide the physical basis for evaluating ecological integration options. The permitting framework that governs what can be built, and in what sequence, is in [institutions-and-permitting](/research/territorial-engineering/institutions-and-permitting/), including ESA Section 7 consultation obligations for projects affecting listed species in living shoreline settings. The reclamation engineering context is in [reclamation-methods](/research/territorial-engineering/reclamation-methods/).
