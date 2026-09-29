---
title: "OpenSDL"
description: "Open-source software for self-driving labs, still an alpha that runs only in simulation."
date: 2026-09-28
status: "Active"
period: "2026–present"
role: "Creator and maintainer"
thread: "loop"
links:
  - label: "Repository"
    url: "https://github.com/fl-sean03/OpenSDL"
  - label: "Documentation"
    url: "https://seanflorez.com/OpenSDL/"
  - label: "Replay a run"
    url: "https://seanflorez.com/OpenSDL/viewer/"
  - label: "X"
    url: "https://x.com/seanf1orez"
image: "/images/opensdl/reference-cell.jpg"
image_alt: "A rendered model of OpenSDL's reference laboratory cell, a T-slot frame with a gantry over a bench of instruments and plate magazines. A simulation, not a photograph."
weight: 1
---

How fast a lab learns depends on how fast it gets from one result to the next experiment. Iteration rate beats brilliance. The person who tests ten hypotheses learns more than the person who tests one.

OpenSDL is open-source software for self-driving labs. You declare what a laboratory can do, and OpenSDL turns those declarations into reproducible workflows. It keeps the evidence from every run and uses each result to choose the next experiment. For now it is an alpha, and it does all of this only in simulation.

- A capability is a named operation, and a person, an instrument, a robot, a simulator or an optimizer can perform it. A workflow names the capability and an adapter handles the details.
- The runtime is durable. It executes workflows as a graph with retries, timeouts, resource leases and policy checks, reconciles state after a restart, and keeps metadata in SQLite and artifacts in content-addressed storage.
- The reference profile ships simulated adapters for a mixer, a balance, a colorimeter and labware transport, plus local compute, a record for tasks a person does, and two optimizers, a fixed grid and a contracting search.
- It comes with a CLI, a Python SDK, an HTTP API and an optional MCP hook. Runs export as a portable archive, and a read-only viewer replays a recorded run inside a rendered model of the lab, the reference cell pictured on this page.
- The repository holds fourteen library packages, with applications, adapters and domain packs alongside. CI runs the tests on Python 3.12, 3.13 and 3.14, and the docs are rebuilt from main on every push.

![A frame from the discovering-colors run. On the left, a 96-well plate seen from directly above, every well a different mixed color. On the right, the target color beside the closest well so far, 14.0 apart in RGB after round 2 of 6, and a plot of the search space with the sampling region contracted to 0.62.](/images/opensdl/discovering-colors.jpg)

*A frame generated from the recorded run, after round two of six. Ninety-six recipes on one plate, each well colored by what its own run measured, beside the search that proposed them.*

In the discovering-colors example, the lab is handed one color and has to find the three-dye recipe that makes it, with no idea how the dyes behave. Each round fills a 96-well plate, reads every well on a simulated colorimeter, and draws the next round from a region that has contracted around whatever came closest. After six rounds and 576 wells it recovered cyan 0.4612, magenta 0.0858 and yellow 0.2989. The target was mixed from 0.46, 0.09 and 0.30, and the search never saw those numbers. The median well started 95 RGB units from the target and ended 12.6 away, and the best well of the last round was 0.5 away.

The reference profile is simulator-only, and no adapter has been connected to physical equipment. The HTTP API has no authentication. It's an executable alpha, not production-qualified laboratory control software, and nothing is tagged or published to a package index. A CI job re-runs the example and checks it against the committed record. Its README puts production authentication, richer approval workflows, Slurm execution and a first low-risk hardware integration among the current work.

To try it, you need Python 3.12 or newer and uv. The example takes about 80 seconds and runs on those two alone, with no hardware or accounts.

```bash
git clone https://github.com/fl-sean03/OpenSDL.git opensdl && cd opensdl
uv sync --locked --all-packages --group dev
uv run --locked python examples/discovering-colors/run_campaign.py
```

Results should compound, and too often they don't, because connecting one to the next is manual. I'm building OpenSDL to keep that connection in the record, next to the result.
