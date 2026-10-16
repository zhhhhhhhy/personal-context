# GAIA Claude test：trace与验收契约

- id: `project.gaia-claude-trace-contract-v2`
- kind: project
- status: active
- scope: 历史D:/worker/gaia_claude_test项目的联调与Agent team日志核对
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

对应gaia_claude_test版本保留完整轨迹/原始响应、token统计覆盖范围、代理层级及verification/recovery记录要求，LiteLLM数据按对话区分。联调连通性与答案质量分开验收，不固定旧试跑题量。

## Boundaries

- 日志字段是该项目验收口径，不是日常Context成本实验义务；不可观测项明确未知。
- 链路优先只限联调阶段，不代表正式评测忽略答案质量；当前实现未核。
- 旧5题、9题批次与启动命令不成为默认配额或新运行权限；与gaia_claude_code保持分开。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- review_after: 2027-01-16
- target: references/projects/gaia-claude-trace-contract.md

## Evidence pointers

- R012-M044: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L68` — 源会话cwd为gaia_claude_test；用户要求合并目录联调。
- R012-M045: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L371` — 仅原联调阶段先打通流程，答案错误不作阻塞。
- R012-M046: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L381` — 逐项要求trace、token范围与代理日志指标，未证明已运行。
- R012-M047: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L436` — 需要LiteLLM按对话分开采集。

- candidates: none
