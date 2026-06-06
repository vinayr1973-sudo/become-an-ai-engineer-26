# Project 5 — Enterprise Workflow Agent (Master)

**Proves:** Production orchestration.

Monitors Slack/Jira → plans execution → delegates → reports with audit logs.
See `SKILL.md` → *The 5 Portfolio Projects*.

- Event-driven: Slack, Jira, email, monitoring systems
- Multi-agent delegation: orchestrator → communication, data, analysis, documentation agents
- Self-healing: exponential backoff, circuit breakers, retry decisions
- Immutable audit log: every action, authorisation, outcome
- Human-in-the-loop: agent proposes a plan before executing critical workflows
