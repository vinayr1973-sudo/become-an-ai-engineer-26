# Stack Decisions

The recommended 2026 production stack, with the reasoning for each call.

## Use

| Layer | Choice | Why |
|---|---|---|
| Framework | **LangGraph 1.0 + Deep Agents** | State machine + durable checkpointing + observability. Survives process kills, resumes mid-run. |
| Harness reference | **Claude Agent SDK** | Same harness as Claude Code: CLAUDE.md + Skills + sub-agents + hooks + filesystem-as-memory. |
| Observability | **LangSmith** (LangGraph-native) / **Braintrust** (framework-agnostic, CI gating) / **Arize Phoenix** (open-source, OTEL-native, free) | Pick one. You cannot improve what you cannot trace. |

## Avoid in production

| Avoid | Reason |
|---|---|
| CrewAI in production | Fast demo, fragile at scale. Fine for hackathons only. |
| OpenAI Swarm | Their own README says "not production-ready". |
| OpenAI Assistants API | Sunsetting mid-2026. |
| No-code agent platforms | Throwaway prototypes only. |
| Custom vector store (by default) | Measure recall first — most apps don't need one. |

## The decision rule

1. What is the **simplest** thing that solves this problem?
2. What does it look like at **10×** current scale (not 100×)?
3. What is the **cost of being wrong** — easy to change, or locked in?

Start with a monolith. Start serverless. Buy everything that isn't your core
product (auth, email, payments). Split into services only when parts genuinely
need to scale independently.

> Update with benchmark-backed comparisons only — see CONTRIBUTING.md.

---

*Reference for "Become An AI Engineer 26". See SKILL.md → The Stack.*
