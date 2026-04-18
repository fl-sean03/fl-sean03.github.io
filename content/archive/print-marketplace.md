---
title: "Print Marketplace"
description: "Quote engine, maker network, fulfillment, and trust layer for distributed 3D printing"
date: 2026-04-05
---

Custom 3D printing sits between two bad options. Centralized services like Xometry and Protolabs price for enterprise aerospace and kill turnaround. Hobbyist DMs on Reddit or Discord are cheaper and faster but with no payment rails, no quality bar, no recourse. Everyone in the middle — small brands, prop makers, product designers needing a handful of parts — is stuck picking between slow-and-expensive or fast-and-sketchy.

**The thesis:** The wedge is a two-sided marketplace with an instant quote engine, a vetted maker network matched down to specific machines, handled payments and shipping, and a trust layer that becomes the actual moat. Faster and cheaper than the centralized services, cleaner than the hobbyist DMs. Phase 1 narrows aggressively: FDM only, U.S. only, small parcels only, manual maker acceptance, ranked instant quotes instead of auctions.

**What was built:** Pre-development spec and planning only. Full product spec, data model, API contracts, user flows, architecture, MVP scope, competitive analysis across MakeXYZ / Treatstock / Xometry / Protolabs, plus design notes on the quote algorithm, trust/rating/dispute system, OctoPrint agent integration, and CuraEngine AGPL licensing. A full design system was drafted. No code was written.

**Why it's parked:** The unit economics need a captive maker fleet to work at launch, and I wasn't in a position to acquire one. The planning stack is solid; someone with a distribution edge or an existing maker network could pick this up and move.
