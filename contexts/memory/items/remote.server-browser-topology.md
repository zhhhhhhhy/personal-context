# 一次服务器与本机浏览器分工

- id: `remote.server-browser-topology`
- kind: memory
- status: active
- scope: 恢复该次远程模型与主机浏览器联合测试
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该次实现方案明确服务器可使用 Qwen32B，其他工程工作放服务器，浏览器使用用户主机的浏览器，测试后释放模型资源。这是指定任务的部署选择；重用前确认当前模型、GPU、服务器和真实浏览器通道。

## Boundaries

- 不是所有项目的固定部署拓扑。
- 不含登录凭据，也不授予新的远程或浏览器操作权限。
- review_after: 2026-10-15

## Evidence pointers

- E161: `01a0f78f-e0ea-7a70-ab46-85f58a670924` / `rollout-2026-10-03T16-19-22-01a0f78f-e0ea-7a70-ab46-85f58a670924_01a100d8-ac5f-7cd2-83e2-762f1858158f.jsonl:L1051` — 用户明确服务器Qwen32B、主机浏览器和测试后释放资源。

- candidates: C-20261014-044
