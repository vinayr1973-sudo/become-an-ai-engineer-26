# Project 2 — Self-Improving Coding Agent (Intermediate)

**Proves:** Agentic loops, debugging.

Agent writes code → runs tests → learns from failures → loops until functional.
See `SKILL.md` → *The 5 Portfolio Projects*.

- Plan → Execute → Test → Reflect loop with a max-iteration limit
- Isolated execution per task with resource limits
- Memory: short-term (last 5) + long-term (successes) + failure memory (error signatures)
- Static analysis before execution — detect dangerous operations
