# Context Index

## 每次会话必读（L3 核心）

`rules/SOUL.md` → `profile.md` → `habits/communication.md` → 本索引。文件已在当前上下文中时无需重复读取。核心文件的修改只来自用户授权，不由历史日志自动改写。

## 按任务读取

| 任务信号 | 优先加载 |
|---|---|
| 用户背景、长期目标 | `profile.md` |
| 价值观、自我理解、职业取舍、学习与执行方式 | `profile.md` 中的使用说明，按需加载 `references/personal/zhenghuiyu.md` |
| 沟通、写作、汇报 | `habits/communication.md` |
| 研究、论文、实验 | 匹配的 Skill；研究取舍和长期判断再读 `habits/axioms/INDEX.md`，项目事实再查 `references/projects/` |
| 具体 Skill 工作流 | 按名称加载 `skills/<skill-name>/SKILL.md` |
| Context/Skill 设计与维护 | `rules/CONTEXT_LOADING.md`、`skills/personal-context/SKILL.md`；Skill 来源再查 `references/skills/README.md` |
| 项目约定、历史决策、个性化习惯与重复纠正 | `contexts/memory/INDEX.md`；关键词检索后只读命中条目，长期规则入口为 `habits/learned.md` |
| 当前任务产生新偏好、可复用方法或项目约定，需要更新记忆 | `skills/personal-context/SKILL.md` → `docs/evolution/POLICY.md`；写入时再读 `references/skills/personal-context-memory.md` |
| 用户明确要求批量提炼历史对话 | `skills/personal-context/SKILL.md` → `references/skills/personal-context-evolution.md` 的专项入口 |

修改已有材料、指定范围验收或继续已有项目时，按当前任务检索相关条目；核心和已读记忆足够时不再检索。普通问题无需查历史，详细规则不重复读取。

## 记忆状态

记忆按范围使用，待核事实不能当作结论；合并、替代、归档或舍弃的旧内容退出默认检索。稳定偏好不因时间自动失效，临时约定只按明确有效期处理。敏感证据只留本地。

历史46条的去向在 `notes/candidate-dispositions.md`，历轮记录在 `notes/evolution/`、`docs/evolution/round-*/`；只在需要追溯时读取，不是日常更新的必读材料。axioms 的 baseline 仍是参考起点。
