# Activation and long-run routing

Record selector boundary (`upstream-unobserved` when no upstream evidence), then append `trigger_evaluated → route_decision → state_transition` before each question or answer. Include `event_id`, `trace_id`, `session_id`, `run_id`, `event_seq`, `timestamp`, `source`, `matched_signals`, `reason_codes`, `evidence_refs`, `state_before/state_after`, and `route_revision`.

When the plan, answer, dependency, or stop condition changes, checkpoint the conversation, increment `route_revision`, preserve confirmed decisions and open risks, and do not enact the plan until the user confirms shared understanding.
