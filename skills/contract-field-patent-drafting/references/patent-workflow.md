# Contract Field Patent Drafting

## 触发与长程状态记录

本 Skill 的被动候选由 frontmatter description 的正向信号决定：合同字段/RAG/LLM 研究材料转专利交底书、权利要求书、说明书、摘要、附图和证据边界验收包。仅有专利法咨询、单纯现有技术检索、普通论文改写或缺少技术材料时应抑制本 Skill，并保留待补输入。

- 上游 selector 未提供候选、winner、suppressed candidates 或 policy version 时，记录 `selection_observability_boundary=upstream-unobserved`；Skill 加载后才能记录 `considered|accepted|suppressed|deferred|active`，不能把“没有看到 Skill 名称”写成“没有触发”。
- 每次消息/观察先写 `trigger_evaluated`，再写 `route_decision`，再执行动作。事件至少带 `event_id`、`trace_id`、`session_id`、`run_id`、`event_seq`、`timestamp`、`skill`、`source`、`matched_signals`、`candidates`、`selected`、`reason_codes`、`evidence_refs`、`state_before/state_after` 和 `route_revision`。
- 长程任务按以下原因重评估或重路由：权威源被替换、证据状态变化、权利要求/说明书边界变化、渲染验收失败或申请人/公开日事实被补充；保留源清单、claim anchors、未决元数据和渲染证据。重路由前保存 checkpoint（目标/约束版本、已完成工件、未决事项、预算、状态版本、幂等键），递增 `route_revision`，把旧动作标记为 `stale|superseded`，再恢复或切换；不得重置上下文或重复已完成副作用。
- 状态至少区分 `received|evaluating|matched|active|observing|verifying|completed|partial|needs_input|failed|blocked|stopped|expired|suppressed|deferred|reroute_pending|rerouted|handoff`。`unknown`/`conflict` 只能进入 `needs_input|blocked|handoff`；`completed` 必须有实际 Observation 和 VerificationResult 证据。

完整事件字段和离线回放规则见 `references/activation-routing.md`。


Use this skill to turn a research package into a reviewable patent disclosure package. The package may contain a thesis or technical report, an editable source, figures, an earlier short draft, and a reference patent. Keep technical evidence, optional embodiments, and open work visibly separate.

## Source discipline

1. Inventory all candidate sources before drafting. Prefer the newest editable technical source (for example, TeX, Markdown, or source code) and use its matching rendered PDF for page and layout verification.
2. If the user identifies a stale chapter export or says it has been replaced, exclude it from extraction and record the exclusion in the source ledger. Do not silently merge versions.
3. Use an earlier draft to recover useful engineering structure only after checking it against the current source. Use a reference patent for section order, claim layering, and drawing conventions; do not copy its technical subject, model names, formulas, or results.
4. Record file paths, modification times when available, hashes for authoritative files, page counts, and each file's role. Never invent applicant, inventor, priority, or experimental facts.

5. Audit a reference patent package for bibliographic fields separately from its technical prose. Word author/editor properties and an internal school/project number are not applicant or inventor evidence unless the document explicitly labels them as such. Use a reference patent for organization and drafting style only.
6. Treat applicant, inventor, ownership, priority and earliest public disclosure as separate factual tracks. If a university is a candidate applicant, verify its official name/address from an authoritative page but do not infer ownership from student status; record the candidate and highlight the missing school/mentor confirmation.
7. Explain the filing fields concretely: applicant and inventor counts have no fixed upper limit; list every actual applicant and every person making a creative contribution, and keep representative/contact/agent fields separate. If there are multiple applicants and no agency, identify the representative according to the applicable request-form rules.

## Evidence model

For contract-field filling, first express the technical interface as:

`x_i = (q_i, s_i, E_i)` where `q_i` is the field question, `s_i` is the field schema, and `E_i` is the fixed evidence packet.

