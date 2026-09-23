"""
Progress chart for a run: reads results.tsv and ventures.tsv, writes progress.png.

    uv run analysis.py            # lower metric is better (default)
    uv run analysis.py --higher   # higher metric is better

For the human, not for the agent.
"""

import csv
import sys

import matplotlib.pyplot as plt


def read_tsv(path):
    try:
        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f, delimiter="\t"))
    except FileNotFoundError:
        return []


higher = "--higher" in sys.argv
results = read_tsv("results.tsv")
ventures = read_tsv("ventures.tsv")

fig, ax = plt.subplots(figsize=(14, 6))

# every non-crash experiment, colored by direction
directions = sorted({r["direction"] for r in results})
for d in directions:
    pts = [(i, float(r["metric"])) for i, r in enumerate(results)
           if r["direction"] == d and r["status"] != "crash"]
    if pts:
        xs, ys = zip(*pts)
        ax.scatter(xs, ys, s=18, label=d)

# kept experiments and the running best across all directions
best, frontier = None, []
for i, r in enumerate(results):
    if r["status"] == "keep":
        v = float(r["metric"])
        if best is None or (v > best if higher else v < best):
            best = v
    if best is not None:
        frontier.append((i, best))
if frontier:
    xs, ys = zip(*frontier)
    ax.step(xs, ys, where="post", color="black", linewidth=1, label="best so far")

ax.set_xlabel("experiment #")
ax.set_ylabel("metric")
ax.set_title(f"{len(results)} experiments, {len(directions)} directions, {len(ventures)} ventures")
ax.legend()
fig.tight_layout()
fig.savefig("progress.png", dpi=120)
print(f"wrote progress.png, best: {best}")
