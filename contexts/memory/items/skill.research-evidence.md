# 学术证据核验已吸收

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `skill.research-evidence`
- kind: skill
- status: merged
- scope: 论文或实验结果的来源、人工审核与结论范围检查
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

把用户陈述、论文写作请求、已核验记录和缺失归档分开。人工审核汇总不证明所有模型输出逐题人工评分；模型辅助参考不能直接叫人工金标准。

## Boundaries

- 仅用于上述场景；当前用户要求、当前项目协议和事实核查结果优先。
- review_after: 2027-01-15
- target: skills/academic-write/references/evidence-and-artifacts.md
- merged_into: skill.academic-writing-entry

## Evidence pointers

- E134: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-08T23-13-42-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3_01a11c13-cd58-7681-8a0a-437158e937cb.jsonl:L2297` — 用户明确列出逐题人审归档和模型评分依据仍待对应的缺口。
- E143: `01a09902-7e8e-7290-af3d-e24a15f69e60` / `rollout-2026-09-14T11-27-11-01a09902-7e8e-7290-af3d-e24a15f69e60_01a09df4-569b-7a30-86d9-3badd1999ad3.jsonl:L53` — 用户要求核查材料和结果边界。
- E094: `01a11266-18ff-7b92-bdec-81772b1c0b18` / `rollout-2026-10-07T14-02-01-01a11266-18ff-7b92-bdec-81772b1c0b18_01a114f4-5f69-7071-9452-011db73195e6.jsonl:L1268` — 用户要求到实际项目查找论文证据缺口。
- E095: `01a11266-18ff-7b92-bdec-81772b1c0b18` / `rollout-2026-10-09T17-47-15-01a11266-18ff-7b92-bdec-81772b1c0b18_01a1200f-4915-7602-9658-c9f6fa81d259.jsonl:L3853` — 用户提出实际评分与数据诊断问题。

- candidates: C-20261014-023, C-20261014-036
