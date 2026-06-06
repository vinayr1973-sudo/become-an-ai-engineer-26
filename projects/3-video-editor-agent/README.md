# Project 3 — Video Editor Agent (Advanced)

**Proves:** Multimodal AI, tool integration.

Fork an open-source editor. User says "make this cinematic"; the agent handles
cuts, transitions, colour. See `SKILL.md` → *The 5 Portfolio Projects*.

- Vision model analyses frames + audio model analyses dialogue
- Intent translation: "cinematic" → concrete parameters
- Scene detection via frame-difference analysis
- Incremental preview — only re-render affected sections
