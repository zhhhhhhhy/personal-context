---
name: personal-context
description: Load the user's personal profile, habits, principles, or project history only when the task depends on them.
---

# Personal Context Skill

1. Read the repository `INDEX.md` first.
2. Classify the task and load only the matching `profile.md`, `habits/`, `skills/<skill-name>/`, or `references/` files.
3. Do not load all conversation history by default.
4. Record new reusable lessons in `notes/observations.md`.
5. Keep candidate rules pending until their evidence and scope have been reviewed.
6. Treat this repository as the source of truth for both personal Context and personal Skills; use `scripts/sync-skills.ps1` for runtime installation.
