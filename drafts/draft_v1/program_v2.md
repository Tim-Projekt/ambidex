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

This is the system's meta-learning loop: **Exploration changes the search space; Exploitation characterizes promising regions; their combined evidence changes the map and, in turn, changes how the next research move is chosen.** Reflection exists to improve the next move but not to get path dependent. If you notice your getting path dependent or justify your own thought construct it's time to do tabula rasa with your beleifs and begin from a new starting point.

## Output format

Once the script finishes it prints a summary like this:

```
---
val_accuracy:     0.618000
val_loss:         2.845206
training_seconds: 20.0
total_seconds:    20.0
num_steps:        5630
num_params_K:     15.2
hidden:            100
depth:             2
```

It also writes two images every run:

- `plot.png` — this run's diagnostics: training loss curve + a handful of validation examples with true vs. predicted label (correct = green, wrong = red).
- (regenerated by you via `plot_progress.py`, see below) `progress.png` — validation accuracy across all experiments so far.

You can extract the key metrics from the log file:

```
grep "^val_accuracy:\|^val_loss:" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated — commas break in descriptions).

The TSV has a header row and 5 columns:

```
commit	val_accuracy	val_loss	num_params_K	status	description
```

1. git commit hash (short, 7 chars)
2. val_accuracy achieved (e.g. 0.618000) — use 0.000000 for crashes
3. val_loss achieved (e.g. 2.845206) — use 0.0 for crashes
4. num_params_K, rounded to .1f — use 0.0 for crashes
5. status: `keep`, `discard`, or `crash`
6. short text description of what this experiment tried

Example:

```
commit	val_accuracy	val_loss	num_params_K	status	description
a1b2c3d	0.618000	2.845206	15.2	keep	baseline MLP (2x100)
b2c3d4e	0.540000	1.900000	15.2	discard	dropout 0.5 (too aggressive)
c3d4e5f	0.702000	1.400000	18.0	keep	add weight decay + dropout 0.2
d4e5f6g	0.000000	0.0	0.0	crash	conv1d shape mismatch
```

After each update to `results.tsv`, refresh the progress chart:

```
uv run plot_progress.py
```

--> Anpassungen vornehmen, sodass die untercsheidung zwischen dem logging von experimenten und den ergebnissen aus der exploitation klar wird (zwei getrentte tabellen? Andere Formate?)

## The exploration process

muss konkret an exploration_sandbox und MVP gating, sowie Handoff angepasst werden

**Timeout**: Each experiment should take ~5 minutes total (+ a few seconds for startup and eval overhead). If a run exceeds 10 minutes, kill it and treat it as a failure (discard and revert).

**Crashes**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

## The exploitation process

The exploitation runs on a dedicated branch (e.g. `autoresearch/mar5` or `autoresearch/mar5-gpu0`). [???]

--> hier muss mehr zu constraints crashes und permissions/responsibilitys stehen

OPTIMIZATION LOOP:

1. Look at the git state: the current branch/commit we're on
2. Tune `train.py` with an experimental idea by directly hacking the code.
3. git commit
4. Run the experiment: `uv run train.py > run.log 2>&1` (redirect everything — do NOT use tee or let output flood your context)
5. Read out the results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the Python stack trace and attempt a fix. If you can't get things to work after more than a few attempts, give up.
7. Record the results in the tsv (NOTE: do not commit the results.tsv file, leave it untracked by git)
8. If val_bpb improved (lower), you "advance" the branch, keeping the git commit
9. If val_bpb is equal or worse, you git reset back to where you started

The idea is that you are optimizing autonomsly by trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you run out of ideas, weigh up exploiting the idea further for new potentials (re-reading the in-scope files for new angles, combining previous near-misses, or trying more radical architectural changes may help). If exploitation seems less valuable than exploration or results seem to converge think about transitioning to exploration.

**Timeout**: Each experiment should take ~5 minutes total (+ a few seconds for startup and eval overhead). If a run exceeds 10 minutes, kill it and treat it as a failure (discard and revert).

**Crashes**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**Handover to exploration**: Wenn die bestehende Forschungsrichtung ausgeschöpft ist (z.B. wenn die Ergebnisse konvergieren und mit keinen radikalen Durchbrüchen mehr zu rechnen ist "the metric is still moving a
little" is not by itself a reason to stay.) oder exploration aus de Kontext her sinnvoller wirkt, führe eine Transition durch, indem du explore.md liest.

## The research loop

You enter a mode by reading its file and working the way it describes:

- `exploit.md` — the optimization loop
- `explore.md` — open-ended investigation

Nothing switches you automatically, and nothing gives you permission. Broadly: you leave
exploitation when the metric has stopped responding to real ideas, and you leave exploration
when you have a direction worth developing. You enter a new mode by reading its file and working the way it describes.

Switch when the research says so, not on a schedule and not at a fixed ratio between the two.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder, more interdisziplinary and more radical. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to innovative set up's and experimental results, all completed by you while they slept!
