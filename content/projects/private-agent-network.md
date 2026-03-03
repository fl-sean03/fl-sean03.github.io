---
title: "Seed Fleet"
description: "A self-managing network of autonomous AI agents on dedicated infrastructure"
date: 2026-03-01
---

Personal infrastructure for running concurrent projects without the coordination cost. Seven Claude-powered agents on dedicated ARM servers in Nuremberg, each with persistent memory, its own identity, and a specific domain of work. The whole fleet runs for about $35/month in compute. No containers, no orchestrator, no central controller. Each agent is a dedicated machine with its own filesystem, its own context, and an inbox.

Three system agents maintain the network. Fleet Ops handles deployment, provisioning, and operations across all servers. Platform Seed develops the shared infrastructure: the agent wrapper, the messaging system, the test framework, the deployment tooling. Research Lab reviews changes, runs experiments on agent architecture, and validates fleet health. These three agents coordinate to keep the network running without human involvement.

Four venture agents do domain work. Lab Agent runs computational research pipelines. OpSpawn builds software products. LabLink handles nonprofit operations. Growth Agent manages outward-facing strategy, content, and market research. Each venture agent focuses entirely on its domain because the system agents handle everything underneath.

**How it works:**
- Seven dedicated Hetzner ARM VMs ($4-7/month each), persistent and always available
- Inbox-driven execution: file arrives in inbox, inotify triggers systemd, agent wakes, processes work, exits
- Stateless cycles: each invocation starts fresh from disk, no long-running processes, no accumulated state bugs
- Encrypted inter-agent messaging via a DM API on the private network
- File-first memory: agents read and write Markdown, accumulate context over weeks and months
- Self-scheduling: agents manage their own crontabs, dropping trigger files into their own inboxes
- Self-modifying: agents can rewrite their own prompts, adjust their own capabilities, evolve their own workflows

The fleet manages its own code. Platform Seed develops changes in a shared infrastructure repo. Fleet Ops pulls updates, runs a three-level test suite (unit, single-seed health, cross-fleet consistency), and deploys across all agents. When a bug surfaces anywhere in the network, the system agents can discover it, develop a patch, test it, and roll it out fleet-wide. This full cycle, from detection through deployment, has completed without any human involvement. The agents found the bug, wrote the fix, verified it, and shipped it to every server in under four hours.

New agents can be provisioned autonomously. Fleet Ops holds a Hetzner API token and a provisioning script. It can create a new VM, install the base seed template, configure networking, register the agent with the fleet, and bring it online. The process takes about fifteen minutes.

The broader argument for why this kind of infrastructure matters is in [Private Agent Networks](/writings/private-agent-networks/). Running since January 2026 across seven seeds in Nuremberg.
