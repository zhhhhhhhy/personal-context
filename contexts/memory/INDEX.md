# 按需记忆入口

这里保存可立即调用的项目约定、已有 Skill 去向和长期规则。详细内容只在任务相关时读取；原候选文本不是生效指令。

1. 用当前任务的关键词检索：`python -X utf8 D:/worker/personal-context/scripts/context-memory.py search --query "论文 人工审核"`。已知项目可加 `--project contract-research`。
2. 从返回的标题和范围中选择，再用 `show --id research.core200-status` 读取正文、条件、出处和待核状态。Skill/core 条目只指向已有规范，继续加载对应目标。
3. 敏感主题默认不检索。本人材料任务确实需要时加 `--include-local`；这些内容不进入公开报告或 Git。

默认只返回最多5个匹配条目的路由信息，不读取全部记忆。当前用户要求优先；历史项目约定先核对当前项目和协议。待核事实可作调查线索，不能当作已验证结果。

合并和替代后的旧条目、归档和舍弃条目不进入默认检索。到复核日期只提醒检查；仅明确设定有效期的临时记忆会过期。

- 查看完整候选去向：[candidate-dispositions.md](../../notes/candidate-dispositions.md)
- 维护记忆时读取：[加载、维护与写入契约](../../references/skills/personal-context-memory.md)
- `registry.json` 是脚本的数据源，不要默认整份加载。
