# 编辑已有材料时保留约定风格

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `documents.preserve-style`
- kind: rule
- status: superseded
- scope: 修改已有简历、专利或其他已经确定风格的文档
- verification: supported_preference
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

编辑已有文档时，沿用用户认可的结构和风格；有参考模板时按约定的模板处理。改文字不自动授权更换整套布局。

## Boundaries

- 用户当前明确要求重做结构或版式时按新要求执行。
- 渲染验收和目标目录的具体要求由对应文档 Skill 或项目约定处理。
- review_after: 2027-01-15
- replaced_by: documents.preserve-style-v2

## Evidence pointers

- E015: `01a1078a-5052-73a2-b38e-5624a193a91f` / `rollout-2026-10-04T23-32-27-01a1078a-5052-73a2-b38e-5624a193a91f_01a1078b-8726-7e61-84d0-98deed6961bf.jsonl:L487` — 用户直接纠正简历整体结构和风格被改变。
- E017: `01a0fde7-9236-78c1-9068-6867a4ce6d8e` / `rollout-2026-10-03T02-43-13-01a0fde7-9236-78c1-9068-6867a4ce6d8e_01a0fded-77c6-71a2-99f6-a91075ef135d.jsonl:L3210` — 另一专利任务要求修复生成材料与指定参考格式的偏差。

- candidates: C-20261014-005
