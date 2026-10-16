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

On 2026-10-15, resolving the historical Context candidates also reconciled the
complete installed `contract-field-patent-drafting` and
`minimal-validation-workflow` packages into this canonical library. The patent
entry now routes to `references/patent-workflow.md`, which preserves its full
previous body. The academic writing references received two narrow additions
on causal claims and attributed human-review assertions. Existing Skill coverage
is credited separately from new personal rules in `notes/candidate-dispositions.md`.

On 2026-10-16, the complete installed `engineering-project-workflow` source
package was imported into this canonical library, with its prior entry retained
as a migration snapshot and the active entry routed under the existing budget.
Four duplicate planning/iteration/startup memories now point to this workflow;
one evidence-gap audit was consolidated into `academic-write`. Project-specific
conditions remain in `references/projects/`, separate from these methods.
