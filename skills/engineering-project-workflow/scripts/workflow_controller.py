#!/usr/bin/env python3
"""Small, dependency-free controller for the engineering workflow state.

The controller keeps the workflow state machine and the append-only event log
outside the model context.  It does not execute project commands; it gates and
records the commands that the workflow chooses to run.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PHASES = ("frame", "preflight", "route", "execute", "verify", "report")
STATUSES = (
    "planned",
    "waiting",
    "preflight",
    "in_progress",
    "verifying",
    "reduced",
    "completed",
    "blocked",
    "not_run",
)
OUTCOMES = ("passed", "failed", "timeout", "unknown", "unverified", "not_run")


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def fail(message: str, code: int = 2) -> None:
    print(json.dumps({"ok": False, "error": message}, ensure_ascii=False))
    raise SystemExit(code)


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def markdown_path(state_path: Path, requested: str | None) -> Path:
    return Path(requested) if requested else state_path.with_suffix(".md")


def parse_acceptance(values: list[str]) -> list[dict[str, Any]]:
    result = []
    for index, value in enumerate(values, start=1):
        if "=" in value:
            criterion_id, condition = value.split("=", 1)
            criterion_id = criterion_id.strip() or f"AC-{index:03d}"
        else:
            criterion_id, condition = f"AC-{index:03d}", value
        condition = condition.strip()
        if not condition:
            fail(f"acceptance condition is empty: {value}")
        result.append(
            {
                "id": criterion_id,
                "condition": condition,
                "status": "pending",
                "evidence": [],
                "note": "",
            }
        )
    return result


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"state file does not exist: {path}")
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read state file {path}: {exc}")
    if not isinstance(state, dict) or state.get("schema_version") != 1:
        fail("state file must be a schema_version=1 JSON object")
    return state


def add_event(
    state: dict[str, Any], event_type: str, detail: dict[str, Any] | None = None
) -> None:
    state.setdefault("events", []).append(
        {
            "event_id": f"EV-{uuid.uuid4().hex[:12]}",
            "time": timestamp(),
            "type": event_type,
            "phase": state.get("phase"),
            "status": state.get("status"),
            "detail": detail or {},
        }
    )


def save_state(state: dict[str, Any], path: Path, mirror: Path) -> None:
    state["updated_at"] = timestamp()
    state["state_version"] = int(state.get("state_version", 0)) + 1
    atomic_write(path, json.dumps(state, ensure_ascii=False, indent=2) + "\n")
    atomic_write(mirror, render_markdown(state))


def render_markdown(state: dict[str, Any]) -> str:
    lines = [
        "# Workflow Transaction State",
        "",
        f"- Schema version: {state.get('schema_version', '')}",
        f"- State version: {state.get('state_version', '')}",
        f"- Transaction ID: {state.get('transaction_id', '')}",
        f"- Objective: {state.get('objective', '')}",
        f"- Scope: {state.get('scope', '')}",
        f"- Status: {state.get('status', '')}",
        f"- Current phase: {state.get('phase', '')}",
        f"- Owner: {state.get('owner', '')}",
        f"- Next action: {state.get('next_action', '')}",
        f"- Created: {state.get('created_at', '')}",
        f"- Updated: {state.get('updated_at', '')}",
        "",
        "## Acceptance conditions",
        "",
        "| ID | Condition | Status | Evidence |",
        "|---|---|---|---|",
    ]
    for item in state.get("acceptance", []):
        evidence = "; ".join(item.get("evidence", []))
        lines.append(
            f"| {item.get('id', '')} | {item.get('condition', '')} | "
            f"{item.get('status', '')} | {evidence} |"
        )

    lines.extend(["", "## Preflight", ""])
    preflight = state.get("preflight", {})
    lines.extend(
        [
            f"- Status: {preflight.get('status', 'not_run')}",
            f"- Evidence: {preflight.get('evidence', '')}",
            f"- Checked at: {preflight.get('checked_at', '')}",
            f"- Detail: {preflight.get('detail', '')}",
            "",
            "## Constraints and blockers",
            "",
        ]
    )
    for constraint in state.get("constraints", []):
        lines.append(f"- Constraint: {constraint}")
    for blocker in state.get("blockers", []):
        lines.append(f"- Blocker: {blocker}")
    if not state.get("constraints") and not state.get("blockers"):
        lines.append("- None recorded.")

    lines.extend(["", "## Gate checkpoints", ""])
    gates = state.get("gates", {})
    for gate in ("route", "execute", "verify", "report"):
        lines.append(f"- {gate}: {gates.get(gate, 'not_run')}")

    lines.extend(["", "## Decisions", ""])
    decisions = state.get("decisions", [])
    if decisions:
        for decision in decisions:
            lines.append(f"- {decision.get('time', '')}: {decision.get('note', '')}")
    else:
        lines.append("- None recorded.")

    lines.extend(
        [
            "",
            "## Attempt log",
            "",
            "| Attempt | Phase | Action | Result | Outcome | Evidence |",
            "|---|---|---|---|---|---|",
        ]
    )
    for attempt in state.get("attempts", []):
        lines.append(
            f"| {attempt.get('id', '')} | {attempt.get('phase', '')} | "
            f"{attempt.get('action', '')} | {attempt.get('result', '')} | "
            f"{attempt.get('outcome', '')} | {'; '.join(attempt.get('evidence', []))} |"
        )

    lines.extend(["", "## Event log", ""])
    for event in state.get("events", []):
        detail = json.dumps(event.get("detail", {}), ensure_ascii=False, sort_keys=True)
        lines.append(
            f"- `{event.get('event_id', '')}` {event.get('time', '')} "
            f"`{event.get('type', '')}` {detail}"
        )
    return "\n".join(lines) + "\n"


def common_paths(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--state", required=True, help="canonical JSON state path")
    parser.add_argument("--markdown", help="human-readable state mirror path")


def load_paths(args: argparse.Namespace) -> tuple[Path, Path, dict[str, Any]]:
    state_path = Path(args.state)
    return state_path, markdown_path(state_path, args.markdown), load_state(state_path)


def command_init(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    mirror = markdown_path(state_path, args.markdown)
    if state_path.exists():
        state = load_state(state_path)
        if args.objective and args.objective != state.get("objective"):
            fail("objective differs from existing state; create a new transaction or use checkpoint")
        add_event(state, "resumed", {"actor": args.owner or state.get("owner", "")})
        save_state(state, state_path, mirror)
        print(json.dumps({"ok": True, "action": "resumed", "state": str(state_path)}, ensure_ascii=False))
        return
    if not args.objective:
        fail("--objective is required when creating a state")
    if not args.acceptance:
        fail("at least one --acceptance condition is required when creating a state")
    state = {
        "schema_version": 1,
        "state_version": 0,
        "transaction_id": args.transaction_id or f"TX-{uuid.uuid4().hex[:12]}",
        "objective": args.objective,
        "scope": args.scope or "",
        "status": "planned",
        "phase": "frame",
        "owner": args.owner or "agent",
        "next_action": "Run the read-only preflight gate.",
        "constraints": args.constraint or [],
        "blockers": [],
        "acceptance": parse_acceptance(args.acceptance),
        "preflight": {"status": "not_run", "evidence": "", "detail": ""},
        "gates": {},
        "attempts": [],
        "events": [],
        "artifacts": [],
        "created_at": timestamp(),
        "updated_at": timestamp(),
    }
    add_event(state, "initialized", {"actor": state["owner"]})
    save_state(state, state_path, mirror)
    print(
        json.dumps(
            {
                "ok": True,
                "action": "initialized",
                "transaction_id": state["transaction_id"],
                "state": str(state_path),
                "markdown": str(mirror),
            },
            ensure_ascii=False,
        )
    )


def command_preflight(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    if args.status not in ("ready", "needs_remote_check", "blocked"):
        fail("preflight status must be ready, needs_remote_check, or blocked")
    state["phase"] = "preflight"
    state["preflight"] = {
        "status": args.status,
        "evidence": args.evidence or "",
        "detail": args.detail or "",
        "checked_at": timestamp(),
    }
    state["gates"] = {}
    state["status"] = "preflight" if args.status == "ready" else (
        "waiting" if args.status == "needs_remote_check" else "blocked"
    )
    state["next_action"] = (
        "Create the task allocation before execution."
        if args.status == "ready"
        else "Resolve the preflight condition before execution."
    )
    add_event(state, "preflight_recorded", {"status": args.status, "evidence": args.evidence or ""})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "status": args.status}, ensure_ascii=False))


def gate_failures(state: dict[str, Any], target: str) -> list[str]:
    failures = []
    if not state.get("objective"):
        failures.append("objective is missing")
    if not state.get("acceptance"):
        failures.append("acceptance conditions are missing")
    if target in ("route", "execute", "verify", "report"):
        if state.get("preflight", {}).get("status") != "ready":
            failures.append("preflight is not ready")
    gates = state.get("gates", {})
    if target in ("execute", "verify", "report") and not gates.get("route"):
        failures.append("route gate has not passed")
    if target in ("verify", "report") and not gates.get("execute"):
        failures.append("execute gate has not passed")
    if target == "report" and not gates.get("verify"):
        failures.append("verify gate has not passed")
    if target == "execute" and state.get("status") in ("blocked", "waiting"):
        failures.append(f"state is {state.get('status')}")
    if target == "verify" and not any(
        attempt.get("outcome") in ("passed", "failed", "timeout", "unknown", "unverified")
        for attempt in state.get("attempts", [])
    ):
        failures.append("no observed attempt result exists")
    if target == "report":
        pending = [item.get("id", "") for item in state.get("acceptance", []) if item.get("status") != "passed"]
        if pending:
            failures.append("acceptance conditions not passed: " + ", ".join(pending))
    return failures


def command_gate(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    failures = gate_failures(state, args.for_stage)
    if failures:
        print(json.dumps({"ok": False, "stage": args.for_stage, "failures": failures}, ensure_ascii=False))
        raise SystemExit(3)
    state.setdefault("gates", {})[args.for_stage] = timestamp()
    add_event(state, "gate_passed", {"stage": args.for_stage})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "stage": args.for_stage}, ensure_ascii=False))


def command_begin(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    failures = gate_failures(state, "execute")
    if not state.get("gates", {}).get("execute"):
        failures.append("execute gate has not passed; run gate --for-stage execute first")
    if failures:
        fail("execution gate failed: " + "; ".join(failures), 3)
    if any(item.get("id") == args.attempt_id for item in state.get("attempts", [])):
        fail(f"attempt already exists: {args.attempt_id}")
    state["phase"] = "execute"
    state["status"] = "in_progress"
    state.setdefault("gates", {}).pop("verify", None)
    state.setdefault("gates", {}).pop("report", None)
    state["next_action"] = f"Finish attempt {args.attempt_id} and record its evidence."
    state.setdefault("attempts", []).append(
        {
            "id": args.attempt_id,
            "time": timestamp(),
            "phase": "execute",
            "action": args.action,
            "expected_effect": args.expected_effect,
            "owner": args.owner or state.get("owner", "agent"),
            "result": "",
            "outcome": "running",
            "evidence": [],
            "failure_cause": "",
        }
    )
    add_event(state, "attempt_started", {"attempt_id": args.attempt_id})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "attempt_id": args.attempt_id}, ensure_ascii=False))


def command_finish(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    attempts = [a for a in state.get("attempts", []) if a.get("id") == args.attempt_id]
    if not attempts:
        fail(f"attempt does not exist: {args.attempt_id}")
    attempt = attempts[-1]
    if attempt.get("outcome") != "running":
        fail(f"attempt is already closed: {args.attempt_id}")
    if args.outcome not in OUTCOMES:
        fail("invalid attempt outcome")
    attempt.update(
        {
            "finished_at": timestamp(),
            "result": args.result or "",
            "outcome": args.outcome,
            "evidence": args.evidence or [],
            "failure_cause": args.failure_cause or "",
        }
    )
    state["phase"] = "verify"
    state["status"] = "verifying" if args.outcome == "passed" else "reduced"
    state.setdefault("gates", {}).pop("verify", None)
    state.setdefault("gates", {}).pop("report", None)
    state["next_action"] = "Verify each acceptance condition against the recorded evidence."
    add_event(state, "attempt_finished", {"attempt_id": args.attempt_id, "outcome": args.outcome})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "attempt_id": args.attempt_id, "outcome": args.outcome}, ensure_ascii=False))


def command_verify(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    if not state.get("gates", {}).get("verify"):
        fail("verification gate has not passed; run gate --for-stage verify first", 3)
    matches = [item for item in state.get("acceptance", []) if item.get("id") == args.criterion]
    if not matches:
        fail(f"acceptance criterion does not exist: {args.criterion}")
    item = matches[0]
    item["status"] = args.result
    item["evidence"] = args.evidence or []
    item["note"] = args.note or ""
    pending = [x for x in state.get("acceptance", []) if x.get("status") != "passed"]
    if not pending:
        state["status"] = "completed"
        state["phase"] = "report"
        state["next_action"] = "Report the verified result and link the evidence."
    else:
        state["status"] = "verifying" if args.result == "passed" else "reduced"
        state["phase"] = "verify"
        state["next_action"] = "Resolve or verify the remaining acceptance conditions."
    add_event(state, "acceptance_verified", {"criterion": args.criterion, "result": args.result})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "criterion": args.criterion, "result": args.result}, ensure_ascii=False))


def command_checkpoint(args: argparse.Namespace) -> None:
    state_path, mirror, state = load_paths(args)
    if args.phase not in PHASES:
        fail("invalid phase")
    if args.status not in STATUSES:
        fail("invalid status")
    state["phase"] = args.phase
    state["status"] = args.status
    state["next_action"] = args.next_action
    if args.owner:
        state["owner"] = args.owner
    if args.note:
        state.setdefault("decisions", []).append({"time": timestamp(), "note": args.note})
    add_event(state, "checkpoint", {"note": args.note or ""})
    save_state(state, state_path, mirror)
    print(json.dumps({"ok": True, "phase": args.phase, "status": args.status}, ensure_ascii=False))


def command_status(args: argparse.Namespace) -> None:
    _, _, state = load_paths(args)
    if args.json:
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return
    print(
        json.dumps(
            {
                "ok": True,
                "transaction_id": state.get("transaction_id"),
                "status": state.get("status"),
                "phase": state.get("phase"),
                "next_action": state.get("next_action"),
                "preflight": state.get("preflight", {}).get("status"),
                "gates": state.get("gates", {}),
                "acceptance": [
                    {"id": x.get("id"), "status": x.get("status")}
                    for x in state.get("acceptance", [])
                ],
            },
            ensure_ascii=False,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Control an engineering workflow transaction state")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="create or resume a transaction")
    common_paths(init)
    init.add_argument("--objective")
    init.add_argument("--scope")
    init.add_argument("--acceptance", action="append")
    init.add_argument("--constraint", action="append")
    init.add_argument("--owner")
    init.add_argument("--transaction-id")
    init.set_defaults(func=command_init)

    preflight = sub.add_parser("preflight", help="record a preflight result")
    common_paths(preflight)
    preflight.add_argument("--status", required=True, choices=("ready", "needs_remote_check", "blocked"))
    preflight.add_argument("--evidence")
    preflight.add_argument("--detail")
    preflight.set_defaults(func=command_preflight)

    gate = sub.add_parser("gate", help="check whether a workflow stage may start")
    common_paths(gate)
    gate.add_argument("--for-stage", required=True, choices=("route", "execute", "verify", "report"))
    gate.set_defaults(func=command_gate)

    begin = sub.add_parser("begin-attempt", help="register a bounded state-changing attempt")
    common_paths(begin)
    begin.add_argument("--attempt-id", required=True)
    begin.add_argument("--action", required=True)
    begin.add_argument("--expected-effect", required=True)
    begin.add_argument("--owner")
    begin.set_defaults(func=command_begin)

    finish = sub.add_parser("finish-attempt", help="record the result of an attempt")
    common_paths(finish)
    finish.add_argument("--attempt-id", required=True)
    finish.add_argument("--outcome", required=True, choices=OUTCOMES)
    finish.add_argument("--result")
    finish.add_argument("--evidence", action="append")
    finish.add_argument("--failure-cause")
    finish.set_defaults(func=command_finish)

    verify = sub.add_parser("verify", help="record one acceptance result")
    common_paths(verify)
    verify.add_argument("--criterion", required=True)
    verify.add_argument("--result", required=True, choices=("passed", "failed", "unknown"))
    verify.add_argument("--evidence", action="append")
    verify.add_argument("--note")
    verify.set_defaults(func=command_verify)

    checkpoint = sub.add_parser("checkpoint", help="update the current phase and next action")
    common_paths(checkpoint)
    checkpoint.add_argument("--phase", required=True, choices=PHASES)
    checkpoint.add_argument("--status", required=True, choices=STATUSES)
    checkpoint.add_argument("--next-action", required=True)
    checkpoint.add_argument("--owner")
    checkpoint.add_argument("--note")
    checkpoint.set_defaults(func=command_checkpoint)

    status = sub.add_parser("status", help="show current workflow status")
    common_paths(status)
    status.add_argument("--json", action="store_true")
    status.set_defaults(func=command_status)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
