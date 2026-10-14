# Benchmark-first academic writing reference

Use this reference when the paper is a benchmark or evaluation paper, or when a method has started to overshadow the evaluation contribution.

## Preflight worksheet

Write these privately or show them to the user when requested:

1. **Paper type:** benchmark, method, application, or another explicitly named type.
2. **Central claim:** one sentence that remains true if any single evaluated system is removed.
3. **Primary object:** task, dataset, protocol, metric, model, or deployed outcome.
4. **Secondary objects:** baselines, gates, generators, verifiers, or case studies.
5. **Evidence boundary:** data split, visible evidence, reference source, evaluator type, and what was not measured.
6. **Contribution map:** each contribution linked to a definition, artifact, or experiment.

If the central claim depends on a method name when the paper is supposed to be a benchmark, stop and repair the hierarchy before editing sentences.

## Five-paragraph introduction

Use one paragraph for each function. Combine or split only when the venue's format requires it.

1. **Need and setting.** State the practical task, why errors matter, and any privacy or deployment constraint that motivates the setting.
2. **Task boundary.** Explain why the task is more than extraction. Define the necessary content of a complete field and the choice between filling and review.
3. **Gap.** Summarize what adjacent benchmarks or metrics evaluate, then state the precise missing connection. Avoid claiming that prior work evaluates nothing when it evaluates a neighboring dimension.
4. **Benchmark.** State the input, output, data scope, task categories, evidence states, annotation or reference protocol, and the joint metrics. Keep implementation details out.
5. **Questions and findings.** State the experimental questions, the main findings, and contributions. Mention an evaluated method only as evidence for what the benchmark reveals.

## Main-paper versus artifact filter

| Keep in the main paper | Move to appendix or artifact | Remove from the paper |
| --- | --- | --- |
| Task definition and field completion rules | Exact JSON schema and parser behavior | Internal file paths |
| Dataset scope and evidence construction | Full prompts and per-item logs | SHA/checksum bookkeeping |
| Metrics and denominators | Reproduction commands | Internal version strings |
| Model and baseline identity needed for interpretation | Long error taxonomies | Study IDs and project directory names |
| Limitations affecting validity | Hardware and timing details, if relevant | “Completed”, “next step”, or draft-status updates |

The middle column is optional. Move a detail only if it supports reproducibility and does not change the paper's research identity.

## Reviewer checklist

- Would the benchmark contribution still stand if every named method were removed?
- Does the title and first paragraph foreground the task or benchmark?
- Does each contribution have a corresponding definition, artifact, or result?
- Are input sufficiency, output correctness, field completeness, and citation support distinguished?
- Are review or abstain benefits reported together with automation coverage and over-review cost?
- Are method-specific results attributed only to the evaluated module and setting?
- Are model-assisted labels or evaluators clearly separated from human gold?
- Are internal hashes, versions, paths, study identifiers, and project-status language absent from the main paper?
- Can any sentence be removed without weakening the claim-evidence chain?
