# 现有19条记忆整理结果

日期：2026-10-16。按用户批准的评估执行：**精简保留6条、方法合并5条、转项目资料5条、归档旧执行记录3条**。没有处理新对话。原始记录和证据均保留，可追溯；最终实用性等待用户评估。

## 精简保留的6条

| 原编号 | 精简正文 | 适用范围与边界 |
|---|---|---|
| 4 | [陌生插件逐步引导](../../contexts/memory/items/learning.plugin-first-use.md)：首次使用且需要帮助时，分步解释操作，并让用户看见实际修改效果。 | 陌生插件或浏览器工具的初次引导；熟悉或已直接授权执行时，按当前要求推进。 |
| 5 | [按知识点整理题库](../../contexts/memory/items/learning.deduplicate-by-knowledge.md)：按知识点去重，保留覆盖多个知识点的题；提供代表题和答案解释。 | 题库整理与重复题筛选；批次大小和题量依当前任务确定；旧2000题、20题一批不是默认值。 |
| 6 | 仅本地保留，公开报告不展开正文 | 需 `--include-local`；不写Git |
| 7 | [迁移后再按授权清理](../../contexts/memory/items/migration.verify-before-cleanup.md)：清理旧目录前，更新路径引用，核对迁移文件及哈希，并保留提交或完整归档。 | 目录迁移与旧副本清理；清理前核对当前绝对路径、影响范围与授权；历史删除许可不延续。 |
| 14 | [中文逐题人工审核](../../contexts/memory/items/research.chinese-item-review.md)：需要本人逐项判定时，用中文逐题展示，并查当前台账避免重复已审条目。 | 用户参与的研究样本人工审核；审核进度和批次从当前台账读取；旧10/20批次不是默认值。 |
| 18 | [希望个人Skill按任务匹配](../../contexts/memory/items/skills.prefer-passive-routing.md)：希望合适的个人Skill按任务被动匹配，并能区分已加载、已执行和触发状态。 | 个人Skill的选择与维护；上游选择器不可观测时明确说明，不能仅凭回答声称已自动触发。 |

这些是可用的场景记忆，没有新增全局长期规则。单次任务数量、旧模型与阶段性权限退出正文，仍保留在旧记录中。

## 19条完整去向

| 原编号 | 原条目 | 去向 | 现行入口 |
|---|---|---|---|
| 1 | 浏览器填表项目的执行与迭代约定 | 合并到Skill | [工程计划、失败迭代与实验启动方法](../../skills/engineering-project-workflow/SKILL.md)；`skill.engineering-methods` |
| 2 | 自动填表的错误填写指标 | 项目资料 | [浏览器AutoFill：指标与续接约束](../../references/projects/browser-autofill.md)；`project.autofill-safety` |
| 3 | DemoPilot 的数据与失败记录 | 合并到Skill | [工程计划、失败迭代与实验启动方法](../../skills/engineering-project-workflow/SKILL.md)；`skill.engineering-methods` |
| 4 | 陌生插件的逐步引导 | 精简保留 | [陌生插件逐步引导](../../contexts/memory/items/learning.plugin-first-use.md)；`learning.plugin-first-use` |
| 5 | 大题库按知识点去重 | 精简保留 | [按知识点整理题库](../../contexts/memory/items/learning.deduplicate-by-knowledge.md)；`learning.deduplicate-by-knowledge` |
| 6 | 本地核验方法 | 精简保留，仅本地 | `.local/context-memory/` |
| 7 | 迁移后清理旧目录的检查清单 | 精简保留 | [迁移后再按授权清理](../../contexts/memory/items/migration.verify-before-cleanup.md)；`migration.verify-before-cleanup` |
| 8 | 新产品原型的可调整计划 | 合并到Skill | [工程计划、失败迭代与实验启动方法](../../skills/engineering-project-workflow/SKILL.md)；`skill.engineering-methods` |
| 9 | RAGSystem 的历史执行契约 | 项目资料 | [RAGSystem：历史契约定位](../../references/projects/rag-system.md)；`project.rag-contract` |
| 10 | 一次服务器与本机浏览器分工 | 归档旧执行记录 | [约定转存位置](../../references/projects/browser-autofill.md)；旧ID `remote.server-browser-topology` 用history追溯 |
| 11 | JEV 对照组与输入协议 | 项目资料 | [合同研究：JEV对照与任务边界](../../references/projects/contract-research.md)；`project.jev-comparison` |
| 12 | Core200 用途与人审事实的待核边界 | 项目资料 | [Core200：人审证据待补](../../references/projects/contract-research.md)；`project.core200-open-evidence` |
| 13 | 研究材料与标签缺口核对 | 合并到Skill | [学术证据核验已吸收](../../skills/academic-write/references/evidence-and-artifacts.md)；`skill.research-evidence` |
| 14 | Benchmark 逐题人工审核约定 | 精简保留 | [中文逐题人工审核](../../contexts/memory/items/research.chinese-item-review.md)；`research.chinese-item-review` |
| 15 | 特定论文的局部修改约定 | 归档旧执行记录 | [约定转存位置](../../references/projects/contract-research.md)；旧ID `research.localized-paper-edits` 用history追溯 |
| 16 | 论文同步要求的实际时间线 | 归档旧执行记录 | [约定转存位置](../../references/projects/contract-research.md)；旧ID `research.paper-sync-current` 用history追溯 |
| 17 | 科研启动与小批实验约定 | 合并到Skill | [工程计划、失败迭代与实验启动方法](../../skills/engineering-project-workflow/SKILL.md)；`skill.engineering-methods` |
| 18 | 个人 Skill 的触发期望 | 精简保留 | [希望个人Skill按任务匹配](../../contexts/memory/items/skills.prefer-passive-routing.md)；`skills.prefer-passive-routing` |
| 19 | 任务图产品的设计选择 | 项目资料 | [任务图：范围与验收设计](../../references/projects/taskgraph.md)；`project.taskgraph-design-scoped` |

