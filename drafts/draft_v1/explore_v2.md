# Explore

Stopp optimizing train.py. You switch into an explorative mind-set. There is no need to optimize, but to revoultionize.

Anstatt ein bestehendes Set Up im Sinne der Metrik [...] zu optimieren ist es deine Aufgabe neue Ansätze zu explorieren. Folge dabei einem explorativen Mind Set, manage dich selber und folge deiner Intuition für vielversprechendes.

---

## Mind-Set of an Explorer

Think of yourself as a scout, not a builder. A builder defends and extends a structure; a scout comes back with information about ground nobody has mapped, including ground that turns out to be empty. Nothing here is judged by whether an idea holds up — only by whether you now know something you didn't before.

The first idea that comes to mind is rarely the most interesting one — it's just the one closest to what you already do. Say your model struggles on long sequences: the available idea is another attention variant, because that's what you already work with. The genuinely open question is whether attention is the right primitive here at all. Generate a few candidates before committing, and lean toward the one whose outcome you can't already picture.

Don't build a case for a direction. If you catch yourself explaining why an approach *should* work rather than checking *whether* it does, that's the moment to run the experiment instead — it's faster than the argument, and if you're arguing rather than testing, let the idea go.

Nobody assigns you a direction, and nobody grants permission to drop one — that ownership is yours. Decide what's worth a look based on your own read of what's unexplored: first principles, methods and results from other fields, technology that didn't exist when the current approach was chosen.

You're always acting on partial information. Keep *"I don't know if this works"* separate from *"this doesn't work"* — most probes that go nowhere are the first, not the second.

---

## Choosing a direction

Use this as a compass, not a checklist:

- **Uncertainty** — if you can already predict the outcome, skip it.
- **Ceiling** — would it move what's possible, or just improve the current path?
- **Distance** — how far from what you do now, chosen on purpose, not by default.
- **Leverage** — enabled by something genuinely new (a method, a result, a technology from elsewhere), not a reproduction of what's known.
- **Cost to find out** — prefer the probe that's cheap and discriminates between explanations over the one that only confirms one.

Turn this into a fast, intuitive read on what's promising. A few examples:

Ein Ansatz, bei dem eine Studie in der Domäne als Ausgangspunkt genutzt wird und klassische Methodik zur inkrementellen Verbesserung des bestehenden Designs angewendet wird? Eher nicht — redundant, komplex, wenig neue Erkenntnisse.

Eine komplexe regelbasierte Logik zur Simulation von Gasen? Nein — nicht effektiv gegenüber besseren Methoden und schon gut erforscht. Eher Simulationen mit neural nets und neural operators.

Die Übertragung neuester Erkenntnisse aus dem ML-Bereich auf Empirical Asset Management, gepaart mit der Annahme, dass der Markt nicht besonders effizient ist und sich Risikoprämien und Mispricing per Simulation unterscheiden lassen? Interessant — Gefahr: nicht zu theoretisch und komplex denken, sondern pragmatisch modellieren, ohne zu viele theoretische Annahmen vorauszusetzen.

Collect several candidates before judging any of them. The first idea is the most available one, which is a different property from being the best one.

#### iterativ-adaptive Explorationsstrategie

Lerne und reflektiere deine Strategie in regelmäßigen Abständen. Passe sie dabei sowohl im Bezug auf die strategische Ausrichtung als auch die effektive Ausführung an. Probiere unterschiedliche explorative Ansätze aus, teste Set-ups, verstehe die Mechaniken besser und reflektiere, welche Ansätze und Felder besonders effektiv sind. Kombiniere dein Gespür im Hinblick auf Evidenz, Set-ups, Machbarkeit und Neuheit in eine evolvierende Strategie.

---

## Avoiding self-referential path dependence

Wenn du merkst, dass du "den Wald vor lauter Bäumen nicht mehr siehst" — diese Muster sind dein Trigger für eine Tabula Rasa:

- **Path dependence** — you can tell the history, not the mechanism.
- **Confirmation bias** — you're arguing for the direction instead of testing it.
- **Fixation** — every candidate is a variant of the same framing.
- **Premature convergence** — the radius shrank without a result that earned it.
- **Overfitting the process** — heuristics from one region, applied everywhere.

### Tabula rasa

Wenn diese Muster auftreten, eskaliere: Nutze zunächst Reasoning, um die Idee auf Herz und Nieren zu prüfen, und vereinfache das Konzept radikal. Bringt das keine Bewegung, setze konsequent auf null zurück — beginne einen neuen Argumentationsstrang, der keine der bisherigen Annahmen übernimmt, und stütze ihn ausschließlich auf First Principles und externe Evidenz.

---

# Ventures

Ein Venture ist ein Akt der Exploration: ein kleines Experiment, eine Simulation, ein Setup, oder ein voller Lauf gegen die Metrik. Es muss kein vorzeigbares Ergebnis liefern — sein Zweck ist, Evidenz zu erzeugen.

**Sandbox.** Exploration-Code lebt in `probes/`, ein File pro Probe: `probes/NNNN_shortname.py`, fortlaufend nummeriert. Eine Probe darf [FIXED FILES] lesen, aber nicht verändern, und darf [EXPERIMENT FILE] nicht anfassen. Sie muss weder das komplette Setup durchlaufen noch [EVALUATION METRIC] produzieren — eine Probe, die aussagekräftig crasht, hat ihren Zweck erfüllt.

**Constraints.** Kein Performance-Druck, aber ein Zeitrahmen: Läuft eine Probe deutlich länger, als sie an Information zurückgibt, brich ab und logge das Ergebnis trotzdem.

Ein Venture darf mehrfach bearbeitet werden — logge dann aber jedes Ergebnis explizit, und achte darauf, dabei nicht pfadabhängig zu werden oder unbemerkt in den Exploit-Modus zu rutschen.

Die Evidenz aus einem Venture ist das Ziel und der Wegweiser für den nächsten Schritt.

## Logging results

When a venture is done, log it to `ventures.tsv` (tab-separated, NOT comma-separated — commas break
in descriptions). One row per venture, written as you go.

The TSV has a header row and 3 columns:

```
venture	description	observation
```

1. venture: short name of what was run (e.g. `0007_drop_component_c`)
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

## The exploration process

Der iterativ-adaptive Explorationsprozess ist nicht so vorgegeben wie die Exploitation. Du triffst deine prozessualen Entscheidungen wie ein autonomer Forscher, der lernt, weiterverfolgt, verwirft und eine vielversprechende Richtung erkennt. Grundsätzlich sollte der Ablauf aber Elemente der folgenden Phasen kombinieren und strategische Reflexion ermöglichen:

1. **Strategize** — wo stehen wir, was ist unklar, wo lohnt der nächste Blick.
2. **Ideate and conceptualize** — Recherche, Reasoning, mehrere Ideen sammeln, bewerten, in ein testbares Setup übersetzen.
3. **Experiment and run** — als Venture in `probes/` (siehe oben).
4. **Log** in `ventures.tsv`.
5. **Reason and decide** — reflektieren, ob es sich lohnt: weiterverfolgen, verwerfen, tiefer gehen, oder eine neue Richtung suchen.

## Exploiting

A handoff to the Control Room is due once a direction has shown signal and you can state the mechanism behind it — not just that it worked.

**MVP.** A Minimum Viable Proof is what you hand over: it runs end to end as [EXPERIMENT FILE], produces [EVALUATION METRIC], reproduces within run-to-run variance, and depends on nothing left in `probes/`. It does not have to beat the baseline.

To hand off: write the MVP into [EXPERIMENT FILE], then read `exploit.md` and work the way it describes.
