#!/usr/bin/env python3
"""Evaluate a captured workflow state on activation, process, and outcome.

The upstream Skill selector is outside this file's visibility.  This evaluator
therefore reports activation as indeterminate unless a controller state exists,
and checks the two locally observable dimensions deterministically.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read state: {exc}")
    if not isinstance(value, dict):
        raise SystemExit("state must be a JSON object")
    return value


def event_types(state: dict[str, Any]) -> list[str]:
    result = []
    for event in state.get("events", []):
        event_type = event.get("type", "")
        if event_type == "gate_passed":
            event_type = f"gate_passed:{event.get('detail', {}).get('stage', '')}"
        result.append(event_type)
    return result


def ordered(events: list[str], expected: list[str]) -> tuple[bool, list[str]]:
    failures = []
    cursor = -1
    for item in expected:
        try:
            cursor = events.index(item, cursor + 1)
        except ValueError:
            failures.append(f"missing or out-of-order event: {item}")
    return not failures, failures


def evaluate(state: dict[str, Any]) -> dict[str, Any]:
    events = event_types(state)
    has_controller_state = "initialized" in events
    activation = {
        "status": "indeterminate" if has_controller_state else "failed",
        "selector_observable": False,
        "detail": (
            "controller initialization is present, but upstream Skill selection/loading "
            "is not exposed in the local state"
            if has_controller_state
            else "no controller initialization event"
        ),
    }
    process_expected = [
        "initialized",
        "preflight_recorded",
        "gate_passed:route",
        "gate_passed:execute",
        "attempt_started",
        "attempt_finished",
        "gate_passed:verify",
        "acceptance_verified",
        "gate_passed:report",
    ]
    process_ok, process_failures = ordered(events, process_expected)
    process = {"status": "passed" if process_ok else "failed", "failures": process_failures}

    acceptance = state.get("acceptance", [])
    incomplete = [
        item.get("id", "")
        for item in acceptance
        if item.get("status") != "passed" or not item.get("evidence")
    ]
    outcome_ok = state.get("status") == "completed" and not incomplete
    outcome = {
        "status": "passed" if outcome_ok else "failed",
        "failures": []
        if outcome_ok
        else [
            *([f"state status is {state.get('status')!r}, expected 'completed'"]
              if state.get("status") != "completed" else []),
            *(["acceptance lacks passed evidence: " + ", ".join(incomplete)] if incomplete else []),
        ],
    }
    return {"activation": activation, "process": process, "outcome": outcome}


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate a workflow controller state")
    parser.add_argument("--state", required=True)
    parser.add_argument("--strict", action="store_true", help="return non-zero when process or outcome fails")
    args = parser.parse_args()
    result = evaluate(load(Path(args.state)))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.strict and any(result[name]["status"] == "failed" for name in ("process", "outcome")):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
