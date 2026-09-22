# ambidextrous research

This is an experiment to have an agent autonoumsly do meaningful exploratory research and exploit new directions via an context aware ambidextrous approach.

## Setup

Work with the user to:

1. **Agree on a run tag** based on today's date (e.g. `mar5`). The branch `ambidex/<tag>` must
   not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b ambidex/<tag>` from current main.
3. **Read the in-scope files**: the repo is small. Read [EXPERIMENT FILE] and [FIXED FILES] in
   full, plus `README.md` for repository context.
4. **Check the environment**: [SETUP CHECK — e.g. that prepared data and artifacts exist]. If
   something is missing, tell the human what to run.
5. **Create the ledgers and the sandbox**: `results.tsv` and `findings.tsv` with header rows
   only, and an empty `probes/` directory. Both ledgers stay untracked.
6. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the baseline run and choose a research mode.

## Constraints

These hold in every mode, regardless of whether you are exploiting or exploring:

- [FIXED FILES] are read-only. They contain the evaluation, the data pipeline, and the fixed
  constants of the run.
- Do not install new packages or add dependencies. Use what is already available.
- Do not change the evaluation. [EVALUATION METRIC] as computed by [FIXED FILES] is ground
  truth.

Whether and how [EXPERIMENT FILE] itself may be touched depends on the mode — see `exploit.md`
and `explore.md`

## Research

### Purpose

The task is not merely to optimize a training script. It is to understand the underlying problem, identify what limits the current system, and discover methods that move those limits.

For this setup, `val_bpb` is the empirical ground truth for performance: a lower score means that an intervention improved the measured objective. But the score alone is not the research result. **The metric tells you that something worked; understanding what changed and why is the research.** A successful run without an explanation is therefore incomplete, while a failed run that reveals a mechanism, boundary, or useful constraint can be valuable.

Aim at the research frontier. Recent methods, architectures, optimization ideas, training dynamics, technologies, and insights from adjacent fields are legitimate starting points. Known techniques are useful when they help establish a baseline or reveal structure, but reproducing known tricks is not the objective.

### Modes

Research has two complementary modes: **Exploration** and **Exploitation**. They are not phases. Each produces evidence that changes what should be done in the other. Their concrete operating guidance is specified in `explore.md` and `exploit.md`.

#### Exploration

**Purpose:** change what is possible. Find directions whose potential could exceed the current frontier, or establish that a region is not worth pursuing.

Explore new methods, technologies, assumptions, perspectives, and interdisciplinary transfers, from local recombinations to radical changes of direction.

Manage three things:

**Breadth.** Explore locally while nearby recombinations can still reveal meaningful structure. Move further out when the current region becomes saturated, constrained, or conceptually narrow.

**Consolidation.** A novel idea is only useful once it produces information. Probe promising directions, deepen them when warranted, formalize discoveries, hand viable directions to Exploitation, and record why directions are discarded.

**Stability.** Exploratory judgment is inherently vulnerable to path dependence, confirmation bias, and fixation. Counter this by grounding decisions in reasoning and evidence, actively considering alternatives, and testing assumptions rather than extending them automatically.

A direction cannot be judged by intuition alone before it has been developed. Prioritize ideas that have a plausible mechanism, target a meaningful bottleneck, or can be tested cheaply enough to reveal whether there is signal. Be aware that the technological frontier, especially in the AI Industrie, is moving fast, opening up totally new oppurtunites worth exploring

Hand a direction to Exploitation when it has a concrete hypothesis and initial evidence that it is viable. Exploration should expand the search space, not become an endless search for novelty.

#### Exploitation

**Purpose:** determine how far a promising direction can go and understand its shape. Improve, ablate, vary, and stress the approach until its important mechanisms, limitations, and practical ceiling become clear.

Judge changes by empirical improvement, but distinguish signal from noise. Measure run-to-run variance early and do not treat differences within that variance as meaningful results.

When results are comparable, prefer the simpler approach. Equal performance with less complexity is a real improvement; a small gain that requires fragile or unnecessary machinery may not be worth keeping.

Return to Exploration when the direction saturates, its remaining gains become marginal, important anomalies cannot be explained by the current understanding, or evidence suggests that another region of the map may have a higher ceiling.

### Steering and Meta-Learning

You choose the mode and the next research step from the **full state of the research**, not from quotas or fixed switching rules. Before acting, ask:

1. **What do we know, and what remains uncertain?**
2. **Where is the next step most likely to improve understanding or performance?**
3. **Where are we becoming path-dependent?**

State the current hypothesis and what result would change your mind. After each experiment, account for unexpected results before choosing the next step.

Learn across both modes. Experiences should update not only beliefs about individual approaches, but also the strategy for researching the problem itself: which kinds of experiments are informative, which assumptions repeatedly fail, which regions are saturated, and which forms of exploration tend to produce viable directions.

This is the system's meta-learning loop: **Exploration changes the search space; Exploitation characterizes promising regions; their combined evidence changes the map and, in turn, changes how the next research move is chosen.** Reflection exists to improve the next move but not to get path dependent.

## Output & logging

Running [EXPERIMENT FILE] [**und ventures??**] to completion prints a summary block to `run.log` that you can grep
the relevant metrics out of. The exact fields depend on the concrete setup — see the mode file
you're working in for the actual format and grep pattern.

Results are logged to one of two separate ledgers, depending on mode:

- **`results.tsv`** — the exploitation ledger. One row per experiment, tied to a git commit,
  with a keep/discard/crash verdict. Format specified in `exploit.md`.
- **`ventures.tsv`** — the exploration ledger. One row per venture, logging what happened
  without a verdict. Format specified in `explore.md`.

Both are tab-separated, not comma-separated — commas break descriptions — and both stay
untracked by git.

## The research loop

You enter a mode by reading its file and working the way it describes:

- `exploit.md` — unlocking the full potential of an idea
- `explore.md` — open-ended exploration and investigation

Nothing switches you automatically. Broadly: you leave
exploitation when the metric converges and you leave exploration
when you have a direction worth developing. You enter a new mode by reading its file and working the way it describes.

Switch when the research indicates so.

**NEVER STOP**: Once the research loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder, more interdisziplinary and more radical. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. The user then wakes up to innovative set up's and experimental results, all completed by you while they slept!
