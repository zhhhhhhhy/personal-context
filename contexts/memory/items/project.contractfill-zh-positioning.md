# ContractFill：中文稿定位与入口

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `project.contractfill-zh-positioning`
- kind: project
- status: superseded
- scope: 指定icml_chinese中文稿；不覆盖其它副本或后续新定位
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

2026-10-12中文稿采纳Benchmark/Evaluation定位：任务、构造和联合评测为主，回答系统实验次之，JEV-A gate为案例；中文评审先读指定目录索引。当前本地AGENTS仍列paper_zh为主稿，但正文/PDF一致性未重查。

## Boundaries

- 原摘要仅中文的范围只限该次任务。
- gate不等同完整系统、内部机制或跨场景泛化；当前论文版本需确认。
- review_after: 2026-11-16
- target: references/projects/contractfill-zh-20261012.md
- replaced_by: project.contractfill-zh-positioning-v2

## Evidence pointers

- R010-M088: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L627` — 用户明确认可基准论文定位、贡献顺序和结论边界。
- R010-M087: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L421` — 原任务只改指定目录中文摘要。
- R010-M090: `01a12dfc-1aab-7101-bf6d-c2758be02026` / `rollout-2026-10-12T10-40-59-01a12dfc-1aab-7101-bf6d-c2758be02026.jsonl:L903` — 先建立中英文稿索引，随后评中文稿。

- candidates: none
