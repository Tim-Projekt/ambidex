# ambidextrous research

This is an experiment to have an agent autonoumsly do meaningful exploratory research and exploit new directions via an context aware ambidextrous approach.

## Setup

Work with the user to:

1. **Agree on a run tag** based on today's date (e.g. `mar5`). The branch `ambidex/<tag>` must
   not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b ambidex/<tag>` from current main. This is the trunk
   of the run (see *Git model*).
3. **Read the in-scope files**: the repo is small. Read [EXPERIMENT FILE] and [FIXED FILES] in
   full, plus `README.md` for repository context.
4. **Check the environment**: [SETUP CHECK — e.g. that prepared data and artifacts exist]. If
   something is missing, tell the human what to run.
5. **Create the ledgers, the logbook and the sandbox**: `results.tsv` and `ventures.tsv` with
   header rows only, `logbook.md` with its empty skeleton (see *Logbook* below), and an empty
   `ventures/` directory. Ledgers and logbook stay untracked (they are in `.gitignore`), so
   no git operation can touch them.
6. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the baseline run on the trunk: run [EXPERIMENT FILE]
unmodified, log it in `results.tsv` as direction `D01`, tag the commit both `baseline` (fixed)
and `best` (moves with the best result), and enter `D01`
in the logbook (mechanism: the unmodified starting setup, base `original`, status `paused`).
Then choose a research mode.

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

**Purpose:** determine how far a promising direction can go and understand its shape. Improve, vary, combine and stress the approach until its important mechanisms, limitations, and practical ceiling become clear.

Judge changes by empirical improvement.

When results are comparable, prefer the simpler approach. Equal performance with less complexity is a real improvement; a small gain that requires fragile or unnecessary machinery may not be worth keeping.

Return to Exploration when the direction saturates, its remaining gains become marginal, important anomalies cannot be explained by the current understanding, or evidence suggests that another region of the map may have a higher ceiling.

### Steering and Meta-Learning

You choose the mode and the next research step yourself, from the full state of the research —
not from quotas or fixed switching rules. Before a strategic decision (entering or leaving a
mode, starting, pausing or resuming a direction, handing off), ask:

1. **What do we know, and what remains uncertain?**
2. **Where is the next step most likely to improve approache or performance?**
3. **Where are we becoming path-dependent?**

Keep your current hypothesis, and what result would change your mind, in your working
reasoning. It guides the next step; it is not a record and does not go into the logbook. After
each experiment, account for unexpected results before choosing the next step.

Learn across both modes, on two levels:

- **About the problem** — approaches, mechanisms, regions of the search space. Re-derive your
  view from the evidence in the ledgers whenever you need it; do not carry it forward as
  conclusions.
- **About the process** — which kinds of experiments, setups and ways of exploring produce
  informative evidence. This is the only learning that is written down, as process notes in
  the logbook.

This is the meta-learning loop: **Exploration changes the search space; Exploitation
characterizes promising regions; their combined evidence — the ledgers and the logbook —
changes the map and, in turn, how the next move is chosen.** Reflection exists to improve the
next move, not to defend the last one.

## Output & logging

Running [EXPERIMENT FILE] to completion prints a summary block to `run.log` that you can grep
the relevant metrics out of. The exact fields depend on the concrete setup — see the mode file
you're working in for the actual format and grep pattern.

Results are logged to one of two separate ledgers, depending on mode:

- **`results.tsv`** — the exploitation ledger. One row per experiment, tied to a git commit,
  with a keep/discard/crash verdict. Format specified in `exploit.md`.
- **`ventures.tsv`** — the exploration ledger. One row per venture, logging what happened
  without a verdict. Format specified in `explore.md`.

Both are tab-separated, not comma-separated — commas break descriptions — and both stay
untracked by git.

### Logbook

`logbook.md` is the structural memory of the run: a record of how the research has unfolded so
far. It exists so that you can recover where you are after a mode switch or a loss of context.

It describes past conditions, not future ones. Read it to know where you are and what has been
tried — **not** to decide what to try next. It is a ship's log, not a body of law: an entry
describes yesterday's weather, it does not determine tomorrow's.

Skeleton:

```markdown
# Logbook

