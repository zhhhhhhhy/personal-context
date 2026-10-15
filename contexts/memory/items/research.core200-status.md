# Core200 用途与人审事实的待核边界

- id: `research.core200-status`
- kind: memory
- status: active
- scope: 核对该合同研究的 Core200 协议、人审归档和论文表述
- verification: claims_pending_source_verification
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

用户要求将 Core200 作为固定200题评测集表述，模型选择与阈值拟合使用开发集。用户提供的写作要求包含200题全部人审、两名独立审核者、第三人裁决分歧且未看模型建议；后续材料缺口明确逐题审核记录与样本ID尚未对应齐全，部分答案评分仍有模型评审记录。因此这些审核过程细节必须保留为用户陈述或待核事实，不能仅凭修改论文的请求当作已证实。

## Boundaries

- 不得推断 Core200 从未用于诊断或开发；历史使用需查记录。
- 审核汇总不证明每个模型输出都经过独立人工评分。
- 重用前核对最新台账；本轮没有重新验证历史实验数值。
- review_after: 2026-10-15

## Evidence pointers

- E131: `01a116a5-96a5-7cb3-8150-3c62ba850e3f` / `rollout-2026-10-08T18-23-02-01a116a5-96a5-7cb3-8150-3c62ba850e3f_01a11b09-b103-74e1-8e5d-763c1027e4e7.jsonl:L314` — 用户给出的200题与两人加第三人审核流程是论文写作要求。
- E134: `01a111b0-3cc1-70e1-9f7c-7d22cae53bd3` / `rollout-2026-10-08T23-13-42-01a111b0-3cc1-70e1-9f7c-7d22cae53bd3_01a11c13-cd58-7681-8a0a-437158e937cb.jsonl:L2297` — 用户同时列出逐题原始记录和人工评分依据尚待对应的缺口。

- candidates: C-20261014-033
