# How To Become An AI Engineer in 2026

> Without a CS degree. Without a bootcamp. Without knowing what a transformer is today.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Oriro-Labs](https://img.shields.io/badge/Oriro--Labs-Learning%20Series-blue)](#)
[![2026](https://img.shields.io/badge/Updated-June%202026-orange)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## The One Number You Need to Know

```
Same model. Two harnesses. CORE benchmark:

  Claude Code harness:  78%
  Smolagents harness:   42%
                        ───
                   36-point gap
```

**The harness is the job.** This repository teaches you how to build it.

---

## What's In Here

```
become-an-ai-engineer-26/
│
├── SKILL.md                        ← The complete engineering skill (start here)
├── BecomeAnAIEngineer26.pdf        ← Illustrated PDF with all diagrams
├── README.md                       ← This file
├── CONTRIBUTING.md                 ← How to contribute
├── LICENSE                         ← MIT
│
├── phases/
│   ├── phase-0-mental-models/
│   │   ├── README.md               ← Workflow vs Agent, 5 patterns, harness model
│   │   └── project/
│   │       └── TEMPLATE.md         ← 2-page concept doc template
│   │
│   ├── phase-1-first-agent/
│   │   ├── README.md               ← Raw loop + Agent SDK walkthrough
│   │   └── code/
│   │       ├── raw_loop.py         ← ~100-line raw agent loop
│   │       └── agent_sdk_agent.py  ← Same agent on Claude Agent SDK
│   │
│   ├── phase-2-architecture/
│   │   ├── README.md               ← LangGraph + Deep Agents
│   │   └── code/
│   │       ├── research_agent/     ← Lead + 3 sub-agents + writer
│   │       │   ├── graph.py
│   │       │   ├── nodes.py
│   │       │   └── tools.py
│   │       └── requirements.txt
│   │
│   ├── phase-3-harness/
│   │   ├── README.md               ← 10 components walkthrough
│   │   └── code/
│   │       └── mini_harness/       ← 1,500-line reference implementation
│   │           ├── harness.py
│   │           ├── tools.py
│   │           ├── hooks.py
│   │           ├── context.py
│   │           └── persistence.py
│   │
│   ├── phase-4-evals/
│   │   ├── README.md               ← 4 eval types + CI setup
│   │   └── code/
│   │       ├── evals/
│   │       │   ├── golden_dataset.py
│   │       │   ├── trajectory_eval.py
│   │       │   ├── llm_judge.py
│   │       │   └── end_state_eval.py
│   │       └── .github/
│   │           └── workflows/
│   │               └── eval.yml    ← GitHub Actions CI gate
│   │
│   └── phase-5-production/
│       ├── README.md               ← Cost, latency, safety, monitoring, resilience
│       └── code/
│           ├── cost_routing.py
│           ├── sandboxing.py
│           └── monitoring.py
│
├── projects/
│   ├── 1-mobile-app-slm/           ← Beginner: Edge AI + resource constraints
│   ├── 2-self-improving-coder/     ← Intermediate: Agentic loops
│   ├── 3-video-editor-agent/       ← Advanced: Multimodal AI
│   ├── 4-personal-life-os/         ← Expert: Deep context + privacy
│   └── 5-enterprise-workflow/      ← Master: Production orchestration
│
├── references/
│   ├── yarn-context-extension.md   ← YaRN: 128K context in 10× fewer steps
│   ├── mhc-stable-training.md      ← mHC: Manifold-constrained residual streams
│   ├── benchmark-numbers.md        ← May 2026 benchmark scores
│   └── stack-decisions.md          ← Framework comparisons and decisions
│
└── community/
    ├── BUILDS.md                   ← Community project showcase
    └── DISCUSSIONS.md              ← Open questions and ongoing research
```

---

## The 17-Week Roadmap

| Phase | Weeks | Build | Milestone |
|-------|-------|-------|-----------|
| 0 — Mental Models | 1-2 | 2-page concept doc | Explain a harness in plain English |
| 1 — First Agent | 3-5 | Raw loop + SDK agent | Agent shipped with Skill + hook |
| 2 — Architecture | 6-9 | LangGraph research agent | Architecture solid + LangSmith traces |
| 3 — Build the Harness | 10-13 | 1,500-line mini-harness | Harness complete + post-mortem |
| 4 — Evals & CI | 14-17 | Regression harness | Eval suite in GitHub Actions |
| 5 — Production | Forever | Harden everything | Never ends |

**Moonlighting?** Multiply every duration by 2.5×.

---

## Start Here (Technical Quick-Start)

### Phase 0 (this weekend, no code)

Read `SKILL.md` sections: Core Insight → What an AI Engineer Does → Phase 0.
Write the 2-page doc. Do not skip this.

### Phase 1 (Weeks 3-5)

```bash
cd phases/phase-1-first-agent/code
pip install anthropic
python raw_loop.py       # understand the loop
python agent_sdk_agent.py  # feel what the harness gives you for free
```

### Phase 2 (Weeks 6-9)

```bash
cd phases/phase-2-architecture/code/research_agent
pip install -r requirements.txt
# Requires: ANTHROPIC_API_KEY, POSTGRES_URL, LANGSMITH_API_KEY
python -m research_agent.main "What are the current AI engineering best practices?"
```

### Phase 3 (Weeks 10-13)

```bash
cd phases/phase-3-harness/code/mini_harness
pip install -r requirements.txt
python harness.py --task "Research and summarise the top 5 AI frameworks in 2026"
```

### Phase 4 (Weeks 14-17)

```bash
cd phases/phase-4-evals/code
python evals/run_golden.py --dataset evals/golden_dataset.jsonl
python evals/trajectory_eval.py --traces traces/
# Copy .github/workflows/eval.yml into your repo to gate CI
```

---

## The 5 Portfolio Projects

Pick one. Build it this weekend. Ship something real.

| # | Project | Level | What It Proves |
|---|---------|-------|----------------|
| 1 | [Mobile App + SLM](projects/1-mobile-app-slm/) | Beginner | Edge AI, resource constraints |
| 2 | [Self-Improving Coding Agent](projects/2-self-improving-coder/) | Intermediate | Agentic loops, debugging |
| 3 | [Video Editor Agent](projects/3-video-editor-agent/) | Advanced | Multimodal AI, tool integration |
| 4 | [Personal Life OS Agent](projects/4-personal-life-os/) | Expert | Deep context, privacy-first |
| 5 | [Enterprise Workflow Agent](projects/5-enterprise-workflow/) | Master | Production orchestration |

---

## The Stack Decision

```
✅ Use:   LangGraph 1.0 + Deep Agents    (state machine + durability + observability)
✅ Use:   Claude Agent SDK               (same harness as Claude Code)
✅ Use:   LangSmith / Braintrust / Phoenix  (pick one for observability)

❌ Avoid: CrewAI in production           (fast demo, fragile at scale)
❌ Avoid: OpenAI Swarm                   (their README says "not production-ready")
❌ Avoid: OpenAI Assistants API          (sunsetting mid-2026)
⚠️ Demo:  CrewAI                         (fine for hackathons, not production)
```

---

## Benchmark Context (May 2026)

The leaderboard changes weekly. What doesn't change:

```
Same model, different harness = 10-36 point swing on any benchmark.

SWE-bench Verified:  Claude Opus 4.7 ~87.6%  |  GPT-5.5 ~88.7%
GAIA (agents):       Claude Sonnet 4.5  74.6%  ← leads
τ-bench (service):   Claude Mythos Preview 89.2% ← leads
```

**The engineer who builds the harness writes the benchmark score.**

---

## Advanced References

For engineers who want to go deeper:

- **[YaRN: Context Window Extension](references/yarn-context-extension.md)** — How to give a model 128K token context using 10× fewer training steps than prior methods. ICLR 2024.

- **[mHC: Stable Training at Scale](references/mhc-stable-training.md)** — How DeepSeek solved training instability at 27B+ parameters using Sinkhorn manifold constraints. arxiv:2512.24880.

- **[Benchmark Numbers](references/benchmark-numbers.md)** — Current leaderboard with context on what each benchmark actually measures.

- **[Stack Decisions](references/stack-decisions.md)** — Detailed framework comparison with reasoning for each recommendation.

---

## Contributing

This is a living document. The field moves weekly.

```
What we want:
  ✓ Phase project implementations (open PRs)
  ✓ Bug fixes in example code
  ✓ Benchmark updates as new scores publish
  ✓ New reference material on emerging techniques
  ✓ Translations
  ✓ Your build in BUILDS.md

What we don't want:
  ✗ Promotional content
  ✗ Framework comparisons without benchmark evidence
  ✗ "AI wrapper" projects presented as agent systems
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## The Uncomfortable Truth

Most people who read this will do nothing.
They will bookmark it, say "great resource," and go back to building wrappers.

57% of teams now have agents in production.
89% of those have observability wired.
Quality is the #1 barrier — 32% of teams cite it as the blocker.

**The entire field is bottlenecked on engineers who can build evals and harnesses.
Not on engineers who can call an LLM API.
That is the job opening.**

---

## License

MIT — use freely, build openly, teach everyone.

---

*AI Engineering by Vinay · Oriro-Labs Learning Series · 2026*
