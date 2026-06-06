---
name: become-an-ai-engineer-26
description: >
  Complete AI Engineering skill for 2026. Use this skill whenever someone wants
  to become an AI engineer, learn agent systems, build production agents, understand
  harness engineering, context engineering, eval design, or needs a learning roadmap
  for AI engineering. Triggers on: "become an AI engineer", "learn AI engineering",
  "build an agent", "agent loop", "harness engineering", "context engineering",
  "eval harness", "LangGraph agent", "production agent", "AI engineer roadmap",
  "how to build AI systems", "agent architecture", "tool dispatch", "sub-agents",
  "LLM evals", "regression harness", "build AI without CS degree", or any question
  about professional AI engineering practice. Always use this skill when the goal
  is building systems around AI models — not just calling APIs.
author: Vinay — Oriro-Labs Learning Series
version: "1.0"
year: "2026"
license: MIT
---

# How To Become An AI Engineer in 2026

> Built from production experience. No CS degree required.
> No bootcamp required. No prior AI knowledge required.

---

## CORE INSIGHT FIRST

The companies hiring right now don't need people who understand the math.
They need people who **build systems that survive production.**

```
Same model. Two harnesses. 36-point benchmark gap.

Claude Code harness  →  78% on CORE benchmark
Smolagents harness   →  42% on CORE benchmark

The harness is the job.
```

**The replaceable:** building thin API wrappers
**The unfireable:** shipping autonomous systems with evals and durability

---

## WHAT AN AI ENGINEER ACTUALLY DOES

Not writing prompts. Not picking models.
An AI engineer builds and operates the **system around the model.**

- Designs the agent loop and tool dispatch
- Engineers context — what tokens appear in front of the model at every step
- Writes tools the model picks correctly
- Adds memory, durability, and sandboxing for production traffic
- Wires evals and CI regression gates so "better" becomes measurable
- Ships agents that survive real users and real cost

### The 4 Context Primitives

| Primitive | What It Means |
|-----------|---------------|
| **Write** | Scratchpads and memory files the agent reads and updates |
| **Select** | Retrieval at the point of use — not upfront dumping |
| **Compress** | Summarisation at 85–95% of the context window |
| **Isolate** | Sub-agents with their own separate context windows |

> **Context engineering replaced prompt engineering.** Prompt engineering is dead
> as a standalone skill. The four primitives above are the new fundamentals.

---

## THE 17-WEEK ROADMAP

17 weeks full-time. 40 weeks moonlighting.
Every phase ships something concrete. No exceptions.

```
Phase 0  Weeks 1-2   Mental Models         → 2-page concept doc
Phase 1  Weeks 3-5   First Agent           → Agent shipped with Skill + hook
Phase 2  Weeks 6-9   Real Architecture     → LangGraph agent + LangSmith trace
Phase 3  Weeks 10-13 Build the Harness     → 1,500-line mini-harness
Phase 4  Weeks 14-17 Evals & CI            → Regression harness in GitHub Actions
Phase 5  Forever     Production Hardening  → Never ends
```

---

## PHASE 0 — BUILD CORRECT MENTAL MODELS (Weeks 1-2)

**Do not write a single line of agent code yet.**

### 1. Workflow vs Agent

```
Workflow:  fixed control flow YOU wrote     A → B → C → Done
Agent:     dynamic control flow MODEL decides  Think → Act → Observe → Repeat
```

Building an agent when you need a workflow costs 10× more and breaks twice as often.

### 2. The 5 Workflow Patterns (from Anthropic)

```python
# 1. Prompt chaining — pass output from one call to the next
result_1 = llm(prompt_1)
result_2 = llm(prompt_2 + result_1)

# 2. Routing — different models for different tasks
model = route(task)  # haiku / sonnet / opus

# 3. Parallelisation — run multiple tasks at the same time
results = await asyncio.gather(*[llm(p) for p in prompts])

# 4. Orchestrator-worker — one brain, many hands
plan = orchestrator.plan(task)
results = [worker.execute(step) for step in plan]

# 5. Evaluator-optimiser — generate → judge → improve
while not judge(output): output = generate(feedback)
```

### 3. The Harness Stack

