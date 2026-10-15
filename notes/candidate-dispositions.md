# 46 条历史候选的最终去向

原候选是历史提炼文本；实际使用以目标条目的范围、状态和例外为准。已有覆盖与本次新增分开记录。

| 编号 | 去向 | 处理方式 | 目标 | 理由 |
|---|---|---|---|---|
| 001 | Skill | already_covered | [专利材料工作流已吸收](../contexts/memory/items/skill.patent-workflow.md) | 与003合并；专利Skill已经要求步骤.md，不把同一任务重复计数。 |
| 002 | 舍弃 | discarded | — | 原线程未定位，且不能把一次先讨论要求变成所有Skill修改都要审批。 |
| 003 | Skill | already_covered | [专利材料工作流已吸收](../contexts/memory/items/skill.patent-workflow.md) | 保留专利场景的输入输出与步骤要求；其他材料未逐项支持的泛化不采纳。 |
| 004 | Skill | already_covered | [专利材料工作流已吸收](../contexts/memory/items/skill.patent-workflow.md) | 模板与本人事实隔离已由专利Skill明确承载。 |
| 005 | 长期规则 | new | [编辑已有材料时保留约定风格](../contexts/memory/items/documents.preserve-style.md) | 不同材料任务均直接纠正风格偏移；仅晋升风格保持，视觉验收仍由对应Skill承载。 |
| 006 | Skill | already_covered | [论文类型与贡献层级已吸收](../contexts/memory/items/skill.paper-hierarchy.md) | 论文类型和贡献层级已被academic-write覆盖；历史章节冻结不作永久规则。 |
| 007 | 可用记忆 | new_scoped | [个人 Skill 的触发期望](../contexts/memory/items/skills.passive-routing.md) | 保存明确的个人Skill路由期望，不冒充已经验证自动触发。 |
| 008 | Skill | already_covered | [最小充分验证已吸收](../contexts/memory/items/skill.minimal-validation.md) | 最小验证Skill已有完整约束，本次纳入统一维护源。 |
| 009 | 可用记忆 | narrowed | [RAGSystem 的历史执行契约](../contexts/memory/items/remote.rag-execution-contract.md) | 只保存一份明确RAGSystem执行契约；多个登录地址不算泛化证据。 |
| 010 | 可用记忆 | narrowed | [陌生插件的逐步引导](../contexts/memory/items/learning.plugin-guidance.md) | 保留陌生插件逐步引导；移除没有证据的自动接管推断。 |
| 011 | 长期规则 | already_covered | [已有沟通规则覆盖](../contexts/memory/items/core.communication.md) | 已有沟通核心覆盖，去掉固定意图审计格式的泛化。 |
| 012 | Skill | already_covered | [专利材料工作流已吸收](../contexts/memory/items/skill.patent-workflow.md) | 专利实施步骤直接动作与逐项对应已在Skill中。 |
| 013 | Skill | already_covered | [专利材料工作流已吸收](../contexts/memory/items/skill.patent-workflow.md) | 文稿与渲染检查由专利Skill承载，具体图形格式保持项目范围。 |
| 014 | 可用记忆 | narrowed | [新产品原型的可调整计划](../contexts/memory/items/project.adjustable-plan.md) | 保留该原型项目可调整计划，不把重复任务Prompt当三次独立偏好。 |
| 015 | 长期规则 | merged_existing | [已有委派规则与任务 Prompt](../contexts/memory/items/core.delegation.md) | 与040合并，主行为已在SOUL委派规则中，不算新增长期规则。 |
| 016 | 可用记忆 | merged_scoped | [科研启动与小批实验约定](../contexts/memory/items/research.startup-protocol.md) | 保留明确小批实验和条件；与041的特定启动边界合并。 |
| 017 | 可用记忆 | corrected_and_replaced | [论文同步要求的实际时间线](../contexts/memory/items/research.paper-sync-current.md) | 按原消息日期限定：10月4日曾指定更新ICML稿，10月6日随后要求当前阶段只做工程、不自动同步；旧摘要时间线已纠正。 |
| 018 | Skill | already_covered | [论文类型与贡献层级已吸收](../contexts/memory/items/skill.paper-hierarchy.md) | 合并到benchmark写作层级，不把所有论文固定为benchmark。 |
| 019 | Skill | refined | [研究因果链与证据边界](../contexts/memory/items/skill.research-causality.md) | 只吸收直接表达的任务难点与机制区分，引用意见不作个人偏好。 |
| 020 | 长期规则 | new | [按约定范围说明验收结果](../contexts/memory/items/validation.agreed-coverage.md) | Demo与科研均明确指定验收范围；与日常最小验证保持兼容。 |
| 021 | 可用记忆 | narrowed | [DemoPilot 的数据与失败记录](../contexts/memory/items/demopilot.acceptance.md) | 保存DemoPilot工作流；剔除自动Builder作为个人偏好证据。 |
| 022 | 长期规则 | already_covered | [已有授权内自主执行规则](../contexts/memory/items/core.autonomy.md) | 已授权内自主推进由SOUL覆盖；不从历史扩大当前权限。 |
| 023 | 可用记忆 | narrowed | [研究材料与标签缺口核对](../contexts/memory/items/research.data-audit-task.md) | 保存该研究材料补缺任务，不把混合反馈拼成所有研究的强制流程。 |
| 024 | 长期规则 | merged_existing | [已有沟通规则覆盖](../contexts/memory/items/core.communication.md) | 与011/035/046合并到已有沟通规则。 |
| 025 | 舍弃 | discarded | — | 原候选含矛盾和敏感来源，不选择性拼成稳定偏好；原始证据保留本地。 |
| 026 | 可用记忆 | local_only | `local.project-material-verification`（仅本地） | 收窄为明确的材料核验任务；敏感主题仅本地，不确认未经证实的个人事实。 |
| 027 | 舍弃 | discarded | — | 三个来源均为自动exec模板，不能作为三次独立个人偏好；项目要求由021的直接来源保留。 |
| 028 | 可用记忆 | new_scoped | [大题库按知识点去重](../contexts/memory/items/learning.question-dedup.md) | 保留约2000题、知识点去重与约20题分批的具体任务范围。 |
| 029 | 可用记忆 | new_scoped | [迁移后清理旧目录的检查清单](../contexts/memory/items/migration.old-directory-checklist.md) | 保存一次明确迁移清单；方法不等于未来删除权限。 |
| 030 | Skill | already_covered | [研究因果链与证据边界](../contexts/memory/items/skill.research-causality.md) | 与019合并为可检验假设和证据范围，不重复新增同义规则。 |
| 031 | 可用记忆 | new_scoped | [Benchmark 逐题人工审核约定](../contexts/memory/items/research.human-review.md) | 保存逐题中文审核约定和历史10/20数量，当前进度待台账确认。 |
| 032 | 可用记忆 | narrowed | [特定论文的局部修改约定](../contexts/memory/items/research.localized-paper-edits.md) | 只保留指定稿件与当次外部编辑Prompt审核要求。 |
| 033 | 可用记忆 | pending_facts_usable_scope | [Core200 用途与人审事实的待核边界](../contexts/memory/items/research.core200-status.md) | 用途约定可调用；200题及2人/第三人流程保留出处和待核状态。 |
| 034 | 可用记忆 | narrowed | [JEV 对照组与输入协议](../contexts/memory/items/research.comparison-protocol.md) | 保存对照组、83条提议和方差追问，不把提议或疑问写成已完成实验。 |
| 035 | 长期规则 | already_covered | [已有沟通规则覆盖](../contexts/memory/items/core.communication.md) | 直白说明机制由已有沟通规则覆盖，不强制每次都读全部代码。 |
| 036 | Skill | refined | [学术证据核验已吸收](../contexts/memory/items/skill.research-evidence.md) | 已有证据规则补足陈述、写作要求和可核验记录的区分。 |
| 037 | 可用记忆 | new_scoped | [任务图产品的设计选择](../contexts/memory/items/taskgraph.project-design.md) | 保存特定任务图设计和未实现期望，不约束其他产品架构。 |
| 038 | 可用记忆 | merged_scoped | [浏览器填表项目的执行与迭代约定](../contexts/memory/items/autofill.execution-method.md) | 与039/042/045合并成该项目执行约定，不要求所有项目固定文档清单。 |
| 039 | 可用记忆 | merged_scoped | [浏览器填表项目的执行与迭代约定](../contexts/memory/items/autofill.execution-method.md) | 保留失败归因循环；重要环境阻塞仍须报告。 |
| 040 | 长期规则 | merged_existing | [已有委派规则与任务 Prompt](../contexts/memory/items/core.delegation.md) | 与015合并到已有委派规则，按任务补缺，不机械扩大Prompt。 |
| 041 | 可用记忆 | merged_scoped | [科研启动与小批实验约定](../contexts/memory/items/research.startup-protocol.md) | 保留当次六项启动询问，历史暂停不延续成当前执行禁令。 |
| 042 | 可用记忆 | merged_scoped | [浏览器填表项目的执行与迭代约定](../contexts/memory/items/autofill.execution-method.md) | 限定该长程项目，保留尽可能和资源/权限限制；不是两个独立父对话。 |
| 043 | 可用记忆 | new_scoped | [自动填表的错误填写指标](../contexts/memory/items/autofill.safety-target.md) | 保存错误填写硬指标及95%暂定目标，不伪造已测成绩或零错误。 |
| 044 | 可用记忆 | new_scoped | [一次服务器与本机浏览器分工](../contexts/memory/items/remote.server-browser-topology.md) | 保留32B、主机浏览器和释放资源的当次选择；重用前复核环境。 |
| 045 | 可用记忆 | merged_scoped | [浏览器填表项目的执行与迭代约定](../contexts/memory/items/autofill.execution-method.md) | 保留该项目按错误原因复用开源的选择，不授予额外外部修改权限。 |
| 046 | 长期规则 | merged_existing | [已有沟通规则覆盖](../contexts/memory/items/core.communication.md) | 合并已有简洁汇报规则，删除停止指令这项无关支持。 |
