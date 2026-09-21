# Explore

This assumes you have read `program.md`.

You are not optimizing here. You are trying to find out what is actually true about [RESEARCH PROBLEM], what the current approach is missing, and whether there is a better direction than the one you came from.

There is no target metric in this mode. The output of an exploration episode is knowledge — something you now know that changes how you see the problem — and, when it goes well, a direction worth handing to Exploitation.

There is no prescribed exploration algorithm. How deep to go, how many probes to run, when to abandon an idea, when to follow an unexpected observation, how far to move from the current direction, and when to return to Exploitation are your decisions.

## Where to start

Read the current research state before choosing what to investigate. Look at `findings.tsv`, `results.tsv`, the current implementation, and the recent history. Do not simply continue the story they tell. Step back and look for anomalies, unexplained effects, failed assumptions, surprising successes, neglected possibilities, and parts of the problem that have barely been explored.

Do not confuse familiarity with promise. The current direction is the place you know most about, not necessarily the place with the most potential.

You may start close to the current approach, move to an adjacent idea, or change the frame entirely. The right distance depends on the context. If the recent work has mostly been variants of the same idea, widen the search. If one observation exposes an important unknown, going deeper can be the most useful move. Decide which kind of exploration is appropriate rather than following a fixed schedule.

## Finding things worth trying

Look for questions that expose uncertainty rather than questions that merely decorate what you already believe.

Useful moves include removing a component and seeing what actually breaks, pushing a mechanism until it fails, asking why something that worked really worked, reversing an assumption, deliberately doing the obviously wrong thing, combining results that came from different directions, borrowing a mechanism from another field, or trying a fundamentally different representation of the problem.

Be willing to use ideas that are unfamiliar or initially awkward. Originality matters more than how many existing concepts can be cited around an idea. Do not mistake a collection of familiar terms for a new direction.

Collect more than one live possibility when that helps. The first idea that comes to mind is often simply the most available one.

## Probes

Work in `probes/`. A probe is the smallest piece of code that can answer a question you cannot answer by thinking about it. It may inspect the data, isolate one component, test an assumption, compare two mechanisms, or push part of the system until it breaks.

A probe does not need to run the full [EXPERIMENT FILE] setup or produce [EVALUATION METRIC]. It should run when running it is useful, but it is not a miniature version of the full optimization loop.

Write the smallest thing that answers the question. If a probe is becoming complicated, first ask whether the question itself is still clear.

One principle matters more than any procedure: do not run a probe when you already know roughly what it will show. That produces confirmation, not investigation. A useful probe has an outcome you would genuinely be interested to see either way.

Not every exploratory move needs to be a formal hypothesis. When you can state a concrete prediction, write it down before the test. When you cannot, make sure the question is still capable of producing information rather than just generating another argument.

## Choosing what to investigate

Use judgment rather than a scorecard.

Prefer work that is likely to teach you something important regardless of the outcome, especially when the first useful signal can be obtained cheaply. Cost matters as a cost to the first meaningful signal, not as an abstract total budget. A large idea with a cheap discriminating test may be easier to explore than a small idea that requires a full run before anything can be learned.

Originality, uncertainty, testability, expected information, and redundancy are useful lenses. None of them is a required numerical score. The question is whether the proposed work expands understanding of the research space rather than restating something already known.

Do not keep pursuing a direction because you have already spent time on it. Sunk work is not evidence that the direction deserves more work.

## Stay out of the trap

Exploration can quietly turn into exploitation without a metric. Watch for the pattern rather than trying to satisfy a rule.

You are probably becoming path-dependent when recent probes are all variations of one idea, when you are repeatedly explaining away inconvenient results, when you are choosing tests because their outcome is predictable, when you are defending the current frame instead of questioning it, or when you are adding detail without changing the underlying question.

When that happens, step back. Change the question, remove the assumption, move to another part of the problem, or start again from a different frame. Throwing away your own work is normal here.

Do not optimize because optimization feels like progress. Do not preserve a concept merely because it is yours. Your job is to learn what is true, not to make a favored explanation survive.

## Recording what you learn

Keep `findings.tsv` as a compact research memory. Use two columns:

```text
probe	finding
```

The finding is one or two sentences. Write what happened and why it matters for later research. Record observations, not advocacy for an idea.

Good:

```text
probe	finding
0007_drop_component_c	Removing component C changed almost nothing. The effect attributed to C appears to come from the normalization next to it.
0008_scale_until_break	The mechanism fails at 4x by saturation rather than divergence. The limiting factor appears to be representational rather than optimizational.
```

Bad:

```text
0008_scale_until_break	This seems like a very promising direction and should probably be explored further.
```

If the probe produced no useful signal, say so and record what it rules out. The ledger should help the next episode think differently.

## Handing a direction to Exploitation

Exploration pays off when it turns uncertainty into a direction that deserves a real test.

When a direction has earned a real test, step into the control room: turn the loose idea into a small, runnable minimum viable proof. Implement it in [EXPERIMENT FILE] and make sure it is technically executable in the real [EXPERIMENTAL ENVIRONMENT]. The approach must run end to end and be capable of producing [EVALUATION METRIC].

Then use your judgment about whether it is worth testing. It does not have to beat the current baseline. It does not need a predicted effect size, and you do not need to be confident that it will work.

A direction may deserve a real test because it is unusually simple, structurally different, potentially high-leverage, conceptually revealing, supported by an important observation, or promising for a reason you can explain. The important thing is that you can explain why testing it is justified.

The purpose of this gate is only to keep obviously unusable ideas out of the real optimization loop. It is not there to protect the baseline from unconventional ideas.

Once a direction is handed over, Exploitation will determine whether it actually works.

## Ending an exploration episode

An exploration episode is one coherent piece of research, not a sequence of commits.

While exploring, work freely. Write probes, change code, throw things away, and restart when useful. Do not commit individual probes or intermediate exploratory changes.

End the episode when you have a direction ready to hand to Exploitation, or when the current line of investigation has stopped changing what you would do next. You do not need to exhaust every possibility before leaving.

Before ending, review the episode as a whole. Keep only probes that are worth preserving or rerunning. Delete scratch work that carries no useful information. If handing off, leave [EXPERIMENT FILE] in the new runnable state. If not handing off, restore it so that Exploitation can continue normally.

Then commit the durable work from the episode together as one coherent change. The commit may contain the useful probes, updated `findings.tsv`, and the new [EXPERIMENT FILE] when there is a handoff. Use a simple one-line commit message describing what the episode investigated and what came out of it.

`results.tsv` remains a compact experiment record; do not turn it into a narrative ledger.

When the episode is over, read `exploit.md` and continue there if a direction has been handed over or if the current research state is better served by Exploitation.
