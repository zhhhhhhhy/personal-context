## Evidence and wording boundaries

- Report what the experiment measures, not what the system was intended to achieve.
- If only a pre-generation gate was evaluated, attribute gains to action control or false-fill reduction; do not call them gains in the generator or the complete multi-module system.
- If references or evaluators are model-assisted, state that limitation without presenting them as human gold.
- When diagnosing missing research evidence, inspect the actual project artifacts and map scores to labels, references and source records. List what is missing and the effort to recover it; final scores cannot establish that an annotation process occurred. Concrete unresolved gaps belong to that project.
- A user-provided description or request to rewrite the paper records what was stated or requested; it does not establish that the annotation procedure occurred. Preserve concrete counts and conditions as attributed, pending claims until records support them. Human-review summaries do not establish that every model output was independently scored by humans.
- If a benchmark is diagnostic or not independently held out, limit generalization claims accordingly.
- Treat privacy as a motivation and deployment constraint unless a privacy evaluation was actually performed.
- If a sentence mainly serves to preempt criticism but does not advance the research question, argument chain, evidence interpretation, or conclusion boundary, omit it from the main text; retain a qualifier only when it changes how readers should understand the conclusion or constitutes a necessary evidence boundary.

Do not turn pilot runs, internal materials, unfinished candidates, or engineering checkpoints into claims about method effectiveness. Phrases such as “已有材料显示……未形成明确收益”“前置试验表明……” and “当前候选方案……” describe project status and should be removed from the main prose unless they refer to a defined experiment with an explicit protocol and reportable evidence. In a research plan, state the question and evaluation design instead, for example “将通过统一条件下的对照实验检验……”；in a completed study, report the measured metric, comparison and scope.

## LaTeX and artifact handling

When the task targets an open LaTeX document, preserve the user's selected source file and edit it in place. Keep benchmark structure and prose changes in that source; do not create a replacement document merely to avoid restructuring. After edits, use the built-in LaTeX compiler when available, repair source errors, and report any compiler-environment failure separately from source validation. Keep the editor open.

For a substantial rewrite, tell the user the paper type, central claim, hierarchy of contributions, deleted information classes, and paragraph plan before editing when the user requests that review step. Do not turn the plan into prose inside the paper.
