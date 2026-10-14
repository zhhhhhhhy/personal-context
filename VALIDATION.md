# Personal-context Skill validation

Date: 2026-10-14

This repository now contains the personal Context files and the four reusable
Skill packages migrated from `zhy-private-skill`: `academic-write`,
`deep-research`, `grill-me`, and `grilling`. The current package inventory and
tree hashes are recorded in `skill_sources.json`.

The migration source was the working tree at `D:\worker\zhy-private-skill`.
That source repository remains unchanged and is no longer the maintenance
入口. The historical README, validation snapshot, and old manifest are under
`references/skills/imported/`.

Acceptance checks for this merge:

- all source Skill files are present under the corresponding target directory;
- each package has a valid `SKILL.md` frontmatter manifest;
- the existing personal portrait remains byte-identical;
- no raw conversation exports, credentials, nested Git repositories, or
  symlinks were introduced;
- `scripts/sync-skills.ps1` copies the repository packages without deleting
  unrelated runtime Skills;
- local and remote `main` point to the same merge commit.