## 项目与版本核对

- AutoFill与RAGSystem保留为不同项目，未因名称相似合并。远端当前根目录、commit和运行状态未重新核验，明确留待核。AutoFill早期32B选择后续变为GPU条件选择；主机浏览器及同任务的语言/分工约定保留。
- 合同研究按任务与稿件分开：10月4日指定稿同步，10月6日该工程任务不自动同步文章；10月8日原外部编辑任务的Claude Code与发送Prompt前确认条件仍保留。归档不表示这些条件已失效或任务已完成。
- 任务图本地MVP_SPEC定义只读观测，与旧混合验收设计不同。旧接口方案标为历史意图；当前实现不由历史记忆推断。DemoPilot核对了本地HEAD、修改状态和验收文件，只合并通用方法，不沿用旧统计为当前成绩。
- Core200的200题、人审人数/裁决及模型辅助评分边界继续作为项目待核问题；83、135/200、136/200、164/200等具体提议或问题没有消失，也没有变成已验证结果。

详细记录：[version-checks.json](version-checks.json)。

## 以后按需加载

1. 仍先读4个核心入口一次，当前正文合计1,931 tokens。
2. 普通任务：`search --query "人工审核"` → `show --id research.chinese-item-review`。只加载命中的偏好/方法；项目资料默认不返回。
3. 已知项目：先核对目录、remote/commit和当前协议，再 `search --project contract-research --query "Core200 人审"` → `show --id project.core200-open-evidence` → 只读[项目页](../../references/projects/contract-research.md)的对应小节。带关键词的项目检索仍返回相关通用偏好。
4. 工程方法：命中 `skill.engineering-methods` 后加载 `skills/engineering-project-workflow/SKILL.md`，再按阶段选参考文件。学术证据缺口走 `academic-write` 的证据参考。两个完整Skill包已同步运行时。
5. 本地敏感条目只在确实需要时用 `--include-local`。追溯旧数量/执行约定用 `history --id <旧ID>`，不把旧正文当现行指令。

## 验证与实际限制

- 19条映射和46条候选去向均已核对；新活跃池为6条记忆（5公开、1本地）、5条项目资料，以及原有规则/核心与Skill路由。3条旧执行记录退出默认检索。
- 聚焦检查覆盖默认检索、指定项目、错误项目、通用偏好仍可检索、私有条目限制、归档正文禁止默认读取、证据延续、用户原有编辑保留、Skill包同步与预算；没有全量独立复核。
- 同口径统计保留6条的标题/正文/范围/例外：776 → 500 tokens，减少35.6%。这只是条目内容量，不是本次会话或未来每次任务的实际总加载量。
- 没有验证当前远端部署、重新做人审或运行科研实验；存下的待核问题仍待真实材料解决。检索与结构检查通过不等于用户已认可提炼质量。

检查证据：[validation.json](validation.json)、[budget.json](budget.json)、[工作状态](WORKFLOW_STATE.md)。记忆写入使用本地受保护事务；本轮先初次整理，再做任务图版本修正，回滚时须按逆序，Skill/说明文件另由Git保留变更历史。
