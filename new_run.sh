#!/usr/bin/env bash
# Create a flat run repository from the template and a setup.
#
#   ./new_run.sh <setup_dir> <target_dir>
#   ./new_run.sh setups/shakespeare ../ambidex-shakespeare
#
# The run repo gets the research org (program.md, explore.md, exploit.md), .gitignore,
# the plotting scripts and every file of the setup, then an initial commit on main.
# If the setup has a params.md, it replaces the Parameters section of program.md;
# otherwise fill in that table by hand and commit it before starting the agent.

set -euo pipefail

if [ $# -ne 2 ]; then
  echo "usage: $0 <setup_dir> <target_dir>" >&2
  exit 1
fi

here="$(cd "$(dirname "$0")" && pwd)"
setup="$1"
target="$2"

[ -d "$setup" ] || { echo "setup not found: $setup" >&2; exit 1; }
[ -e "$target" ] && { echo "target already exists: $target" >&2; exit 1; }

mkdir -p "$target"
cp "$here"/program.md "$here"/explore.md "$here"/exploit.md "$here"/.gitignore \
   "$here"/analysis.py "$here"/plot_directions.py "$target"/
tar -C "$setup" --exclude=.venv --exclude=__pycache__ --exclude=params.md -cf - . | tar -C "$target" -xf -

if [ -f "$setup/params.md" ]; then
  # replace everything from "## Parameters" up to (not including) "## Glossary"
  awk -v params="$setup/params.md" '
    /^## Parameters/ { while ((getline line < params) > 0) print line; skip = 1; next }
    /^## Glossary/   { skip = 0 }
    !skip
  ' "$here/program.md" > "$target/program.md"
  filled=1
fi

cd "$target"
git init -q -b main
git add -A
git commit -q -m "run setup from $(basename "$setup")"

echo "created $target"
if [ "${filled:-0}" = 1 ]; then
  echo "next: uv sync, then point the agent at program.md"
else
  echo "next: fill in the Parameters table in program.md, commit it, then point the agent at program.md"
fi
