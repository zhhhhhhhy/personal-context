# 自进化规则

## 授权与范围

2026-10-14 用户要求建立自进化功能、用历史对话试跑，再由用户评估。该授权替代过去“所有候选逐条人工批准”的门槛；仅适用于可撤回、非敏感、有充分证据的协作经验。历史日志、子代理和模型自评不能授予新权限。

每次会话常驻核心：`rules/SOUL.md`、`profile.md`、`habits/communication.md`、`INDEX.md`。画像详情、Skill 正文和 L1/L2 历史按任务读取。新经验进入可路由的 `habits/learned.md`，不自动膨胀核心。

## Observer：记录，不改规则

- 按日期、父对话和消息指纹增量处理；源日志只读。每批冻结输入哈希及训练/复核分区。
- 区分直接用户表达、引用资料、助手建议、工具输出和运行时包装。只有父对话中直接用户表达能支持个人偏好；子线程最多支持过程或失败分析。
- 保留具体出处、适用范围、反例和不确定性。单次要求不升级成“永远如此”。记录需要保留的上下文，避免把“先讨论这个方案”改成“所有修改都必须先问”。
- 密钥脱敏不等于隐私审查。职业、家庭、健康、财务等敏感细节及包含私密主题的观察只留本地；不得凭“confidence=high”发布。

## Reflector：合并、限定、晋升

- 先查既有 core、learned 和历史候选，执行 promote / update / reinforce / defer / reject。一次观察只处理一次；不要用换句话说增加规则数量。每个自动候选必须写 `candidate_audit.action`（`new` 或 `refine`）和关联的候选 ID；脚本会验证 ID 存在。
- Reflection 必须显式记录 `conflict_check`：是否检查 core、learned 和 candidate ledger。缺少冲突检查时即使证据数量足够也不得应用。
- 自动晋升需要至少两个独立父对话、不同的直接用户表述、明确范围与例外、没有未解决反证，且通过语义与隐私检查。重复粘贴、代理转述、助手建议不算独立支持。
- 用户一次明确的当前指令可直接修改框架，但不能伪装成从历史中学习的结果。本次规则移植与历史进化分开统计。
- 冲突、只出现一次、事实会很快过期、只有助手表达、无法区分引用或用户意图时 defer/reject。记录原因；不要补全不存在的个人事实。
- 每条经验有稳定 key、领域、范围、例外、证据和更新时间；更新相同 key 保留旧版本于本地事务快照。规则到复核日期需重新检查，不能仅因到期就推翻用户偏好。
- 本地观察保留原始审计记录；已处理观察通过 disposition 退出活跃队列。过期临时观察只归档，不删除源日志。历史 `notes/candidates.md` 的 46 条不自动批准；若得到新证据，只标记关联，不冒充新发现。

## 应用与边界

`scripts/context-evolution.py` 检查真实引文、父线程、时间范围、重复证据、现有文件哈希和输出字段后，只更新 `habits/learned.json`、`habits/learned.md`、本批 `notes/evolution/` 报告。模型不能给它任意目标文件路径。

核心规则、身份与价值观、隐私边界、外部发布权限及修改其他 Skill 都不由这个自动写入路径处理。需要改动时生成建议，由当前用户指令决定。自动应用后的经验标记为 `auto_applied`，不等于用户认可；用户可纠正或要求回滚。

模型的语义复核是判断而非数学证明。脚本负责可验证边界，不能证明一句话足以代表用户。最终报告必须展示实际证据强度与局限。

## 触发方式

对 Codex 说“用最近一周未处理的对话进化 Context”，或调用 `$personal-context`。当前会话完成两阶段推理并调用脚本。系统已具备按需自进化流程；每日 Observer / 每周 Reflector 可作为运行节奏，但未创建定时任务。触发、自动应用和后台调度是三个不同状态。

参考：[SOUL](https://github.com/grapeot/context-infrastructure/blob/main/rules/SOUL.md)、[COMMUNICATION](https://github.com/grapeot/context-infrastructure/blob/main/rules/COMMUNICATION.md)、[Observer/Reflector SOP](https://github.com/grapeot/context-infrastructure/blob/main/periodic_jobs/ai_heartbeat/docs/KNOWLEDGE_BASE.md)。实现是本仓库的适配，没有导入作者个人画像、公理或执行环境。
