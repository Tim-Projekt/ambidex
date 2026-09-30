"""
Data preparation and evaluation for character-level language modeling on Tiny Shakespeare.
Downloads the text once; provides the fixed data split, the vocabulary and the evaluation.

Usage:
    uv run prepare.py        # download data (one-time, ~1 MB)

Data is stored in ~/.cache/ambidex-shakespeare/.
This file is fixed: do not modify it.
"""

import math
import os
import sys
import urllib.request

import torch
import torch.nn.functional as F

# ---------------------------------------------------------------------------
# Constants (fixed, do not modify)
# ---------------------------------------------------------------------------

TIME_BUDGET = 60   # training time budget in seconds (wall clock)
EVAL_LEN = 256     # evaluation chunk length: each char is predicted from its preceding chars in the chunk

DATA_URL = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "ambidex-shakespeare")
DATA_PATH = os.path.join(CACHE_DIR, "input.txt")

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

def download():
    if os.path.exists(DATA_PATH):
        print(f"Data: already at {DATA_PATH}")
        return
    os.makedirs(CACHE_DIR, exist_ok=True)
    print(f"Data: downloading {DATA_URL}")
    urllib.request.urlretrieve(DATA_URL, DATA_PATH)
    print(f"Data: saved to {DATA_PATH}")


def load_data():
    """
    Returns (train_ids, val_ids, vocab).
    train_ids, val_ids: 1-D LongTensors of character ids (first 90% / last 10% of the text).
    vocab: sorted list of all characters in the text; id i <-> vocab[i].
    """
    if not os.path.exists(DATA_PATH):
        sys.exit(f"Data not found at {DATA_PATH}. Run: uv run prepare.py")
    with open(DATA_PATH, encoding="utf-8") as f:
        text = f.read()
    vocab = sorted(set(text))
    stoi = {c: i for i, c in enumerate(vocab)}
    ids = torch.tensor([stoi[c] for c in text], dtype=torch.long)
    n = int(0.9 * len(ids))
    return ids[:n], ids[n:], vocab

# ---------------------------------------------------------------------------
# Evaluation (fixed, this is the ground truth)
# ---------------------------------------------------------------------------

@torch.no_grad()
def evaluate_bpc(logprob_fn, batch_size=64):
    """
    Validation bits per character.

    The validation text is cut into non-overlapping chunks of EVAL_LEN + 1 characters.
    For each chunk, x = chunk[:-1] and y = chunk[1:]; every character of y is predicted
    from the characters before it within the same chunk.

    logprob_fn(x) gets a LongTensor of shape (B, EVAL_LEN) and must return log-probabilities
    of shape (B, EVAL_LEN, len(vocab)), where [b, t] is the distribution over the next
    character after x[b, :t+1]. It must not look at later positions.
    Any model works (neural or not), as long as it follows this contract.
    """
    _, val_ids, vocab = load_data()
    n_chunks = (len(val_ids) - 1) // (EVAL_LEN + 1)
    chunks = val_ids[: n_chunks * (EVAL_LEN + 1)].view(n_chunks, EVAL_LEN + 1)
    total_nats, total_chars = 0.0, 0
    for i in range(0, n_chunks, batch_size):
        batch = chunks[i : i + batch_size]
        x, y = batch[:, :-1], batch[:, 1:]
        logp = logprob_fn(x)
        assert logp.shape == (x.shape[0], EVAL_LEN, len(vocab)), f"bad logprob shape {tuple(logp.shape)}"
        logp = logp.float().log_softmax(-1)  # renormalize defensively
        total_nats += F.nll_loss(logp.reshape(-1, len(vocab)), y.reshape(-1), reduction="sum").item()
        total_chars += y.numel()
    return total_nats / total_chars / math.log(2)

# ---------------------------------------------------------------------------
# Resource measurement
# ---------------------------------------------------------------------------

def peak_memory_mb():
    """Peak resident memory of this process in MB (Windows, Linux, macOS)."""
    import psutil
    info = psutil.Process().memory_info()
    if hasattr(info, "peak_wset"):  # Windows
        return info.peak_wset / 1024**2
    import resource
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return peak / 1024**2 if sys.platform == "darwin" else peak / 1024


if __name__ == "__main__":
    download()
    train_ids, val_ids, vocab = load_data()
    print(f"Train: {len(train_ids):,} chars | Val: {len(val_ids):,} chars | Vocab: {len(vocab)}")
    uniform = evaluate_bpc(lambda x: torch.full((x.shape[0], x.shape[1], len(vocab)), -math.log(len(vocab))))
    print(f"Sanity check, uniform model: val_bpc = {uniform:.4f} (expected {math.log2(len(vocab)):.4f})")
