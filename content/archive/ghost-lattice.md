---
title: "Ghost Lattice"
description: "Mission digital twin for heterogeneous drone swarms under DDIL conditions"
date: 2025-12-01
---

Defense drone programs evaluate swarms on clean test ranges. Real missions happen in degraded, denied, intermittent, and limited (DDIL) conditions where GPS dies, comms partition, nodes get jammed or shot down, and the swarm has to reassign roles mid-flight without an operator in the loop.

**The thesis:** You can't evaluate swarm autonomy without a simulator that punishes it. Ghost Lattice runs a six-drone mixed-vendor swarm through an adaptive ISR scenario with active jamming, forced node loss, GPS degradation, and decentralized role reallocation — then replays the mission with synchronized 3D, network, and operator views, and scores it against a single-agent baseline.

**What was built:** ROS2 simulation stack, replay UI, scoring pipeline, documented mission scenario.

**Why it's parked:** Defense procurement cycles are long and I'm a materials PhD, not a defense founder. The sim stands on its own as a research artifact and a demo of what honest swarm evaluation looks like.
