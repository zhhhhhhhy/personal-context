---
name: contract-field-patent-drafting
description: "Use when converting contract-field/RAG/LLM research materials into a Chinese patent disclosure (专利交底书、权利要求书、说明书、摘要、附图) with evidence boundaries and acceptance artifacts; exclude patent-law advice, pure prior-art search, ordinary academic papers, or unsupported filing claims."
---

# Contract-field patent drafting

Use the author's research as technical facts and reference patents only for structure and layout. Do not infer completed experiments, human annotation or filing readiness from a writing request.

- For drafting or revising a disclosure, claims, specification, abstract or drawings, read [patent-workflow.md](references/patent-workflow.md). It contains the source inventory, step mapping, document generation and acceptance requirements.
- For a completeness or handoff evaluation, read [patent-material-evaluation.md](references/patent-material-evaluation.md). A deterministic file-list pass does not establish claim support or enablement.
- For final package verification, use [acceptance-checklist.md](references/acceptance-checklist.md) and `scripts/validate_materials.py`; render and inspect requested document artifacts.
- Read [activation-routing.md](references/activation-routing.md) only when maintaining Skill routing or resuming a staged drafting task.

For `具体实施方式`, write one direct-action subsection per actual step, preserving its input, action, condition and output. Keep the agreed reference format and original template unless the current user requests a change. Never substitute planning language or grouped headings for the actual implementation.
