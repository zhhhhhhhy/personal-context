# zhy-private-skill

Private, portable snapshots of personal Codex skills.

## Layout

- `skills/`: self-contained skill directories.
- `skill_sources.json`: snapshot provenance, file counts, tree hashes, and caveats.

## Install a skill

Copy a skill into the user-level Codex skill directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -a skills/enhance-prompt "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Start a new Codex conversation or refresh the session after installing so the
skill catalog is rediscovered.

## Scope

This repository vendors personal and explicitly selected workspace skills.
Codex system skills and plugin-managed Lark skills are not copied because their
own installers or plugins remain the authority for updates.

`cs-paper-figures` is a detached snapshot of a project-specific skill. It must
not read from or link back to the source project at runtime. Review its caveat
in `skill_sources.json` before reusing it elsewhere.

## Safety

Generated caches, local environment files, and credentials are excluded. Before
pushing updates, scan staged content for secrets and verify the recorded tree
hashes.
