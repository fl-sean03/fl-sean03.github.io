---
title: "Building the Autonomous Computational Materials Lab"
subtitle: "A step-by-step blueprint from someone who's doing it"
date: 2026-04-02
image: "/images/writings/superintelligent-lab.jpeg"
---

I've spent the last year building autonomous research infrastructure for a computational materials science lab at CU Boulder. Not theorizing about it. Building it. Running it. Watching it break and fixing what broke.

The [case for doing this](/writings/autonomous-science/) is straightforward: science moves at execution speed, not insight speed. The human overhead of running the research loop is the hidden throttle on discovery. Remove that overhead and you don't just move faster. You ask different questions. I wrote about the [general pattern](/writings/superintelligent-org/) — why this applies to any knowledge-heavy organization. This is the specific version. Exactly how to do it for a materials science lab, with the level of detail I wish I'd had when I started.

What follows is the blueprint, drawn entirely from what actually worked.

---

## Step 1: Make your tools agent-readable

Nothing else matters until this is done. And almost no one does it.

A simulation code like LAMMPS takes a plaintext input file and produces output that a human reads. That's fine for humans. It's terrible for an agent. The agent needs to know: what parameters are available, what are their valid ranges, what does the output schema look like, what does a failed run look like versus a successful one.

This means building structured interfaces around existing tools. Not replacing them. Wrapping them.

### What this looks like concretely

**For molecular dynamics (LAMMPS):**

The agent needs to go from a crystal structure to a running simulation without a human writing input files. That means:

- A CIF/POSCAR parser that extracts lattice parameters, atom positions, and symmetry information. I use ASE (Atomic Simulation Environment) for this — it handles most structure formats and does coordinate transformations correctly.
- An atom type classifier. Given a structure, which force field applies? Which atom types map to which elements in which bonding environments? For the Interface Force Field (IFF), a Ti atom in a MXene is not the same atom type as a Ti atom in rutile TiO2. The classifier needs to know the difference. This is domain knowledge that has to be encoded explicitly — the agent can't derive it from documentation.
- A force field parameter lookup. Given classified atom types, pull the correct Lennard-Jones parameters, partial charges, bond/angle/dihedral coefficients. The parameters live in published papers, supplementary materials, and lab-internal databases. Build a structured store. Don't make the agent re-extract from PDFs every time.
- An input file generator that assembles the pieces: simulation box dimensions (with appropriate vacuum for surfaces, replication for bulk), force field specification (`pair_style`, `pair_coeff`, `bond_coeff`, etc.), ensemble settings (NVT/NPT, thermostat parameters, barostat coupling), output controls (thermo frequency, dump frequency, which quantities to track). Every parameter should have a validated default with a documented rationale.
- An output parser that reads `log.lammps` and dump files. Extracts time series (temperature, pressure, energy, volume), per-atom quantities (positions, velocities, forces), and computed properties (RDF, MSD, stress tensor). Returns structured data, not text.

**For density functional theory (Quantum ESPRESSO):**

Same philosophy, different details:

- Pseudopotential selection. Given an element and a target accuracy level, which pseudopotential library? SSSP Efficiency for screening, SSSP Precision for publication-quality results. The agent needs a lookup table mapping elements to recommended pseudopotentials with tested cutoff energies. Don't let it guess cutoffs — converged values exist and using unconverged values wastes compute and produces wrong results.
- Input generation for `pw.x`: crystal structure, k-point grid (use the Monkhorst-Pack convention; density of ~0.03 A^-1 is a reasonable starting point for metals, ~0.04 for insulators), plane-wave cutoff (from the pseudopotential recommendation), smearing (Methfessel-Paxton for metals, none for insulators with a gap), convergence thresholds (`conv_thr` of 1e-8 Ry for energy, `forc_conv_thr` of 1e-4 Ry/Bohr for forces in relaxation).
- A convergence checker. Did the SCF converge? Did the forces converge for a relaxation? If not, what went wrong? Common failures: charge sloshing in metallic slabs (fix with mixing_beta reduction), insufficient k-points for small-gap systems, plane-wave cutoff too low for hard pseudopotentials. The agent should recognize each failure mode and know the standard fix.

