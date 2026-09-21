Ergebni# ambidextrous research

This is an experiment to have an agent autonoumsly do meaningful exploratory research and exploit new directions via an context aware ambidextrous approach.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
3. **Read the in-scope files**: The repo is small. Read these files for full context:
   - `README.md` — repository context.
   - `prepare.py` — fixed constants, data prep, tokenizer, dataloader, evaluation. Do not modify.
   - `train.py` — the file you modify. Model architecture, optimizer, training loop.
4. Hier ggf. was zu scope und responsibilitys sagen (wo lebt was, was darf geändert werden was nicht; altertnative: untenfür die beiden Phasen dezidert staten)
5. **Verify data exists**: Check that `~/.cache/autoresearch/` contains data shards and a tokenizer. If not, tell the human to run `uv run prepare.py`.
6. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
7. **Confirm and go**: Confirm setup looks good.

#Anpassen

Once you get confirmation, kick off the baseline run and follow explore.md

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

## Research

There are two ambidextrous modes of work inside this research set up: Exploration and Exploitation.

#### Exploration

Der explorative Forcshungsansatz besteht darin neues zu entdecken. Dabei werden neue Wege gegangen: neue Technologien, neue radikale Perspektiven, neue Ansätze und Methoden oder interdisziplinäre Anregungen gepaart mit einem breiten, offenen und simplen Verständnis der Domäne.

Im explorativen Forschungsmodus wird dir das (Selbst-)Management anvertraut. Das geht mit der Verantwortung einher unterschiedliche Ansprüche auszubalancieren. Hier ein grober Überblick:

a) Domäne: Welche Art von exploration ist im angesicht der reife der Domäne, sowie den Spillovers aus anderen Disziplinen sinnvoll und machbar? Wie können lokale, rekombinierende und inkrementelle explorationen gegenüber technologisch getriebenen, radikalen und interdisziplinären Explorationen abgewogen werden?

b) Systems: Wie kann ein adaptiver, selbstgesteuerter Forschungsansatz welcher unter großer Unsicherheit und Varriabilität strategische Abwägungen (verwerfen/verfolgen/vertiefen/formalisieren) treffen muss, mit den Ansprüchen an eine formalisierung, sicherung und Produktivierung von Erkenntnissen in vernünftiger Art und Weise abgewogen und ausbalanciert werden?

c) Prozesstabilität: Wie kann der adaptive, nachforschende und theory building ansatz der die exploration auszeichnet vor selbst referenzierter pfadabhängigkeit („Den Wald vor lauter Bäumen nicht sehen“) und conformation bias geschützt werden? Wie können Reasoning, exploratives Mind-Set, Evidenz und Prozesse kombiniert werden um Prozesstabilität vor Conformation Bias usw. zu schützen?

Im Exploration-Modus gibt es keine externe Metrik, die deine Forschungsrichtungen bewertet oder dir vorgibt, ob ein Ansatz sinnvoll ist. Stattdessen legt `explore.md` eine Mentalität und Heuristiken für eine kalibrierte, kontextsensitive Selbststeuerung dar.

Die Guidance im Exploration-Modus ist damit qualitativ: Deine Entscheidungen beruhen auf eigenem Urteil, Erfahrung, Intuition und den in `explore.md` beschriebenen Heuristiken und sind entsprechend anfällig für Bias. Gerade deshalb ist Prozessstabilität entscheidend: Da dieselbe Instanz sowohl ihr Verhalten steuert als auch ihre eigenen Forschungsrichtungen bewertet, ist eine stabile, selbstkritische und bias-resistente Arbeitsweise die Voraussetzung für gute und nachhaltige Exploration.

Ziel und Antrieb des explorativen Forschungsansatzes ist das Entdecken radikaler Innovationen und völlig neuer Möglichkeiten zur Lösung des vorliegenden Problems [ggf. spezifizieren]

#### Exploitation

Der exploitative Forschungsansatz besteht darin einen gegebenen Ansatz oder eine Forschungsrichtung auszureizen und an die Performance grenzen zu bringen. Dabei zeigt sich, wo die Performance grenzen liegen und wie viel ein neues Konzept im Vergleich zu bestehenden Methoden bringt. Die folgende Übersicht hilft den strukturierten, exploitativen Ansatz in der Praxis umzusetzen unter Berücksichtighung der Constraints und der quantitaiven Metrik, die dich guided.

Each experiment runs on a single GPU. The training script runs for a **fixed time budget of 5 minutes** (wall clock training time, excluding startup/compilation). You launch it simply as: `uv run train.py`.

**What you CAN do:**

- Modify `train.py` — this is the only file you edit. Everything is fair game: model architecture, optimizer, hyperparameters, training loop, batch size, model size, etc.

**What you CANNOT do:**

- Modify `prepare.py`. It is read-only. It contains the fixed evaluation, data loading, tokenizer, and training constants (time budget, sequence length, etc).
- Install new packages or add dependencies. You can only use what's already in `pyproject.toml`.
- Modify the evaluation harness. The `evaluate_bpb` function in `prepare.py` is the ground truth metric.

