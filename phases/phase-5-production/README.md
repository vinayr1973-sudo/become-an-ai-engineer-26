# Phase 5 — Production Hardening (Forever)

This phase never ends. See `SKILL.md` → *Phase 5* for the code patterns.

The five fronts:

1. **Cost discipline** — prompt caching (up to 90% savings), route by difficulty
   (Haiku → Sonnet → Opus), Batch API for non-real-time work (50% off).
2. **Latency** — parallel tool calls always; sub-agent fan-out turns a 60-step
   sequential run into a 10-step lead + parallel sub-agents.
3. **Safety & sandboxing** — never `exec()` model output; run it in an isolated
   container. Never put credentials in the model's context — broker them.
4. **Monitoring & drift** — alert on cost/request, tool-failure rate, judge
   score, p95 latency. Re-baseline after every model upgrade.
5. **Resilience** — durable execution (PostgresSaver) for anything running >60s,
   so a process kill is a resume, not a restart.
