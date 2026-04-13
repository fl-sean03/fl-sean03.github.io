---
title: "Tessure"
description: "Sovereign defense perimeter for fixed critical infrastructure"
date: 2026-03-01
link: "https://v0-tessure.vercel.app"
---

Fixed infrastructure sites (datacenters, power substations, pipelines, fuel depots) are soft. Physical security is a mix of fences, cameras, and a guard who may or may not be watching the monitor. Detection is a 2010-era problem solved with 2010-era tools: video-only systems that misfire on shadows, wildlife, and glare, leaving response teams chasing false alarms until the real event gets missed.

**The thesis:** Build a baby Anduril, scoped to fixed sites. Fuse video, thermal, and radar at the edge. Keep the fusion local so raw feeds never leave the device. Ship only verified events to response. The operator stops being a classifier and starts being an actuator.

The original concept was built a while back as a general security play. It was parked because the thesis was right but the timing felt early.

**What changed:** Datacenters and power facilities are now actively being targeted. Copper theft at substations, drone incursions at chip fabs, physical attacks on grid infrastructure. The set of sites that need autonomous, verified perimeter security is expanding faster than the incumbent industry can respond. The timing window that felt early in the original sketch is now open.

**What was built:** Landing page at [v0-tessure.vercel.app](https://v0-tessure.vercel.app), positioning, sensor fusion architecture sketch, deployment scenarios across environments and threat profiles. Source on GitHub at [fl-sean03/tessure](https://github.com/fl-sean03/tessure).

**Why it's still here:** I haven't picked it back up. If you're building in physical security or sovereign defense for critical infrastructure, the thesis is free to take.
