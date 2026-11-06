# Founder research memo

Date: 6 November 2026

## Executive summary

The existing synthetic lab contains four completed A/B task pairs, with one fresh coding-agent run per condition per task. On the frozen deterministic checks, repository-only A and instruction-file B had the same outcome on T01, T03, and T04. On T02, both passed three visible functional tests, but A failed both predeclared failure-safety audits and B passed them. The result is a useful failure contrast, but one observation per condition cannot establish a general or causal effect.

There is no measured A/B/C comparison. The isolated T04 Contexer decision remains pending_approval, with no approval provenance and no evidence that a fresh coding agent retrieved it. Do not present installation or a stored pending decision as a Condition C result.

The original 0.940 synthetic classification accuracy was reproduced exactly. That is a seeded scikit-learn smoke test and says nothing about whether Contexer improves coding agents.

## What works

- The independent, deterministic audits expose a real safety difference that ordinary functional tests missed in T02: the direct write passed the visible tests yet failed when the write or replacement operation was injected to fail.
- T01, T03, and T04 show that the repository-only baseline can pass these particular simple tasks. T01 had a shared-client README, so A was not without relevant repository evidence.
- T04's frozen tests successfully exercised exact URL handling with zero calls to four monkeypatched network boundaries in both A and B.
- The synthetic classifier example is reproducible from its fixed seed and pinned packages.

## What does not work or is not established

- T02-A did not preserve the previous file when either injected failure occurred. The functional suite alone did not detect this.
- The project's current MVP table defines T01 as a JSON settings task, while the saved T01 run is a shared HTTP-client task. Treat that run as exploratory, not as a faithful run of the current T01 row.
- Contexer delivery, approval lifecycle, retrieval relevance, Guard enforcement, and three-way A/B/C performance are not measured by these pilots.
- Screenshots and the narrated video are not available.

## Baseline comparison

Within the observed task pairs, A matched B on T01, T03, and T04. On T02's partial-write and replacement-failure checks, B passed where A failed. These are outcomes for static project instructions versus repository context; B is not Contexer. There is no observed result in which the baseline equaled, beat, or lost to Contexer because C never ran.

## Failure analysis

T02-A used a direct truncating write. A partial write changes the destination before the new report is complete; a failed publication leaves the old destination changed. B used a temporary sibling, os.replace, and cleanup, and passed both injected failure audits. The failure mode supports testing failure semantics, not just successful output, whenever the product claim concerns durable engineering constraints.

T04 also had two failed startup attempts before A task execution (an incompatible CLI flag combination and an unsupported default model). They are preserved in the launch-attempt record and excluded from completed-run counts. A later independent wrapper issue was also corrected; it is not an agent outcome.

## Evidence-backed recommendations

1. Retain deterministic failure-injection checks for safety properties. T02 shows that all visible functional tests can pass while failure behavior violates the decision.
2. Keep task correctness and decision compliance as separate metrics. T02 functional tests were 3/3 in both conditions; the compliance result differed.
3. Report per-task outcomes, model settings, failed launches, missing budgets, and the exact checks. Do not collapse four heterogeneous tasks into a single success rate.
4. Reconcile the T01 task-definition discrepancy before using T01 as a preregistered case.
5. Require an approval-state and retrieval receipt before calling an agent run “Condition C.”

## Experimental hypotheses

- Hypothesis: Contexer's retrieval may help when a relevant approved decision is phrased differently from the task, but relevance could also fail. Test with paraphrased task wording, fixed candidates, and blind deterministic scoring.
- Hypothesis: Human approval and provenance can reduce the risk of an AI-captured proposal being mistaken for trusted guidance. Test approval, revision, and rejection lifecycle separately from code-quality outcomes.
- Hypothesis: Long static instruction files may hide a relevant rule depending on position or length. Test fixed decisions at start/middle/end and measure exact retrieval and task outcomes.
- Hypothesis: Untrusted repository/tool text could try to override an approved decision. Test prompt-injection resilience in an isolated synthetic environment, scoring benign task utility and security outcomes separately.

These are proposed experiments, not observed Contexer behavior in this lab.

## Risks

The dataset has one run per condition per task; no sampling variance can be estimated. Tasks are short, synthetic, Python-only, and from one setup. Conditions T01–T03 used gpt-6-luna/medium; T04 used gpt-5.6-terra/high with a different CLI. T02 and T03 ran concurrently; T01–T03 have no explicit token/time cap. T04 used the same default one-turn budget but no explicit token cap. A/B order was not randomized consistently. The grader is deterministic but narrow. T01's project roots did not isolate Git, and read-only Git status commands escaped to a parent context. No C result, screenshots, or video exists.

## Recommended next experiment

Run the frozen T04 task in Condition C only after the pending decision is explicitly approved.

- Hypothesis: an approved T04 decision retrieved by the isolated Contexer/Codex integration yields the same six exact URL outputs and zero calls to all four patched network boundaries as A and B.
- Setup: fresh isolated T04 C repo with the frozen starter, no AGENTS.md, clean isolated Codex profile, approved store entry whose text hash matches the T04 B decision; use the same Codex CLI/model/reasoning/tools and default one-turn budget as T04 A/B.
- Before coding: capture review provenance and a sanitized retrieval receipt showing the decision ID/status/text reaching the fresh agent.
- Metric: frozen URL examples passed (0–6), network-boundary calls (0 expected at each of four boundaries), independent scorer exit, agent exit, and any launch failures. Record token use if exposed.
- Decision rule: call the C run compliant only if the independent grader passes all six outputs and all four no-network boundaries, and the approved decision's delivery is evidenced. Any failure remains a valid result; do not edit the frozen checks.

## Product proposals

Evidence-backed: make an experiment-facing delivery receipt available (decision ID, approved status, revision, delivered text/hash, session ID) so researchers can tell whether the agent actually received trusted context. The present C setup lacks this proof.

Experimental hypotheses: test paraphrase-aware retrieval; add an explicit user-visible capture confirmation for new decisions; evaluate contradiction and prompt-injection handling. Each proposal needs a preregistered evaluation before it is described as a product improvement.