```
┌─────────────────────────────┐
│         Your Agent          │  ← your code + skills
├─────────────────────────────┤
│       Harness (OS)          │  ← loop, tools, context, memory
├─────────────────────────────┤
│       Model API (CPU)       │  ← raw inference
└─────────────────────────────┘

The OS determines what the CPU can do.
The harness determines what the model can do.
```

**Phase 0 project:** Write a 2-page doc in your own words defining:
workflow vs agent · the 5 patterns · the 4 context primitives · orchestrator-worker.
If you can't write it without looking, you haven't understood it yet.

---

## PHASE 1 — BUILD YOUR FIRST AGENT FROM SCRATCH (Weeks 3-5)

Write the agent twice. Raw API first. Agent SDK second. Feel the difference.

### Build #1 — The Raw Loop (~100 lines of Python)

```python
messages = [{"role": "user", "content": user_input}]
stop_reason = None

while stop_reason != "end_turn":
    response = client.messages.create(
        model="claude-sonnet-4-5",
        messages=messages,
        tools=tools
    )
    stop_reason = response.stop_reason

    if stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})
```

Give it 3 tools: `web_search` · `read_file` · `write_file`
Run on a research task. Read every step of the trace.

### Build #2 — The Same Agent on Claude Agent SDK

```
Add to your agent:
  CLAUDE.md          → project conventions the agent reads
  skills/research/   → SKILL.md defining output format
  hooks/post_tool.py → PostToolUse: auto-format every written file
  Task tool          → spawn a sub-agent for a subtask
```

**Phase 1 project:** Daily briefing agent.
Reads your Markdown notes + RSS feeds.
Writes a summarised briefing to disk every morning.
Run it for a week. Watch it fail. Fix it.

---

## PHASE 2 — REAL ARCHITECTURE (Weeks 6-9)

Build on **LangGraph + Deep Agents.** This is the production stack.

### LangGraph Gives You

```python
from langgraph.graph import StateGraph
from langgraph.checkpoint.postgres import PostgresSaver

# State machine with durable checkpointing
graph = StateGraph(AgentState)
graph.add_node("plan", plan_node)
graph.add_node("execute", execute_node)
graph.add_edge("plan", "execute")

# Survive any process kill — resume exactly where you left off
checkpointer = PostgresSaver.from_conn_string(POSTGRES_URL)
app = graph.compile(checkpointer=checkpointer)
```

### Middleware Hooks

```python
# Customise without forking the packaged harness
@agent.before_agent
def inject_context(state): ...        # runs before the loop starts

@agent.wrap_model_call
def add_system_prompt(call): ...      # wraps every LLM call

@agent.before_tools
def validate_tool_input(tool): ...    # runs before any tool executes

@agent.after_tools
def log_tool_result(result): ...      # runs after any tool executes
```

### Sub-Agents with Isolated Context

```
Lead Agent (plans, writes TODO list)
    │
    ├── Search Sub-Agent 1  ← isolated context
    ├── Search Sub-Agent 2  ← isolated context
    └── Search Sub-Agent 3  ← isolated context
                │
            Files on Disk
                │
         Writer Agent
                │
         Final Report
```

> Sub-agents = isolated context, not just parallel processes.
> Each sub-agent has NO access to the lead agent's memory.
> They communicate via files and compressed summaries.

**Phase 2 project:** Research Analyst Agent
→ Lead agent plans → spawns 3 search sub-agents in parallel
→ Sub-agents write results to files → citation sub-agent verifies
→ Writer agent produces Markdown with inline citations
→ State persists via PostgresSaver (kill → resume)
→ Human-in-the-loop interrupt before exceeding $1 in tokens
→ Ship a LangSmith trace URL with your README

---

## PHASE 3 — BUILD THE HARNESS YOURSELF (Weeks 10-13)

**This is the highest-leverage phase in the roadmap.**
You will never make the right trade-offs in production until you've built one.

### The 10 Components

