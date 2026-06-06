# Phase 2 — Real Architecture (Weeks 6-9)

Build on **LangGraph + Deep Agents** — the production stack. See `SKILL.md` →
*Phase 2* for the full walkthrough (StateGraph, PostgresSaver checkpointing,
middleware hooks, isolated-context sub-agents).

**Deliverable:** a Research Analyst Agent.
- Lead agent plans → spawns 3 search sub-agents in parallel (isolated context)
- Sub-agents write results to files → a citation sub-agent verifies
- Writer agent produces Markdown with inline citations
- State persists via `PostgresSaver` (kill → resume)
- Human-in-the-loop interrupt before exceeding $1 in tokens
- Ship a LangSmith trace URL in your README

> Reference implementation (`research_agent/graph.py`, `nodes.py`, `tools.py`)
> is left for you to build — that's the point of the phase.
