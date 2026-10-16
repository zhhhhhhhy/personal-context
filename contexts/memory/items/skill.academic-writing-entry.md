# 学术写作：层级、因果链与证据入口

- id: `skill.academic-writing-entry`
- kind: skill
- status: active
- scope: 论文写作或大幅修改及其中的论证、来源和结论边界核查
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T06:51:20+00:00

论文层级、研究因果链和证据核验按academic-write读取相关小节：paper-workflow.md管定位与论证，evidence-and-artifacts.md管来源、人工审核与结论范围。

## Boundaries

- 先确认当篇论文类型；Benchmark中的方法定位不能推广到所有论文，存在方法贡献时按该篇定位处理。
- 人工审核汇总不等于所有输出逐题人工评分；模型辅助参考不自动成为人工金标准。
- 旧章节冻结和项目结果留历史；覆盖入口不取代专门评审Skill，也不强制加载全部写作参考。
- review_after: 2027-01-15
- target: skills/academic-write/SKILL.md

## Evidence pointers

- E024: `01a129b0-b99c-7f42-96c0-a0f4b948f786` / `rollout-2026-10-11T14-40-10-01a129b0-b99c-7f42-96c0-a0f4b948f786.jsonl:L31` — 用户对当前论文逻辑和贡献层级提出要求。
- E079: `01a0fe11-bb1e-7611-afc3-6a939e318c78` / `rollout-2026-10-03T05-34-38-01a0fe11-bb1e-7611-afc3-6a939e318c78_01a0fe8a-6932-7a43-9823-4e5d3522f69f.jsonl:L36` — 用户明确要求 benchmark-first。
- E082: `01a11266-18ff-7b92-bdec-81772b1c0b18` / `rollout-2026-10-07T14-02-01-01a11266-18ff-7b92-bdec-81772b1c0b18_01a114f4-5f69-7071-9452-011db73195e6.jsonl:L691` — 用户直接批评判定节点尚不足以构成机制，并要求回到合同任务问题。
- E120: `01a09902-7e8e-7290-af3d-e24a15f69e60` / `rollout-2026-09-14T11-27-11-01a09902-7e8e-7290-af3d-e24a15f69e60_01a09df4-569b-7a30-86d9-3badd1999ad3.jsonl:L444` — 用户要求将核心主张改成可检验假设。
- E134: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-08T23-13-42-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3_01a11c13-cd58-7681-8a0a-437158e937cb.jsonl:L2297` — 用户明确列出逐题人审归档和模型评分依据仍待对应的缺口。
- E143: `01a09902-7e8e-7290-af3d-e24a15f69e60` / `rollout-2026-09-14T11-27-11-01a09902-7e8e-7290-af3d-e24a15f69e60_01a09df4-569b-7a30-86d9-3badd1999ad3.jsonl:L53` — 用户要求核查材料和结果边界。
- E094: `01a11266-18ff-7b92-bdec-81772b1c0b18` / `rollout-2026-10-07T14-02-01-01a11266-18ff-7b92-bdec-81772b1c0b18_01a114f4-5f69-7071-9452-011db73195e6.jsonl:L1268` — 用户要求到实际项目查找论文证据缺口。
- E095: `01a11266-18ff-7b92-bdec-81772b1c0b18` / `rollout-2026-10-09T17-47-15-01a11266-18ff-7b92-bdec-81772b1c0b18_01a1200f-4915-7602-9658-c9f6fa81d259.jsonl:L3853` — 用户提出实际评分与数据诊断问题。

- candidates: C-20261014-006, C-20261014-018, C-20261014-019, C-20261014-023, C-20261014-030, C-20261014-036
