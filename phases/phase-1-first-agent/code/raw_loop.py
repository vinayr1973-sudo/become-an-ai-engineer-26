"""
Phase 1 — The Raw Agent Loop (~100 lines)

The entire job of a harness, stripped to its skeleton. No framework.
Just the loop: the model thinks, picks a tool, you run it, you feed the
result back, repeat until the model says it's done.

Build this first. Read every step of the trace. Once you can see what the
loop does for you, you'll understand what every framework is hiding.

Requires:  pip install anthropic
Env:       ANTHROPIC_API_KEY
Run:       python raw_loop.py "Research the top 3 AI agent frameworks in 2026"
"""

import json
import sys
from anthropic import Anthropic

client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment

# --- 1. Define the tools the model is allowed to call -----------------------
TOOLS = [
    {
        "name": "web_search",
        "description": "Search the web and return short text snippets.",
        "input_schema": {
            "type": "object",
            "properties": {"query": {"type": "string"}},
            "required": ["query"],
        },
    },
    {
        "name": "read_file",
        "description": "Read a UTF-8 text file from disk and return its contents.",
        "input_schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
        },
    },
    {
        "name": "write_file",
        "description": "Write text to a file on disk. Overwrites if it exists.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
]


# --- 2. Implement the tools -------------------------------------------------
def web_search(query: str) -> str:
    # Stub. Wire to a real search API (Tavily, Brave, SerpAPI) in practice.
    return f"[search results for: {query!r}] — replace this stub with a real API."


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:  # surface the error to the model, don't crash the loop
        return f"ERROR reading {path}: {e}"


def write_file(path: str, content: str) -> str:
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Wrote {len(content)} chars to {path}."
    except Exception as e:
        return f"ERROR writing {path}: {e}"


def execute_tool(name: str, args: dict) -> str:
    return {
        "web_search": web_search,
        "read_file": read_file,
        "write_file": write_file,
    }[name](**args)


# --- 3. The loop ------------------------------------------------------------
def run(user_input: str) -> None:
    messages = [{"role": "user", "content": user_input}]
    stop_reason = None

    while stop_reason != "end_turn":
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            messages=messages,
            tools=TOOLS,
        )
        stop_reason = response.stop_reason

        # Echo any text the model produced this turn
        for block in response.content:
            if block.type == "text":
                print(block.text)

        if stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"  -> {block.name}({json.dumps(block.input)})")
                    result = execute_tool(block.name, block.input)
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result,
                        }
                    )
            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": tool_results})


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "Say hello and stop."
    run(task)
