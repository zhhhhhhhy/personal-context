# Round 003: evolution with measured progressive loading

User request: evolve Context from another unused batch using the new loading rules and compare actual loaded content. Raw evidence and native message IDs remain local.

| Work | Owner | Evidence |
|---|---|---|
| Refresh metadata and freeze cohort | Script + parent | Exclude prior 115 roots, current chats, automated tasks and the diagnostic-read root; 8 training and 4 held-out roots |
| Recover selected evidence | Native read-only app API + script | Export only actual userMessage records with thread/turn/item provenance; no assistant or tool log substitution |
| Observe and reflect | Parent AI | Train only; progressive candidate overlap retrieval; novelty, scope, privacy and rejection reasons |
| Measure loading | Local instrumented reader | Count returned Context fragments and evidence with o200k_base; same batch and same constraints for whole-file comparison |
| Review usefulness | Independent semantic review / isolated response checks when supported | No forced promotion, no tuning on held-out evidence, no human-accuracy claim |
| Apply and deliver | Validator + parent | Supported low-risk learned rules or a justified zero-promotion result, privacy boundary, budget and Git checks |

Selection is metadata-guided and historical (April–October), not a random weekly sample. Related industrial-report roots share one family, giving seven training families. The application can still read messages for many threads whose old local JSONL paths are absent. Native IDs and export line numbers must be distinguished from original rollout line numbers.

Measurement protocol: separate core/routing, candidate retrieval, historical evidence and engineering/setup overhead. Count actual returned text payloads, including repeated fragments when present, rather than file size limits. Whole-file comparison keeps semantic inputs and constraints constant; use a real measured reading run where available, otherwise label the number a reconstruction. Platform prompts, tool schemas and the already-long parent conversation are unobserved. Do not call a file-payload estimate total live-context usage.

Freeze held-out IDs before exporting message bodies. Do not inspect their semantic content before freezing reflection candidates. Keep core rules and Skills unchanged during the evolution application; no scheduler is requested.
