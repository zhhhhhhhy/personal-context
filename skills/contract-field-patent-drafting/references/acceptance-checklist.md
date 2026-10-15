# Acceptance checklist for contract-field patent materials

Run these checks before calling a package complete.

When the user asks for a quality or completeness judgment, also read [patent-material-evaluation.md](patent-material-evaluation.md). The checklist proves selected package conditions; the evaluation protocol decides the handoff status and weighted score.

## Evaluation target and hard gates

- [ ] The report states whether the target is a lawyer handoff draft, attorney drafting preparation, or formal-filing preparation.
- [ ] The latest technical source and excluded versions are identified.
- [ ] The independent claim has a problem–means–result chain and no unsupported necessary limitation.
- [ ] The specification contains enough processing detail to implement the main flow.
- [ ] Model-assisted results, open metadata, and pending experiments are labeled with their evidence status.
- [ ] The report records the A–F dimension scores, hard-gate results, open items, and limitations.

## Source and provenance

- [ ] The latest authoritative editable source and its matching rendered PDF are named.
- [ ] Stale or explicitly excluded sources are recorded as excluded and were not used for technical conclusions.
- [ ] The earlier draft and reference patent have separate roles from the current technical source.
- [ ] The reference package was checked for formal bibliographic fields; Word metadata and internal reference numbers were not mistaken for applicant/inventor data.
- [ ] Paths, sizes, hashes, modification dates, and page counts are recorded when available.

## Technical support

- [ ] The field input, schema, frozen evidence packet, and structured output are defined.
- [ ] Necessary information items are derived from the field schema.
- [ ] Evidence states and the pre-generation action gate are defined.
- [ ] Write, review, repair, and audit/replay outcomes are distinguishable.
- [ ] The independent method claim includes a technical processing sequence and a concrete result.
- [ ] Dependent claims add supported implementation details rather than benchmark conclusions.
- [ ] System, device, and storage-medium claims map to the method when they are requested.
- [ ] Each claim limitation has specification support.

## Evidence boundaries

- [ ] Direct source facts, optional embodiments, and pending work are separated.
- [ ] Model-assisted labels are not called human gold without explicit evidence.
- [ ] Risk-control results are not presented as general generation improvement.
- [ ] Pending experiments, audits, and product tests are listed as open items.
- [ ] No applicant, inventor, priority, legal conclusion, or performance number was invented.
- [ ] Applicant and inventor counts, representative/contact roles, and school/ownership confirmation needs are stated separately.
- [ ] If evidence states can coexist, no unsupported precedence rule was added to the claims.

## Documents and presentation

- [ ] Claim numbers are contiguous and cross-references resolve.
- [ ] The abstract is under the internal character ceiling after removing the heading and whitespace.
- [ ] Titles, terminology, symbols, and figure numbers are consistent across files.
- [ ] Every editable document has been rendered and every page has been inspected.
- [ ] There is no clipping, overlap, missing glyph, or detached figure caption.
- [ ] Rendering fallbacks and their limitations are documented.
- [ ] Markdown syntax markers are absent from Word body text and each local numbered list starts with its intended number.

## Final status

Use `pass_with_open_items` for a usable disclosure draft that still needs prior-art search, attorney review, formal applicant data, or pending experiments. Reserve `ready_for_formal_filing` for a package whose requested legal and formatting review has actually been completed.
