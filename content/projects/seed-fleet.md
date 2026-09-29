---
title: "Seed Fleet"
description: "A self-managing network of autonomous AI agents on dedicated infrastructure"
date: 2026-03-01
status: "Past"
period: "Jan–Mar 2026"
role: "Creator"
image: "/images/projects/seed-fleet.png"
image_alt: 'Screenshot of the Seed Fleet dashboard, titled Command Center, showing the tagline "7 autonomous agents. $35/mo hosting. Model layer pluggable." above four counter tiles for agents, cycles, messages and days online.'
aliases:
  - /projects/private-agent-network/
---

The fleet ran from January to March 2026 and has been retired. The [agent-fleet](https://github.com/fl-sean03/agent-fleet) harness I run now is a different system, with its agents on one machine instead of seven servers.

Personal infrastructure for running concurrent projects without the coordination cost. Seven Claude-powered agents ran on dedicated ARM servers in Nuremberg, each with persistent memory, its own identity, and a specific domain of work. No containers, no orchestrator, no central controller. Each agent was a dedicated machine with its own filesystem, its own context, and an inbox.

Compute ran about $35/month across seven Hetzner ARM VMs. The LLM runtime was separate and the larger cost. It ran on a Claude Code subscription shared across the fleet, though the architecture was model-agnostic. Any provider would work. Pay-per-token services like OpenRouter, locally hosted models on owned hardware, or a flat-rate subscription. The agents didn't care where the intelligence came from as long as they could call it.

Each agent ran on its own dedicated Hetzner ARM VM at $4-7 a month, persistent and always available. Execution was inbox-driven. A file arrived in the inbox, inotify triggered systemd, and the agent woke, processed the work, and exited. Cycles were stateless, so each invocation started fresh from disk, with no long-running processes and no accumulated state bugs.

Agents exchanged encrypted messages through a DM API on the private network. Memory was file-first. Agents read and wrote Markdown and accumulated context over weeks and months. They managed their own crontabs, dropping trigger files into their own inboxes, and they could rewrite their own prompts, adjust their own capabilities, and evolve their own workflows.

&nbsp;

**Fleet Ops** was the deployment authority. It held the Hetzner API token, provisioned new agents from scratch in fifteen minutes, and deployed infrastructure updates across every server. Pulled from the shared code repo every two hours, ran a three-level test suite, and rolled out changes fleet-wide. First responder when something broke.

&nbsp;

**Platform Seed** developed everything the other agents ran on. It owned the fleet-infra repo, which held the agent wrapper, the inbox execution model, the messaging API, the test framework, and the deployment tooling. Designed new capabilities, built them, handed them to Fleet Ops for deployment.

&nbsp;

**Research Lab** was the quality gate. It reviewed every infrastructure change before it shipped, ran controlled experiments on agent architecture, validated fleet health, and tracked external developments in models and tooling. Nothing got deployed fleet-wide without its sign-off.

&nbsp;

**Lab Agent** handled computational materials research. Literature extraction, simulation configuration, result validation against published benchmarks. Delegated complex work to dedicated project agents. Completed a seven-phase, publication-ready research workflow autonomously. [More on the Heinz Lab Agent](/projects/heinz-lab-agent/)

&nbsp;

**OpSpawn** was a software development studio. Built products end-to-end with its own sub-agent loops for parallel development. About 48 build cycles per day. Handled its own project management, testing, and deployment. [More on OpSpawn](/archive/opspawn/)

&nbsp;

**LabLink** ran nonprofit operations. Managed web properties, content, outreach, and organizational coordination for a nonprofit connecting labs with shared infrastructure. Multiple live sites and a Slack presence for community engagement. [More on LabLink](/projects/lablink/)

&nbsp;

**Growth Agent** managed strategy and market research. Content production, affiliate programs, and public web properties. Maintained a live site with original analysis. Handled the outward-facing work that system agents didn't touch.

The fleet managed its own code. Platform Seed developed changes. Fleet Ops pulled, tested, and deployed. When a bug surfaced anywhere in the network, the system agents could discover it, develop a patch, test it, and roll it out fleet-wide. This full cycle, from detection through deployment, completed without any human involvement. The agents found the bug, wrote the fix, verified it, and shipped it to every server in under four hours.

The broader argument for why this kind of infrastructure matters is in [Private Agent Networks](/writings/private-agent-networks/).
