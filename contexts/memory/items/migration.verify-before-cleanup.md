# 迁移后再按授权清理

- id: `migration.verify-before-cleanup`
- kind: memory
- status: active
- scope: 目录迁移与旧副本清理
- verification: historical_user_instruction
- validity: stable
- updated_at: 2026-10-16T01:41:42+00:00

清理旧目录前，更新路径引用，核对迁移文件及哈希，并保留提交或完整归档。

## Boundaries

- 清理前核对当前绝对路径、影响范围与授权；历史删除许可不延续。
- review_after: 2027-01-16

## Evidence pointers

- E118: `01a12aaf-133a-7d63-977d-927f3b56711e` / `rollout-2026-10-11T19-17-59-01a12aaf-133a-7d63-977d-927f3b56711e.jsonl:L384` — 用户直接给出引用、文件哈希、提交或归档、最后删除的四步顺序。

- candidates: C-20261014-029
