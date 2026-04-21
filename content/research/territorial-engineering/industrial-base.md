---
title: "Industrial Base"
description: "Dredging fleet, component supply chain, labor, autonomous dredging, cyber-physical exposure, and cost curves. The US capacity gap and what closes it."
date: 2026-04-21
image: /images/research/territorial-engineering/industrial-base.png
---

The United States dredges approximately 210 million cubic yards of sediment per year to keep navigation channels open, and projects demand rising to roughly 400 million cubic yards per year by 2045 (Florez 2025, p. 5). The industrial base that has to absorb that increase is undersized, aging, and concentrated in three firms. European competitors operate vessels four times the size of the largest US unit and have built projects, like Maasvlakte 2, at speeds and costs that American contractors cannot match under current conditions.

This document covers the supply side of that equation: fleet structure, component dependencies, workforce, autonomous systems, cyber-physical exposure, and cost. The demand side and regulatory stack are in [institutions-and-permitting](/research/territorial-engineering/institutions-and-permitting/). The engineering methods the fleet executes are in [reclamation-methods](/research/territorial-engineering/reclamation-methods/).

---

## Market structure

The global dredging market is dominated by four European firms headquartered in Belgium and the Netherlands: Boskalis (Netherlands), Van Oord (Netherlands), DEME (Belgium), and Jan De Nul (Belgium). These four firms, often called the "big four," operate the world's largest trailing suction hopper dredgers (TSHDs), the most capable cutter suction dredgers (CSDs), and the majority of sophisticated support vessels. Each firm employs several thousand people and operates globally. Together they have built virtually every large reclamation megaproject completed in the past forty years.

On the US side, three firms hold the majority of domestic fleet capacity: Great Lakes Dredge and Dock, Weeks Marine, and Manson Construction (Florez 2025, p. 7). A handful of smaller operators work in estuarine and inland settings. The Jones Act and the Foreign Dredge Act of 1906 prohibit foreign-flagged dredges from working in US waters, which means the US market is fully closed to direct European competition. This protection has preserved a domestic industry that would otherwise be uncompetitive on open-market terms. It has also shielded that industry from the competitive pressure that would otherwise force capacity investment.

The private sector has invested more than $3 billion in new US-built dredges since 2018 (Florez 2025, p. 2). USACE has separately maintained a small government fleet for emergency and lower-tier channel work. The private investment represents real progress. It does not close the capacity gap relative to the European firms.

---

## Fleet comparison

The core asymmetry is hopper capacity. A TSHD loads sediment by dragging suction pipes across the seabed while underway, filling an onboard hopper, transiting to the fill site, and discharging. Vessel throughput scales with hopper volume and cycle time. European big-four vessels include units with hoppers above 40,000 cubic meters; the Boskalis HAM 318, Vox Maxima, and Van Oord's Vox Apolonia operate in this range. The largest European vessels reach 46,000 cubic meters of hopper capacity (Florez 2025, p. 2).

The largest US TSHD under construction as of 2025 will carry approximately 15,000 cubic yards (roughly 11,500 cubic meters) of hopper capacity (Florez 2025, p. 7). The ratio is approximately four to one.

| Parameter | European Big Four | US Fleet |
|---|---|---|
| Largest TSHD hopper (m³) | 46,000+ | ~11,500 (~15,000 cy) |
| Large-vessel monthly throughput | 3 to 10+ million m³ | 1 to 3 million m³ |
| Very large vessel (>46,000 m³) monthly throughput | above 10 million m³ | not available |
| Flagship CSD output | 6,000 m³/hr (DEME Spartacus) | lower capacity |
| Unit cost TSHD (contractor) | $3 to $8 per m³ | higher (see cost curves below) |

At Maasvlakte 2, Boskalis and Van Oord deployed 23 TSHDs through the PUMA joint venture and set a production record of 3.8 million cubic meters in a single week in spring 2010, using up to 12 vessels simultaneously. The entire US private hopper fleet would struggle to match that single-week production. When Florez (2025, p. 2) notes that "some foreign companies field fleets larger than the entire US fleet," this is the specific comparison.

US fleet age compounds the capacity problem. About one-third of US hopper dredges are over 20 years old, and the median age across all vessel classes exceeds 15 years (Florez 2025, p. 7). European operators have maintained newer average ages through continuous fleet renewal financed by larger project revenues.

---

## What the gap costs in practice

Two metrics from Florez (2025) translate the capacity gap into operational terms.

