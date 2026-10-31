# 大版本规划：整体方案先经子智能体评审，至多三轮

- id: `skill.major-version-plan-review`
- kind: skill
- status: active
- scope: 科研、前端、后端及通用任务中，主智能体准备提出或实质修订跨模块/阶段、影响项目主线的大版本总体方案时
- verification: explicit_user_future_instruction
- validity: stable
- updated_at: 2026-10-31T17:08:37+00:00

用户明确要求：在提出大版本规划时，主智能体应基于当前整体进展给出全面的总体版本方案，先交由真实评审子智能体审核，再处理意见后交付；提出与评审可以循环但最多三轮，真正小任务豁免。具体触发、计数、早停、上限未通过及与既有评审去重，统一由major-plan-review Skill承载，不在记忆另存流程。

## Boundaries

- 真正的小任务、既定总体方案内的局部下一步、润色和普通状态查询不单独触发。
- 当前用户明确限制范围、禁止委派或另作要求时，服从当前指令；规划及评审不授权实施。
- 独立Agent意见不等同于真人认可、零记忆隔离或实际实施效果；无真实评审时保留未审状态。
- target: skills/major-plan-review/SKILL.md

## Evidence pointers

- U20261101-major-plan-review: `01a138aa-2f25-70b3-bca8-406bf55d1c10` / `rollout-2026-10-23T14-18-14-01a138aa-2f25-70b3-bca8-406bf55d1c10_01a16768-f834-7970-94ce-c3608e22ccca.jsonl:L4131` — 用户明确要求记住：大版本规划基于整体进展给出全面版本，先让子智能体评审，可以循环但不超过三轮，小任务除外，并要求落地测试。

- candidates: none
