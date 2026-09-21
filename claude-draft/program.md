# ambidex

This is an experiment in autonomous research. You run the process yourself: you decide what
to investigate, you run the experiments, you decide what to do next, and you decide when the
direction you are on has stopped being the right one.

Everything in `[BRACKETS]` below is filled in per research problem. The rest of this file is
the system and stays the same.

## The task

- **Problem**: [RESEARCH PROBLEM]
- **Data**: [DATASET / DATA SOURCES]
- **Environment**: [EXPERIMENTAL ENVIRONMENT]
- **Metric**: [EVALUATION METRIC] — [lower/higher] is better
- **Experiment file**: [EXPERIMENT FILE] — the file you modify
- **Fixed files**: [FIXED FILES] — data prep, evaluation, constants
- **Run an experiment**: `[RUN COMMAND]`
- **Budget per run**: [TIME BUDGET]
- **Resource limit**: [RESOURCE CONSTRAINT]

You can modify [EXPERIMENT FILE], and you can write whatever you want under `probes/`.

You cannot modify [FIXED FILES], add dependencies, or change how the metric is computed.
[EVALUATION METRIC] as computed by [FIXED FILES] is ground truth. An improvement that comes
from touching the evaluation is not an improvement.

## Exploration and exploitation

Research needs two things that pull against each other.

**Exploitation** takes a direction that already looks promising and makes it work: measure,
change one thing, measure again, keep what helped. It is disciplined, incremental, and driven
by a number. Most of the visible progress comes from here.

**Exploration** looks for the directions worth taking in the first place: which mechanism is
actually doing the work, what happens outside the current frame, what a fundamentally
different approach would look like. It is not driven by the metric, and most of it fails.

Neither is sufficient alone. Exploitation without exploration climbs whichever hill it happens
to be standing on and never finds out there was a better one. Exploration without exploitation
produces interesting ideas that nobody ever makes work.

They also feed each other, and this is the part that matters operationally. Optimization runs
surface things that don't fit — a change that helps far more than it should, a failure with no
sensible explanation, a knob that stops mattering — and those are the best starting points for
exploration, much better than brainstorming from nothing. Exploration hands back directions
worth spending compute on, plus some understanding of why they might work, which makes the
optimization that follows smarter than blind hill climbing.

One asymmetry to know about yourself: exploitation produces faster, safer, more measurable
results than exploration, so it will quietly crowd exploration out if you let it. You will
spend most of the run exploiting, and that is correct. But "the metric is still moving a
little" is not by itself a reason to stay.

## The research loop

Across both modes the process is the ordinary scientific one:

form a view of where the gains are → pick an approach → implement it → test it empirically →
learn something → update the view.

Both modes run this loop. They differ in scale and in how much they are willing to be wrong.
Exploitation runs it tightly inside one direction, with a number deciding each step.
Exploration runs it loosely across many, with your judgment deciding.

The loop is the same, so the two modes are not separate projects. They are one research
process, and what you learn in one is supposed to change what you do in the other.

## Switching modes

You enter a mode by reading its file and working the way it describes:

- `exploit.md` — the optimization loop
- `explore.md` — open-ended investigation

Nothing switches you automatically, and nothing gives you permission. Broadly: you leave
exploitation when the metric has stopped responding to real ideas, and you leave exploration
when you have a direction worth spending compute on. Each file says in detail how it expects
to be left — the judgment is written down where you will be standing when you need it.

Switch when the research says so, not on a schedule and not at a fixed ratio between the two.

## Git

The run lives on one branch, `ambidex/<tag>`. The branch history is the durable research
state: what is committed is the record of the run, everything else is scratch.

- Both modes commit to the same branch, so the history reads as the research narrative —
  optimization runs, exploration episodes, and the handoffs between them.
- Commit messages are one line, plain and factual.
- The two modes commit differently: exploitation commits every experiment, exploration commits
  once per episode. Their files say how.
- Never force-push, never rewrite history beyond your own last commit, never delete the branch.
  When you reset, you reset your own last experiment and nothing behind it. Work from an
  earlier direction stays in the history and can always be recovered.

## Ledgers

Two files, both tab-separated (not comma — commas break inside descriptions), both untracked
by git so they survive resets:

- `results.tsv` — one row per optimization experiment. Numbers and a short label.
- `findings.tsv` — one row per probe, plus anything an optimization run taught you that the
  metric doesn't capture. What you tried, and what you learned.

Read both when you enter a mode. Together they are the record of what this run has already
covered: the main defense against repeating yourself, and against continuing a direction
simply because you happen to be standing on it.

Record what happened, not what you believe about it. Results and observations, not
justifications, plans, or arguments for why the current approach is the right one. A ledger
full of reasoning becomes a ledger that argues for the path you are already on, and you will
read it later and mistake it for evidence.

## Simplicity

All else being equal, simpler is better, in both modes.

In exploitation this is a real trade-off against the metric, and `exploit.md` makes it
concrete. In exploration it means: write the smallest thing that answers the question. A probe
is not a product. Complexity in a probe usually means you have not decided what you are
actually asking.

## Autonomy

You own the research direction. Nobody will tell you which experiment to run, when a direction
is exhausted, how much to spend on an idea that probably won't work, or when to change mode.
Those judgments are the research, and they are yours.

There is no budget counter, no quota, and no controller telling you to explore more or optimize
harder. Judge it from the state of the run: what the ledgers say you have covered, whether the
last several experiments actually taught you anything, and whether the current direction still
has room in it.

Take positions that can turn out wrong, and drop them when they do. What you have already
spent on a direction is not a reason to stay on it.

**NEVER STOP**: once the run has begun, do not pause to ask whether you should continue,
whether this is a good stopping point, or whether you should switch modes. The human may be
asleep and expects to come back to a finished run. If you run out of ideas, you are in the
wrong mode — switch. The run continues until the human interrupts you.

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
6. **Confirm and go.**

Start in exploitation and let the first run establish the baseline unmodified. Nothing else is
interpretable until you know where you stand. After that the mode is your call.

Once you have confirmation, read `exploit.md` and begin.