US dredging costs have risen approximately 200% in inflation-adjusted terms since 1970 (Florez 2025, p. 2). This is not a function of sediment prices or fuel. It reflects a combination of constrained competition, aging equipment, and a permitting environment that extends project timelines and therefore increases contractor mobilization costs. Florez (2025, p. 12) puts the nominal range at $5 to $10 per cubic yard for basic dredging, rising above $20 for specialty or deepening work. The cost-versus-duration relationship matters: projects running five years cost approximately 55% more per cubic yard than those completing in one year, with benefit-cost ratios falling from roughly 2.2 to 1.4 over that range (Florez 2025, p. 12, Fig. 6).

US projects take approximately twice as long as comparable projects overseas (Florez 2025, p. 2). The federal project timeline (feasibility study through construction completion) averages 8.2 years (Florez 2025, p. 14). The Maasvlakte 2 project moved from permit approval to delivered Phase 1 in approximately five years (2008 to 2013), on budget, on schedule. Jacksonville Harbor deepening took from WRDA 2014 authorization to construction completion in 2022, an eight-year arc for a channel-deepening project.

---

## Component supply chain

The US dredging industrial base has two categories of critical import dependency.

The first is port crane infrastructure. Approximately 80% of cranes at US container ports are manufactured by ZPMC, a Chinese state-owned company (Florez 2025, pp. 2, 8). ZPMC's global market dominance reflects cost competitiveness and production scale that no US or European crane manufacturer has been willing to compete with directly. This creates a structural dependency: the port infrastructure that dredged channels must serve is dominated by equipment from a strategic competitor.

The second is dredge components. Key dredge pumps and control systems are sourced primarily from Europe (Florez 2025, p. 2). This is less acute than the crane dependency in practice, since US-European trade relations are stable, but it represents a vulnerability in scenarios where European supply chains are disrupted or where European allies place restrictions on technology transfer. The specific dependencies are in cutter-suction pump systems, specialized impeller alloys, hydraulic controls, and automation hardware.

Sand supply is a third category, geographically concentrated and increasingly constrained. The Bureau of Ocean Energy Management's Marine Minerals Program has conveyed approximately 164 million cubic yards of outer continental shelf sand since 1995 (Florez 2025, p. 8). Southeast Florida's nearshore shelf is approaching exhaustion of beach-quality sand sources at economical dredging depths (Florez 2025, p. 2). As closer borrow areas are depleted, dredges must travel farther per load cycle, increasing unit costs and extending project schedules. A national offshore sand inventory, including assessment of regional borrow strategies and manufactured-sand alternatives, does not yet exist in complete form.

---

## Workforce

The dredging workforce spans three categories that each require different training pipelines.

Mariners operate the vessels themselves: captains, officers, and deck crew licensed through USCG and maritime academies. Dredge plant is specialized enough that most licensed mariners cannot directly operate production dredges without additional training. The industry has historically relied on apprenticeship under experienced operators rather than formal credentialing programs, which creates bottlenecks when expanding capacity.

Dredge operators and plant engineers manage suction systems, cutter drives, pipeline hydraulics, and positioning systems. These are the skilled technical core. European firms have long-standing apprenticeship and academic programs in the Netherlands and Belgium feeding into their fleets. The US has no equivalent pipeline at national scale.

Shoreside engineers provide survey, design, quality control, environmental monitoring, and project management. US coastal engineering programs (universities with strong coastal programs include Stevens Institute, University of Delaware, Texas A&M Galveston, and LSU) produce capable graduates, but enrollment does not scale with projected demand. Beneficial reuse projects (see below) require sediment characterization and ecological monitoring expertise that is separate from dredging operations.

Florez (2025, p. 8) identifies expanding workforce pipelines through maritime academies, community colleges, and the Department of Defense SkillBridge program as a necessary near-term action. The six-to-ten-year policy horizon in the Florez roadmap places workforce development in the long-term bucket (Florez 2025, p. 17), which may underestimate the lead time problem: training pipelines that do not start now will not produce experienced operators when the demand surge arrives in the early 2030s.

---

## Autonomous dredging and AI-enabled placement

Autonomous and semi-autonomous dredging systems are in active development at the major European firms. The current state separates into demonstrated capability and plausible next steps.

Demonstrated: GPS-referenced positioning is standard on all modern TSHDs and allows automated draghead depth maintenance within centimeters. Automated fill monitoring integrates survey data from multibeam echosounders to track fill progress against design elevations. APMT MVII at Maasvlakte 2 uses fully automated STS cranes and lift-AGV transport, demonstrating that AI-enabled logistics control works at commercial scale in port operations, though this is post-construction operations rather than dredge production.