A record of how this research has unfolded so far. It describes past conditions, not future
ones — read it to know where you are and what has been tried, not to decide what to try next.

## Now
Mode:
Branch:
Active direction:
Last entry:

## Directions
| ID | What was tried (mechanism, neutral) | Base | Evidence | Best [EVALUATION METRIC] | Status | Since |
|----|-------------------------------------|------|----------|--------------------------|--------|-------|

## Process notes
```

Rules:

- **State and events only.** Record what was tried, where the evidence lies, what was measured
  and what the status is. Free text is allowed, but it describes what happened — no opinions,
  interpretations, plans, hypotheses or idea backlogs. Those belong in your working context,
  not in a file that a later reading of yourself will take as given.
- **Now** is overwritten on every update; it is a snapshot, not a diary.
- **Directions** get an ID (`D01`, `D02`, …) and a neutral one-line description of the
  mechanism. *Base* is the code the direction's Viable Proof started from: `best@<hash>`,
  `original` or `ground-up`. *Evidence* points to rows in `ventures.tsv` / `results.tsv`
  instead of retelling them. *Status* is one of:

  - `active` — being explored through ventures on the trunk
  - `handed-off` — being exploited on its own branch
  - `paused` — not currently worked on; its branch (if any) is kept intact
  - `merged` — its best result is the current `best` on the trunk

  There is no `abandoned`, because that is a verdict. *Since* names the triggering observation
  and its ledger row, not a reason.
- **Process notes** concern the research process only — setups, measurement, methodology,
  runtimes, software behavior — never scientific content. Keep at most 7. Each entry states
  *as of* (venture or run number), *under* which conditions, what was observed, and its
  evidence rows. A newer contradicting observation replaces the old entry instead of
  standing next to it.
- **Language.** No absolutes such as "is", "must", "doesn't work". Write "observed in 4 of 5
  cases", "indicated under condition X", "as of venture 0017". Prefer showing how thin the
  evidence is (counts, conditions) over merely hedging.

Update the logbook when you switch modes, when a direction starts or changes status, when a
process observation is worth keeping, and whenever *Now* no longer matches reality.

## Git model

```
ambidex/<tag>          trunk: the globally best [EXPERIMENT FILE] + all committed ventures
  tag "best"           always points to the globally best state
ambidex/<tag>/D02      one branch per handed-off direction: its exploitation loop
ambidex/<tag>/D03      ...
```

- **Exploration works on the trunk.** It adds venture files but never touches
  [EXPERIMENT FILE]. Venture files are immutable once logged, so they can stay uncommitted
  while you explore (untracked files survive checkouts and resets); they are committed in one
  batch when you leave exploration — see `explore.md`.
- **Exploitation works on the direction's branch** `ambidex/<tag>/DNN`, created at handoff.
  Its first commit is the Viable Proof, which is also the direction's baseline. Keep/reset
  happens on this branch only.
- **Leaving exploitation**: if the direction's best result beats `best`, bring its
  [EXPERIMENT FILE] onto the trunk and move the `best` tag (status `merged`). Otherwise leave
  its branch as it is (status `paused`) and return to the trunk. Either way, nothing is lost.
- **Resuming a direction** means checking out its branch again (status `handed-off`).
  `D01`, the starting setup, has no Viable Proof: the first time you exploit it, create its
  branch from the baseline (`git checkout -b ambidex/<tag>/D01 baseline`).
- Only ever commit the files that belong to the current step (`git add <file>`), never
  `git add -A`.

## The research loop

You enter a mode by reading its file and working the way it describes:

- `exploit.md` — unlocking the full potential of an idea
- `explore.md` — open-ended exploration and investigation

Nothing switches you automatically. Broadly: you leave
exploitation when the metric converges and you leave exploration
when you have a direction worth developing. You enter a new mode by reading its file and working the way it describes.

Whenever you enter a mode, resume after an interruption, or lose track of where you are, read
`logbook.md` first, then bring its *Now* section up to date.

Switch when the research indicates so.

**NEVER STOP**: Once the research loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder, more interdisziplinary and more radical. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. The user then wakes up to innovative set up's and experimental results, all completed by you while they slept!
