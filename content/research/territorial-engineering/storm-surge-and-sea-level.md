---
title: "Designing for Water That Will Arrive"
description: "Coastal design as a moving envelope of tides, storms, waves, rainfall, sea-level change, settlement, and observed performance, not one permanent elevation."
date: 2026-04-21
image: /images/research/territorial-engineering/storm-surge-and-sea-level.png
image_alt: "Night satellite view of a hurricane with a clear eye, moving toward a coastline lit by city lights."
---

The crest elevation is fixed on the drawing. Neither side of the measurement is fixed in the field.

Water levels shift with tide, weather, waves, and long-term sea-level change. Reclaimed ground settles under its own weight and the weight of what is built on it. Regional land motion changes the reference surface beneath both. A benchmark can remain perfectly intact while the protection it controls loses clearance year by year.

The design problem is not to find the correct water level and add freeboard. It is to define the combinations of water, waves, rainfall, erosion, and ground movement that matter to the site, then preserve acceptable performance as those conditions change.

---

## Start with one vertical language

Every elevation in the project has to refer to a stated datum and survey control network. Tide levels, topographic surveys, geotechnical settlement plates, wave-model output, drainage inverts, floor elevations, and barrier crests are otherwise easy to compare incorrectly.

The distinction between still-water level and wave effects is equally important. Astronomical tide provides a moving baseline. Wind and pressure can raise that baseline through storm surge. Waves can add setup near shore and drive run-up on a slope or structure. Rain can accumulate behind a perimeter when the receiving water is too high for gravity drainage. Long-term relative sea-level change and land subsidence shift the starting point before the next storm begins.

