# ambidex

![Ambidextrous organizations – How to embrace disruption and ...](https://www.adlittle.com/sites/default/files/capture_du_2018-04-27_14-52-32.png)

Autonomous, ambidextrous research: an agent that switches by itself between **exploration**
(finding new directions) and **exploitation** (pushing one direction as far as it goes).
Inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch), which is pure
exploitation.

## Layout

```
program.md  explore.md  exploit.md   the research org: agent instructions (a template)
.gitignore  analysis.py              copied into every run
setups/<name>/                       task-specific code: prepare.py, train.py, pyproject.toml
new_run.sh                           creates a flat run repo from template + setup
ambidex_v0/                          karpathy's autoresearch snapshot (reference, needs an H100)
```

This repo is where the research org is designed. Runs happen elsewhere, one flat repo per run,
like autoresearch: the setup *is* the repo.

## Starting a run

```bash
./new_run.sh setups/<name> ../ambidex-<name>
cd ../ambidex-<name>
# fill in the Parameters table in program.md, commit it
uv sync
```

Then open your agent in the run repo and prompt something like:

```
Read program.md and let's set up a new run.
```

While it runs: `uv run analysis.py` (add `--higher` if a higher metric is better) writes
`progress.png`; `logbook.md` shows where the research stands.
