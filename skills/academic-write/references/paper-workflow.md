## First decide what the paper is

Before rewriting, identify the paper type and write its central claim in one sentence. Preserve the hierarchy throughout the paper:

- A benchmark paper centers the task, data, annotation or reference construction, evaluation protocol, metrics, and diagnostic findings.
- A method paper centers the proposed model or algorithm, its mechanism, and evidence that the mechanism improves the target task.
- An application paper centers the deployed setting, constraints, system behavior, and validated use outcomes.

Do not let the strongest available experiment silently redefine the paper. If the paper is benchmark-first, a method such as JEV is an evaluated system or case study unless the user explicitly changes the paper type.

## Structural workflow

1. **Build the argument map.** Record the practical problem, task definition, literature gap, primary contribution, secondary systems, evaluation questions, and evidence supporting each claim.
2. **Separate information layers.** Keep scientific content in the main paper; put reproducibility details in an appendix or artifact; keep project management and internal provenance out of the paper unless they change a scientific interpretation.
3. **Rewrite the outline before sentences.** When the user reports logic drift, verbosity, or a wrong research emphasis, rewrite from the argument map rather than patching the old paragraphs.
4. **Draft the introduction by rhetorical function.** For a benchmark paper, use the default five-part progression in [benchmark-first-template.md](benchmark-first-template.md), adapting the number of paragraphs to the venue.
5. **Write methods and experiments in the same hierarchy.** Define the benchmark before describing systems that are evaluated on it. Place a system-specific section after the task and protocol sections unless the method itself is the paper's contribution.
6. **Run a compression pass.** Give each paragraph one job. Remove repeated explanations, implementation inventories, conversational transitions, and sentences that do not change the reader's interpretation.
7. **Run a claim-evidence pass.** Do not generalize a result from one module, split, evaluator, or fixed-evidence setting to the whole method or deployment scenario. Distinguish model-assisted evaluation from independent human gold.
8. **Run a reviewer pass.** Apply the checklist in the reference file and report material limitations separately from project status.
