# 第七轮：减少重复加载，按风险类别补查

用户直接授权修改流程并再验证。本轮框架改动与从历史学习的经验分开统计；最终评价由用户给出。状态见 WORKFLOW_STATE.json。

脚本负责冻结来源、完整传递原文、共享范围字典、分页哈希、复核覆盖 ID、风险类别扩展和计量。主代理完成选样、Observer 与 Reflector，不再把全部观察重新送回主代理。独立复核职责只读所选原文和观察，返回已检查 ID 与问题，不重复无问题明细。工程 Skill 明确允许委派独立实现及复核；不另设全量独立组。用户负责效果评估。

修改后先通过最小针对性检查并冻结代码，再读取新来源。沿用用户已授权的历史未充分覆盖补提方式，换用上轮之外的父对话；排除早期候选引用以及已有完整覆盖账本的消息，目标 4,000–8,000 个正文 tokens，至少两份父对话。缺少账本只称覆盖未知。按元数据和长度选样，不按提炼成果挑样；保留独立留出，项目族以实际语义核对。

初轮保留全部原风险条件及固定 20% 低风险抽查。冻结前为全部消息建立可重叠的风险类别，覆盖数量、条件、格式/指代、交付阶段、主体、因果和忠实归纳。发现问题后只补查未读的同类消息；新问题可继续扩展新类别，已读内容不重复发送。无法分类的问题需明确记录范围，最多先扩展同一父对话，不能静默漏过或自动全量。另对未进入补查的内容作固定 10%、至少 2 条、最多 4 条的外部类别抽查；该抽查额外成本单列。命中缺口仍按对应类别扩展，不修改已冻结路由来美化结果。

同批来源比较旧格式、新格式和新流程的材料计数；旧全量只作机械估算，不生成第二份模型结果。完整性仅报告本轮实际发现、修复、抽查范围和剩余未知，不声称召回率 100%。原文不删减，完整观察和修订账本仍在本地。输入计量包含提炼、复核、补查、裁决、候选读取和调度；框架开发、平台注入与生成输出另说明，不冒充账单。

验收只覆盖此次改变：完整解码、重复/漏 ID 拒绝、错误分类拒绝、同类扩展不扫无关内容、分页和冻结变更拒绝、旧协议兼容，以及一批实际端到端验证。核心入口预算不增长。新经验仍通过既有 validate/apply/rollback；敏感原文不入库。通过后同步仓库，并保留失败与解决过程。
# Execution outcome and deviations

The user resumed the interrupted implementation without changing the frozen cohort.
Initial v2 review reached all 106 messages because shared scope contaminated risk
tags. The original observations, code snapshot, reports and measured cost were
retained. Fourteen accepted issues were repaired; one isolated antecedent finding
was rejected using only its neighboring source message. A subsequent implementation
repair excludes shared scope, separates semantic issue classes from keyword clues,
and covers short target corrections. The first retrospective replay reached 13 of
14 known findings; the repaired replay reaches 14 of 14 while selecting 88 messages.
These replays are development evidence, not a second blind cohort or actual savings.
The final router has 10 focused checks passing. No additional whole-reference agent
or fresh-response comparison was run. The two held-out messages are too small to
establish usefulness of deferred content. Human assessment remains pending.
