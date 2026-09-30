# Tiny Shakespeare, CPU

Character-level language modeling on Tiny Shakespeare (~1.1M characters, 65-character
vocabulary), trained on CPU for a fixed 60-second budget. The metric is validation bits per
character (`val_bpc`, lower is better).

- `prepare.py` — fixed: download, 90/10 split, vocabulary, `evaluate_bpc`, memory measurement.
- `train.py` — the experiment file. Baseline: a small decoder-only transformer.

The evaluation is model-agnostic: anything that turns a batch of character contexts into
next-character log-probabilities can be evaluated (neural networks, n-gram or compression
models, hybrids). See the `evaluate_bpc` docstring for the contract. Reference points: a
uniform model scores log2(65) ≈ 6.02 bpc; Karpathy's char-rnn (~3M parameters, trained far
longer) reaches around 1.3 bpc.

## Parameters

The parameters for this task are in `params.md`. `new_run.sh` writes them into the Parameters
section of `program.md` when it creates the run repo.
