# 速度比较：先对齐被测任务和计时阶段

- id: `evaluation.match-measurement-stage`
- kind: memory
- status: active
- scope: 比较判别模块效率、模型流水线延迟，或核查当前Codex会话输出速度时
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T14:55:54+00:00

比较模型或模块速度时，先对齐实际任务和计时阶段：判别工作与判别工作比较；若用户问当前会话吐字速度，测实际会话输出的tokens/s，不拿整条推理流水线耗时替代。

## Boundaries

- 用户关心端到端耗时时可以比较整条流程，但须明确各自包含的阶段。
- 未取得对应会话或运行日志时保留未测状态；历史模型版本与旧速度不作为当前实测。

## Evidence pointers

- HB00690: `01a0de32-f9d8-7691-9871-af57b35b13fd` / `rollout-2026-09-27T15-57-42-01a0de32-f9d8-7691-9871-af57b35b13fd_01a0e1de-aef2-71b1-ab79-fa0f2026c559.jsonl:L348` — 直接用户表达；仅在本条限定场景使用，不证明所请求的事实或工作已完成。
- HB01185: `01a11073-f72f-7a40-b656-de4089ed6078` / `rollout-2026-10-06T17-03-17-01a11073-f72f-7a40-b656-de4089ed6078.jsonl:L36` — 直接用户表达；仅在本条限定场景使用，不证明所请求的事实或工作已完成。
- HB01187: `01a11073-f72f-7a40-b656-de4089ed6078` / `rollout-2026-10-06T17-09-35-01a11073-f72f-7a40-b656-de4089ed6078_01a11079-b8d2-7bf2-aa8b-3cb493e3b80b.jsonl:L8` — 直接用户表达；仅在本条限定场景使用，不证明所请求的事实或工作已完成。

- candidates: none