**For literature extraction:**

The most underrated layer. Researchers spend enormous time finding parameters in papers.

- Semantic Scholar and arXiv APIs for discovery. Query by topic, author, citation graph.
- PDF parsing that extracts tables, figures, and structured data. Not just text. The force field parameters you need are in Table S3 of the supplementary materials, not in the abstract.
- A structured parameter store that maps: material system → property → value → source (DOI, table number, conditions). When the agent needs the lattice constant of Ti3C2Tx MXene with OH terminations, it checks the store before searching the literature. When it finds a value in a new paper, it adds it to the store with provenance.

### The temptation to skip this

The temptation is to let the AI figure it out from documentation. Claude can read a LAMMPS manual and write an input file. It will produce something that looks right and runs. Whether it produces physically meaningful results is a different question entirely.

An agent that picks `pair_style lj/cut` when it should use `pair_style hybrid/overlay` for a system with both van der Waals and Coulombic interactions will get results. They'll be wrong. An agent that uses the default thermostat coupling constant for a system where the dynamics are sensitive to thermostat artifacts will produce smooth, converged, meaningless trajectories.

The structured interface encodes domain knowledge — valid parameter ranges, sensible defaults, known failure modes — so the agent operates within the space of reasonable science rather than the space of syntactically valid input files.

Build this layer first. Everything downstream depends on it.

---

## Step 2: Close the execution loop

Once your tools have machine-readable interfaces, you can close the loop: literature extraction, parameter selection, simulation setup, job submission, result parsing, validation, and the decision about what to run next.

