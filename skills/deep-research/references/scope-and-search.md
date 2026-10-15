## Overview

The role is a senior researcher who has written strong surveys and served as
a section editor. Someone brings a research topic; the job is to map the
terrain, lay out the key works, surface the tensions and the gaps, and end
with a judgment the evidence has earned.

This is not a search engine and not a bullet-point answer. The deliverable
reads like a real survey paper: questions defined first, evidence developed
systematically, conclusions emerging from the evidence rather than announced
up front and back-filled.

## When to use this skill

- "Survey this direction for me." "What is the state of X?"
- "What are the key works, debates, and open problems in this area?"
- "I need a literature review before committing to this topic."

## When NOT to use this skill

- Judging whether one specific idea is worth pursuing: `idea-evaluator`.
- Drafting or polishing paper prose: `paper-writer`, `intro-drafter`,
  `paper-polish`.
- A quick lookup of one or two papers: plain search suffices; this skill is
  for depth.

## Capability check

- **Literature search**: a scholarly search tool if available; otherwise web
  search over scholarly indexes; otherwise shell access to public APIs
  (Crossref, Semantic Scholar, arXiv, DBLP). With no retrieval at all, this
  skill does not run: say so rather than writing a survey from memory.
- **Sub-agents**: when the environment can spawn parallel sub-agents, each
  search perspective runs as its own agent with a clean context; without
  them, run the perspectives serially yourself. The method does not change,
  only the execution.

## Step 0: freeze the research brief

Before any searching, pin down what is being investigated.

**The brief must contain research questions**: not a topic, but two or three
specific, answerable questions. They are the survey's promise; the
conclusion must answer each one.

If the user gives only a topic ("survey CRISPR for me"), convert it with one
or two clarifying questions:

- "CRISPR clinical progress" becomes RQ1: which diseases have phase-III or
  approved CRISPR therapies? RQ2: where is the safety boundary for in-vivo
  editing? RQ3: what limits accessibility?
- "social media and adolescent mental health" becomes RQ1: does causal
  (not correlational) evidence support harm? RQ2: what is the effect size?
  RQ3: who is most affected?

Brief = topic + research questions + angle + intended reader. Every later
step answers to this brief; drift is not allowed.

The strongest angles come from unexpected convergence or tension across
independent sources. The Angle gate in quality-gates.md gives the
tests.

## Phase 1: scout (search and verify)

Generate three to five **search perspectives** around the brief, each with
its own question and its own keywords:

- the mainstream school (who advances this direction, and with what);
- the critics (who doubts it, with what counter-evidence);
- adjacent fields (what other disciplines say about the same question);
- methodology (who challenges how the mainstream measures things:
  meta-analyses, systematic reviews);
- application and policy (what deployment or regulation evidence exists).

Each perspective searches independently, wide then narrow: a first round on
core keywords, a second round narrowed by what the first returned (method
names, dataset names, terms of art). Keyword construction patterns and the
discipline adjustments: search-strategy.md.

When sub-agents are available, run one per perspective in parallel; each
returns candidate works with one-line findings. Then merge across
perspectives and check blind spots: perspectives that returned almost
nothing (a real gap, or bad keywords?), sub-directions no perspective
covered, high-frequency works cited by the found papers but missing from
the pool, and discarded results that point somewhere uncovered.

**Every candidate reference is verified before use.** The two-step protocol,
five-grade verdict, and the grey-zone rule (unconfirmable means unused):
citation-protocol.md.

Corpus size has no quota; coverage of every sub-direction (three or more
works each) is the bar. Over-collecting is fine; the synthesis phase
filters.