Plausible: Boskalis and Van Oord have both announced R&D investment in autonomous vessel operation for survey and support functions. Fully autonomous TSHD operation for production dredging, where a vessel selects its own borrow area, manages draghead contact, transits without crew, and positions for discharge, is not yet demonstrated at commercial scale. The engineering path is clear: the same sensor fusion, navigation software, and machine-learning classification tools that govern autonomous surface vessels in harbor settings scale to offshore dredging. The regulatory path is not clear. USCG certification and USACE quality-assurance requirements for dredged material placement have not been adapted for autonomous operation.

AI-enabled placement control, where real-time placement quality is assessed from sensor feeds and adjusted during production to optimize for design specification, is similarly plausible. Current practice uses pre-shift survey and post-shift survey with manual QC between them. Closed-loop real-time control would reduce over-placement and deficiency, both of which add cost.

The Florez (2025, p. 17) roadmap places "research on nature-based designs, autonomous dredging, AI-enabled sediment management, and turtle-safe dredges for year-round operations" in the six-to-ten-year long-term tier. This is the appropriate confidence label: Plausible, not Demonstrated, using the [ontology](/research/territorial-engineering/ontology/) from this corpus.

---

## Cyber-physical exposure

The ZPMC crane dependency has a second dimension beyond supply chain. US officials have warned that Chinese-manufactured cranes may contain remote-access backdoors enabling espionage or operational disruption (Florez 2025, pp. 2, 10). The specific mechanism: ZPMC cranes contain programmable logic controllers and network-connected diagnostic systems that were installed during manufacture and have not been systematically audited for foreign access capabilities. The 2021 breach of the Port of Houston network, attributed to a suspected state-sponsored actor, is the highest-profile confirmed incident in the sector; it was detected before harm occurred (Florez 2025, p. 10).

The vulnerability is not theoretical in structure. Port operations depend on crane availability. A crane that can be remotely disabled or whose sensor data can be manipulated creates leverage against port throughput. The same logic applies to SCADA systems controlling navigation locks, pump stations, and water control structures associated with channel infrastructure. The Houston Ship Channel is the nation's busiest port by tonnage and a concentration of petrochemical processing (Florez 2025, p. 3); a sustained disruption there inflicts multi-sector economic damage.

Dredges themselves present a different exposure profile. Modern TSHDs use GPS, GNSS, and inertial navigation for positioning, with hydrographic survey integration from multibeam sonar. Sensor spoofing of positioning data could cause fill to be placed out of specification or borrow material to be extracted from unauthorized areas. These are lower-consequence risks than crane sabotage but are more difficult to detect in real time.

Florez (2025, p. 10) cites NIST SP 800-82 (industrial control systems security) and ISA/IEC 62443 (secure design and operation for industrial automation) as the relevant standards frameworks. The US Coast Guard's 2025 Maritime Security Directive requires certified secure PLCs and network segmentation on new dredges and port equipment (Florez 2025, p. 10). Operators at Tier 1 ports must demonstrate manual operations capability for at least five days without network access (Florez 2025, p. 11).

The audit deficit is the immediate problem. Standards exist. Inspection capacity and enforcement priority to apply them at scale do not.

---

## Cost curves

Three cost bands define the economics of dredged production.

For trailing suction hopper dredging, the contractor cost range is $3 to $8 per cubic meter (equivalently, approximately $2.30 to $6.10 per cubic yard) in competitive international markets. This range holds for straightforward sand-in-sand extraction at moderate distances. The upper end reflects hard material, long transit cycles, or thin-layer placement requirements.

For cutter suction dredging, the range is $5 to $15 per cubic meter. CSD is used for consolidated material, longer pump ranges, or confined waterways where a TSHD cannot maneuver. Chinese CSD pricing in the Spratly campaign is not publicly documented; the Tian Jing Hao's 4,500 m³/hr rated output and 6 km pump range suggests production at the lower end of the CSD band for carbonate substrate at shallow depth.

US-market dredging runs above these ranges. Florez (2025, p. 12) puts the domestic baseline at $5 to $10 per cubic yard ($6.50 to $13 per cubic meter) for basic work, with specialty and deepening above $20 per cubic yard ($26 per cubic meter). Miami Beach nourishment has run $30 to $50 per cubic yard cumulatively, reflecting small project scale, nearshore site complexity, and environmental constraints on vessel access season.

The cost-duration relationship from Florez (2025, p. 12, Fig. 6) matters more than the point estimates. Projects that complete in one year cost approximately $5.50 per cubic yard with a benefit-cost ratio of roughly 2.2. Projects that run to five years cost approximately $8.50 per cubic yard with a BCR of roughly 1.4. NEPA timelines alone can push projects from the first regime into the second before a dredge enters the water. This is why the Florez (2025, p. 13) assertion that "federal navigation projects typically require five to ten years from feasibility to groundbreaking" is not merely a scheduling inconvenience; it is a direct cost multiplier on every cubic yard of material moved.

