"""
"Directions compared": best result of each line of research, in real metric values.
Reads results.tsv (columns: direction, metric, status[keep/discard/crash]). Task-agnostic.

    python plot_directions.py
    python plot_directions.py --higher --metric-name accuracy --labels "D01=cnn,D02=svm"
    python plot_directions.py --out plots --dpi 160

Every direction starts at x = 0 (its own experiment counter), so directions that ran one
after the other sit side by side. The first row of results.tsv is the unmodified
baseline run (by protocol); it is drawn as a reference line, or noted when it lies far outside,
and does not set the y-range.
"""

import argparse
import csv
import os
from collections import OrderedDict

import matplotlib.pyplot as plt
import numpy as np

PALETTE = ["#4361ee", "#f4a261", "#2a9d8f", "#e76f51", "#9b5de5", "#00b4d8", "#8d99ae", "#c9184a"]

plt.rcParams.update({
    "axes.facecolor": "white", "figure.facecolor": "white", "axes.edgecolor": "#444",
    "axes.grid": True, "grid.color": "#e6e8ec", "axes.axisbelow": True,
    "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
    "axes.titlesize": 13, "axes.titleweight": "bold", "axes.titlelocation": "left",
})


def load(path, higher, labels):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    dirs, baseline = OrderedDict(), None
    for r in rows:
        try:
            v = float(r["metric"])
        except (KeyError, ValueError, TypeError):
            continue
        st = (r.get("status") or "").strip().lower()
        if st == "crash" or not np.isfinite(v):
            continue
        if baseline is None:  # by protocol the first row is the unmodified baseline run
            baseline = v
            continue
        dirs.setdefault(r["direction"], []).append((v, st == "keep"))
    pick = max if higher else min
    out = []
    for k, (d, pts) in enumerate(dirs.items()):
        vals = np.array([p[0] for p in pts])
        out.append(dict(
            label=f"{d} · {labels[d]}" if d in labels else d,
            color=PALETTE[k % len(PALETTE)], vals=vals, kept=np.array([p[1] for p in pts]),
            rb=np.array([pick(vals[: i + 1]) for i in range(len(vals))]),
        ))
    return out, baseline


def plot(dirs, baseline, higher, name):
    allv = np.concatenate([d["vals"] for d in dirs])
    pad = 0.06 * (allv.max() - allv.min())
    lo, hi = allv.min() - pad, allv.max() + pad

    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.set_ylim(lo, hi)
    notes = []
    if lo <= baseline <= hi:
        ax.axhline(baseline, color="#888", lw=1.3, ls="--", zorder=1)
        ax.text(0.995, baseline, f"baseline {baseline:.3f}", transform=ax.get_yaxis_transform(),
                ha="right", va="bottom" if not higher else "top", fontsize=9, color="#666")
    else:
        notes.append(dict(label="baseline", rb=[baseline], color="#666"))
    for d in dirs:
        x = np.arange(len(d["vals"]))
        ax.step(x, d["rb"], where="post", color=d["color"], lw=2.6, zorder=4,
                label=f"{d['label']}  ({len(x)} experiments)")
        ax.scatter(x[~d["kept"]], d["vals"][~d["kept"]], s=14, color=d["color"], alpha=0.25, zorder=3)
        ax.scatter(x[d["kept"]], d["vals"][d["kept"]], s=34, color=d["color"], edgecolors="white",
                   linewidths=0.8, zorder=5)
        ax.scatter(x[-1:], d["rb"][-1:], s=80, color=d["color"], edgecolors="#1b1f27", linewidths=1.2, zorder=6)
        # real values at start and end of the direction
        sign = 1 if not higher else -1
        if len(x) > 1:
            ax.annotate(f"{d['vals'][0]:.3f}", (0, d["vals"][0]), xytext=(8, 9 * sign),
                        textcoords="offset points", fontsize=9, color=d["color"], fontweight="bold")
        ax.annotate(f"{d['rb'][-1]:.3f}", (x[-1], d["rb"][-1]), xytext=(10, 0),
                    textcoords="offset points", va="center", fontsize=10, fontweight="bold", color=d["color"])
    for k, d in enumerate(notes):
        ax.text(0.99, 0.97 - 0.055 * k, f"{d['label']}: {d['rb'][-1]:.3f}  (off scale)",
                transform=ax.transAxes, ha="right", va="top", fontsize=9, color=d["color"])
    ax.set_xlabel("experiments within the direction")
    ax.set_ylabel(f"best {name} so far ({'higher' if higher else 'lower'} is better)")
    ax.set_title("Directions compared")
    ax.legend(frameon=False, loc="center right" if notes else "upper right")
    ax.set_xlim(-0.8, max(len(d["vals"]) for d in dirs) + 4)
    fig.tight_layout()
    return fig


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", default="results.tsv")
    ap.add_argument("--out", default="plots")
    ap.add_argument("--higher", action="store_true", help="higher metric is better")
    ap.add_argument("--metric-name", default="val_bpc")
    ap.add_argument("--labels", default="", help='e.g. "D01=transformer,D02=n-gram"')
    ap.add_argument("--dpi", type=int, default=150)
    a = ap.parse_args()

    labels = dict(p.split("=", 1) for p in a.labels.split(",") if "=" in p)
    dirs, baseline = load(a.results, a.higher, labels)
    if not dirs:
        raise SystemExit(f"no plottable rows in {a.results}")
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, "directions.png")
    plot(dirs, baseline, a.higher, a.metric_name).savefig(path, dpi=a.dpi, bbox_inches="tight")
    print("wrote", path)


if __name__ == "__main__":
    main()
