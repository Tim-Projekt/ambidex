#!/usr/bin/env bash
# Create a flat run repository from the template and a setup.
#
#   ./new_run.sh <setup_dir> <target_dir>
#   ./new_run.sh setups/mnist1d ../ambidex-mnist1d
#
# The run repo gets the research org (program.md, explore.md, exploit.md), .gitignore,
# analysis.py and every file of the setup, then an initial commit on main.
# Afterwards: fill in the Parameters table in <target_dir>/program.md, then start the agent.

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
cp "$here"/program.md "$here"/explore.md "$here"/exploit.md "$here"/.gitignore "$here"/analysis.py "$target"/
cp -r "$setup"/. "$target"/

cd "$target"
git init -q -b main
git add -A
git commit -q -m "run setup from $(basename "$setup")"

echo "created $target"
echo "next: fill in the Parameters table in program.md, commit it, then point the agent at program.md"