Derive a necessary-information set `M_i` from the field schema. Before generating a candidate value, classify the evidence as sufficient, partial, no-evidence, or conflict. Generate a structured result `(a_i, v_i, I_i)` containing the action, candidate value, and evidence identifiers. A write action must pass the joint checks for action, value, necessary-content completeness, and citation sufficiency. Otherwise route the field to review or a bounded repair path and retain an audit trail.

Do not turn this notation into a claim unless the source supports the corresponding technical operation. Adapt the names to the user's actual system when its source uses different terms.

## Drafting workflow

1. **Plan the task.** Create a `步骤.md` with each step's inputs, outputs, and completion criterion. Include source inventory, evidence extraction, invention boundary, claims, specification, abstract/drawings, editable files, acceptance, and skill handoff when requested.
2. **Extract evidence.** Build an `证据摘录.md` containing input/output structures, fixed-evidence construction, field schemas, mandatory items, evidence states, decision gates, checks, logging, and the exact status of experiments.
3. **Define the invention.** Write `发明点与证据边界.md`. Separate directly supported technical features, reasonable optional embodiments, and pending or unsupported assertions. Focus the invention on an implementable control loop, not on a benchmark score.
4. **Build claims.** Draft a method independent claim that covers the input, evidence gate, structured generation, joint verification, and write/review outcome. Add dependent claims for evidence construction, state classification, mandatory-content checks, citation checks, bounded repair, review queues, and replay logs. Add system, device, and storage-medium protection when supported.
5. **Write the specification.** Include technical field, background, invention content, drawings, detailed implementation, effects, and limitations. Every claim limitation must have an identifiable explanation or embodiment in the specification.
   In the formal `具体实施方式`, map the reference's implementation steps one-to-one: use one `步骤一`/`步骤二`/… subsection per actual step, and state the implemented input, module action, condition and output directly (for example, “步骤一：读取…并形成…”). Do not merge several steps under headings such as “步骤一至三”, do not leave a heading-only rename as the fix, and do not describe the core implementation with planning language such as “拟采用”“计划采用” or “将采用”. The reference may use “实施例” as its own convention, but that word is not a substitute for the completed step mapping in this section.
6. **Write the abstract and drawings.** Keep the Chinese abstract concise (use a 300-character internal ceiling after removing the heading and whitespace). Draw the complete path from evidence input to write or review and show audit/replay data where relevant. State when a figure is only a disclosure draft and needs formal patent drawing normalization.
7. **Match every reference block.** When a reference patent package is supplied, inventory its actual files and headings, then produce a corresponding specification, claims, drawings, abstract, and abstract drawing. Preserve the reference's block order, heading hierarchy, claim numbering style, and drawing conventions without copying its technical subject. Compare the generated and reference character/page scale; aim for the generated specification and claims to meet or exceed the reference where no legal ceiling applies. Keep the abstract within the 300-character ceiling even if the reference abstract is longer.
8. **Add source-grounded formulas when requested.** If the user asks for a formula-rich draft, first identify a technical paper or matching editable source that supports the notation. Add roughly 13–14 numbered formula groups to the specification's implementation or evaluation embodiments when that is the agreed target, and record each formula's source anchor. Do not use a formula merely to increase length, copy formulas from a structural reference patent, or turn an evaluation metric into an unsupported independent-claim limitation.
9. **Generate editable files.** Produce Markdown source plus editable DOCX for the specification, claims, abstract, drawings, and abstract drawing when useful. Render every DOCX to PDF or page images and inspect every page for clipping, overlap, missing glyphs, formula readability, and detached captions. If the preferred renderer is unavailable, record the fallback renderer and its evidence.
10. **Accept the package.** Run the checklist in `references/acceptance-checklist.md` and the deterministic checker in `scripts/validate_materials.py`. Write an acceptance report that distinguishes “usable disclosure draft” from “ready for formal filing,” and report the reference/generated character and page comparison, numbered-formula count, source hashes, and render-evidence paths.
   Acceptance must include a semantic audit of the detailed implementation: all expected step headings are present in order, each step has non-empty direct-action prose, grouped step headings are absent, and future/planning markers are absent from the core implementation section. A structural file-list pass alone is insufficient.
