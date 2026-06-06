# mHC — Stable Training at Scale

> How to keep training stable at 27B+ parameters using manifold-constrained
> residual streams. DeepSeek · arxiv:2512.24880 (Dec 2025)

---

## The problem

Standard **residual connections** preserve signal by adding the input back to
the output: `x_out = x_in + f(x_in)`. The identity term (`x_in`) is what keeps
gradients flowing through very deep stacks.

**Hyper-Connections (HC)** generalised this by adding several parallel residual
streams and a learned matrix that mixes them. More capacity — but the learned
mixing matrix can drift away from preserving identity, and when it does you get
**loss spikes** (in the reported runs, around step 12,000). One spike can undo
hours of training or diverge the run entirely.

## The fix: constrain the mixing matrix to a manifold

**mHC (manifold-constrained Hyper-Connections)** projects the stream-mixing
matrix onto the **Sinkhorn manifold** — the set of doubly-stochastic matrices
where every row and every column sums to 1. On that manifold, identity mapping
is preserved automatically, so the residual stream can't blow up or collapse.

```python
import torch

def sinkhorn(M: torch.Tensor, iters: int = 8, eps: float = 1e-6) -> torch.Tensor:
    """Project a positive matrix toward doubly-stochastic (rows & cols sum to 1)."""
    M = M.clamp_min(eps)
    for _ in range(iters):
        M = M / M.sum(dim=1, keepdim=True)   # normalise rows
        M = M / M.sum(dim=0, keepdim=True)   # normalise columns
    return M

class ManifoldHyperConnection(torch.nn.Module):
    def __init__(self, n_streams: int):
        super().__init__()
        self.logits = torch.nn.Parameter(torch.zeros(n_streams, n_streams))

    def mixing_matrix(self) -> torch.Tensor:
        # exp keeps entries positive; Sinkhorn makes it doubly-stochastic
        return sinkhorn(self.logits.exp())

    def forward(self, streams: torch.Tensor) -> torch.Tensor:
        # streams: (n_streams, batch, dim) -> mixed streams, identity preserved
        return torch.einsum("ij,jbd->ibd", self.mixing_matrix(), streams)
```

## Results

- **6.7% compute overhead** vs standard residuals.
- **Zero loss spikes** across the reported runs.
- Evaluated at **3B / 9B / 27B** parameter scales.

## The harness parallel

The lesson generalises beyond model internals. **Constrain the system at the
right point and the whole thing becomes stable under real load.** In harness
design the equivalent constraints are:

- **Context compaction at ~85%** of the window — never let context overflow.
- **Credential brokering** — the model never sees raw secrets.
- **Sandboxed execution** — model output runs in an isolated container.

Same principle: pick the one invariant that must always hold, enforce it
structurally, and stop firefighting the symptoms.

---

*Reference for "Become An AI Engineer 26". See SKILL.md → Advanced Science.*
