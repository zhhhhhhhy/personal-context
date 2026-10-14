# Personal Context Router

这是 Context 的入口文件，不是完整规则手册。

1. 先读 `INDEX.md`，判断当前任务需要哪些文件。
2. 常规任务按需加载 `profile.md` 和 `habits/communication.md`。
3. 研究、工程或写作任务只加载对应的 `habits/`、`skills/` 和 `references/` 文件。
4. 不要默认读取 `references/conversations/` 下的原始对话；只有需要证据追溯时才读取。
5. 新经验只追加到 `notes/observations.md`，不要未经确认直接修改长期规则。
6. 不要把密码、Token、私钥或其他秘密写入本仓库。
7. 任务涉及可复用工作流时，按名称读取 `skills/<skill-name>/SKILL.md`；不要默认加载整个 Skill 库。
8. `D:\worker\personal-context` 是 Context 和个人 Skill 的唯一维护入口；`D:\worker\zhy-private-skill` 只作为历史副本，不再作为来源。
9. 需要更新 Codex 运行时 Skill 时使用 `scripts/sync-skills.ps1`，不要直接把运行时目录当成源文件修改。
