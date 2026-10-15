# 陌生插件的逐步引导

- id: `learning.plugin-guidance`
- kind: memory
- status: active
- scope: 初次使用且用户需要指导的插件或浏览器工具
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-15T13:49:28+00:00

第一次使用插件、尚不清楚界面和修改效果时，用户要求一步一步指导，并能实时看到修改。先说明当前操作和下一步，再根据用户熟悉程度调整。

## Boundaries

- 已有熟练操作经验或当前直接授权执行时，不机械退回教学流程。
- 不从这段历史推断完成授权后必须自动接管。
- review_after: 2027-01-15

## Evidence pointers

- E049: `019ff24d-6d48-7321-80f0-e96c1cedbeda` / `rollout-2026-08-12T03-29-48-019ff24d-6d48-7321-80f0-e96c1cedbeda.jsonl:L433` — 用户明确要求一步一步教使用。
- E055: `019ff24d-6d48-7321-80f0-e96c1cedbeda` / `rollout-2026-08-12T03-29-48-019ff24d-6d48-7321-80f0-e96c1cedbeda.jsonl:L1261` — 用户说明第一次做插件并询问如何实时看修改。

- candidates: C-20261014-010
