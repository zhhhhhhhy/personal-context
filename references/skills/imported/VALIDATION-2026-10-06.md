# Validation snapshot

Date: 2026-10-06

This snapshot contains four selected personal Skill packages: `academic-write`,
`deep-research`, `grill-me`, and `grilling`. The three shared routing packages
were synchronized with the active user-level catalog; `deep-research` was
updated in place with the same activation, checkpoint, and reroute contract.
`skill_sources.json` records the resulting file counts and tree hashes.

## Current validator result

All four packages pass the current `skill-creator` `quick_validate.py` check.
All four expose an `agents/openai.yaml` policy with
`allow_implicit_invocation: true`, positive and negative frontmatter routing
signals, and an activation/observability reference. `grill-me` no longer uses
the unsupported legacy `disable-model-invocation` key, and its companion
`grilling` package is included in the snapshot.

`deep-research` still contains references to optional external skills such as
`academic-paper` and `academic-pipeline`; those references are preserved as
integration boundaries and are not silently fabricated in this snapshot.

## Safety checks

- No common API-token, GitHub-token, AWS-key, or private-key patterns detected.
- No credential-like files, `.env` files, symlinks, nested Git repositories, or
  files larger than 10 MB detected.
- No runtime references back to the source projects were added by the routing
  update.
