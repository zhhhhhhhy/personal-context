# RAGSystem：契约入口与GPU停用约束

## 续接摘要

历史权威根目录为/workspace/zhy/RAGSystem，续接先定位对应版本的docs/autofill_contract契约，以当前项目文件为准；该任务约定技术材料英文、用户汇报中文，不导入其他AutoFill任务的模型和数据设置。2026-10-21同一来源任务的用户明确要求停止该项目使用GPU；旧模型或运行参数不构成恢复GPU使用的许可，需后续明确变更该约束。实际停用和资源占用尚未由本维护核实。

- 历史位置不证明当前远程目录、commit或部署状态；恢复任务时核对。
- 与browser-autofill的仓库身份及契约等价性未确认，保持分开；不延续旧服务器访问权限。

本次只整理已有Context，没有读取项目运行状态。先用本节确认范围，只有相关任务需要时才读取下面的版本细节；旧约定未因摘要精简而取消。

## GPU停用要求（2026-10-21同源任务）

- 用户在同一父对话`01a1065a-38b3-74f0-b70a-b05d3e7c9c9c`于`2026-10-21T07:37:15.315Z`明确说：“停止吧 这个项目不要使用GPU了。”来源证据为`D20261021-037`。
- 后续续接该项目，不能凭旧模型、运行参数或历史授权自行恢复GPU使用；需要后续明确变更这一约束。询问历史占用或服务器情况不等于恢复使用许可。
- 只适用于这个RAGSystem来源任务，不扩展到MASArena、其他项目或他人服务；具体资源归属和影响范围仍待核对。
- 这里保存的是用户指令，**不是GPU已停止的完成证据**。本维护没有连接服务器、终止任务或核实占用；也没有更改其他项目的资源安排。

## 来源版本与历史细节（按需追溯）

### RAGSystem: locate the current execution contract

Identity: project key `rag-system`; source family `01a1065a-38b3-74f0-b70a-b05d3e7c9c9c`; E042 supplied a project prompt at 2026-10-04 09:59:06Z. It specified `/workspace/zhy/RAGSystem` as the authoritative root. This is verified as a historical supplied contract, not verified as today's remote revision.

On continuation, establish the current root and revision before applying the agreement. At the source version, read `docs/autofill_contract/PROJECT_GOAL.md`, `PROJECT_PLAN.md`, `PROJECT_CONSTRAINTS.md`, `EVALUATION_AND_RESULTS.md`, `ERRORS_AND_LESSONS.md`, and `CONVERSATION_CONTEXT.md`. Technical artifacts/prompts were English and user reports Chinese. Use current files instead of loading the whole historical prompt.

The related browser AutoFill record is a different source task. No repository identity/commit equivalence was established here; its model, dataset and delegation choices are not imported into this contract. No new remote access or execution permission follows from the stored prompt.

Evidence: E042. Destination of original memory 9; detailed pointer remains in `project.rag-contract`.
