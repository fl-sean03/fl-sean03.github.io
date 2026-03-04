---
title: "Heinz Lab Agent"
description: "Turning a computational materials science group into an agent-native research lab"
date: 2026-02-20
---

A research agent in my PI's computational materials science group completed a seven-phase workflow autonomously. It formulated a hypothesis, pulled parameters from the literature, configured and ran simulations, validated results against published benchmarks, analyzed the data, and produced a formatted manuscript. Full logging at every step. No human in the loop until the final review.

That was the proof of concept. What's being built now is the infrastructure around it.

The agent runs on the [Seed Fleet](/projects/private-agent-network/) and inherits its scientific capabilities from the [Agentic Science Worker](/projects/agentic-science-worker/) toolkit. It sits in the lab's Slack, answers questions, summarizes results, monitors HPC jobs, and scans the literature weekly for papers relevant to the group's research. But the interesting part isn't what the agent does alone. It's what happens when it starts delegating.

The agent spawns dedicated project agents for complex, long-running work. One built a production molecular visualization tool over 72 hours of continuous autonomous development. Others are scoped for MLIP validation (automated "can I trust this potential?" testing against DFT and experiment), trajectory analysis (turning days of manual post-processing into minutes), and experimental data pipelines that connect computational predictions back to XRD, DSC, and other lab measurements. The agent coordinates all of them: assigning work, tracking progress, recovering when something fails.

The roadmap goes further. Autonomous materials screening campaigns that evaluate hundreds of candidate structures against target properties. Active learning loops that propose new configurations, run DFT, retrain interatomic potentials, and iterate. A lab data warehouse where every simulation the group has ever run is indexed and searchable, so no one reruns what's already been done.

What compounds isn't the automation. It's the knowledge. The agent remembers which parameters work for which systems, which approaches failed and why, which papers matter for which questions. That context doesn't leave when a senior student graduates. A new student inherits it on day one, structured, searchable, connected to the tools where the work happens.

Another lab saw the Slack integration and asked for their own. The pattern is general: a persistent agent with domain knowledge, plugged into the tools a specific group actually uses. The scientific engine comes from the Agentic Science Worker repo. The runtime comes from the Seed Fleet. What makes each deployment useful is the domain context it accumulates over time.

The trajectory is from a traditional computational group to an agent-native one. Not a lab that uses AI tools, but a lab where the infrastructure itself reasons about the research, and gets better the longer it runs.
