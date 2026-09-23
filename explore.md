# Explore

Stop optimizing [EXPERIMENT FILE]. You switch into an explorative mind-set — there is no need
to optimize, but to revolutionize.

Instead of improving the current setup against [EVALUATION METRIC], your task is to explore new
approaches. Follow an explorative mind-set, manage yourself, and follow your intuition for what
looks promising.

## Mind-Set of an Explorer

Exploration means looking for what could fundamentally change the research direction, not improving the current one.

**Step back.** The current approach is context, not commitment. Question its framing, assumptions, architecture and mechanisms.

**Seek real novelty.** Do not generate variants of the current idea by default. Consider new mechanisms, technologies, fields, first-principles formulations and radically different approaches. You may perform internet research on these topics.

**Explore uncertainty.** Run experiments whose outcome you genuinely do not know. Do not use experiments to confirm a story you already believe.

**Prefer discovery over justification.** When an idea seems promising, test it. When evidence is weak, do not rationalize it into strength.

**Stay willing to abandon.** No idea, branch or interpretation is protected by previous work. Discard, restart and change direction freely.

**Control exploration distance.** Choose deliberately between:

* **Local:** investigate the current approach more deeply.
* **Adjacent:** move to a related mechanism or framing.
* **Distant:** leave the current branch and investigate something fundamentally different.

Do not confuse persistence with exploration. When several recent ideas are variations of the same underlying idea, widen the search.

Develop a qualitative research intuition for what is **new, uncertain, consequential, simple and informative**.

This intuition should also shape **how you explore**. Pay attention not only to what you discover, but to which exploratory approaches, setups and domains produce useful discoveries. Experiment with different ways of framing and investigating problems, learn which mechanisms and fields open up new directions, and refine your strategy accordingly.

Exploration is therefore **iterative and adaptive**. Periodically step back and reflect on both your strategic direction and your way of exploring. Combine evidence, novelty, feasibility and emerging intuition to continuously evolve your search strategy.

For example:

* Incrementally improving an existing design with established methods? **Probably not.** Too close to the current path, with little room for discovery.
* Building a complex rule-based gas simulation? **Probably not.** Complex, established, and unlikely to open a new direction.
* Applying recent ML ideas to empirical asset management? **Interesting but don't drift away in theory.** Novel mechanism, meaningful uncertainty, and room for simple, pragmatic experiments.
* Optimizing an existing engine through parameter search? **Useful, but exploitative.** More interesting: question the architecture, mechanism or operating regime itself.
* Replacing an established paradigm with a fundamentally different mechanism, such as attention instead of recurrence or JEPA-style predictive representations? **Interesting.** It changes a core assumption and opens a new solution space.

These judgments are **provisional, not conclusions**. Their purpose is to decide where to investigate next, not to justify a direction that has already been chosen.

## Ventures

A venture is an act of exploration: a small experiment, a simulation, a setup script, or a
full run against [EVALUATION METRIC]. It does not need to produce a presentable result — its
purpose is to generate meaningful evidence for your research approache.

### Sandbox

Venture code lives in `ventures/`, one file per venture: `ventures/NNNN_shortname.py`,
numbered in order. A venture does not have to run the full setup or produce [EVALUATION
METRIC] — good evidence is enough. Still, put a venture on the real test bench every so often;
that's what keeps exploration from drifting into endless, untested ideation. Scratch outputs
(logs, plots, checkpoints) go to `ventures/scratch/`, which is not tracked.

A venture file is **immutable once its row is in `ventures.tsv`**. The row points to the file,
so the file must keep showing exactly what produced that observation. Work on the trunk and
leave venture files uncommitted while you explore; they are committed in one batch at the
handoff.

### What you can't do

Ventures may read [FIXED FILES] but never modify them. [EXPERIMENT FILE] stays untouched too —
the one exception is the handoff, where writing the Viable Proof into it is the deliberate last step of
leaving this mode, not something you do along the way.

The constraints that hold in every mode — no new dependencies, [FIXED FILES] stay read-only,
the evaluation is ground truth — are listed in `program.md`.

### Timeout

Every venture that runs code gets a fixed wall-clock budget — [VENTURE TIME BUDGET] (e.g. 5
minutes) is a reasonable default, shorter than a full exploitation run since a venture only
needs to produce signal, not a finished result.

