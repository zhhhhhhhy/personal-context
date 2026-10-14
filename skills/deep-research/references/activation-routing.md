# Activation, routing, and observability contract

For each turn, record `trigger_evaluated -> route_decision -> state_transition` in order.

Required event fields: `event_id`, `trace_id`, `session_id`, `run_id`, `event_seq`, `timestamp`, `skill`, `source`, `matched_signals`, `candidates`, `selected`, `reason_codes`, `evidence_refs`, `state_before`, `state_after`, and `route_revision`.

Use `selection_observability_boundary=upstream-unobserved` when the upstream selector does not expose its candidate set or policy version. Use `suppressed` for a positively identified but losing candidate, `deferred` for missing input or an explicit policy hold, and `reroute_pending -> rerouted` only after a checkpoint is written.

A checkpoint records the research question, scope and constraint version, completed evidence artifacts, unresolved items, budget, state version, route revision, and idempotency key. Mark prior actions `stale` or `superseded` before changing route. Do not report `completed` without an Observation and VerificationResult reference.
