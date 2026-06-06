# Phase 4 — Evals & Regression Harness (Weeks 14-17)

> Without this, every "improvement" is vibes.

See `SKILL.md` → *Phase 4*. The four eval types: single-turn, trajectory,
LLM-as-judge, end-state.

The CI gate lives at
[`code/.github/workflows/eval.yml`](code/.github/workflows/eval.yml) — a
reference GitHub Actions workflow that blocks a merge if the golden-dataset
pass rate drops 3+ points below baseline. Copy it into your own repo and wire
`ANTHROPIC_API_KEY` as a repo secret.

**Deliverable:**
- Golden dataset: 30–50 hand-graded questions across 3 difficulty levels
- Deterministic graders for factual queries
- LLM-as-judge with a 5-criterion rubric
- Trajectory eval: did it plan, spawn sub-agents, cite, stay under budget?
- Wired into GitHub Actions, blocking merges on a 3-point regression
- Production sampling: 1% of live traces auto-graded nightly
