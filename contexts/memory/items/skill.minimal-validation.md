# 最小充分验证已吸收

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `skill.minimal-validation`
- kind: skill
- status: merged
- scope: 代码、配置、Skill 和工程变更
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

默认选择能够证明变更路径的最小检查，避免无关扩测和无变化时重复已经通过的检查；用户指定的验收范围仍须完成。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2027-01-15
- target: skills/minimal-validation-workflow/SKILL.md
- merged_into: validation.scoped-acceptance

## Evidence pointers

- E036: `01a117d1-2764-72e2-ad04-6d9436d6ce3e` / `rollout-2026-10-08T03-22-25-01a117d1-2764-72e2-ad04-6d9436d6ce3e.jsonl:L315` — 用户明确指出验证过多、耗时。
- E041: `01a117d1-2764-72e2-ad04-6d9436d6ce3e` / `rollout-2026-10-08T03-22-25-01a117d1-2764-72e2-ad04-6d9436d6ce3e.jsonl:L594` — 用户要求减少重复和无关验证。

- candidates: C-20261014-008
