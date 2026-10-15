---
name: minimal-validation-workflow
description: "Use for every code or configuration change, bug fix, integration, evaluation, or debugging task to prevent over-validation: choose the smallest sufficient evidence, avoid full-suite and repeated checks by default, and stop once the changed path is proven. Expand only for explicit acceptance, safety, contract, or changed-risk evidence."
metadata:
  short-description: Risk-based minimal validation for engineering work
---

# Minimal Validation Workflow

Apply this skill as a reduction-first policy whenever an engineering task changes code or configuration, fixes a bug, integrates components, evaluates a system, debugs a failure, or asks what should be verified. It limits validation work; loading it does not add a separate testing phase. Its purpose is to prevent redundant test volume while preserving enough evidence that the changed path works end to end.

## Trigger intent

Use this policy before choosing or running checks for code and configuration work. The default behavior is to keep validation small and stop early, not to expand the test plan. A code task does not justify a full suite, repeated passing checks, or tests unrelated to the changed path unless a project contract, safety gate, or changed risk requires them.

## Default decision

Before running a test, state the behavior that needs evidence and the smallest check that can prove it. Prefer one representative end-to-end smoke run plus the narrow regression needed for the changed behavior. Stop when the required evidence is complete.

Use this minimum set unless a contract or user request requires more:

- Code or configuration change: syntax/import validation and the smallest targeted test covering the changed path.
- Retrieval, model, or backend change: one representative end-to-end task and one negative or abstention case when unsafe writes are possible.
- Browser or file write change: one real execution, reread the DOM or exported bytes, verify the intended value, and verify no submission or original-file overwrite.
- Bug fix: reproduce the failure, run the focused regression after the fix, and stop when it passes.
- Model/configuration freeze or sealed holdout: follow the contract exactly; never replace a required holdout or safety gate with a sample.

## Reduction rules

- Do not run the full test suite by default. Run it only when the user requests it, the repository contract requires it, the change crosses many modules, or targeted evidence cannot cover the risk.
- Do not create a second validation phase merely because this policy was loaded; it scopes the checks that the engineering workflow already needs.
- Do not repeat a passing test without a new code/config/data change, a changed environment, or a reason to distrust the result.
- Do not add tests that merely mirror the implementation or multiply equivalent easy cases.
- Prefer a hard representative case over many simple cases. Keep calibration, regression, and holdout data separate.
- Do not modify gold labels, thresholds, or the frozen model to make a minimal test pass.
- Bound retries: after the first failure, preserve the raw error, make the smallest diagnosis-driven correction, and rerun only the affected check once. If the same root cause persists, stop and report the blocker.
- Treat transient service readiness, temporary directory, import path, and ordinary timeout errors as targeted-retry candidates; do not launch an unrelated test campaign.
- Release model, browser, and service processes started for the check after evidence is saved.

## Safety and acceptance exceptions

Minimal validation never permits skipping a required safety gate. For any write-capable path, always verify protected-field preservation, no-answer/conflict abstention, no submission, and actual post-write reread. For file paths, verify original hashes remain unchanged. For live or authenticated browser work, use only the authorized channel and do not infer local-browser success from a server browser.

If a project contract names a full suite, a required case count, a frozen holdout, or a hard acceptance metric, execute that requirement exactly and record why the broader run was necessary. Do not claim overall acceptance from the minimum smoke test when a mandatory gate remains unrun.

## Evidence and stopping condition

Record a compact validation note for each run: purpose, command or scenario, result, and the acceptance gate it covers. The run is complete when the changed path has passed the minimum evidence set and no required gate is pending. If the system is blocked by missing tools, unavailable environments, or repeated failure, stop testing and report the blocker, attempts, current safety state, and the next decision needed.

When a detailed test report is explicitly requested, keep the minimum validation result first and list only the additional runs that materially changed confidence.
