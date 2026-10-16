# Reporting Standard Mode

## Audience and purpose

Assume the reader is outside the implementation team. The report must let the reader answer four questions quickly: What is the project for? What can it do now? Is something blocking it? Why is it blocked?

## Required report order

1. **Project purpose:** one or two sentences about the user outcome, not the internal architecture.
2. **Current situation:** describe what a user can do today and what remains unavailable.
3. **Method used in this stage:** explain what was changed or tested and why that method was chosen.
4. **Effect:** state the visible change first. Add numbers with a plain-language interpretation, for example, “20 of 25 new fields were correct, so about one in five still needs correction.”
5. **Blocker and cause:** say whether there is a blocker. Separate the symptom (`the system is not ready`) from the cause (`new page layouts produce retrieval or locator errors`).
6. **Iteration change:** state what improved, what did not improve, and whether the method reduced, resolved, or only measured the problem.
7. **Next method:** name the next concrete method for the remaining cause and the evidence that will decide whether to continue.

## Plain-language rules

- Replace internal labels with their meaning before using them. Say “new pages that the system had not seen before” before saying “holdout.” Say “the browser actually found and wrote the field” before saying “DOM observation.”
- Explain every method as a before/after behavior change before presenting its technical name: what the old flow did, what the new flow does, why the change targets the problem, and what remains unproven. A method name alone is not an explanation.
- Define unfamiliar implementation terms at first use and connect them to the user-visible behavior. For example: “LoRA is a small trainable add-on placed on top of the fixed base model; it teaches the existing model a target behavior without replacing the model or retraining every parameter.” Follow that definition with the concrete training data, inference flow, and evaluation boundary. Do not imply that using LoRA itself proves improvement or production readiness.
- When a report contains a model or training method, describe the input, transformation, and output in one short flow (for example, “field question plus visible evidence → completeness check and answer/review decision → structured fill or review result”).
- Do not list raw test names or metric names without explaining their practical meaning.
- Keep the distinction between “implemented,” “tested,” “works in the test environment,” and “authorized for real use.”
- Report safety and authorization boundaries explicitly: unchanged fields, review-only suggestions, no automatic submission, and any unavailable evidence.
- If a number is useful, include the denominator and the implication. Avoid presenting a high calibration score as overall readiness when a broader test is lower.
- For an iterative update, state the previous situation, the new method, the new result, and the next decision in one connected paragraph or a short numbered list.

## Compact stakeholder template

```text
项目目的：
当前情况：
本阶段采用的方法：
得到的效果：
是否有阻力：
阻力原因：
相比上阶段的变化：
下一步方法：
```

Use the user's language for the report. Keep the project iteration log and evaluation artifacts in the project's required artifact language.
