# 迁移后清理旧目录的检查清单

- id: `migration.old-directory-checklist`
- kind: memory
- status: active
- scope: 迁移完成后讨论旧目录清理
- verification: historical_user_instruction
- validity: project
- updated_at: 2026-10-15T13:49:28+00:00

该次迁移清理的顺序是：更新旧路径引用；核对迁移文件与哈希；提交迁移内容或完整压缩归档；最后才处理旧目录。复用时先确认当前目标、影响范围和本次删除授权。

## Boundaries

- 保留检查方法不等于保留未来删除权限。
- 每次操作按当前系统核对真实路径、目标和备份，不沿用旧目录名。
- review_after: 2026-10-15

## Evidence pointers

- E118: `01a12aaf-133a-7d63-977d-927f3b56711e` / `rollout-2026-10-11T19-17-59-01a12aaf-133a-7d63-977d-927f3b56711e.jsonl:L384` — 用户直接给出引用、文件哈希、提交或归档、最后删除的四步顺序。

- candidates: C-20261014-029
