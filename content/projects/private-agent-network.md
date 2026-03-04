---
title: "Seed Fleet"
description: "A self-managing network of autonomous AI agents on dedicated infrastructure"
date: 2026-03-01
---

Personal infrastructure for running concurrent projects without the coordination cost. Seven Claude-powered agents on dedicated ARM servers in Nuremberg, each with persistent memory, its own identity, and a specific domain of work. No containers, no orchestrator, no central controller. Each agent is a dedicated machine with its own filesystem, its own context, and an inbox.

Compute runs about $35/month across seven Hetzner ARM VMs. The LLM runtime is separate and the larger cost: currently a Claude Code subscription shared across the fleet, though the architecture is model-agnostic. Any provider works. Pay-per-token services like OpenRouter, locally hosted models on owned hardware, or a flat-rate subscription. The agents don't care where the intelligence comes from as long as they can call it.

**How it works:**
- Seven dedicated Hetzner ARM VMs ($4-7/month each), persistent and always available
- Inbox-driven execution: file arrives in inbox, inotify triggers systemd, agent wakes, processes work, exits
- Stateless cycles: each invocation starts fresh from disk, no long-running processes, no accumulated state bugs
- Encrypted inter-agent messaging via a DM API on the private network
- File-first memory: agents read and write Markdown, accumulate context over weeks and months
- Self-scheduling: agents manage their own crontabs, dropping trigger files into their own inboxes
- Self-modifying: agents can rewrite their own prompts, adjust their own capabilities, evolve their own workflows

**Fleet Ops** is the deployment authority. It holds the Hetzner API token, provisions new agents from scratch in fifteen minutes, and deploys infrastructure updates across every server. Pulls from the shared code repo every two hours, runs a three-level test suite, and rolls out changes fleet-wide. First responder when something breaks.

&nbsp;

**Platform Seed** develops everything the other agents run on. It owns the fleet-infra repo: the agent wrapper, the inbox execution model, the messaging API, the test framework, the deployment tooling. Designs new capabilities, builds them, hands them to Fleet Ops for deployment.

&nbsp;

**Research Lab** is the quality gate. It reviews every infrastructure change before it ships, runs controlled experiments on agent architecture, validates fleet health, and tracks external developments in models and tooling. Nothing gets deployed fleet-wide without its sign-off.

&nbsp;

**Lab Agent** handles computational materials research. Literature extraction, simulation configuration, result validation against published benchmarks. Delegates complex work to dedicated project agents. Completed a seven-phase, publication-ready research workflow autonomously. [More on the Heinz Lab Agent](/projects/heinz-lab-agent/)

&nbsp;

**OpSpawn** is a software development studio. Builds products end-to-end with its own sub-agent loops for parallel development. About 48 build cycles per day. Handles its own project management, testing, and deployment. [More on OpSpawn](/projects/opspawn/)

&nbsp;

**LabLink** runs nonprofit operations. Manages web properties, content, outreach, and organizational coordination for a nonprofit connecting labs with shared infrastructure. Multiple live sites and a Slack presence for community engagement. [More on LabLink](/projects/lablink/)

&nbsp;

**Growth Agent** manages strategy and market research. Content production, affiliate programs, and public web properties. Maintains a live site with original analysis. Handles the outward-facing work that system agents don't touch.

The fleet manages its own code. Platform Seed develops changes. Fleet Ops pulls, tests, and deploys. When a bug surfaces anywhere in the network, the system agents can discover it, develop a patch, test it, and roll it out fleet-wide. This full cycle, from detection through deployment, has completed without any human involvement. The agents found the bug, wrote the fix, verified it, and shipped it to every server in under four hours.

The broader argument for why this kind of infrastructure matters is in [Private Agent Networks](/writings/private-agent-networks/). See the fleet running live at [fleet.seanflorez.com](https://fleet.seanflorez.com). Running since January 2026 across seven seeds in Nuremberg.
