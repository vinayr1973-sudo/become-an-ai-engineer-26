# Benchmark Numbers (May 2026)

The leaderboard changes weekly. What does **not** change: the same model on a
different harness swings 10–36 points on any benchmark. The harness writes the
score.

## The one number

```
Same model. Two harnesses. CORE benchmark:

  Claude Code harness:  78%
  Smolagents harness:   42%
                        ───
                   36-point gap
```

## Current scores

| Benchmark | What it measures | Leader (May 2026) |
|---|---|---|
| SWE-bench Verified | Real-world coding fixes | GPT-5.5 ~88.7% · Claude Opus 4.7 ~87.6% |
| GAIA | General agent tasks | Claude Sonnet 4.5 — 74.6% |
| τ-bench | Customer-service agents | Claude Mythos Preview — 89.2% |

## How to read a benchmark

- **A single number is meaningless without the harness.** Always ask: which
  scaffold produced this score? Tool set, context strategy, retry policy and
  sub-agent structure move the number more than the base model does.
- **Re-baseline after every model upgrade.** Harnesses encode assumptions about
  model limitations; those assumptions go stale when the model changes.
- **Your own golden dataset beats any public leaderboard** for deciding whether
  *your* system got better. Public benchmarks tell you the field is moving;
  your evals tell you *you* are.

> Update this file as new scores publish — cite the primary source in the PR.

---

*Reference for "Become An AI Engineer 26".*
