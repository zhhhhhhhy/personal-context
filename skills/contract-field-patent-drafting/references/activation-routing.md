# Activation and long-run routing

This package uses `routing-observability/v1` concepts. The upstream selector and the loaded Skill are separate evidence layers. If selector evidence is absent, report `selection_observability_boundary=upstream-unobserved`; do not infer that a Skill was not triggered from its absence in the transcript.

For every loaded-task message or runtime observation, append an event before the next action:

```json
{"event_type":"trigger_evaluated|route_decision|state_transition","event_id":"...","trace_id":"...","session_id":"...","run_id":"...","event_seq":1,"timestamp":"...","skill":"...","source":"explicit|implicit|passive|observer|user_feedback|timer","matched_signals":[],"candidates":[],"selected":null,"reason_codes":[],"evidence_refs":[],"state_before":"...","state_after":"...","route_revision":1}
```

Use `received|evaluating|matched|active|observing|verifying|completed|partial|needs_input|failed|blocked|stopped|expired|suppressed|deferred|reroute_pending|rerouted|handoff` as the observable state vocabulary. `unknown` or `conflict` cannot become `completed` without real Observation and VerificationResult evidence.

For a long task, checkpoint before waiting, pausing, or changing route. On goal/constraint/evidence/tool/budget drift, repeated failure, no progress, timeout, or explicit user redirection, increment `route_revision`, retain the same `run_id` and completed artifacts, mark old actions `stale|superseded`, and resume idempotently. Query and report events by trace, session, run, Skill, revision, and event type.

This reference is a contract for observable behavior; static instructions do not prove live selector or harness behavior.
