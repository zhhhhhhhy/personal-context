# Round11: reduce source and preparation overhead

- Objective: audit the exact76,413 baseline, make source formatting lossless and sparse, reuse already-loaded protocols with hash checks, then freeze and test on new roots.
- Ownership: current agent handles semantics; scripts handle source identity, formatting, payload accounting and lifecycle; user judges usefulness. No sub-agents.
- Changes: short IDs plus shared conversation dictionary and bounded source pages; complete hashes/paths stay local. Reuse cached qualification metadata, recheck selected source files; suppress full script/schema/status dumps unless a relevant failure occurs. Review selection and same-class escalation unchanged.
- Validation: one same-corpus lossless packaging comparison on the previous91 messages and one tampered-page/oversize check, then a fresh cohort with targeted review and actual all-tool snapshot. No full independent inventory.
- Acceptance: AC-1 exact baseline breakdown and lossless cheaper source payload; AC-2 new categorized contents with focused omissions reported; AC-3 whole returned-input accounting including setup/checks, protected user edits and private sources.
