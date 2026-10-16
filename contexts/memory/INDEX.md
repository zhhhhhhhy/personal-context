# 按需记忆入口

这里路由可复用记忆、Skill 和长期规则；项目资料单独限定范围。只在当前任务需要时检索，已读信息足够就直接使用。原候选文本不是生效指令。

1. 用当前任务关键词检索：`python -X utf8 D:/worker/personal-context/scripts/context-memory.py search --query "人工审核"`。默认排除项目资料；继续已有项目时先核对身份，再加 `--project contract-research`。项目键见 [项目入口](../../references/projects/index.md)。
2. 选择命中条目，再用 `show --id research.chinese-item-review` 读取正文与边界。项目示例为 `show --id project.core200-provenance-v4`；Skill/core/project 条目继续读取目标文件的相关小节。
3. 敏感主题默认不检索。本人材料任务确实需要时加 `--include-local`；这些内容不进入公开报告或 Git。

默认最多返回5个路由条目，不读取全部记忆。带项目的关键词检索仍保留匹配的通用偏好；只指定项目则仅列该项目。当前要求优先；待核事实可作线索，不能当作已验证结果。

合并和替代后的旧条目、归档和舍弃条目不进入默认检索。到复核日期只提醒检查；仅明确设定有效期的临时记忆会过期。

- 当前任务出现值得复用的新要求或纠正时，按 [个人 Context Skill](../../skills/personal-context/SKILL.md) 更新相关条目；没有新增价值就不写。
- 写入、合并、替代或归档时再读：[现有写入契约](../../references/skills/personal-context-memory.md)。不要求批量提炼、成本统计或全库维护。
- 只有追溯旧候选时才看：[candidate-dispositions.md](../../notes/candidate-dispositions.md)。
- `registry.json` 是脚本的数据源，不要默认整份加载。
