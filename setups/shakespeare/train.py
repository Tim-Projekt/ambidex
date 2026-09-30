"""
Character-level language model on Tiny Shakespeare, trained on CPU for a fixed time budget.
Baseline: a small decoder-only transformer.

Usage:
    uv run train.py
"""

import time

import torch
import torch.nn as nn
import torch.nn.functional as F

from prepare import EVAL_LEN, TIME_BUDGET, evaluate_bpc, load_data, peak_memory_mb

# ---------------------------------------------------------------------------
# Hyperparameters
# ---------------------------------------------------------------------------

SEQ_LEN = EVAL_LEN     # training context length (positions beyond it would be untrained at eval)
BATCH_SIZE = 8
N_LAYER = 3
N_HEAD = 4
N_EMBD = 96
DROPOUT = 0.0
LR = 3e-3
WEIGHT_DECAY = 0.1
WARMUP_STEPS = 50
SEED = 1337

# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

class Block(nn.Module):
    def __init__(self):
        super().__init__()
        self.ln1 = nn.LayerNorm(N_EMBD)
        self.qkv = nn.Linear(N_EMBD, 3 * N_EMBD)
        self.proj = nn.Linear(N_EMBD, N_EMBD)
        self.ln2 = nn.LayerNorm(N_EMBD)
        self.mlp = nn.Sequential(nn.Linear(N_EMBD, 4 * N_EMBD), nn.GELU(), nn.Linear(4 * N_EMBD, N_EMBD))

    def forward(self, x):
        B, T, C = x.shape
        q, k, v = self.qkv(self.ln1(x)).split(N_EMBD, dim=2)
        q, k, v = (t.view(B, T, N_HEAD, C // N_HEAD).transpose(1, 2) for t in (q, k, v))
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True, dropout_p=DROPOUT if self.training else 0.0)
        x = x + self.proj(y.transpose(1, 2).reshape(B, T, C))
        return x + self.mlp(self.ln2(x))


class CharTransformer(nn.Module):
    def __init__(self, vocab_size, max_len):
        super().__init__()
        self.tok = nn.Embedding(vocab_size, N_EMBD)
        self.pos = nn.Embedding(max_len, N_EMBD)
        self.blocks = nn.Sequential(*[Block() for _ in range(N_LAYER)])
        self.ln = nn.LayerNorm(N_EMBD)
        self.head = nn.Linear(N_EMBD, vocab_size)

    def forward(self, idx):
        T = idx.shape[1]
        x = self.tok(idx) + self.pos(torch.arange(T))
        return self.head(self.ln(self.blocks(x)))

# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

t_start = time.time()
torch.manual_seed(SEED)
train_ids, val_ids, vocab = load_data()

model = CharTransformer(len(vocab), max_len=max(SEQ_LEN, EVAL_LEN))
num_params = sum(p.numel() for p in model.parameters())
print(f"Vocab: {len(vocab)} | Params: {num_params:,} | Threads: {torch.get_num_threads()}")

optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY, betas=(0.9, 0.95))


def get_batch():
    ix = torch.randint(len(train_ids) - SEQ_LEN - 1, (BATCH_SIZE,))
    x = torch.stack([train_ids[i : i + SEQ_LEN] for i in ix])
    y = torch.stack([train_ids[i + 1 : i + SEQ_LEN + 1] for i in ix])
    return x, y


model.train()
step, training_time = 0, 0.0
while training_time < TIME_BUDGET:
    t0 = time.time()
    progress = training_time / TIME_BUDGET
    lr_mult = min(1.0, (step + 1) / WARMUP_STEPS) * (1.0 - progress)  # warmup, then linear decay to 0
    for g in optimizer.param_groups:
        g["lr"] = LR * lr_mult
    x, y = get_batch()
    loss = F.cross_entropy(model(x).view(-1, len(vocab)), y.view(-1))
    optimizer.zero_grad(set_to_none=True)
    loss.backward()
    optimizer.step()
    training_time += time.time() - t0
    step += 1
    if step % 50 == 0:
        print(f"step {step:05d} | loss {loss.item():.4f} | lr {LR * lr_mult:.2e} | {training_time:.0f}s/{TIME_BUDGET}s", flush=True)

# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

model.eval()
val_bpc = evaluate_bpc(lambda x: F.log_softmax(model(x), dim=-1))

print("---")
print(f"val_bpc:          {val_bpc:.6f}")
print(f"training_seconds: {training_time:.1f}")
print(f"total_seconds:    {time.time() - t_start:.1f}")
print(f"peak_mem_mb:      {peak_memory_mb():.1f}")
print(f"num_steps:        {step}")
print(f"num_params_K:     {num_params / 1e3:.1f}")