These components interact, but they should not be added twice. The Stockdon formulation for the 2 percent exceedance run-up level, R2%, was developed as a combined estimate of wave setup and swash above the still-water level. The [original USGS publication](https://www.usgs.gov/publications/empirical-parameterization-setup-swash-and-runup) separates the processes in its derivation and combines them in the run-up statistic. A calculation that adds an independent setup estimate and then adds R2% again counts setup twice.

The same discipline applies across models. If a nearshore wave model already transforms offshore waves and reports setup at the structure, the handoff to a run-up or overtopping calculation must state what is included. Labels such as "surge," "total water level," and "run-up" are not interchangeable.

## The event is a combination, not a column of maxima

A coastal load case is a sequence in time.

The peak astronomical tide may not coincide with the peak surge. The largest offshore waves may arrive before or after the highest still-water level. Wind direction controls both wave attack and local setup. A long storm can saturate the ground and fill interior storage even if its peak surge is lower than that of a shorter event. A closed tide gate can stop saltwater inflow while also blocking rainfall outflow.

Adding the independent maximum of every component produces a number, but not necessarily a physically coherent event. Designing only to the most likely coincidence can miss a damaging but less intuitive sequence. The right method is to define joint load cases and test the system response through each one.

For an exposed reclamation perimeter, those cases usually include ordinary high-water operation, wave attack at elevated water, overtopping into the drainage system, erosion or scour at the toe, and the consequences of a local breach. For a polder, pump capacity, storage, gate operation, and backup power become part of the coastal load case. For an open waterfront, controlled flooding of low-value space may be acceptable while access roads, utilities, and occupied buildings remain above specified thresholds.

The consequence of failure decides how far the analysis must go. A park edge can recover from erosion. A navigation wall, tunnel portal, fuel terminal, hospital access route, or occupied district with no safe evacuation path carries a different requirement.

## Annual probability is not lifetime probability

Return period language creates false distance from risk. A "100-year" event is not scheduled once per century. It is shorthand for a 1 percent annual-exceedance probability under the assumptions used to estimate the event.

The probability of at least one exceedance over \(n\) years is:

\[
P = 1 - (1-p)^n
\]

where \(p\) is the annual-exceedance probability. For a 1 percent annual event over 25 years:

\[
1 - 0.99^{25} = 0.222
\]

The cumulative probability is about 22.2 percent. It is not 25 percent, and it is not evidence that an exceedance will occur exactly once. The [USGS explanation of the 100-year flood](https://www.usgs.gov/water-science-school/science/100-year-flood) also stresses that two nominally rare floods can occur in consecutive years.

This calculation assumes an annual probability that is stable and independent from year to year. Coastal design over decades cannot take that stability for granted. Sea-level change can increase the frequency with which a fixed threshold is crossed. Shoreline change can alter wave transformation. New bathymetry, inlet geometry, or nearby structures can change local response. The probability label belongs to a model and a period of conditions, not to the concrete itself.

## Sea level is a scenario input

No single projection should be promoted into a universal finished-grade rule.

The [2022 federal sea-level report](https://earth.gov/sealevel/us/resources/2022-sea-level-rise-technical-report/) provides scenarios for relative sea-level change along the United States coast and emphasizes that location matters. Ocean change, vertical land motion, and regional processes produce different relative outcomes from the same global trajectory. The scenarios also diverge more over longer design lives.

USACE policy follows the same logic. Its [regulation on incorporating sea-level change](https://www.publications.usace.army.mil/Portals/76/Publications/EngineerRegulations/ER_1100-2-8162.pdf) directs Civil Works studies to evaluate a range of relative sea-level-change scenarios rather than rely on one deterministic line. The design question is not which scenario is "the answer." It is which decisions fail under each plausible path, when they fail, and what can still be changed at that point.

This matters because different project elements have different lives. A buried outfall may be difficult to raise. A perimeter crest can sometimes be widened and lifted if space and foundation capacity were reserved. Electrical equipment can be relocated during renewal. A road network can tolerate occasional shallow flooding that an emergency route cannot.

Scenario analysis should therefore be element-specific. It should test the service life, consequence, replaceability, and lead time of each decision.

## The ground moves too

Relative sea-level change already includes regional vertical land motion at the measurement location. Reclaimed land adds a local process: consolidation and deformation of the fill and foundation.

Those processes should be tracked separately even though both reduce effective freeboard. Regional subsidence changes the whole district. Primary consolidation follows pore-pressure dissipation. Secondary compression can continue after primary consolidation. Differential settlement can be more damaging than uniform settlement because it distorts pavements, pipes, gates, rails, and building connections.

A design allowance is not a substitute for observation. Settlement plates, survey monuments, piezometers, and structural monitoring should establish how the site is actually moving. The forecast can then be updated before the remaining margin is consumed.

The crucial quantity is not settlement alone. It is the evolving difference between the protection level and the relevant water and wave thresholds. A crest that settles slowly may remain adequate if it began with recoverable margin and can be raised. A drainage outfall can lose function much earlier because a small change in tailwater eliminates gravity head.

## Elevation is one control among several

A resilient site is not a flat platform set to one number.

Finished grade, perimeter protection, drainage, critical-floor elevations, sacrificial shoreline width, access, utility placement, and future raising provisions divide the risk. Low areas can store or convey water. Buildings can sit above streets. A beach or dune can spend sediment during a storm while a landward structure limits the consequence of erosion. Pumps can protect a polder only if power, maintenance, discharge capacity, and interior storage remain available.

The design should state performance by condition:

- What remains fully operational during frequent high water?
- Where is wave overtopping allowed, and where is it not?
- How much erosion can occur before a road, wall, or buried utility is exposed?
- Which assets must remain dry during the selected rare event?
- What happens beyond that event?
- How will people leave or shelter if the perimeter is damaged?

Freeboard is then assigned against named uncertainties and consequences. It is not an unexplained remainder added after the hydraulic model.

## Build the trigger before the threshold

Adaptation is credible only when the project reserves the ability to act.

That can mean a wider dike foundation that can support a future lift, a wall designed for an added cap, space for a landward drainage channel, utility connections that tolerate regrading, or a monitoring system tied to funded inspections. It also means choosing trigger points before the data become politically inconvenient.

Useful triggers are observable. They include measured settlement rate, loss of crest elevation, increasing overtopping frequency, drainage outfalls that remain tide-locked for longer periods, beach or dune volume falling below a maintenance section, and sea-level observations departing from the path used in design. Each trigger needs an action, a lead time, an owner, and a funding route.

The fixed benchmark from the opening problem becomes safe only when it is part of that system. Its elevation is surveyed against stable control. The ground around it is monitored. The water-level assumptions are updated. The project knows how much margin remains and what happens when the trigger is crossed.

The next question is physical: how to build a perimeter, place the fill, improve the foundation, and hand over land whose remaining movement is understood rather than hidden.
