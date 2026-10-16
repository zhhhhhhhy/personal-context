# Mandatory Preflight Gate

Use this gate before every material engineering implementation or evaluation. Its purpose is to catch environmental, dependency, input, protocol, and safety problems before they consume a long run or invalidate a result.

## Procedure

1. Identify the project root, active instructions, current checkout or revision, and the intended execution stage.
2. Locate and run the project's read-only preflight command. If no project-specific command exists, perform the checks below directly and save the report beside the iteration record.
3. Verify required files, configuration, dependencies, executable entrypoints, data/model paths, versions, resource availability, and service or network reachability that the planned stage actually needs.
4. Verify protocol boundaries before evaluation: data split, labels or gold answers, frozen checkpoints, scoring version, output schema, and any holdout or blind-input rule.
5. Verify the side-effect boundary: credentials are transient, destructive operations are excluded, and the planned command cannot silently overwrite historical results or shared files.
6. Write a machine-readable report and link it from the engineering iteration entry.

## Report contract

The report should contain a stable identifier, timestamp, scope, overall status, check results, evidence paths or commands, and the next action. Each check should identify its owner and evidence:

```json
{
  "preflight_id": "project-stage-date",
  "scope": "dev|evaluation|deployment|other",
  "status": "ready|needs_remote_check|blocked",
  "checks": [
    {
      "id": "runtime.gpu",
      "owner": "script",
      "status": "passed|needs_remote_check|blocked",
      "evidence": "path or command",
      "detail": "observed fact"
    }
  ],
  "next_action": "..."
}
```

## Decision boundary

- Continue only when the overall status is `ready`.
- `needs_remote_check` permits local diagnostics and evidence collection only. It does not permit starting a dependent remote run.
- `blocked` stops implementation, delegation, and evaluation until the recorded cause is repaired or the missing input is supplied.
- A static check proves only the checked layer. It does not prove model execution, browser behavior, deployment, or user acceptance.
- Re-run the gate after any change to code, dependencies, model or data artifacts, server session, GPU allocation, network path, or evaluation protocol.

## Typical checks

Use only the checks relevant to the planned stage:

- project instructions, revision, working-tree state, and required files;
- Python/Node dependencies and syntax of the exact entrypoint;
- model, adapter, dataset, reference, and checkpoint existence plus recorded hashes;
- GPU/CPU/memory availability and service readiness;
- network or SSH reachability with bounded timeouts;
- deterministic decoding, chat-template, label-blind, holdout, and scoring-version invariants;
- output directory ownership and protection of historical results;
- transient credential handling and explicit authorization for external or irreversible actions.

Keep unresolved checks visible. Do not turn a missing runtime observation into a pass, and do not infer an end-to-end result from a local-only report.
