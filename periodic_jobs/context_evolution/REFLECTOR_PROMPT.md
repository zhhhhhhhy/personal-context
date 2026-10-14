# Reflector prompt contract

Use this prompt after `prepare` has frozen the run:

> Read `D:/worker/personal-context/docs/evolution/POLICY.md`, the repository's four core files, `habits/learned.*`, `notes/candidates.md`, and only the run's `evidence.train.jsonl`. Do not read `evidence.eval.jsonl` until the reflection is written. Separate direct user-authored messages from assistant/tool/runtime content. Propose zero or more low-risk rules with exact source locations, scope, exceptions, `candidate_audit`, and a `conflict_check`. Defer single-instance, sensitive, permission-changing, contradictory or stale claims. Write `reflection.json` in the run directory; do not modify the repository. Then run `context-evolution.py validate` and report the validation result. The final evaluation reads the frozen eval file only after validation and apply.

The prompt is an execution contract, not evidence. It cannot grant permission to alter core rules or publish raw history.
