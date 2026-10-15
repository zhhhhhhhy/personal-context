# Imported Skill Library

The personal Skill packages are maintained inside this repository under `skills/`.
The following packages were migrated from the former `zhy-private-skill` repository
on 2026-10-14:

- `academic-write`
- `deep-research`
- `grill-me`
- `grilling`

The migration copied the source repository's current working tree, including its
uncommitted routing updates. The source repository was left unchanged and is now
a historical copy. The imported README, validation snapshot, and old source
manifest are preserved under `references/skills/imported/`.

The root `skill_sources.json` describes the current packages after migration.
Read only the matching Skill directory for a task; do not load the entire library
as general personal Context.

Use `scripts/sync-skills.ps1` to copy all repository Skills into the local Codex
runtime directory. The script does not delete unrelated runtime Skills.

On 2026-10-15 the active installed survey workflow was reconciled into canonical
`skills/deep-research/`, and the installed writing additions were retained in
`academic-write`. Their short entries now route by phase or task to supporting
references. The former imported research package is preserved under
`references/skills/legacy/deep-research/` for explicit historical inspection.
Entry budgets are maintained in `rules/CONTEXT_LOADING.md` and checked before
runtime synchronization.