```python
class MiniHarness:
    # 1. Loop control
    def run(self, task: str) -> str:
        while self.stop_reason != "end_turn":
            self._step()

    # 2. Tool dispatch
    @tool(schema={"type": "function", ...})
    def web_search(self, query: str) -> str: ...

    # 3. Context management
    def _maybe_compact(self):
        if self._token_count() > 0.85 * self.context_limit:
            self._summarise_and_compress()

    # 4. Persistence
    def _checkpoint(self, state: dict):
        self.db.execute(
            "INSERT INTO runs VALUES (?,?,?)",
            [self.run_id, self.step, json.dumps(state)]
        )

    # 5. Sub-agent orchestration
    def spawn(self, task: str) -> "MiniHarness":
        child = MiniHarness(context=[])  # isolated context
        return child

    # 6. Skills / progressive disclosure
    def _load_skill(self, name: str) -> str:
        return Path(f"skills/{name}/SKILL.md").read_text()

    # 7. Hooks
    def pre_tool(self, tool_name: str, args: dict): ...
    def post_tool(self, tool_name: str, result: str): ...

    # 8. Observability
    @tracer.start_as_current_span("tool_call")
    def _execute_tool(self, name: str, args: dict): ...

    # 9. Sandboxing
    def execute_code(self, code: str) -> str:
        return modal.run_sandbox(code)  # never exec() directly

    # 10. Auth brokering
    def call_api(self, service: str, **kwargs):
        creds = vault.get(service)  # model never sees the key
        return requests.post(endpoint, headers={"Authorization": creds})
```

**Phase 3 project:** 1,500-line mini-harness in Python.
Must include: tool registry · CLAUDE.md loader · SKILL.md progressive disclosure
· sub-agent spawn primitive · filesystem offload (>20K tokens → disk)
· auto-compaction at 85% · pluggable hooks · OpenTelemetry · SQLite resume.

Deliverable: a 1,000-word post-mortem comparing your harness to
Claude Agent SDK and Deep Agents. What you got right. What you cut.
What you'd do differently.

---

## PHASE 4 — EVALS & REGRESSION HARNESS (Weeks 14-17)

> Without this, every "improvement" is vibes.

### The 4 Eval Types

```
1. Single-turn evals
   Input → Output → deterministic check
   "Did it produce valid JSON?"  "Is the answer factually correct?"
   Cheapest. Run constantly. Block CI on failure.

2. Trajectory evals
   Input → [tool_1, tool_2, tool_3] → expected sequence
   "Did it search before answering?"
   "Did it call calc before making a financial claim?"

3. LLM-as-judge
   Response → LLM grader → score on rubric
   Use for: research reports, code review, explanations
   Calibrate weekly against human-graded examples.

4. End-state evals
   Before state → agent runs → After state → compare
   "Did the correct rows get written to the database?"
   "Did the right files get created?"
```

### Regression Harness in GitHub Actions

```yaml
# .github/workflows/eval.yml
name: Agent Regression
on: [pull_request]

jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run golden dataset
        run: python evals/run_golden.py
      - name: Check pass rate
        run: |
          PASS_RATE=$(cat results/pass_rate.json | jq .rate)
          BASELINE=$(cat evals/baseline.json | jq .rate)
          python -c "
          pass_rate = $PASS_RATE
          baseline = $BASELINE
          if pass_rate < baseline - 0.03:
              print(f'FAIL: {pass_rate:.1%} < baseline {baseline:.1%} - 3pp')
              exit(1)
          print(f'PASS: {pass_rate:.1%} (baseline {baseline:.1%})')
          "
```

**Phase 4 project:**
→ Golden dataset: 30-50 hand-graded questions (3 difficulty levels)
→ Deterministic graders for factual queries
→ LLM-as-judge with 5-criterion rubric
→ Trajectory eval: did the agent plan, spawn sub-agents, cite, stay under budget?
→ Wire into GitHub Actions: block merge if pass rate drops 3+ points
→ Production sampling: 1% of live traces auto-graded nightly

---

## PHASE 5 — PRODUCTION HARDENING (Forever)

### 1. Cost Discipline

```python
# Cache system prompt, CLAUDE.md, tool definitions — up to 90% savings
client.messages.create(
    system=[{"type": "text", "text": system_prompt,
             "cache_control": {"type": "ephemeral"}}],
    ...
)

# Route by difficulty
model = (
    "claude-haiku-4-5" if complexity < 0.3 else
    "claude-sonnet-4-5" if complexity < 0.8 else
    "claude-opus-4-6"
)

# Batch API: 50% off for non-real-time work
```