**The goal is simple: get the lowest val_bpb.** Since the time budget is fixed, you don't need to worry about training time — it's always 5 minutes. Everything is fair game: change the architecture, the optimizer, the hyperparameters, the batch size, the model size. The only constraint is that the code runs without crashing and finishes within the time budget. --> hier das ziel in kontext mit den mechanismen von exploration setzen

**VRAM** is a soft constraint. Some increase is acceptable for meaningful val_bpb gains, but it should not blow up dramatically.

**Simplicity criterion**: All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win. When evaluating whether to keep a change, weigh the complexity cost against the improvement magnitude. A 0.001 val_bpb improvement that adds 20 lines of hacky code? Probably not worth it. A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep.

**The first run**: Your very first run should always be to establish the baseline, so you will run the training script as is.

## Ambidextre Systemintelligenz

Exploration und Exploitation sind keine getrennten Phasen, sondern zwei komplementäre Modi eines gemeinsamen Forschungsprozesses. Exploitation vertieft vielversprechende Ansätze; Exploration erweitert oder hinterfragt den aktuellen Suchraum. Jeder Modus nutzt die Evidenz des anderen: Exploitation kann durch Anomalien oder abnehmenden Erkenntnisgewinn Exploration auslösen, während Exploration neue Richtungen hervorbringt, die anschließend gezielt exploitiert werden.

Der Agent steuert diese Balance selbst aus dem gesamten Forschungszustand. Er fragt fortlaufend: **Was wissen wir, was ist noch unsicher, wo entsteht Erkenntnisgewinn und wo werden wir pfadabhängig?** Daraus wählt er den nächsten Schritt: Ansatz vertiefen, gezielt variieren, Annahme hinterfragen oder Richtung wechseln. Es gibt keine festen Quoten, Budgets oder Umschaltregeln; die Entscheidung ist kontextabhängig.

Über beide Modi hinweg betreibt der Agent Meta-Learning: Erfahrungen verändern nicht nur die Einschätzung einzelner Ansätze, sondern auch das Verständnis darüber, **welche Art von Forschungsschritt unter den aktuellen Bedingungen sinnvoll ist**. Muster, Anomalien, Fehlversuche und erfolgreiche Strategien fließen daher in die nächste Moduswahl ein. Dabei darf Meta-Analyse Exploration nicht zum Selbstzweck machen: Sie soll die nächste Entscheidung verbessern, nicht den Forschungsprozess von der eigentlichen Erkenntnissuche ablenken.

Das Ziel ist weder maximale Exploration noch maximale Exploitation, sondern eine **selbstgesteuerte, kontextsensitive Bewegung zwischen beiden**, bei der jede Phase die andere informiert und der Forschungsprozess aus seinen eigenen Erfahrungen zunehmend besser gesteuert wird.

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

## The exploitation process

The exploitation runs on a dedicated branch (e.g. `autoresearch/mar5` or `autoresearch/mar5-gpu0`). [???]

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

**Handover**: Wenn die bestehende Forschungsrichtung ausgeschöpft ist (z.B. wenn die Ergebnisse konvergieren und mit keinen radikalen Durchbrüchen mehr zu rechnen ist "the metric is still moving a
little" is not by itself a reason to stay.) oder exploration aus de Kontext her sinnvoller wirkt, führe eine Transition durch, indem du explore.md liest.

## The research loop

There are two modes of work inside this loop: Exploration and Exploitation.

**Exploitation** develops a direction that already has enough evidence to deserve focused work. It is close to the autoresearch loop: make a concrete change, run the real experiment, keep what helps, discard what does not, and repeat. The evaluation metric is the main guide for deciding whether a local change is worth keeping.

**Exploration** is for finding out what else may be true. It can question assumptions, investigate unexplained observations, try structurally different approaches, move to an adjacent or distant idea, or change the way the problem itself is framed. It is not optimization without a metric. Its output is knowledge and, when justified, a direction that can be developed further.

These modes are distinct but complementary. Do not treat them as fixed phases or run them according to a schedule. Choose the mode that best fits the research context.

Stay in Exploitation while further work on the current direction is still likely to produce useful progress. Move toward Exploration when local work is becoming narrow, repetitive, poorly understood, or unlikely to change much; when an important assumption needs to be questioned; or when an observation suggests a different research direction worth investigating.

Leave Exploration when it has produced a direction that is concrete enough to test in the real setup and you judge that developing it further is worth the compute and attention. Exploration does not need to prove that the direction is already better than the current baseline. Exploitation exists to find that out.

The boundary between the modes is a judgment call. There is no required number of experiments, no exploration quota, and no mechanical controller deciding when to switch. Use the research state and your understanding of the problem.

Insights should move in both directions. Exploration should change what you exploit next. Exploitation should expose failures, limitations, anomalies, and questions that can become material for later exploration. Treat this as one research process, not two disconnected loops.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!

## Switching modes

You enter a mode by reading its file and working the way it describes:

- `exploit.md` — the optimization loop
- `explore.md` — open-ended investigation

Nothing switches you automatically, and nothing gives you permission. Broadly: you leave
exploitation when the metric has stopped responding to real ideas, and you leave exploration
when you have a direction worth spending compute on. Each file says in detail how it expects
to be left — the judgment is written down where you will be standing when you need it.

Switch when the research says so, not on a schedule and not at a fixed ratio between the two.
