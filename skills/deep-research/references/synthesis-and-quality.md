## Phase 2: synthesize

With the verified corpus in hand: extract per-paper findings, cluster by
theme into a MECE taxonomy, assign works to branches, then write the
branches serially, each section citing only its assigned works. In-sentence
cross-comparison is mandatory; contradictions are presented with condition
analysis, never averaged away. The full method:
synthesis-framework.md.

After synthesis, run the self-adversarial review (three retrospective
questions, perspective-omission check, concession rules):
self-adversarial.md.

## The six gates and the iteration loop

Throughout, six internal gates guard quality (never shown to the reader):

| Gate | One line | Severity | Failure route |
|---|---|---|---|
| Angle | a judgment, or just a listing? | CRITICAL | back to Step 0 |
| Coverage | key works all found? | MAJOR | targeted re-scout |
| Citation | references real and honestly quoted? | CRITICAL | re-verify; delete inventions |
| Taxonomy | organized by theme, MECE? | MAJOR | redesign axes |
| Calibration | claim strength matches evidence? | MAJOR | re-calibrate wording |
| Weaving | in-sentence comparison present? | MAJOR | rewrite flagged sections |

Detection questions and routes: quality-gates.md.

The loop this creates is the point: a Coverage or Citation failure sends the
work back to scouting for a **targeted** supplement (new works append to the
corpus; the synthesis updates incrementally), not a restart. Iterate until
every gate is CLEAR and the self-adversarial pass stops finding corrections.
Depth is driven by the topic's complexity, not by a fixed round count.

## Cross-discipline evidence standards

Switch what counts as strong evidence by field:

- **CS / AI**: benchmarks, ablations, reproducibility; note model versions
  and evaluation conditions.
- **Biomedicine**: trial phase, patient counts, follow-up length, approval
  status.
- **Social science**: causal versus correlational designs (RCT, natural
  experiments, IV); effect sizes and heterogeneity.
- **Economics and finance**: identification strategy (IV, DID, RDD);
  statistical versus economic significance.
- **Cross-disciplinary**: separate model predictions, observational
  attribution, and field experiments; carry uncertainty ranges.

Non-CS reports include the evidence-type table from the output-structure
reference so readers can weigh evidence kinds.
