---
title: "Ghost Lattice"
description: "Mission digital twin for heterogeneous drone swarms under DDIL conditions"
date: 2025-12-01
link: "https://github.com/fl-sean03/ghost-lattice"
---

Defense drone programs evaluate swarms on clean test ranges. Real missions happen in degraded, denied, intermittent, and limited (DDIL) conditions where GPS dies, comms partition, nodes get jammed or shot down, and the swarm has to reassign roles mid-flight without an operator in the loop.

**The thesis:** You can't evaluate swarm autonomy without a simulator that punishes it. Ghost Lattice runs a six-drone mixed-vendor swarm through an adaptive ISR scenario with active jamming, forced node loss, GPS degradation, and decentralized role reallocation, then replays the mission with synchronized 3D, network, and operator views, and scores it against a single-agent baseline.

**What was built:** ROS 2 simulation stack, PX4 + Gazebo backbone, DDIL engine, scoring pipeline, and a Next.js replay UI with a tactical map and sandbox mode. Source at [github.com/fl-sean03/ghost-lattice](https://github.com/fl-sean03/ghost-lattice).

**Why it's parked:** Defense procurement is a slow game and I'm not currently running it. The simulator stands on its own as a research artifact and a demo of what honest swarm evaluation looks like. Fork it if you're building in this space.
