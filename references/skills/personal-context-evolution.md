# 显式请求的历史对话导入

本页仅在用户明确要求“提炼历史对话”“用最近一周对话更新”等批量任务时读取。普通任务中的记忆更新直接使用 `docs/evolution/POLICY.md` 和 [现有记忆写入契约](personal-context-memory.md)，不经过本页。

## 使用已有工具

- 先明确本次来源范围；复用 `scripts/context-evolution.py prepare` 的日期筛选、增量去重和本地脱敏能力。不为导入重建框架或改写脚本；源日志只读，完整证据留本地。
- 区分直接用户表达、引用、助手/工具结论和自动工作线程。只有直接父对话表达支持个人偏好；项目数量、对象、条件和待核状态不得因不确定而丢失。
- Observer 聚焦选定来源；Reflector 对照相关活跃记忆、Skill 和 core，决定保存、已有覆盖、合并、替代或不保存。旧候选只在来源追溯或明确处理它们时读取。
- 新写入仍使用 `context-memory.py validate/apply` 和现有本地来源清单。旧版 evolution apply/rollback 不能覆盖当前记忆源。
- 只针对歧义、冲突和疑似遗漏补查相关来源，不默认独立全量复核。没有用户要求的实验时，不建立训练/评测分区，不做 frozen A/B、token 计量或成本比较。
- 汇报保存了哪些可用内容、适用范围和待核事实；不把“当前已知问题已修复”说成“没有未知遗漏”。

## 旧协议和记录

[来源覆盖](personal-context-observation.md)、[重点复核](personal-context-review.md)、`docs/evolution/round-*/`、`notes/evolution/` 和历史候选账本保留为专项参考和追溯资料。仅在任务需要其细节时读取；其中旧的冻结、计量、全库检查等要求不恢复为日常前置条件，当前政策优先。

只在遇到对应错误时查 [已有故障记录](../../docs/evolution/TROUBLESHOOTING.md)。没有后台调度；历史批量导入不是每次真实任务的收尾动作。
