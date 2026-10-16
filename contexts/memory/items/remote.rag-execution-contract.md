# RAGSystem 的历史执行契约

> Historical record. Excluded from active retrieval; do not apply as an instruction.

- id: `remote.rag-execution-contract`
- kind: memory
- status: superseded
- scope: 继续该 RAGSystem/AutoFill 历史工程任务时先定位当前契约
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-16T01:41:42+00:00

该次 AutoFill 执行 Prompt 指定权威根目录为 /workspace/zhy/RAGSystem，先读取 docs/autofill_contract 下的目标、计划、约束、评估、失败记录和对话上下文文件。项目材料和 Prompt 用英文，向用户简洁中文汇报。它是当时提供的任务契约，不能由多次登录地址推导出所有远程任务都遵守同一套协议。

## Boundaries

- 重用前验证当前权威目录和协议文件；历史路径可能已迁移。
- 该 Prompt 的提供不等于跨任务个人偏好或新的服务器访问权限。
- review_after: 2026-10-15
- replaced_by: project.rag-contract

## Evidence pointers

- E042: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c` / `rollout-2026-10-04T17-58-58-01a1065a-38b3-74f0-b70a-b05d3e7c9c9c.jsonl:L12` — 该父对话提供了明确项目目录和执行契约的 Prompt。

- candidates: C-20261014-009
