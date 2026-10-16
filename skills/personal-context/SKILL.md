---
name: personal-context
description: Load relevant personal Context and maintain scoped memories from real tasks. Import past conversations only when explicitly requested; keep raw and sensitive evidence local.
---

# Personal Context Skill

Source of truth: `D:/worker/personal-context` (or the repository containing this source Skill). The installed Skill is a router, not a duplicate memory store.

## Use Context

Read the repository `AGENTS.md` and its four core files once per session; reuse files already in context. Use `INDEX.md` for relevant details. When memory can help the current task, follow `contexts/memory/INDEX.md`, search task keywords and show selected entries. Check project identity/version before loading project material. Current instructions outrank memories; pending claims remain unverified. Do not search history for an ordinary question that needs no memory.

## Learn from the current task

Read `D:/worker/personal-context/docs/evolution/POLICY.md` when there is a useful correction, reusable lesson or project agreement to save. Respect requests to discuss only or not update memory.

1. Observe the relevant evidence already available in this task. Preserve scope, concrete conditions, source and unverified status. Only direct human-parent expressions support personal preferences; assistant proposals and old permissions do not become user instructions.
2. Compare matching active memories and the relevant Skill/core. Reuse existing coverage; add, merge or replace only when useful. One clear scoped agreement may be saved without becoming a global rule. General rules require independent repeated support.
3. For a write, read `D:/worker/personal-context/references/skills/personal-context-memory.md`. Use the existing local plan, source checks and `scripts/context-memory.py validate/apply`; retain guarded rollback. A source manifest is required for new evidence, but batch preparation, observation ledgers, evaluation splits and cost reports are not.
4. Retire only affected entries: merge duplicates, replace explicit superseded agreements, archive invalid project context. Age alone does not retire stable preferences. Check actual message dates and preserve still-valid conditions before archival.
5. Briefly report useful memories applied, changes made and unresolved facts when relevant. If there is nothing worth saving, finish without a memory artifact or a forced update.

## Explicit history import or diagnosis

Only when the user requests past-conversation extraction, read `D:/worker/personal-context/references/skills/personal-context-evolution.md`. Existing batch tools and old candidate dispositions remain available for that task, not as prerequisites for current-task updates. No default full independent review, token metering, frozen comparison or new evaluation round. Do not reopen old candidates unless the task needs their provenance.

The user authorized reversible, evidenced, non-sensitive memory maintenance; do not ask again for each eligible entry. Raw/sensitive material stays local and credentials are not memory. The automatic writer cannot edit core rules, identity, permissions or Skills, nor authorize publication. No scheduler is installed. Loading design and optional diagnostics: `D:/worker/personal-context/rules/CONTEXT_LOADING.md`.