---

## Demand against capacity

Florez (2025, p. 5) projects total annual dredging and reclamation demand rising from approximately 175 million cubic yards per year in 2025 to approximately 400 million cubic yards per year by 2045, roughly a 50% increase over twenty years. The demand decomposition includes port deepening starting at approximately 60 million cubic yards per year and growing to about 100 million by 2045, military base improvements growing from 50 to roughly 70 million cubic yards, and beach and wetland nourishment carrying the remainder.

Beneficial reuse is part of both the supply and demand picture. USACE currently dredges approximately 210 million cubic yards annually. Of this, roughly 45% goes to offshore disposal, 20% to upland disposal, and 35% to beneficial use (beach nourishment, marsh restoration, and land reclamation combined) (Florez 2025, p. 9). The USACE target is 70% beneficial reuse by 2030 (Florez 2025, pp. 3, 8). If achieved, this would redirect approximately 73 million additional cubic yards per year from disposal to productive use, effectively increasing the productive output of the same dredging activity.

Meeting the 2045 demand scenario with the current fleet would require adding roughly 1.4 units of annual throughput for every unit currently operating, while simultaneously aging out a significant fraction of existing vessels. At European production rates, achievable through fleet modernization and scale, this is a financing and contracting problem. At current US rates, with two-times-longer project durations and three-to-four-times-longer permitting timelines, it is not achievable without structural reform.

Florez (2025, p. 15) identifies four additional large hopper dredges and two additional cutter-suction dredges as the immediate gap for responding to a Gulf Coast megastorm scenario. That specific shortage is the floor; the longer-horizon demand growth requires fleet expansion an order of magnitude larger.

---

## What closes the gap

The Florez (2025) policy package sequences actions across three windows.

Near term (zero to two years): a National Sediment Management Strategy coordinated by USACE and NOAA to map offshore sand and establish sediment management districts; statutory authority for multi-year outcome-based contracts and availability payments; allied surge agreements with the Netherlands, Belgium, Japan, and Korea allowing foreign dredges to work under emergency conditions subject to CFIUS review (Florez 2025, p. 17). The allied surge agreements matter most as an immediate capacity backstop. They acknowledge that the US cannot build its way out of a post-storm emergency with domestic capacity alone.

Mid term (three to five years): fleet recapitalization through USACE hopper-dredge replacement and tax-credit or accelerated-depreciation incentives for US-built dredges; completion of the national offshore sand inventory; cybersecurity baseline codifying minimum requirements aligned to NIST and ISA/IEC standards, with a Maritime Cybersecurity Center of Excellence (Florez 2025, p. 17).

Long term (six to ten years): workforce pipelines through apprenticeship and a national maritime construction cadet program; nature-based R&D on autonomous dredging and AI-enabled sediment management; structured allied capacity sharing through joint ventures for large dredge co-development (Florez 2025, p. 17).

The sequencing reflects a specific logic. Institutional and contractual reform (year zero to two) costs little and removes the uncertainty that suppresses private capital formation. Financing incentives (year three to five) then work against a more predictable demand and regulatory environment. Autonomous systems and workforce programs (year six to ten) produce returns only if the preceding layers have been built. None of the individual actions are novel in policy terms; most have been used in other capital-intensive industries. The constraint has been treating dredging as a commodity procurement problem rather than a strategic industrial policy.

The consequence of inaction is not an abstract capacity shortfall. It is a concrete recovery time problem. Florez (2025, p. 15, Fig. 9) estimates that a Category 4 Gulf Coast hurricane requires removing 20 to 30 million cubic yards of sediment within four weeks to restore port operations. With current fleet capacity and organization, mean time to reopen is approximately 30 days. With expanded capacity and pre-positioned resources, it falls to approximately 10 days. The difference is the difference between a supply disruption and a supply chain restructuring.

---

The industrial base problem is not that the technology does not exist. Every technique the European big four use is understood, documented, and operable by US contractors and engineers. The problem is that the US fleet is too small, too old, and too expensive per cubic yard to meet demand that is already growing, in a regulatory environment that doubles project duration and therefore doubles the cost pressure on a fleet that cannot scale fast enough to compensate.

That is the gap. Closing it requires sustained capital commitment, procurement reform, and acceptance that dredging capacity is infrastructure policy, not just waterway maintenance.
