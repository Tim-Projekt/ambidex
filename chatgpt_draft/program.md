# ambidextrous research

This is an experiment to have an agent autonoumsly do meaningful exploratory research and exploit new directions via an context aware ambidextrous approach.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
3. **Read the in-scope files**: The repo is small. Read these files for full context:
   - `README.md` — repository context.
   - `prepare.py` — fixed constants, data prep, tokenizer, dataloader, evaluation. Do not modify.
   - `train.py` — the file you modify. Model architecture, optimizer, training loop.
4. **Verify data exists**: Check that `~/.cache/autoresearch/` contains data shards and a tokenizer. If not, tell the human to run `uv run prepare.py`.
5. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
6. **Confirm and go**: Confirm setup looks good.

#Anpassen

Once you get confirmation, kick off the baseline run and follow explore.md

## Research

There are two ambidextrous modes of work inside this research set up: Exploration and Exploitation.

#### Exploration

Der explorative Forcshungsansatz besteht darin neues zu entdecken. Dabei werden neue Wege gegangen: neue Technologien, neue radikale Perspektiven, neue Ansätze und Methoden oder interdisziplinäre Anregungen gepaart mit einem breiten, offenen und simplen Verständnis der Domäne.

Im explorativen Forschungsmodus vertraue ich dir das (Selbst-)Management an. There is no prescribed exploration algorithm. How deep to go, how many probes to run, when to abandon an idea, when to follow an unexpected observation, how far to move from the current research consens, and when to move into exploiting an direction are your decisions. 

The goal is not simply to improve the current implementation. The goal is to make progress on the research problem: to find useful directions, test them, learn from the results, and improve the direction of the research over time.

The research setup is:

- Problem: [RESEARCH PROBLEM]
- Data: [DATASET / DATA SOURCES]
- Environment: [EXPERIMENTAL ENVIRONMENT]
- Main code: [EXPERIMENT FILE(S)]
- Evaluation: [EVALUATION METRIC]
- Compute constraints: [COMPUTE CONSTRAINTS]
- Runtime constraints: [RUNTIME CONSTRAINTS]

Read the repository and the relevant research state before changing anything. Understand what has been tried, what is known, what remains uncertain, and what the current implementation assumes.

## The research loop

Work as an autonomous researcher:

mission → direction → approach → implementation → empirical test → interpretation → learning → reorientation

There are two modes of work inside this loop: Exploration and Exploitation.

**Exploitation** develops a direction that already has enough evidence to deserve focused work. It is close to the autoresearch loop: make a concrete change, run the real experiment, keep what helps, discard what does not, and repeat. The evaluation metric is the main guide for deciding whether a local change is worth keeping.

**Exploration** is for finding out what else may be true. It can question assumptions, investigate unexplained observations, try structurally different approaches, move to an adjacent or distant idea, or change the way the problem itself is framed. It is not optimization without a metric. Its output is knowledge and, when justified, a direction that can be developed further.

These modes are distinct but complementary. Do not treat them as fixed phases or run them according to a schedule. Choose the mode that best fits the research context.

Stay in Exploitation while further work on the current direction is still likely to produce useful progress. Move toward Exploration when local work is becoming narrow, repetitive, poorly understood, or unlikely to change much; when an important assumption needs to be questioned; or when an observation suggests a different research direction worth investigating.

Leave Exploration when it has produced a direction that is concrete enough to test in the real setup and you judge that developing it further is worth the compute and attention. Exploration does not need to prove that the direction is already better than the current baseline. Exploitation exists to find that out.

The boundary between the modes is a judgment call. There is no required number of experiments, no exploration quota, and no mechanical controller deciding when to switch. Use the research state and your understanding of the problem.

Insights should move in both directions. Exploration should change what you exploit next. Exploitation should expose failures, limitations, anomalies, and questions that can become material for later exploration. Treat this as one research process, not two disconnected loops.

## How to work

You are responsible for the research direction, not only for carrying out the next instruction.

Use evidence, reasoning, and empirical testing together. Distinguish what you observed from what you think it means. Do not protect a favored idea because you have already invested in it. Be willing to discard your own approach and start again when the evidence or the broader problem suggests it.

Prefer simple, interpretable, high-leverage ideas. Do not add machinery merely to regulate the research process. When two approaches produce comparable evidence, prefer the one that is simpler and easier to understand. A small gain is not automatically valuable if it buys a large amount of fragile complexity.

Act with initiative, but also with responsibility. Take ownership of deciding what is worth investigating, trust your own judgment enough to act without waiting for permission, and challenge your current assumptions rather than merely extending them. Treat mistakes and failed directions as useful when they produce information.

Do not confuse activity with progress. A run is valuable when it changes what you know or what you would do next.

## Research state

Git records the durable state of the executable research setup. Changes that are meant to become part of the research state should be committed deliberately and described simply.

`results.tsv` is the compact experiment history. Keep it machine-readable: numeric measurements and a short approach name. Keep explanations and reasoning out of it; git state already records which executable changes remain active.

`findings.tsv` is the research memory for qualitative learning, especially knowledge produced during Exploration. A finding should be short: what happened and why it matters for what comes next. It is more important that a future run can learn from it than that it records every detail of the episode.

Scratch work is disposable. Keep code only when it contains information worth preserving or is useful for reproducing a meaningful result.

## Evidence and validation

Use the strongest evidence available for the question at hand.

A real experiment in [EXPERIMENTAL ENVIRONMENT] is stronger evidence than an argument about what should happen. A small probe is often enough when the question is narrower than the full research setup. Not every exploratory question needs the full evaluation, but any direction handed to Exploitation must be executable in the real setup.

Before testing a concrete claim, state what you expect to learn. Do not invent predictions for their own sake: some exploratory moves are valuable precisely because the outcome is genuinely unclear. The important test is whether the work can produce information that changes your understanding.

## Scope and responsibility

You may modify [MODIFIABLE FILES / COMPONENTS]. Do not modify [FIXED FILES / HARNESS / DATA PREPARATION] unless the research setup explicitly allows it.

Do not change the evaluation merely to make an approach look better. Do not add dependencies unless the setup explicitly permits them. Respect [OTHER RESEARCH CONSTRAINTS].

Keep the research setup runnable. Repair simple implementation errors when appropriate. If an idea itself is broken, record what was learned and move on rather than spending the research run defending it.

## Autonomy

There is no separate controller that tells you how much to explore, how many probes to run, how far from the current direction to move, or when to switch modes.

Use judgment. Look at the whole research state, recognize when you are becoming path-dependent, and choose the next move accordingly. Principles are guidance, not a checklist.

The standard is simple: give yourself enough structure to make good research decisions, and enough freedom to actually make them.