### 2. Latency

```python
# Parallel tool calls — ALWAYS
# Anthropic's own research agent system prompt:
# "you MUST use parallel tool calls"
results = await asyncio.gather(
    search_tool("query_1"),
    search_tool("query_2"),
    read_file("context.md")
)

# Sub-agent fan-out
# 60-step sequential → 10-step lead + 5 parallel 10-step sub-agents
```

### 3. Safety and Sandboxing

```python
# NEVER do this:
exec(model_output)            # ← model output in main process

# ALWAYS do this:
result = modal.run_sandbox(   # ← isolated container
    code=model_output,
    timeout=30,
    network_access=False
)

# NEVER pass credentials to model context:
# BAD:  "Use API key sk-abc123 to call the service"
# GOOD: creds = vault.get("service"); call_api(creds=creds)
```

### 4. Monitoring and Drift

```python
# Alert thresholds — set these on day one
ALERTS = {
    "token_cost_per_request_usd": 0.50,    # alert above $0.50
    "tool_call_failure_rate":      0.05,    # alert above 5%
    "llm_judge_score":             0.70,    # alert below 70%
    "p95_latency_seconds":        10.0,    # alert above 10s
}

# Re-baseline after EVERY model upgrade
# Harnesses encode assumptions about model limitations.
# Those assumptions go stale when the model changes.
```

### 5. Resilience

```python
# Durable execution for any agent running > 60 seconds
from langgraph.checkpoint.postgres import PostgresSaver

# Checkpoint after every node — rewind and fork always possible
@graph.node
def expensive_step(state):
    result = do_expensive_thing(state)
    return {**state, "result": result}
    # LangGraph auto-checkpoints after each node
```

---

## THE 5 PORTFOLIO PROJECTS

Pick one. Build it this weekend.

```
Level       Project                         Proves
──────────────────────────────────────────────────────────────
Beginner    Mobile App + SLM               Edge AI, resource constraints
Intermediate Self-Improving Coding Agent   Agentic loops, debugging
Advanced    Video Editor Agent             Multimodal AI, tool integration
Expert      Personal Life OS Agent         Context management, privacy
Master      Enterprise Workflow Agent      Production orchestration
```

### Project 1 — Mobile App + SLM (Beginner)

Offline-first mobile app using a small language model. Zero API costs. Complete privacy.
- Lazy-load models on demand, unload under memory pressure
- Sliding context window with semantic chunking
- 4-bit quantisation for older devices, 8-bit for newer
- Batch inference to reduce battery wake cycles

### Project 2 — Self-Improving Coding Agent (Intermediate)

Agent writes code → runs tests → learns from failures → loops until functional.
- Plan → Execute → Test → Reflect loop with max iteration limit
- Isolated execution per task with resource limits
- Memory: short-term (last 5) + long-term (successes) + failure memory (error signatures)
- Static analysis before execution — detect dangerous operations

### Project 3 — Video Editor Agent (Advanced)

Fork open-source editor. User says "make this cinematic." Agent handles cuts, transitions, colour.
- Vision model analyses frames + audio model analyses dialogue
- Intent translation: "cinematic" → concrete parameters
- Scene detection via frame-difference analysis
- Incremental preview — only re-render affected sections

### Project 4 — Personal Life OS Agent (Expert)

Manages calendar, finances, and health. Plans months ahead. Detects burnout.
- Real-time ingestion: calendar, finance, health, communications
- Personal knowledge graph of entities and relationships
- Background thread every 6 hours checking anomalies
- Value alignment: user states priorities — recommendations validated against them
- All data encrypted at rest with user-controlled keys

### Project 5 — Enterprise Workflow Agent (Master)

Monitors Slack/Jira → plans execution → delegates → reports with audit logs.
- Event-driven: Slack, Jira, email, monitoring systems
- Multi-agent delegation: orchestrator → communication, data, analysis, documentation agents
- Self-healing: exponential backoff, circuit breakers, retry decisions
- Immutable audit log: every action, authorisation, outcome
- Human-in-the-loop: agent proposes plan before executing on critical workflows

