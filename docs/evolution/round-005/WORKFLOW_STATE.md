# Workflow Transaction State

- Schema version: 1
- State version: 9
- Transaction ID: TX-d5ea5f0019d2
- Objective: Reduce review input with risk-directed checks and verify completeness on unused conversations
- Scope: Compact source-preserving review, deterministic risk routing and sentinel audit, one frozen shared extraction, targeted/full comparison, bounded evolution and delivery
- Status: in_progress
- Current phase: execute
- Owner: agent
- Next action: Finish attempt A-003 and record its evidence.
- Created: 2026-10-15T06:56:20+00:00
- Updated: 2026-10-15T07:19:32+00:00

## Acceptance conditions

| ID | Condition | Status | Evidence |
|---|---|---|---|
| AC-1 | Risk review preserves source and catches known omissions with scoped fallback | pending |  |
| AC-2 | Freeze unused parent conversations before semantic reading and preserve privacy | pending |  |
| AC-3 | Compare completeness and complete pipeline input on identical frozen observations | pending |  |
| AC-4 | Validate final decisions, preserve core budgets, record problems and synchronize repository | pending |  |

## Preflight

- Status: ready
- Evidence: Clean f316419 equals fetched origin/main; Python/tiktoken, previous frozen ledgers and native thread reader available; core/policy loaded; raw evidence remains local
- Checked at: 2026-10-15T06:56:20+00:00
- Detail:

## Constraints and blockers

- None recorded.

## Gate checkpoints

- route: 2026-10-15T06:56:20+00:00
- execute: 2026-10-15T06:56:20+00:00
- verify: not_run
- report: not_run

## Decisions

- None recorded.

## Attempt log

| Attempt | Phase | Action | Result | Outcome | Evidence |
|---|---|---|---|---|---|
| A-001 | execute | Implement compact risk-directed review and freeze new unused cohort from metadata | Compact review/risk/escalation tools implemented; four focused tests passed. Old calibration selects all 15 known gaps using 55/112 messages. New unused 10/4 cohort frozen; Observer validated 37 messages, 79 units, 77 observations. Review conversation aliases added before either review reads inputs. | passed | scripts/context-review.py; scripts/test-context-review.py; .local/context-evolution/round-005-20261015/freeze.json |
| A-002 | execute | Run isolated targeted and compact whole reviews of the same frozen observations; adjudicate differences and measure complete alternative pipelines | Isolated targeted and whole reviews completed on identical frozen observations: 13 versus 37 messages, no additional gaps; one splitting difference adjudicated. Comparable input estimates 22578 versus 25379 tokens, 11.0 percent lower; experiment extra 7813 separately recorded. Zero promotions applied; 45 integrity checks passed. No universal recall or billing claim. | passed | docs/evolution/round-005/measurements.json; .local/context-evolution/round-005-20261015/final-audit.json; notes/evolution/round-005-20261015-evaluation.md |
| A-003 | execute | Finalize public report, inspect scoped diff and privacy, synchronize repository and record acceptance |  | running |  |

## Event log

- `EV-50ecbe54e799` 2026-10-15T06:56:20+00:00 `initialized` {"actor": "agent"}
- `EV-88ac7389dcb4` 2026-10-15T06:56:20+00:00 `preflight_recorded` {"evidence": "Clean f316419 equals fetched origin/main; Python/tiktoken, previous frozen ledgers and native thread reader available; core/policy loaded; raw evidence remains local", "status": "ready"}
- `EV-784fa884e266` 2026-10-15T06:56:20+00:00 `gate_passed` {"stage": "route"}
- `EV-003fe2ba71c9` 2026-10-15T06:56:20+00:00 `gate_passed` {"stage": "execute"}
- `EV-fc1f8cf53e11` 2026-10-15T06:56:20+00:00 `attempt_started` {"attempt_id": "A-001"}
- `EV-925539942098` 2026-10-15T07:06:50+00:00 `attempt_finished` {"attempt_id": "A-001", "outcome": "passed"}
- `EV-06ab1a528718` 2026-10-15T07:06:50+00:00 `attempt_started` {"attempt_id": "A-002"}
- `EV-6049704b9090` 2026-10-15T07:19:30+00:00 `attempt_finished` {"attempt_id": "A-002", "outcome": "passed"}
- `EV-a71e54e2ff30` 2026-10-15T07:19:32+00:00 `attempt_started` {"attempt_id": "A-003"}
