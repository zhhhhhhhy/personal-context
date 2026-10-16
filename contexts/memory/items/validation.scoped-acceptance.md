# 工程验证：最小充分检查与约定验收

- id: `validation.scoped-acceptance`
- kind: rule
- status: active
- scope: 工程变更的验证；存在指定最终验收集合时同时遵守该集合
- verification: supported_preference
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

日常检查按minimal-validation-workflow选择最小充分证据；用户已约定最终验收集合时，按该集合判断完成并说明未覆盖部分。抽样通过只证明抽样范围。

## Boundaries

- 不因小改动重复全量验收，不在未约定时擅自制造全量测试义务。
- 强制安全门槛和明确验收集合仍须满足；具体检查流程只读目标Skill。
- 合并的是既有验收原则和覆盖登记，不是新晋升一条长期规则。
- review_after: 2027-01-15
- target: skills/minimal-validation-workflow/SKILL.md

## Evidence pointers

- E086: `01a1087d-3246-7ec3-a3a0-f49546b4c391` / `rollout-2026-10-05T21-10-27-01a1087d-3246-7ec3-a3a0-f49546b4c391_01a10c2f-e3c1-7a00-9714-cfff64d5eda2.jsonl:L2836` — Demo 项目明确拒绝用单个样本通过代表整体完成。
- E088: `01a0f292-cdfe-7463-ad96-65832ab94c06` / `rollout-2026-10-03T02-46-13-01a0f292-cdfe-7463-ad96-65832ab94c06_01a0fdf0-3692-7ad3-b962-7bb604fd5054.jsonl:L6347` — 另一科研任务指定200条核心集用于最终验收，一般测试使用开发集。
- E036: `01a117d1-2764-72e2-ad04-6d9436d6ce3e` / `rollout-2026-10-08T03-22-25-01a117d1-2764-72e2-ad04-6d9436d6ce3e.jsonl:L315` — 用户明确指出验证过多、耗时。
- E041: `01a117d1-2764-72e2-ad04-6d9436d6ce3e` / `rollout-2026-10-08T03-22-25-01a117d1-2764-72e2-ad04-6d9436d6ce3e.jsonl:L594` — 用户要求减少重复和无关验证。

- candidates: C-20261014-008, C-20261014-020