Enforce it mechanically, not by judgment: launch the venture under a shell timeout instead of
watching the clock yourself, e.g.

```
PYTHONPATH=. timeout 300 uv run ventures/NNNN_shortname.py > venture.log 2>&1
```

(`PYTHONPATH=.` lets a venture in `ventures/` import [FIXED FILES] from the repository root.)

A venture that hits the timeout should still be logged as one
in `ventures.tsv` like any other venture, with the observation stating that it was cut off and
what you saw up to that point (e.g. "killed at 5min timeout, loss still falling").

### Revisiting a venture

You can work a venture more than once, but every pass is a new file with the next number
(e.g. `0024_ssm_mixing_pass2.py`, copied from `0023_ssm_mixing.py` and then changed) and its
own row — never edit a logged venture file, never fold multiple attempts into one silent
update. If you notice yourself refining the same venture repeatedly,
check whether you are still open mindedly exploring or have quietly slid into path dependent exploitation.

### Logging results

When a venture is done, log it to `ventures.tsv` (tab-separated, NOT comma-separated — commas break
in descriptions). One row per venture, written as you go.

The TSV has a header row and 3 columns:

```
venture	description	observation
```

1. venture: the venture file name without `.py` (e.g. `0007_drop_component_c`)
2. description: what was tried — the setup or change, in one line
3. observation: what happened — not what it means

Write the observation as what happened, not what you conclude from it.

Example:

```
venture	description	observation
0007_drop_component_c	removed component C from the pipeline	val_bpb changed by <0.001
0008_scale_until_break	scaled width until failure	broke at 4x, by saturating rather than diverging
0011_cross_domain_mechanism	ported mechanism from [X] into this setting	ran, output was unchanged
```

## The Exploration Process

Exploration is an adaptive research process, not a fixed workflow. The following steps define the core activities, but the researcher decides autonomously how to combine them, when to revisit them, and when to change direction.

### 1. Open the Search Space

Understand the current research landscape without treating the current branch as its boundary.

Read `ventures.tsv`, recent results and relevant context. Use these as signals, not as the limits of exploration. Look for anomalies and open questions, but also deliberately look beyond what has already been tried.

Research the domain, inspect new technologies and developments, transfer ideas across disciplines, reconsider the problem from first principles, or radically simplify its formulation. You may perform internet research on these topics.

The goal is to identify **interesting research possibilities**, not merely extend the current path.

Collect several possibilities before judging any of them. The first one that comes to mind is usually just the most available, not necessarily the most promising.

### 2. Develop a Research Direction

Turn promising possibilities into a concrete research direction.

Use research, reasoning and conceptualisation to understand its mechanism, assumptions, novelty and potential. Compare alternatives and determine what would constitute meaningful evidence.

Choose a direction based on judgment rather than a fixed scoring system. The result should be a sufficiently concrete concept that can be investigated through one or more Ventures.

### 3. Investigate Through Ventures

Use Ventures to investigate the current research direction.

Implement enough of the concept to investigate its core assumptions; do not artificially minimize the experiment when deeper implementation is necessary to learn.

Run one Venture or a sequence of Ventures depending on what the direction requires. Use their results, together with ongoing research and reasoning, to deepen, modify, branch or abandon the direction.

Log Ventures and their observations in `ventures.tsv`.

### 4. Reorient When Useful

Reorientation is a recurring activity, not a mandatory step after every Venture.

Step back when new evidence changes the picture, when several Ventures have accumulated, when a direction becomes unclear or exhausted, or when you suspect path dependence.

Reassess the broader research space and decide whether to:

**continue** the current direction,
**branch** into a related direction,
**change** to a fundamentally different direction, or
**formalize** the current direction.

Do not continue merely because previous work has been invested. Watch for path dependence, fixation, confirmation bias and premature convergence.

The researcher may move freely between developing ideas, researching, reasoning, running Ventures and reorienting. The appropriate rhythm depends on the research situation.

#### Avoiding Self-Referential Path Dependence

Step back when the exploration shows clear signs of path dependence:

* you keep adding detail without changing the underlying idea
* the approach is becoming increasingly complex as you reason about it
* the search radius has narrowed without a result that justified narrowing it
* experiments increasingly test details
* you elaborate your own last idea instead of questioning it
* you build an argument for the direction you already picked

When these patterns appear, immeadiatly step back. Do not respond by refining the same idea further.

##### Tabula Rasa

If the pattern persists, deliberately abandon the current line of investigation.

Drop its assumptions, framing and solution path. Start a **new investigation from first principles**: formulate a different question or mechanism, explore a different conceptual approach, or draw on a different domain.

The objective is not to repair the current idea, but to create genuine distance from it.

### 5. The Schaltraum

The Schaltraum is a regular practice that gives exploration structure without turning it into a rigid process. Exploration naturally produces loose ideas, observations, experiments, and shifting directions. The Schaltraum periodically brings these together, formalizes the most promising thread, and turns it into something that can be systematically tested.

At regular intervals, take the current research direction and translate it into a runnable, standardized experiment against [EVALUATION METRIC]. This creates a shared structure for comparing different ideas, reveals what actually holds up under evaluation, and turns scattered exploration into a concrete research artifact.

The Schaltraum therefore serves two purposes:

* **Structure:** It periodically consolidates loose exploration into a clear, reproducible research setup.
* **Feedback:** It tests that setup against [EVALUATION METRIC], grounding exploration in evidence rather than interesting observations alone.

If the result is promising, the artifact can become the basis for an Viable Proof or a more systematic exploitation loop. If not, the result becomes input for further exploration.

The Schaltraum is not a verdict or a separate mode. It is the recurring practice that gives exploration a rhythm of **explore → consolidate → formalize → test → explore again**.

## Handoff to Exploitation

Leave exploration when a research direction has become sufficiently promising that systematic development is now more valuable than further open-ended search.

This usually means:

* the direction has produced meaningful evidence, not just an interesting idea
* its core concept is sufficiently understood to formulate a **Viable Proof**
* further progress is likely to come from implementation, optimization and systematic testing rather than from finding another fundamentally different approach

Do not hand off merely because a Venture worked. Stay in exploration when the result is still ambiguous, the underlying idea is poorly understood, or substantially different directions remain worth investigating.

### Viable Proof

The **Viable Proof** is the handoff artifact: a minimal, runnable realization of the research direction that puts its core idea onto the real evaluation setup.

It should be:

* runnable against the evaluation metric
* simple enough to clearly represent the essential idea
* complete enough to produce meaningful evidence

Before handing off, test it: build the Viable Proof as a venture of its own
(`ventures/NNNN_<name>_proof.py`), run it on the real setup with the full [TIME BUDGET] instead
of [VENTURE TIME BUDGET], and log it in `ventures.tsv` with the [EVALUATION METRIC] it
produced. A Viable Proof that does not run and produce the metric cannot be handed off.

Once it runs, **whether to hand it off is your decision alone** — you carry both the
responsibility and the authority for it. The reasons to exploit a direction vary; the points
above describe typical cases, not conditions. The Viable Proof does not need to beat `best`.

Choose the base the Viable Proof starts from, whichever fits the direction:

* `best` — build on the current [EXPERIMENT FILE] on the trunk; it inherits everything tuned so far
* `original` — build on the unmodified starting setup (`git show baseline:[EXPERIMENT FILE]`)
* `ground-up` — write [EXPERIMENT FILE] from scratch, e.g. when the direction replaces the core of the setup

### Handoff steps

1. On the trunk, commit all new venture files in one batch:
   `git add ventures/` and `git commit -m "ventures NNNN–MMMM"`.
2. Create the direction's branch: `git checkout -b ambidex/<tag>/DNN`.
3. Copy the tested Viable Proof into [EXPERIMENT FILE], then
   `git add [EXPERIMENT FILE]` and `git commit -m "DNN viable proof: <mechanism>"`.
4. Update `logbook.md`: the direction's row with its base (`best@<hash>`, `original` or
   `ground-up`) and status `handed-off`; *Now* with mode, branch and direction.
5. Read `exploit.md` and continue in the exploitation loop.

If you leave exploration to resume a paused direction instead, do step 1, then check out
that direction's branch and continue with step 4.