11. **Supplement metadata and implementation evidence.** Add an applicant/public-disclosure confirmation page, a preliminary prior-art screen, and a minimum sanitized implementation-evidence specification when the user confirms real code exists. Ask for key code/config/logs and two redacted end-to-end cases; do not require the whole project, secrets, model weights, or confidential contracts.
12. **Reconcile the handoff.** State exactly which reference fields were absent, give the current candidate count for applicants and inventors, and point to the highlighted confirmation page. If public disclosure is unknown, keep it unknown until a dated accessible event is evidenced.

## Evaluation and acceptance

When the user asks whether the patent material is complete, qualified, lawyer-ready, or ready for filing, read [references/patent-material-evaluation.md](references/patent-material-evaluation.md) before judging it.

Apply the evaluation in this order:

1. identify the evaluation target: lawyer handoff, attorney drafting preparation, or formal-filing preparation;
2. audit source versions and assign evidence labels to technical facts, implementation facts, experiments, and bibliographic data;
3. check the independent claim's problem–means–result chain and build a claim-to-specification-to-source matrix;
4. check enablement, evidence boundaries, prior-art preparation, readability, and document rendering;
5. evaluate hard gates before assigning the weighted A–F score;
6. output a status, dimension scores, hard-gate results, open items, limitations, and reproducible checks.

Never treat validate_materials.py or a complete file list as a substitute for claim support, enablement, evidence-boundary, or prior-art review. Never convert the internal score into a grant probability.

## Boundary rules

- Treat model-assisted labels, reconstructed references, small audits, and non-independent holdout subsets as implementation evidence unless the source explicitly establishes a human-verified gold standard.
- Keep action-selection safety, answer-generation quality, repair-loop behavior, and product-level performance as separate claims. A risk-control result does not prove general generation ability.
- Do not claim that pending experiments, human audits, or application tests are complete. List them as open items.
- Do not promise novelty, inventiveness, validity, or grant. Those require prior-art search and patent-agent review.
- If a source is incomplete, finish the supported draft and make the missing inputs actionable: identify the missing fact, where it belongs, and what evidence would close it.
- Keep the core invention understandable: describe one implementable control loop, then add only source-supported optional embodiments. Do not make the claims opaque by listing every model, interface, threshold, fallback, or hypothetical deployment.
- Keep user-facing patent prose readable: explain the core control loop in plain Chinese, avoid defensive lists of every hypothetical variant, and do not introduce a priority rule, threshold, retry limit, or other implementation detail unless the source or sanitized implementation evidence supports it. If multiple evidence problems can coexist and the source did not freeze a precedence rule, retain both diagnostics and leave the routing rule configurable.
- Apply an academic-writing cleanup pass to lawyer-facing prose: describe experiments as conducted under fixed evidence conditions, describe examples as fixed-evidence evaluation examples, and describe evidence handling as determining the evidence packet before downstream processing and keeping it unchanged. Avoid project-log labels for experiment status and internal study codes in Chinese materials; use readable terms such as “固定证据条件下的评测”, “实施例”, “评测设置”, and “核心评测集（200题）”.
- Record public-disclosure dates as unknown until a dated and accessible event is evidenced. A private local or permissioned file is not automatically public, but its sharing scope must be checked.
- For editable-document generation, remove Markdown markers such as backticks or bold delimiters from the Word body, preserve the stated number at the start of each local numbered list, render to PDF/page images, and inspect every page before delivery.

## Reusable deliverables

At minimum, return:

- `步骤.md`
- `材料盘点与来源.md`
- `证据摘录.md`
- `发明点与证据边界.md`
- `权利要求书.md`
- `说明书.md`
- `说明书摘要.md`
- `说明书附图.md` and figure files
- editable documents when requested
- `验收报告.md` and a machine-readable acceptance checklist
- an applicant/inventor/public-disclosure confirmation page with highlighted unknowns
- a claim-to-source/specification anchor table when the source is long or the reference package is only structural

Use the companion checklist and validator when producing the package:

- `references/acceptance-checklist.md`
- `scripts/validate_materials.py`
