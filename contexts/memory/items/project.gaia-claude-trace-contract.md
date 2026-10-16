# 项目：GAIA Claude联调与trace计量口径

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `project.gaia-claude-trace-contract`
- kind: project
- status: superseded
- scope: 历史D:/worker/gaia_claude_test项目的联调与Agent team日志核对
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T06:33:13+00:00

原gaia_claude_test合并项目的联调先确认链路互通，答案正确率另评；需要完整trace/原始响应，说明token计数是否含system、subagent、hidden context、compaction、retry和工具相关模型调用，并统计代理数/深度、verification与recovery；LiteLLM数据按对话分开。

## Boundaries

- 这是用户提出的验收要求，原项目现版本与运行结果未核；没有证明上述日志或指标已具备。
- 链路优先仅适用于原联调阶段，不意味着正式评测忽略答案质量；不可观测计量保留未知。
- 原尝试5题与启动config.yaml是旧执行要求，不转为永久配额或本次运行授权。
- review_after: 2027-01-16
- target: references/projects/gaia-claude-trace-contract.md
- replaced_by: project.gaia-claude-trace-contract-v2

## Evidence pointers

- R012-M044: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L68` — 源会话cwd为gaia_claude_test；用户要求合并目录联调。
- R012-M045: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L371` — 仅原联调阶段先打通流程，答案错误不作阻塞。
- R012-M046: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L381` — 逐项要求trace、token范围与代理日志指标，未证明已运行。
- R012-M047: `019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8` / `rollout-2026-04-24T11-32-28-019dbd8b-c9c9-7f52-aa21-54d8c9b7fda8.jsonl:L436` — 需要LiteLLM按对话分开采集。

- candidates: none