---

## THE STACK

```
Framework:     LangGraph 1.0 + Deep Agents
               (NOT CrewAI for prod / NOT OpenAI Swarm / NOT Assistants API)

Harness ref:   Claude Agent SDK
               Same harness as Claude Code.
               CLAUDE.md + Skills + sub-agents + hooks + filesystem-as-memory.

Observability: LangSmith       (if using LangGraph)
               Braintrust       (framework-agnostic, $249/mo CI gating)
               Arize Phoenix    (open-source, OTEL-native, free)

Skip in 2026:  OpenAI Swarm            (not production-ready)
               OpenAI Assistants API   (sunsetting mid-2026)
               No-code agent platforms (throwaway only)
               Custom vector store     (measure recall first)
```

---

## BENCHMARK NUMBERS (May 2026)

```
SWE-bench Verified (coding):
  Claude Opus 4.7   ~87.6%
  GPT-5.5           ~88.7%

GAIA (general agent tasks):
  Claude Sonnet 4.5   74.6%   ← leads

τ-bench (customer service):
  Claude Mythos Preview   89.2%   ← leads

Key stat: same benchmark, different harness = swing of 10–36 points.
The model matters less than the harness.
```

---

## THE ADVANCED SCIENCE (Context for Engineers)

### Attention and Context Windows

AI models use attention to weight which tokens matter most at each step.
Attention cost grows quadratically with input length — double the input, 4× the compute.
This is why the **Compress** context primitive is not optional: it's survival.

**YaRN (Yet another RoPE extensioN)** — ICLR 2024
Extends context from 4K to 128K tokens using 10× fewer training steps.
Works by treating high-frequency and low-frequency position components differently.
Models with YaRN can read 500 pages in one context window.

### Training Stability at Scale (mHC)

**mHC — Manifold-Constrained Hyper-Connections** (DeepSeek, arxiv:2512.24880, Dec 2025)

Standard residual connections preserve signal by adding input to output.
Hyper-Connections (HC) added 4 parallel streams for better performance —
but broke identity mapping, causing loss spikes at step 12,000.

mHC fixes this by projecting the stream-mixing matrix onto a Sinkhorn manifold
(a mathematical surface where every row and column sums to 1).
Identity mapping is automatically preserved. Result: 6.7% overhead, zero loss spikes,
evaluated at 3B/9B/27B parameter scales.

**Harness parallel:** The same principle applies to harness design.
Constrain the system at the right point (context compaction at 85%, credential brokering,
sandboxed execution) and the whole system becomes stable under real production load.

---

## QUICK REFERENCE

| Term | Definition |
|------|-----------|
| Agent | AI that makes its own control-flow decisions in a loop |
| Workflow | Fixed control flow you wrote — use unless you need an agent |
| Harness | Everything between you and the model API |
| Context window | The model's RAM — all it can see at once |
| Context engineering | Deciding what goes into that RAM at every step |
| Tool | A function the model can call |
| Sub-agent | Agent spawned with isolated context |
| Eval | Automated test measuring if the agent got better or worse |
| LLM-as-judge | Using an AI to grade another AI's output |
| YaRN | Extends context to 128K tokens — 10× efficient |
| mHC | Stable training architecture — 6.7% overhead, zero spikes |
| Checkpoint | Saved state for resume after process kill |
| Sandboxing | Code runs in isolated container — model never has server creds |
| OTEL | OpenTelemetry — standard for tracing every call |

---

## THE CLOSING ARGUMENT

> 57% of teams now have agents in production.
> 89% of those have observability wired.
> Quality is the #1 barrier (32% of teams cite it).
>
> The entire field is bottlenecked on engineers who can build evals and harnesses.
> Not on engineers who can call an LLM API.
> That is the job opening.

**Next:**
1. Pick one project
2. Build it this weekend
3. Document everything — architecture decisions, failures, recoveries
4. Build in public

**Expertise is the only job security left.
Production systems are the only portfolio that matters.**

---

*AI Engineering by Vinay · Oriro-Labs Learning Series · 2026 · MIT License*
*Public domain knowledge — share freely, build openly, teach everyone.*
