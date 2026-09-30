## Parameters

The parameters of this run. Everywhere else, the files refer to these names.

| Parameter | Meaning | Value |
|---|---|---|
| [EXPERIMENT FILE] | the single file exploitation edits | `train.py` |
| [FIXED FILES] | read-only: evaluation, data pipeline, fixed constants | `prepare.py` |
| [EVALUATION METRIC] | ground-truth metric, and which direction is better | `val_bpc`, lower is better |
| [RESOURCE CONSTRAINT] | soft resource limit reported by each run | `peak_mem_mb` (keep well below the RAM of your machine) |
| [RUN COMMAND] | runs [EXPERIMENT FILE] once | `uv run train.py` |
| [TIME BUDGET] | fixed training time per run | 60 s |
| [RUN TIMEOUT] | hard wall-clock limit per run, incl. overhead | 3 min |
| [VENTURE TIME BUDGET] | hard wall-clock limit per venture | 2 min |
| [SETUP CHECK] | what must exist before the first run | `~/.cache/ambidex-shakespeare/input.txt` exists (`uv run prepare.py`) |

