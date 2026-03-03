---
title: "Private Agent Network"
description: "A private network of autonomous AI agents running on dedicated infrastructure"
date: 2026-03-01
---

When you're building across multiple domains simultaneously, the bottleneck isn't ideas or strategy. It's the cumulative overhead of keeping everything moving. Coordination, monitoring, follow-through. Each task is manageable on its own, but together they determine how many efforts one person can actually sustain.

The Private Agent Network is a self-managing system of seven Claude-powered agents running on dedicated ARM servers. Each agent has persistent memory, its own identity, and a specific domain of work. It's not a product. It's personal infrastructure for running concurrent projects without the coordination cost.

**How it works:**
- Seven agents on dedicated Hetzner ARM VMs ($4-7/month each), persistent and always available
- Inbox-driven execution: agents wake only when work arrives, triggered by inotify and systemd
- Encrypted inter-agent messaging for coordination without human relay
- System agents (infrastructure, engineering, research) maintain the network itself
- Venture agents (lab research, dev studio, nonprofit ops) do domain-specific work on top
- Agents control their own schedules, modify their own code, and evolve their own capabilities

The system manages itself. One person runs concurrent efforts across computational research, software development, and nonprofit operations because the infrastructure handles the execution overhead. The system agents deploy code, run tests, monitor health, and fix issues autonomously. When a bug surfaces, the network can discover it, patch it, and deploy the fix across all agents without intervention.

The thesis is the same one applied to my own workflow. Overhead prevents good work from compounding. Remove it and what one person can sustain changes fundamentally.

Running since January 2026 across seven seeds in Nuremberg.
