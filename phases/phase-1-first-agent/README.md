# Phase 1 — Build Your First Agent From Scratch (Weeks 3-5)

Write the agent twice. Raw API first, Agent SDK second. Feel the difference.

## Build #1 — The raw loop
[`code/raw_loop.py`](code/raw_loop.py) — ~100 lines, no framework. Give it three
tools (`web_search`, `read_file`, `write_file`), run it on a research task, and
read every step of the trace.

```bash
cd code
pip install anthropic
export ANTHROPIC_API_KEY=...      # PowerShell: $env:ANTHROPIC_API_KEY="..."
python raw_loop.py "Research the top 3 AI agent frameworks in 2026"
```

## Build #2 — The same agent on Claude Agent SDK
Add `CLAUDE.md`, a `skills/research/SKILL.md`, a `hooks/post_tool.py` PostToolUse
hook, and spawn one sub-agent via the Task tool. See `SKILL.md` → *Phase 1*.

**Deliverable:** a daily-briefing agent. Reads your notes + RSS, writes a
summarised briefing to disk every morning. Run it for a week. Watch it fail.
Fix it.
