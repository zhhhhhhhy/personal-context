# 浏览器AutoFill：续接约束与验收入口

## 续接摘要

继续对应AutoFill版本时，把错误填写单独作为验收指标，保留主机浏览器边界、技术材料英文/用户汇报中文及条件化模型选择。当前实现和阈值按匹配项目契约确认；旧目标、材料范围和试跑选择仅留历史。

- 只用于2026-10-02～04来源对应任务；当前根目录、版本与浏览器通道需在实际续接时核对。
- 95%目标、四类材料和旧模型选择不是当前默认值；GPU条件及主机浏览器边界未被此次整理取消。
- 不与RAGSystem自动合并，不授予委派、服务器或浏览器权限。

本次只整理已有Context，没有读取项目运行状态。先用本节确认范围，只有相关任务需要时才读取下面的版本细节；旧约定未因摘要精简而取消。

## 来源版本与历史细节（按需追溯）

### Browser AutoFill: scoped project material

Identity: project key `browser-autofill`; source family `01a0f78f-e0ea-7a70-ab46-85f58a670924`; source workspace `2026-10-01/new-chat`. Verified source-message version: 2026-10-02 through 2026-10-04 UTC. Current server root, commit and deployed state were not rechecked in this reorganization. Do not merge with `rag-system` until root, remote and contract version are verified.

## Evaluation agreement (original memory 2)

Avoid false fills as a separate hard metric, even at some cost to aggregate accuracy. The user proposed **95%+** on the then-current test set; it is a target, not a measured result. Define dataset version/split, denominator, false-fill measure and threshold in the current contract. Material types: HTML, Word, Excel and Markdown. Historical E160 also proposed a single-answer holdout procedure; do not silently reuse it as a currently frozen evaluation protocol.

## Continuing project constraints (from original memories 1 and 10)

- Preserve requirements, architecture/specification, task inputs/outputs, evaluation and a human-readable acceptance report in the project's chosen documents. Generic failure-analysis/planning method now belongs to the engineering Skill.
- E156 (2026-10-04) requested English technical artifacts/prompts and Chinese user reports; main-agent planning/delegation where the current platform, budget and authorization allow; reuse or repair open-source dependencies only within current scope. Do not infer delegation or repository-modification rights for another task.
- E161 (2026-10-03 11:50:41Z) chose server-side Qwen32B and engineering work, the user's host browser, then release the test model. **Not verified expired.** E160 (2026-10-04 08:25:00Z) subsequently made 32B conditional on available GPU capacity. Preserve the host-browser boundary when continuing that assignment; check actual server, model, GPU and browser channel first. Do not hard-code 32B as the current model. Releasing resources applies to the authorized test's resources, not unrelated processes.

Current instructions and the matching project's present contract take priority. This page preserves potentially live constraints while the standalone old deployment record is archived. It does not grant SSH/browser permissions or claim tests were rerun.

Evidence: E150, E152, E153, E156, E160, E161; complete existing pointers remain in the associated lifecycle records. Original 10: `history --id remote.server-browser-topology`.