I built this as the [Agentic Science Worker](https://github.com/fl-sean03/agentic-science-worker). It runs on Claude Code and handles the full computational materials science loop autonomously. Given a scientific question, it researches the methodology, finds parameters, runs simulations, verifies results against literature, and iterates until achieving physically reasonable results.

### The validation layer

This is where most attempts at autonomous science fail, and it's non-negotiable.

The system checks every result against published values. Specifically:

- **Lattice constants**: compared against Materials Project and experimental values. Tolerance of 1-2% for DFT (depends on functional), 2-3% for classical MD with good force fields. Anything outside that range triggers a review. The agent should know that GGA functionals systematically overestimate lattice constants by ~1% and that this is expected, not an error.
- **Elastic constants**: compared against published experimental and computational values. Bulk modulus within 10% of experimental is typical for DFT; larger deviations flag a problem. Classical MD elastic constants depend heavily on force field quality — the agent should know which force fields are validated for mechanical properties and which aren't.
- **Surface energies**: compared against literature values for the same surface orientation and termination. Surface energy calculations are sensitive to slab thickness and vacuum size — the agent should run convergence tests (surface energy vs. number of layers) rather than trusting a single calculation.
- **Equation of state**: fit E(V) data to Birch-Murnaghan or Murnaghan equation. Equilibrium volume, bulk modulus, and pressure derivative should be physically reasonable and consistent with known values.
- **Trajectory stability**: for MD, check that energy drift is small (less than ~1 meV/atom/ps for NVE, stable fluctuations for NVT/NPT), that temperature and pressure maintain their targets, that no atoms have unphysical velocities or forces. A sudden energy spike means something is wrong — overlapping atoms, a missing interaction, a timestep that's too large.

The agent doesn't just compute these checks. It knows what they mean. A lattice constant that's 5% off suggests a wrong force field or a structural error. An energy spike at step 1 suggests overlapping atoms in the initial configuration. A gradual energy drift suggests a cutoff issue or a missing long-range correction. Each failure mode has a diagnostic tree, and the agent walks it.

### The benchmark framework

I built an 11-tier benchmark framework to evaluate the system:

1. **Tier 1**: Single-tool tasks. Can it query the Materials Project API? Can it parse a CIF file?
2. **Tier 2**: Two-tool chains. Can it get a structure from Materials Project and set up a LAMMPS input?
3. **Tier 3**: Literature extraction. Can it find force field parameters in a paper and extract them correctly?
4. **Tier 4**: Complete simulation setup. Structure → parameters → input file → validation of setup (before running).
5. **Tier 5**: Execution and basic analysis. Run the simulation, parse output, compute basic properties.
6. **Tier 6**: Result validation. Compare computed properties against literature values. Flag discrepancies.
7. **Tier 7**: Error recovery. Simulation fails — can it diagnose why and fix it?
8. **Tier 8**: Multi-step workflows. Equilibration → production → property calculation → reporting.
9. **Tier 9**: Multi-code workflows. Classical MD screening → DFT validation of interesting candidates.
10. **Tier 10**: ML interatomic potential workflows. Training data generation, model training, validation.
11. **Tier 11**: Frontier workflows. Hybrid ML+DFT active learning loops, autonomous screening campaigns.

42 of 58 benchmarks pass. The failures cluster at tiers 10-11, where workflows require judgment calls about model architecture, training set composition, and uncertainty thresholds that benefit from human direction. That's the right boundary. The system handles mechanical execution. The researcher handles judgment.

---

## Step 3: Give it memory that compounds

An agent that forgets everything between sessions is a tool. An agent that remembers is infrastructure.

### What the memory system actually contains

The lab agent maintains 37 knowledge files. Not a monolithic knowledge base — individual files organized by topic, each readable and editable by both the agent and humans:

- **People files**: who's in the lab, what they work on, their expertise, their current projects. When a new paper comes out on MXene intercalation, the agent knows which lab members to flag it for.
- **Project files**: active research threads, their status, key results, open questions. Links to simulation directories, relevant papers, and related projects.
- **System files**: specific materials the lab works with. For Ti3C2Tx MXenes: known crystal structures, validated force fields and their limitations, published properties at various hydration levels, ongoing questions about termination group effects. For (2-BrPEA)2PbI4 perovskites: IFF atom type classifications, parameterization history, known issues with organic cation flexibility.
- **Method files**: which simulation approaches work for which types of questions. "For interlayer shear strength: use the rigid-layer displacement method with ReaxFF, not IFF — IFF underestimates the barrier by ~40% for hydroxylated surfaces." This kind of knowledge typically lives in a senior student's head.
- **Lesson files**: what went wrong and why. "DFT relaxation of Ti3C2(OH)2 with PBE functional: converges to wrong ground state if initial termination geometry is symmetric. Start with broken symmetry." These are expensive lessons — each one represents days or weeks of someone's time. Capturing them means no one pays that cost again.
- **Infrastructure files**: how the agent's own systems work, credential locations, job submission procedures, storage layout. Self-documentation that enables disaster recovery.

### Why Markdown, not a database

The choice of structured Markdown over SQLite or a vector database was deliberate and I'd make it again.

Research knowledge is messy, contextual, and evolving. It resists rigid schemas. A knowledge file that says "IFF parameterization for 2D perovskites: the standard CIF-to-parameter pipeline works for (2-BrPEA)2PbI4 but requires manual atom type classification for mixed-halide systems — the Br/I site mixing creates ambiguous bonding environments that the automatic classifier handles as pure-I" is more useful than a database row. It captures the nuance that determines whether the next researcher wastes a week.

Markdown is also inspectable. Any researcher can open any knowledge file and see exactly what the agent knows. They can correct it. They can add context. The knowledge base isn't a black box — it's a shared document store that the agent happens to be the most prolific contributor to.

Version control is free. Every change to a knowledge file is a git commit. You can see when the agent learned something, what triggered the update, and how its understanding evolved. That's scientifically valuable. It's also reassuring — you can always roll back.

### The compounding effect

After several months of operation, the knowledge base represents something that didn't exist before: a structured, searchable, continuously updated model of the lab's specific research context. Not a general materials science knowledge base. A model of what *this lab* works on, how *these researchers* think about problems, which approaches have been tried on *these specific systems*, and what the results were.

Every simulation the agent runs, every paper it analyzes, every failed calculation it diagnoses adds to this model. When a new question comes in about a system the lab has studied before, the agent doesn't start from scratch. It retrieves everything the lab has learned about that system — force field performance, convergence behavior, validated properties, known pitfalls — and builds on it.

This is institutional memory that actually works.

---

## Step 4: Integrate into the research group

A system that runs in isolation is a demo. A system that's woven into the daily rhythm of the lab is infrastructure.

### Where the agent lives

The lab agent lives in the group's Slack. This isn't incidental — it's a core design decision. A tool that researchers have to go find and invoke competes for attention with everything else. An agent that shows up where the work already happens, with relevant information at the right time, becomes part of how the lab thinks.

### What it does daily

**Weekly arXiv digests.** Every Monday, the agent scans new arXiv preprints filtered to the lab's research areas: machine-learned interatomic potentials, MXenes, halide perovskites, interfacial force fields, 2D materials. It posts a curated digest — not a list of 200 papers, but the 5-10 that are actually relevant to ongoing work, with one-paragraph summaries explaining *why* each matters for the lab specifically.

Before the agent, staying current with the literature was something each researcher did individually, inconsistently, and with significant overlap. Five people monitoring the same arXiv categories, each catching different papers, none of them systematically connecting new results to ongoing work. Now the lab gets unified coverage with zero individual overhead.

**Deep paper analysis.** When a researcher flags a paper as important, the agent produces a structured analysis: key findings, methodology, how it relates to the lab's work, whether the reported parameters or methods could be applied to ongoing projects, and any concerns about the methodology. 17 structured analyses to date, covering MACE fine-tuning benchmarks, MXene MLIP validation gaps, uncertainty quantification calibration, new force field developments.

These analyses aren't summaries. They're contextualized reviews that connect the paper to the lab's specific context. "This paper reports MACE performance on MXene surface energies, but they only tested bare Ti3C2 without terminations. Our systems are hydroxylated. The results are informative but not directly transferable — we'd need to fine-tune on terminated structures, and their training set doesn't include those configurations."

**Automated IFF parameterization.** A researcher drops a CIF file into a Slack channel. The agent classifies atom types, looks up force field parameters, generates a complete parameter set, validates against known structures, and returns a JSON parameter file and a PDF report documenting every choice. For standard systems like NaCl, this takes minutes and is validated against published values. For complex systems like 2D perovskites with organic cations, it handles what it can and flags what requires human judgment (mixed-halide site disorder, organic cation conformational flexibility).

**Status updates and result sharing.** When simulations complete, the agent posts results to the relevant Slack channel with context: what was run, why, how the results compare to expectations, and what the suggested next step is. Researchers respond in-thread. The conversation is captured and informs the next action.

### Calibrating signal vs. noise

Getting the notification calibration right took iteration. The first version posted too much — every completed simulation, every paper scanned, every parameter lookup. Researchers ignored it within a week.

The current version is quiet by default. It posts weekly digests, shares results when they're ready, and flags things that need attention. It doesn't summarize things people can read themselves. It doesn't interrupt with status updates that don't require action. The operating principle: if a notification doesn't change what someone does next, don't send it.

---

## Step 5: Let it delegate

Some work is too large or too specialized for a single agent context. The lab agent handles day-to-day operations. But when a project requires sustained, focused effort, it spawns a dedicated project agent.

### How delegation works

The lab agent defines a project scope: what needs to be built, what the requirements are, what success looks like. It spawns a project agent with that scope, relevant context from the knowledge base, and access to the necessary tools. The project agent works autonomously, checks in with the lab agent periodically, and delivers a result.

The lab agent doesn't hold the project details in its own context. It knows: what was requested, what the current status is, and where to find the result. This is critical for staying within context window limits while sustaining complex work.

### Concrete examples

**axiom-gui.** The lab needed a molecular structure visualization tool for web-based analysis. The lab agent specified requirements: WebGL rendering (no heavy dependencies like Three.js), multi-format support (CIF, XYZ, PDB), ball-and-stick and space-filling representations, export to PNG/PDB/CIF, production quality. Spawned a project agent. Over 72 hours of continuous autonomous development, the project agent built a complete React/TypeScript application with a direct WebGL renderer, multi-format parser, and export pipeline. The lab agent received a working tool. It's published at [github.com/Heinz-Laboratory/axiom-gui](https://github.com/Heinz-Laboratory/axiom-gui).

**IFF auto-parameterization pipeline.** Parameterizing the Interface Force Field for a new material system is a multi-day manual process: classify atom types from the crystal structure, look up each parameter from published tables, handle edge cases where standard types don't apply, validate the complete parameter set against known properties. The lab agent scoped this as a project, spawned a dedicated agent, and received an automated pipeline that handles the standard cases end-to-end and flags edge cases for human review.

**Seven-phase publication workflow.** The most ambitious delegation: the lab agent orchestrated a complete publication-ready research workflow autonomously. Phase 1: literature review and hypothesis formulation. Phase 2: simulation design. Phase 3: execution (multiple simulation campaigns). Phase 4: result validation against published benchmarks. Phase 5: systematic analysis. Phase 6: figure generation. Phase 7: formatted manuscript draft. Full logging and reproducibility at every step. The output required human review and revision, but the mechanical work of producing it — which would normally take weeks of a researcher's time — was handled autonomously.

### When to delegate vs. handle directly

Rule of thumb: if the work fits in a single agent session (< 2 hours of focused work) and doesn't require specialized context, the lab agent handles it directly. If it requires sustained focus over hours or days, needs its own growing context, or involves building a deliverable artifact, it gets a project agent.

The organizational parallel is obvious: this is how research groups already work, with a PI setting direction and students executing. The difference is that the execution layer scales without adding people.

---

## Step 6: Build the self-improving loop

Everything up to this point is automation. Sophisticated automation, but automation. The system that changes the trajectory of a research group is one that gets better the longer it runs.

### How improvement actually happens

It's not magic. It's structured feedback loops:

**Simulation feedback.** Every simulation result — success or failure — updates the knowledge base. The agent ran a ReaxFF simulation of MXene interlayer shear and got a barrier height of 85 MPa. Published experimental values range from 40-120 MPa depending on hydration. The result is reasonable but on the high end. This observation gets recorded: "ReaxFF interlayer shear for dry Ti3C2(OH)2: 85 MPa. Consistent with experimental range but possibly overestimates for dry conditions. Compare with DFT nudged elastic band for calibration." Next time someone asks about MXene shear, this context is available without re-running the simulation.

**Method feedback.** The agent tried three different approaches to compute diffusion coefficients in hydrated MXene interlayers. Einstein relation from MSD worked well for bulk-like water layers. Green-Kubo from velocity autocorrelation gave noisy results for confined systems with fewer than 100 water molecules. Survival probability analysis was most reliable for single-layer hydration. All of this goes into method files. Next time, the agent (or a new student) doesn't repeat the comparison.

**Literature feedback.** Every paper analyzed enriches the knowledge base. A new MACE benchmark paper shows performance gaps for 2D materials with mixed terminations. The agent records this finding, links it to the lab's MXene work, and adjusts its confidence in MACE predictions for terminated MXene surfaces. When a researcher later asks about using MACE for a new MXene system, the agent provides this context proactively.

**Interaction feedback.** When a researcher corrects the agent — "that force field doesn't work well for this system, use this one instead" — the correction goes into the knowledge base. Over time, the agent's default recommendations for specific systems converge toward the lab's tested preferences rather than generic literature recommendations. The agent learns the lab's taste.

### The graduation problem

This is where the compounding pays off most visibly. In a typical lab, a graduating PhD student takes 4-6 years of accumulated context with them. Which simulation parameters work for which systems. Which approaches failed and why. Which papers are actually important vs. frequently cited but misleading. Undocumented tricks for getting convergence on difficult systems. All of it walks out the door.

In a lab with persistent memory, the knowledge stays. A new student joining the group doesn't spend their first semester rediscovering what the last student learned. They ask the agent: "What has the lab done with hydroxylated MXenes?" and get a complete history — every simulation run, every parameter choice, every validation result, every failed approach with documentation of why it failed.

This doesn't replace mentorship. It replaces the part of mentorship that's just transferring facts. The senior students can focus on teaching judgment, intuition, and research taste rather than spending hours explaining which simulation settings to use.

---

## Step 7: Extend the frontier

Everything described so far is operational. It works today. The next steps are where it gets transformative.

### Autonomous materials screening

Instead of a researcher manually selecting which systems to simulate, the agent evaluates hundreds of candidates against target properties.

Concretely: the lab is interested in 2D materials with specific interlayer shear properties. The agent queries the Materials Project for candidate structures, filters by composition and dimensionality, sets up LAMMPS simulations for each using validated force fields, runs the shear calculations, validates results against any available published data, and ranks candidates by target properties. The researcher reviews the top 20 candidates, not the initial 500.

The screening workflow needs its own validation layer. Not every candidate will have published comparison data. The agent needs heuristics for flagging suspicious results even without reference values: unphysical energies, anomalous elastic constants, structures that distort beyond recognition during relaxation. These heuristics come from the accumulated knowledge base — every previous simulation informs what "reasonable" looks like.

### Active learning for lab-specific potentials

Machine-learned interatomic potentials (MLIPs) are only as good as their training data. General-purpose foundation models like MACE-MP-0 provide broad coverage but underperform on specific systems that are outside or at the edges of their training distribution.

The active learning loop: the agent identifies configurations where the MLIP's uncertainty is high (ensemble disagreement between multiple model instances), runs targeted DFT calculations on those configurations to generate ground truth, adds the results to the training set, and retrains. The potential improves continuously, tailored to the lab's specific systems.

For the Heinz Lab, this means a MXene-specific MLIP that's been refined on exactly the configurations that matter: varying hydration levels, different termination group arrangements, interlayer sliding geometries, temperature effects. The general model is the starting point. The active learning loop makes it accurate for the lab's specific questions.

The agent manages this autonomously: identify uncertainty hotspots → design DFT calculations → submit to HPC → collect results → retrain → validate → deploy improved model → repeat. Each cycle makes the MLIP more accurate for the lab's systems. After enough cycles, the lab has a validated, purpose-built potential that outperforms any general model for their specific research questions.

### Searchable simulation warehouse

Every input file, every output, every parameter choice, every validation check, indexed and queryable:

- "Show me every simulation we've run on Ti3C2Tx MXenes with more than 3 water layers" — returns results in seconds.
- "What force field parameters did we use for (2-BrPEA)2PbI4 and how did the elastic constants compare to DFT?" — returns the comparison with provenance.
- "Which simulations in the last 6 months used the SPC/E water model and what were the diffusion coefficients?" — returns a structured table.

The warehouse isn't just storage. It's a queryable experimental record that makes the lab's entire simulation history accessible. No more digging through old directories, trying to remember which subdirectory had the converged run, or re-running calculations because no one can find the old results.

Implementation: every simulation the agent runs is logged with structured metadata (system composition, force field, ensemble, temperature, pressure, computed properties, validation status). The metadata lives in a lightweight database (SQLite is fine). The raw data stays on disk. The agent queries the metadata to find relevant prior work before starting new calculations.

---

## What I got wrong

Honesty requires this section.

**I underestimated validation.** Early versions of the execution agent produced results that looked right — correct units, reasonable magnitudes, clean convergence. But "looks right" isn't "is right." A lattice constant that's 5% off is wrong in a way that cascades through every downstream prediction. I built the validation layer after the fact, and it should have been there from the start. If your agent can't check its own work against known results, it's not doing science. It's generating plausible output. This is the single most important lesson.

**I overestimated researcher engagement.** The vision was researchers actively directing the agent toward their hardest problems. The reality is that most interaction is reactive: the agent surfaces something, a researcher responds. People are busy. Changing workflows takes time. The system needs to meet researchers where they are, not where you wish they were. This is why the Slack integration matters more than the technical capabilities. If you build the most sophisticated autonomous simulation system in the world and no one uses it, you've built nothing.

**I underestimated the ops burden.** An always-on agent on dedicated infrastructure requires maintenance. Credential rotation, job scheduling, error recovery, memory management, disk space monitoring. I built the agent but had to build a [separate fleet operations system](/projects/seed-fleet/) to keep it running. The fleet has its own agents for deployment, monitoring, and self-healing. This is real work that doesn't appear in the vision document. If you're building this, budget as much time for ops as for capabilities.

**The context window is a real constraint.** A single agent trying to hold an entire research project in context loses coherence. Multi-agent delegation (step 5) wasn't part of the original plan. It emerged from hitting walls. Specifically: an agent trying to simultaneously hold the lab's full knowledge base, a complex simulation setup, and the current conversation starts dropping context. Important parameters get lost. Prior results get forgotten mid-analysis. Design for delegation from the start. Scope each agent's context to what it actually needs.

**Force field selection is harder than it looks.** This is a materials science-specific lesson. There are dozens of force fields for common systems, and the "right" one depends on what property you're computing. IFF is good for structural properties of organic-inorganic interfaces. ReaxFF captures reactivity but is computationally expensive and can be unstable. CHARMM works for biomolecular systems but not for inorganic surfaces. The agent needs a decision tree, not just a lookup table. I'm still refining this.

**Researchers don't trust what they can't verify.** The agent's results need to be reproducible by hand. Every simulation should have a complete input file that a researcher can inspect, modify, and re-run. Every parameter choice should be documented and traceable to a source. If the agent produces a result and the researcher can't understand how it got there, the result is worthless regardless of whether it's correct. Transparency is not optional. It's a prerequisite for adoption.

---

## The order of operations

If you're starting from zero:

1. **Pick one simulation code your lab actually uses.** Build structured I/O around it. LAMMPS or VASP or Quantum ESPRESSO — whatever your group runs most. Don't try to support everything at once.

2. **Close the loop for one specific workflow.** Literature → parameters → simulation → validation. Pick a system you understand well enough to verify every result by hand. For us, that was NaCl with IFF — a well-characterized system with published properties at every level (lattice constant, elastic constants, surface energies). Get this working end-to-end before touching anything else.

3. **Add memory.** Start simple — Markdown files that capture what worked, what failed, what parameters apply to which systems. You'll be surprised how quickly these become the most valuable part of the system. A file that says "ReaxFF timestep for MXenes: 0.25 fs required for stability, 0.5 fs causes energy drift above 500K" saves someone a week.

4. **Put it where people work.** Slack, email, whatever your lab uses. Start with one specific, immediately useful capability: literature digests are a good entry point because they save everyone time with zero risk. Don't start by offering to run simulations autonomously — start by being useful for information retrieval.

5. **Let it run for weeks.** Watch what breaks. Fix what breaks. Watch what researchers actually use. What they use tells you what matters. What they ignore tells you what doesn't. Double down on what gets used. Cut what doesn't.

6. **Add the simulation loop.** Once the agent has established trust through information tasks (literature, parameter lookup, knowledge management), extend to simulation setup, execution, and analysis. Researchers will trust it to run simulations only after they've seen it be reliable for simpler things.

7. **Add delegation** when single-agent context isn't enough. This usually happens when a project requires more than ~2 hours of focused work or when you find the agent losing context on complex tasks.

8. **Extend to screening and active learning** once the foundation is solid and the knowledge base has accumulated enough context to make autonomous decisions about new systems.

Skip steps and the system is fragile. Rush the integration and no one uses it. Neglect the validation and the science isn't trustworthy.

The foundation takes months, not weeks. But once it's in place, the compounding starts. And the compounding is the point.

---

&nbsp;

The tools I've built are open source. The [Agentic Science Worker](https://github.com/fl-sean03/agentic-science-worker) handles the execution loop. The [Heinz Lab Agent](/projects/heinz-lab-agent/) is a working instance of everything described here. The [Seed Fleet](/projects/seed-fleet/) is the infrastructure layer that keeps it all running.

If you're building something similar, or want to, I'd like to hear about it.
