# 专利材料：已有Skill入口

- id: `skill.patent-workflow-v2`
- kind: skill
- status: active
- scope: 合同字段/RAG/LLM材料转专利交底书、说明书及配套文档
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

合同字段研究材料转专利包时，按contract-field-patent-drafting处理；本人材料承载事实，参考专利只供结构和格式。具体步骤与渲染要求在该Skill中读取。

## Boundaries

- 步骤.md等文件名属于对应Skill流程，不推广为所有任务的个人硬要求。
- 专利法咨询、单纯检索或局部小修改不因这个入口自动扩成完整材料包；当前范围优先。
- review_after: 2027-01-15
- target: skills/contract-field-patent-drafting/SKILL.md

## Evidence pointers

- E001: `01a0fde7-9236-78c1-9068-6867a4ce6d8e` / `rollout-2026-10-03T02-36-47-01a0fde7-9236-78c1-9068-6867a4ce6d8e.jsonl:L12` — 直接要求专利任务拆解并产出步骤.md。
- E059: `01a0fde7-9236-78c1-9068-6867a4ce6d8e` / `rollout-2026-10-03T02-43-13-01a0fde7-9236-78c1-9068-6867a4ce6d8e_01a0fded-77c6-71a2-99f6-a91075ef135d.jsonl:L9638` — 直接要求实施步骤逐项对应并写实际动作。
- E017: `01a0fde7-9236-78c1-9068-6867a4ce6d8e` / `rollout-2026-10-03T02-43-13-01a0fde7-9236-78c1-9068-6867a4ce6d8e_01a0fded-77c6-71a2-99f6-a91075ef135d.jsonl:L3210` — 直接纠正参考模板与生成材料的格式差异。

- candidates: C-20261014-001, C-20261014-003, C-20261014-004, C-20261014-012, C-20261014-013
