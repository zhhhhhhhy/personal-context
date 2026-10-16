# 编辑已有材料：保留约定风格

- id: `documents.preserve-style-v2`
- kind: rule
- status: active
- scope: 修改已有简历、专利等已经确定结构或参考模板的材料
- verification: supported_preference
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

修改已有文档时，沿用用户认可的结构和风格；改文字不自动授权重做布局。

## Boundaries

- 当前明确要求重做结构或版式时按新要求执行。
- 渲染验收由对应文档Skill或项目约定承载，不在这里另设流程。
- review_after: 2027-01-15

## Evidence pointers

- E015: `01a1078a-5052-73a2-b38e-5624a193a91f` / `rollout-2026-10-04T23-32-27-01a1078a-5052-73a2-b38e-5624a193a91f_01a1078b-8726-7e61-84d0-98deed6961bf.jsonl:L487` — 用户直接纠正简历整体结构和风格被改变。
- E017: `01a0fde7-9236-78c1-9068-6867a4ce6d8e` / `rollout-2026-10-03T02-43-13-01a0fde7-9236-78c1-9068-6867a4ce6d8e_01a0fded-77c6-71a2-99f6-a91075ef135d.jsonl:L3210` — 另一专利任务要求修复生成材料与指定参考格式的偏差。

- candidates: C-20261014-005
