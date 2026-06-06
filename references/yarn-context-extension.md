# YaRN — Context Window Extension

> Give a model a 128K-token context window using ~10× fewer training steps
> than prior methods. ICLR 2024 · [arxiv.org/abs/2309.00071](https://arxiv.org/abs/2309.00071)

---

## Why context extension is hard

Models trained on, say, 4K tokens struggle past 32K at inference. The root
cause is **RoPE** (Rotary Position Embeddings): the position frequencies used
at long positions were *never seen during training* — they are out of
distribution. The model has no learned behaviour for them.

There is also the **"lost in the middle"** problem: models attend strongly to
the beginning and end of a long context and miss information buried at 10–50%
depth. Extending the window does not fix this by itself — you have to test for
it (see NIAH below).

## The RoPE scaling landscape

| Method | Max scale | Quality | Training cost | When |
|---|---|---|---|---|
| Linear PI | 2–4× | Poor | none | avoid |
| NTK-Aware | 4–8× | Moderate | none | quick inference-only fix |
| Dynamic NTK | 8–16× | Good | none | adaptive, inconsistent |
| **YaRN** | **16–32×** | **Best** | **<0.1%** | **standard for fine-tuning** |
| LongRoPE | up to 2M | Best | medium | extreme contexts |

## The YaRN insight

Different RoPE frequency dimensions need different treatment. **Low-frequency**
dimensions (long-range dependencies) get interpolated; **high-frequency**
dimensions (local resolution) are left untouched. A softmax temperature factor
(`attention_factor`) corrects the attention distribution at the new scale.

```python
# rope_scaling block in config.json — 4K base extended to 128K (32x):
rope_scaling = {
    "type": "yarn",
    "factor": 32.0,
    "original_max_position_embeddings": 4096,
    "attention_factor": 0.1,   # softmax temperature — do not omit
}
```

Performance: 200–600 fine-tuning steps are usually enough, using ~0.1% of the
original pre-training token budget. Compatible with KV cache and FlashAttention.

## Always verify the config survived checkpoint load

```python
rope_cfg = getattr(model.config, "rope_scaling", None)
assert rope_cfg is not None, "YaRN rope_scaling missing — STOP"
assert rope_cfg.get("type") in ("yarn", "longrope"), \
    f"Unexpected rope type: {rope_cfg.get('type')}"
print(f"YaRN preserved: {rope_cfg}")
```

---

## Test it: Needle-in-a-Haystack (NIAH)

Insert a specific fact (the *needle*) into a long block of irrelevant text
(the *haystack*) and ask the model to retrieve it. Test at multiple lengths
**and** multiple depths — failures cluster at 50% depth.

```python
import random

NEEDLE = "The magic access code is YARN-NIAH-4731."
QUESTION = "What is the magic access code?"

def build_prompt(filler_paragraph: str, target_tokens: int, depth: float) -> str:
    # crude token proxy: ~0.75 words/token. Repeat filler to reach length.
    haystack = (filler_paragraph + "\n\n") * (target_tokens // 200)
    cut = int(len(haystack) * depth)
    return haystack[:cut] + "\n" + NEEDLE + "\n" + haystack[cut:] + "\n\n" + QUESTION

def passes(model_answer: str) -> bool:
    return "YARN-NIAH-4731" in model_answer

# Sweep a 5x5 grid and print a hit/miss heatmap.
lengths = [8_000, 32_000, 64_000, 128_000]
depths = [0.1, 0.3, 0.5, 0.7, 0.9]
for L in lengths:
    row = []
    for d in depths:
        prompt = build_prompt("Lorem ipsum dolor sit amet. " * 30, L, d)
        answer = run_model(prompt)          # your inference call
        row.append("HIT " if passes(answer) else "MISS")
    print(f"{L:>7}:  " + "  ".join(row))
```

A clean YaRN extension returns HIT across the whole grid. Cold spots at the
50% column mean "lost in the middle" survived — re-check `attention_factor`
and the fine-tune coverage at long positions.

### Go harder: NoLiMa (no literal matching)

NIAH is gameable — the model can keyword-match "magic code" in the question to
"magic code" in the needle. **NoLiMa** removes the lexical overlap:

```
Needle:   "The combination for the safe is 7734."
Question: "What numbers open the vault?"
```

The model must infer *safe ≈ vault* with no shared keyword. Passing NoLiMa is
real long-context comprehension, not string lookup.

---

## Surviving quantization

Standard Q4_K_M can degrade YaRN because the position-embedding weights get
quantized too — long-context recall breaks even when short-context scores look
fine. Keep the embedding layer at F16 when exporting to GGUF, then **re-run the
NIAH grid on the quantized model**, not just short-context benchmarks.

---

*Reference for "Become An AI Engineer 26". See SKILL.md → Advanced Science.*
