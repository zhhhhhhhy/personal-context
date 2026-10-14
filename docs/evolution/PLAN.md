# Context evolution implementation and pilot

Date: 2026-10-14. Transaction: [WORKFLOW_STATE.md](WORKFLOW_STATE.md).

User objective: adopt the reference core loading/autonomy/communication rules, implement self-evolution, run a bounded historical trial, and deliver results for the user's evaluation.

| Step | Owner | Input | Output and acceptance |
|---|---|---|---|
| Core contract | AI + file tools | User authorization, existing files, upstream rules | Four core files plus optional detail routing; preserve personal portrait and existing Skills |
| Evidence preparation | Script | Local metadata index and archived/live logs | Immutable local pack; old imported content excluded; dates and train/eval split frozen |
| Observer | AI | Training evidence | Source-linked observations; task-only and sensitive content identified |
| Reflector | AI | Observations, existing rules and candidates | Scoped rules or abstention; evidence from independent parent conversations |
| Apply | Script | Validated reflection | Deterministic learned-rule view, redacted audit log, atomic write and rollback |
| Assessment | AI independent forward pass + root review | Frozen evaluation partition and output | Evidence fidelity, scope, novelty, limits; no claim of human accuracy |
| Final acceptance | User | Change report and examples | User decides whether the resulting Context represents them |

## Frozen pilot protocol

- Select unused root conversations created during 2026-09-28 through 2026-10-04 (Asia/Shanghai), then keep only messages timestamped within that interval. This is a bounded cohort, not all activity that week.
- Exclude the 80 roots in previous batch manifests. Future runs compare message fingerprints against prior local runs, allowing new messages in the same root.
- Deterministically reserve 3 roots for evaluation before semantic reading. Evaluation content is not used for rule drafting or tuning.
- Raw messages, quotes, file paths, snapshots and full decisions stay outside the Git checkout. Sensitive topics stay local even after keyword redaction.
- Minimum proof: actual pilot apply/re-read, repeat-run idempotence, evidence-role/conflict/secret/stale-base rejection and safe rollback in an isolated temporary repository. These negative checks are required because the pipeline can write persistent instructions.
- Success means a reproducible bounded evolution with honest quality assessment, not a required count of new rules. User acceptance remains pending.
- No recurring schedule, account changes, unrelated Skill updates, or automatic permission changes.
