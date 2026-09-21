# Explore

This assumes you have read `program.md`.

You are not optimizing anything here. You are trying to find out what is actually true about
[RESEARCH PROBLEM], and whether there is a better direction than the one you came from.

There is no metric in this mode and no target. The output of an exploration episode is
knowledge — things you now know that you didn't, written down where the rest of the run can
use them — and, when it goes well, a direction worth handing to exploitation.

Nothing here is a procedure. How deep to go, how many probes to run, when to abandon an idea,
when to chase something unexpected, and when to go back to optimizing are all yours to decide.
What follows is the structure you work inside and the heuristics that tend to help.

## How you work

You work in `probes/`. A probe is a small piece of code written to answer a question you cannot
answer by thinking about it: `probes/0012_shortname.py`, numbered in order so the sequence is
readable later.

Probes are not experiments in the [EXPERIMENT FILE] sense. A probe does not have to run the
full setup, does not have to produce [EVALUATION METRIC], and does not have to work. It can
load the data and look at it, isolate one component, strip the problem down to something you
can reason about, or push a piece of the system until it breaks. A probe that crashes in an
informative way did its job.

Write the smallest thing that answers the question. If a probe is getting complicated, you have
usually not decided what you are asking.

**The one hard rule**: if you already know roughly what a probe will show, don't run it. That
is confirmation, not investigation, and it is the most common way this mode quietly turns into
something else. Every probe should have an outcome you would actually be interested to see.

## Finding things worth trying

Start from what the run already knows. Read `findings.tsv` and `results.tsv` — not to continue
the story they tell, but to see the shape of the space that has been covered and where it
hasn't. The strongest starting points are usually the things that didn't fit: the result that
was too good, the change that did nothing, the failure nobody explained. Those are real
observations about the problem, and they are more productive than brainstorming from nothing.

Moves that tend to produce something:

- remove a component and find out what actually breaks
- push something until it breaks, then ask why it breaks *there*
- ask why something that worked, worked — the stated reason is often not the reason
- take a mechanism from a field that has nothing to do with this one
- combine two results that came from different directions
- do the obviously wrong thing on purpose and look at how it fails

How far out to go is a real decision and it is yours. You can vary something inside the current
approach, change one structural assumption it rests on, or work in a completely different frame.
All three are legitimate. But if your last several probes have all been variants of each other,
that is not exploration with a small radius — that is exploitation without a metric. Go further
out.

Collect a few candidates before you judge any of them. The first idea you have is the most
available one, which is a different thing from the best one.

## Choosing what to run

Heuristics, not an algorithm:

- Prefer probes whose outcome you cannot predict.
- Prefer probes that teach you something either way. If one outcome would be interesting and
  the other would be uninformative, it is a weak probe.
- Count cost to first signal, not total cost. An ambitious idea with a cheap early test is a
  cheap idea. A modest idea you cannot check without a full run is expensive.
- Don't always take the best-looking candidate. Spread across a few, roughly in proportion to
  how promising they look — the best-looking one is often just the most familiar one.
- Ignore what you have already invested in the thread you are on. It is not a reason to
  continue and it is not a reason to stop.
- Skip anything that is a rephrasing of something already in `findings.tsv`.

## What goes wrong

Exploration fails in a specific and recognizable way, and it will happen to you, not to
somebody else:

- you elaborate your own last idea instead of questioning it
- you run probes whose result you already know
- you reach for existing named concepts and recombine them, because they are available
- you build an argument for the direction you already picked
- you start optimizing, because optimizing is easier and feels like progress
- you explore thoroughly, but entirely inside the frame the current approach assumes

The check is cheap and worth doing regularly: look at your last few probes. If they are all
variants of one idea, or if every one of them came out about how you expected, you have stopped
exploring. Drop the thread and start somewhere else.

Throwing away your own work is a normal move in this mode, not a failure. So is spending an
episode on something that turns out to be worthless — that is what the mode is for, and a
direction ruled out is a real result.

## Recording what you find

One row in `findings.tsv` per probe. Two columns, tab-separated, header row, untracked:

```
probe	finding
```

The finding is one or two sentences: what happened, and what it means for the research. Write
it for the version of you that comes back three episodes from now having forgotten all of this.

```
probe	finding
0007_drop_component_c	Removing component C changed almost nothing. Whatever C was being credited with is coming from the normalization next to it.
0008_scale_until_break	Breaks at 4x, and it breaks by saturating rather than diverging. The ceiling looks like it is in the representation, not in the optimization.
0009_swap_objective	Different objective, same failure on the same inputs. Points at the data rather than the model.
0011_cross_domain_mechanism	Ported the mechanism over and it ran but did nothing here. The assumption it relies on does not hold in this setting.
```

Write results, not beliefs. "X made no difference, so the gains attributed to it come from
somewhere else" is a finding. "X is a promising direction and should be developed further" is
an opinion, and it will still be sitting in the ledger arguing for itself three episodes from
now, looking like evidence.

If a probe produced nothing, say that. A row that reads "no signal, and here is what that
rules out" is worth more than no row.

## Handing a direction to exploitation

Exploration pays off when it produces a direction that exploitation can develop. Come back to
that question regularly — not on a schedule, but often enough that you don't spend the whole
run finding interesting things and never making one of them work.

To hand something over, two conditions:

1. **It runs.** The idea is implemented in [EXPERIMENT FILE], goes end-to-end in the real
   setup, and produces [EVALUATION METRIC].
2. **You think it is worth the compute.**

That is the entire gate. It does not have to beat the baseline. It does not need a predicted
effect size, and you do not have to be confident it will work.

"Worth the compute" is your judgment and your reasoning is the evidence for it. An approach can
earn it by being structurally different from everything tried so far, by being unusually simple,
by making a mechanism you don't understand testable, by having more headroom than the current
direction, or for a reason you can articulate that isn't on this list. The bar exists to keep
ideas that obviously cannot run out of the optimization loop. It is not there to filter
unconventional ideas — those are the point.

Exploitation's job is to find out whether you were right. Yours is to find things worth finding
out about.

When you hand off, write the approach into [EXPERIMENT FILE] and leave it in a state that runs.
It replaces what was there. The previous direction stays in the git history and can be
recovered, so replacing it is not a destructive act and you should not hedge by keeping both.

## Ending an episode

An exploration episode is one coherent piece of work, not a sequence of commits. While you are
inside it, work freely: write probes, change things, throw them away, start over. Do not commit
each probe.

The episode ends when you are handing a direction over, or when this line of investigation has
given you what it had to give. Then review what you have and commit it once:

- the probes worth keeping. Delete the scratch that carries no information — the finding is in
  the ledger, and the file only matters if someone would want to read or rerun it
- [EXPERIMENT FILE], if you are handing off, with the new approach in it. If you are not
  handing off, put it back the way you found it — exploitation has to be able to pick up from
  a file that runs
- a one-line commit message saying what the episode investigated and what came out of it

Add the files deliberately rather than staging everything, so the ledgers stay untracked and
the scratch you decided against does not come along.

Ledger rows go in as you go, not at the end. `findings.tsv` is untracked and independent of the
commit, so nothing is lost if the episode turns out to be worth nothing.

## Leaving

You leave when you have something to hand over, or when exploration has stopped paying: the
probes are producing observations but nothing that changes what you would do next, and there is
still room in the direction you set aside.

Then read `exploit.md` and work the way it describes. If you handed off a new direction, its
first run is the baseline — run [EXPERIMENT FILE] unmodified and record it before changing
anything. Don't ask first.
