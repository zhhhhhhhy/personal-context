# Context Index

## 每次会话必读（L3 核心）

`rules/SOUL.md` → `profile.md` → `habits/communication.md` → 本索引。文件已在当前上下文中时无需重复读取。核心文件的修改只来自用户授权，不由历史日志自动改写。

## 按领域和当前任务读取

2026-10-23 用户确认以能力领域积累经验，维持下面的大类粒度。核心已足够时直接使用；需要细节时，按任务目的选一个主领域，再只读该页命中任务的条目。跨领域确有必要时才补读另一领域；不把各领域页面全部加载。

| 主分类 | 入口与适用任务 |
|---|---|
| 个人偏好 | 复用已读 `profile.md`、`habits/communication.md`；画像细节按 profile 使用说明读取，个性化教学等再按记忆入口检索 |
| 论文 | [论文经验](references/domains/papers.md)：选题与贡献、文献、实验与评估、写作与审稿 |
| 前端 | [前端经验](references/domains/frontend.md)：页面与交互、组件与状态、调试与验收 |
| 后端 | [后端经验](references/domains/backend.md)：接口与数据、数据库/缓存/并发、部署与排障 |
| 通用工作方法 | [工作方法](references/domains/work-methods.md)：需求→PRD→模块设计、任务组织、验收、交接、子 Agent 复核及材料编辑 |

需求、PRD、模块设计是任务信号；Java、Go 等是技术或适用条件标签，当前不为它们增加目录。论文中调用 API 做评测仍按论文/评估路由，接口鉴权或服务故障才按后端路由。

## 专项与来源入口

- 需要具体项目的版本、数据、路径、进度或历史约定时，再从 [项目资料](references/projects/index.md) 核对身份和材料；项目名不是经验主分类，项目事实不直接变成通用经验。
- 领域页直达已知经验；查找新增或重叠经验时使用 [记忆入口](contexts/memory/INDEX.md)，只读命中条目。长期规则入口仍为 `habits/learned.md`。
- 明确指定 Skill 时按名称加载；Context/Skill 维护走 `rules/CONTEXT_LOADING.md`、`skills/personal-context/SKILL.md`，Skill 来源再查 `references/skills/README.md`。
- 当前任务产生值得保存的内容时，走 `skills/personal-context/SKILL.md` → `docs/evolution/POLICY.md`；写入时再读写入契约。只有明确要求批量历史提炼时，才读专项入口 `references/skills/personal-context-evolution.md`。

领域页是路由，不扩大记忆原有范围、Skill 权限或任务授权。普通问题不查历史；已读细节不重复读取。

## 记忆状态

记忆按范围使用，待核事实不能当作结论；合并、替代、归档或舍弃的旧内容退出默认检索。稳定偏好不因时间自动失效，临时约定只按明确有效期处理。敏感证据只留本地。

历史46条的去向在 `notes/candidate-dispositions.md`，历轮记录在 `notes/evolution/`、`docs/evolution/round-*/`；只在需要追溯时读取，不是日常更新的必读材料。axioms 的 baseline 仍是参考起点。
