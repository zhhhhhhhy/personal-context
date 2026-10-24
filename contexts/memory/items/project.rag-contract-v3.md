# RAGSystem：契约入口与GPU停用约束

- id: `project.rag-contract-v3`
- kind: project
- status: active
- scope: 2026-10-04提供的RAGSystem契约及2026-10-21同一父对话的GPU停用要求；当前根目录、commit和资源归属待核
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-21T10:28:10+00:00

历史权威根目录为/workspace/zhy/RAGSystem，续接先定位对应版本的docs/autofill_contract契约，以当前项目文件为准；该任务约定技术材料英文、用户汇报中文，不导入其他AutoFill任务的模型和数据设置。2026-10-21同一来源任务的用户明确要求停止该项目使用GPU；旧模型或运行参数不构成恢复GPU使用的许可，需后续明确变更该约束。实际停用和资源占用尚未由本维护核实。

## Boundaries

- 历史位置不证明当前远程目录、commit或部署状态；恢复任务时核对。
- 与browser-autofill的仓库身份及契约等价性未确认，保持分开；不延续旧服务器访问权限。
- 2026-10-16此次仅整理已有Context，未重新核验项目状态；保留详细来源版本约定，不撤销仍适用的条件。
- GPU停用只限该RAGSystem来源任务，不扩展到MASArena、其他项目或他人服务；资源归属和具体影响范围仍须核对。
- 本条记录用户要求，不证明GPU任务已经停止；询问GPU历史占用或服务器情况不等于撤销停用约束。
- review_after: 2026-11-21
- target: references/projects/rag-system.md

## Evidence pointers

- E042: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c` / `rollout-2026-10-04T17-58-58-01a1065a-38b3-74f0-b70a-b05d3e7c9c9c.jsonl:L12` — 该父对话提供了明确项目目录和执行契约的 Prompt。
- D20261021-037: `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c` / `rollout-2026-10-08T18-21-55-01a1065a-38b3-74f0-b70a-b05d3e7c9c9c_01a11b08-aae5-7623-8390-f7097213ea18.jsonl:L22847` — 用户在RAGSystem同源父对话中明确要求停止该项目使用GPU；不证明停用已完成，也不授权本维护任务操作服务器。

- candidates: C-20261014-009
