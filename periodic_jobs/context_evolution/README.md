# Context evolution heartbeat

This is the Codex adaptation of the reference repository's L1 Observer and L2 Reflector. It keeps the three responsibilities separate:

```text
Observer  -> collect and classify new local evidence; never modify active rules
Reflector -> compare observations with core, learned and candidate rules; produce reflection.json
Controller -> validate provenance/scope/privacy/base version; apply only learned rules; keep rollback
```

## One-shot run

Use `scripts/context-evolution.py prepare` for a bounded date window. The command excludes previous selection manifests, freezes a training/evaluation split and invokes the redacting extractor. The current Codex session is the semantic Observer/Reflector; it must write only the local run's `reflection.json`.

```text
prepare -> read evidence.train.jsonl -> write reflection.json
        -> validate -> apply -> evaluate evidence.eval.jsonl
```

## Suggested cadence

- Daily Observer: prepare only the new local evidence window and leave the run in `prepared` state. Do not automatically change `habits/`.
- Weekly Reflector: review accumulated prepared runs, merge duplicate observations, record conflict checks and create a single reflection. Run `validate` before `apply`.
- Evaluation: reserve a small parent-conversation holdout before semantic reading. A holdout failure changes the rule or defers it; it never tunes the holdout.
- Rollback: use the run's backup manifest when the applied wording is too broad, inaccurate or no longer useful.

No Windows Task Scheduler job is installed by this repository change. Scheduling is an operational decision separate from the evolution contract; the user can first evaluate several one-shot runs.

## Safety boundaries

The heartbeat cannot write `rules/SOUL.md`, `profile.md`, `habits/communication.md`, `INDEX.md`, permissions, external messages, or other Skills. Raw conversation bodies and sensitive topics remain local. `auto_applied` means the deterministic controller accepted the evidence contract, not that the user has personally endorsed the rule.
