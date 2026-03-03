---
title: "Seed Fleet"
description: "A self-managing network of autonomous AI agents on dedicated infrastructure"
date: 2026-03-01
---

Personal infrastructure for running concurrent projects without the coordination cost. Seven Claude-powered agents on dedicated ARM servers, each with persistent memory, its own identity, and a specific domain of work. Three system agents maintain the network itself: one handles deployment and operations, one does engineering and testing, one runs research and review. Four venture agents do domain work: computational research, a dev studio, nonprofit operations, and market strategy.

The whole network runs for about $35/month in compute. Each agent is a dedicated machine, not a container or a function. They accumulate context over time, remember what they've worked on, and build on previous results. No shared state, no central controller. Just agents with inboxes.

**How it works:**
- Seven agents on dedicated Hetzner ARM VMs ($4-7/month each)
- Inbox-driven execution via inotify + systemd
- Encrypted inter-agent messaging for coordination without human relay
- System agents (infrastructure, engineering, research) maintain the network
- Venture agents (lab, dev studio, nonprofit, growth) do domain work
- Self-modifying: agents control their own schedules, evolve their own capabilities

The system agents deploy code, run tests, monitor health, and fix issues autonomously. When a bug surfaces, the network can discover it, develop a patch, test it, and deploy the fix across all agents without intervention. The full cycle from detection to fleet-wide deployment has happened without any human involvement.

The broader argument for why this kind of infrastructure matters is in [Private Agent Networks](/writings/private-agent-networks/). Running since January 2026 across seven seeds in Nuremberg.
