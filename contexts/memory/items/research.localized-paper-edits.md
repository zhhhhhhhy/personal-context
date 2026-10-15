# 特定论文的局部修改约定

- id: `research.localized-paper-edits`
- kind: memory
- status: active
- scope: 恢复该次已有 ICML 稿件的外部编辑任务
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该次 ICML 稿件逻辑已基本稳定，用户要求只改定位明确的问题位置，使用当时指定的 Claude Code；另一轮要求发送外部编辑 Prompt 前先供用户审核。恢复同一任务时先查当前编辑约定。

## Boundaries

- 这是特定稿件和委托的约定，不是所有未来修改都先审批。
- 当前用户直接指定的新工具或更大修改范围优先。
- review_after: 2026-10-15

## Evidence pointers

- E128: `01a116a5-96a5-7cb3-8150-3c62ba850e3f` / `rollout-2026-10-08T18-23-02-01a116a5-96a5-7cb3-8150-3c62ba850e3f_01a11b09-b103-74e1-8e5d-763c1027e4e7.jsonl:L410` — 用户明确限定局部位置并指定当时的编辑工具。
- E129: `01a116a5-96a5-7cb3-8150-3c62ba850e3f` / `rollout-2026-10-07T21-57-14-01a116a5-96a5-7cb3-8150-3c62ba850e3f_01a116a7-71b9-7f30-abcf-7d02d42fc46f.jsonl:L4353` — 用户要求当次外部编辑 Prompt 先审核。

- candidates: C-20261014-032
