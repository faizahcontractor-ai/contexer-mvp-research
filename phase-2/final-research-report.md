# Contexer Extended Research — Phase 2 report

Prepared 6 November 2026

## 1. Executive summary

This report audits the existing onboarding workspace and the separate synthetic T01–T04 lab. It reviews five scored outcome cases across four A/B task pairs. Each task has one completed repository-only run (A) and one completed project-instruction run (B), for eight completed coding-agent runs total. The independent deterministic scorers were rerun against the saved outcomes on 6 November 2026. Those rechecks reproduced the saved results.

The only observed A/B difference is T02. Both agents passed all three visible functional tests. A failed the independent partial-write and replacement-failure audits; B passed both. T01, T03, and T04 passed their frozen checks in both conditions. This is a preliminary one-run-per-condition pilot, not a replicated benchmark.

No Condition C agent run exists. The isolated T04 Contexer store contains the decision with ID 8aa46b44-c427-4cda-a20e-4b8abb5b70b2, status pending_approval, and created_by ai. Its text matches the body of the frozen T04 B instruction, but the entry has no approval metadata and no delivery receipt to a fresh coding agent. Therefore there is no empirical baseline-versus-Contexer result, no measured Contexer win or failure, and no basis for attributing any A/B result to Contexer.

The classifier example's reported 0.940 accuracy on 50 synthetic test rows was reproduced exactly from seed 42. It is a deterministic smoke test, not evidence about agent behavior or Contexer.

## 2. Research questions

The MVP question is whether a small approved engineering decision in a project instruction file changes a coding agent's decision compliance relative to repository context alone, without reducing functional correctness.

The planned Contexer extension asks whether a stored, explicitly approved decision, delivered to a fresh coding-agent session under comparable settings, can produce outcomes comparable to the static instruction condition. That question remains unanswered because Condition C was not approved and run.

Phase 2 asks which observed cases show equality or a difference, what failure modes the checks detect, and what a credible next comparison would require.

## 3. Audit and provenance

The audit read the original onboarding README and MVP-experiment.md; the lab README, run protocol, and codebase flow; each T01–T04 task preregistration, fixture-validation record, result record, scorer, A/B run record, patch, and available transcript; the isolated T04 C store metadata; the synthetic classifier source and output; and parent Git status/history. The underlying lab and source records were not edited.

On 6 November, the saved T01–T04 A/B scorers were rerun with bytecode generation disabled. Outputs are saved in logs/reverification/. T04 scoring and visible tests run only through the preregistered monkeypatches; no live network request was made. The seeded sample_analysis.py output matched sample-output.txt exactly.

The current parent Git status had pre-existing deletions and untracked files, including onboarding-contexer. onboarding-contexer is not its own Git root; its toy-repo is a separate three-commit repository. No pre-existing files were staged, committed, reset, or discarded.

## 4. Conditions and experimental setup

| Condition | Actual setup | What it measures |
|---|---|---|
| A — repository only | Fresh agent session; task, ordinary repo files, tests, and starter; no decision-bearing AGENTS.md | Whether repository context alone is enough for the scored behavior |
| B — project instruction | Same task/starter and comparable agent settings; B adds the preregistered decision in AGENTS.md | Effect of explicit static project guidance relative to A |
| C — Contexer | T04 isolated Codex setup with Contexer registration and a matching decision in local store; store status is pending_approval | Preparation only; no approved delivery or scored agent run |

Within T01–T03, A and B each used a fresh Codex session requesting gpt-6-luna at medium reasoning. T02 and T03 sessions ran concurrently. Those tasks have no explicit token/time cap, and consumed-token metadata is unavailable. T01's records show failed unsupported default-model attempts before the successful gpt-6-luna sessions; only the later completed runs count. T01 did not use separate Git roots, and read-only Git status commands exposed parent-context listings; no files changed.

T04 used Codex CLI 0.163.0-alpha.10.2, gpt-5.6-terra, high reasoning, the same task prompt and tools, and the same default one-turn budget in both conditions. There was no explicit token cap. Run records report 87,423 input / 1,517 output / 526 reasoning tokens for A and 109,964 input / 2,513 output / 1,402 reasoning tokens for B; the difference is observed usage, not a controlled budget difference. Two failed A startup attempts are preserved but excluded. A wrapper issue was rerun and is not counted as an agent result.

All comparisons are within-task only. The model/agent setup differs between T01–T03 and T04, and T01–T03 lack comparable usage data. No cross-task aggregate score or inferential test is reported.

## 5. Dataset and evaluation

The code tasks are synthetic, small Python fixtures. Each task has a common starter and task prompt, an A copy, a B copy with AGENTS.md, functional tests, and a deterministic grader outside the agent-visible repository. T02–T04 have frozen preregistrations. The original MVP table currently defines T01 as a JSON settings update, while the saved T01 experiment is a shared HTTP-client profile fetch. T01's run record supports an exploratory observation, but not a faithful execution of the current T01 table definition.

The primary measurements are functional test results and frozen decision-compliance checks. T04 also monitors four monkeypatched network boundaries. Agent-written extra tests do not replace the common frozen grader. The five cases below are four task pairs; T02 contributes two distinct failure-injection cases. Those two checks are not independent agent runs.

## 6. Five concrete cases

| Case | Task/input | A result | B result | C result | Observed difference | Failure mode / interpretation | Evidence |
|---|---|---|---|---|---|---|---|
| C01 — T01 shared HTTP client | Implement a profile fetcher. The shared client is present in the repository README. The current MVP table instead specifies a JSON settings task, so this is exploratory relative to that plan. | 2/2 functional tests; compliance pass | 2/2 functional tests; compliance pass | Not run | Tie on saved and re-scored checks | A could follow repository evidence without AGENTS.md. The audit is a narrow AST check; identifiers beyond the fixed input are not scored. | evidence/source-records/T01/; logs/sanitized/T01/ |
| C02 — T02 partial temporary-write failure | Inject a partial write while replacing an existing report. | Functional suite 3/3, but audit FAIL; old destination changed | Functional suite 3/3 and audit PASS; prior destination preserved and temporary file removed | Not run | B passed where A failed | Direct truncating write did not protect old contents on failure. Visible tests alone missed this. | evidence/source-records/T02/; logs/sanitized/T02/ |
| C03 — T02 replacement failure | Inject os.replace failure after preparing the report. | Functional suite 3/3, but audit FAIL; old destination changed | Functional suite 3/3 and audit PASS; old destination preserved and temp file removed | Not run | B passed where A failed | Atomic replacement and cleanup mattered under an injected failure. One run per condition only. | evidence/source-records/T02/; logs/sanitized/T02/ |
| C04 — T03 label validation | Preserve valid labels exactly; reject empty and whitespace-only strings with exactly ValueError. | All four frozen grader checks pass | All four frozen grader checks pass | Not run | Tie | Agent-added coverage differed (A added non-string TypeError; B added Unicode whitespace), but neither changes the frozen score. | evidence/source-records/T03/; logs/sanitized/T03/ |
| C05 — T04 URL/no-network contract | Preserve URL parts and remove exactly one final path slash; never invoke a network client. | 6/6 URL examples pass; four patched boundary counts are 0 | 6/6 URL examples pass; four patched boundary counts are 0 | No run; matching decision remains pending_approval | A and B tie; C unmeasured | No live request occurred. This is not evidence that Contexer retrieved or enforced the decision. | evidence/source-records/T04/; logs/sanitized/T04/; condition-c-status.md |

## 7. Results and baseline comparison

| Task/case | A | B | C | Comparison |
|---|---|---|---|---|
| T01 | 2/2 tests; compliance pass | 2/2 tests; compliance pass | Not run | Baseline matched B on this task; repository README described the helper |
| T02 partial write | Visible tests pass; failure audit fails | Visible tests pass; failure audit passes | Not run | B had the safer observed implementation |
| T02 replacement failure | Visible tests pass; failure audit fails | Visible tests pass; failure audit passes | Not run | B had the safer observed implementation |
| T03 | Frozen decision checks pass | Frozen decision checks pass | Not run | Baseline matched B |
| T04 | 6/6 output examples; zero calls to four patched boundaries | Same | Pending decision; no run | Baseline matched B; C cannot be compared |

Explicitly: the baseline equaled B in three of four task-level outcomes and failed two predeclared T02 failure-safety checks where B passed. These are A/B observations; B is not Contexer. No local case establishes that Contexer performed better or worse than A/B. The public Contexer benchmark is separate vendor-published evidence, not a C outcome in this experiment.

The public Contexer benchmark describes 1,242 sessions, 38 synthetic coding tasks in one repository, and Contexer v0.50.1 with Claude Sonnet 5.5. At 150 rules it reports 109/114 tasks right for Contexer and 108/114 for each static-rule comparator, and explicitly says this accuracy gap is within noise. It reports lower cost per session and more questions on contradictory rules, while also reporting weaker capture of newly stated rules and a wording/relevance miss. These are claims in the vendor's report, not an independent replication or a substitute for Condition C. [Contexer benchmark](https://github.com/bhargavamin/contexer/blob/main/docs/benchmark.md)

## 8. WHAT THE CURRENT DATA CAN AND CANNOT ESTABLISH

### Supported by evidence

- Each of T01–T04 has one saved completed A run and one saved completed B run.
- On the deterministic checks, T01, T03, and T04 have matching pass outcomes across A and B.
- In T02, both visible suites passed 3/3; A failed two injected failure audits and B passed them.
- T04 scorer rechecks recorded zero calls to each of four patched network boundaries for both A and B.
- The local T04 Contexer decision is pending approval, not approved; no scored C run is present.
- The original seeded classifier script reproduces 0.940 accuracy and confusion matrix [[24, 1], [2, 23]] on 50 synthetic rows.

### Plausible interpretation

- Failure-injection audits may reveal important engineering-policy violations that ordinary happy-path tests miss.
- Ordinary repository context can be sufficient for some simple decisions when the repository already documents the convention.
- Static project instructions may help on some failure-safety decisions; T02 is consistent with that idea, but cannot establish it generally.

### Hypotheses

- Contexer retrieval may help surface relevant rules across differently worded tasks, or may miss them; a preregistered relevance stress test is needed.
- Decision approval/provenance may reduce ambiguity over whether an AI-captured rule is trusted.
- Long context position and prompt injection may affect how decisions are used; neither is tested locally.

### Not established

- That Contexer improves agent code quality, compliance, security, cost, time, or team outcomes.
- That A/B differences are statistically meaningful or causal.
- That results generalize beyond these small synthetic Python tasks, these models/versions, these graders, or a single local environment.
- That an installed hook or pending store record delivered a decision to an agent.
- That the 0.940 classifier accuracy measures any Contexer capability.

## 9. Failures, deviations, and threats to validity

T02-A is the substantive implementation failure: it passed happy-path tests but changed the existing file when write or replacement failed. T04's early CLI start errors and wrapper issue are operational failures before or around the measured run; they are preserved and excluded from successful run counts.

The sample is one run per condition per task. Agent sampling variation is unmeasured. No explicit token/time caps existed in T01–T03; T04 had only a default one-turn budget. T02/T03 were concurrent and A/B ordering was not consistently randomized. Scorers cover only predeclared inputs and narrow code-level invariants. They are independent and deterministic, but are not general security analyzers. Agent-added test count varies, so only frozen grader results are compared.

The tasks are small, synthetic, one-language, and single-repository. T01's task differs from the current T01 row in MVP-experiment.md. T01 also lacked isolated Git roots, and its agents ran read-only Git commands that traversed parent context. The T04 model, agent host, and model version differ from earlier tasks. T04 does not include a C run. The study has no blinded analysis or significance testing.

## 10. Evidence-backed recommendations and experimental hypotheses

### Evidence-backed

- Keep correctness and decision compliance separate: T02's happy-path tests passed in both conditions even though failure behavior differed.
- Preserve failure-injection checks for atomic-write decisions.
- Keep the independent scorer outside agent-visible repositories and use its fixed expected inputs.
- Treat T01 as exploratory until its preregistration discrepancy is resolved.
- Record approval and delivery provenance before counting Condition C.

### Experimental hypotheses

- Test paraphrase/relevance robustness, prompted by the Contexer vendor report's documented rule-wording miss.
- Test capture and human review separately; the vendor report describes lower capture of newly stated decisions than a maintained static file.
- Test prompt-injection resistance with synthetic untrusted tool output. AgentDojo provides a primary benchmark pattern, but no local result supports a Contexer security claim.
- Test decision position/quantity effects using controlled context placement, motivated by long-context evidence.

For each proposal, preregister cases, a deterministic score, and safety criteria before an agent run. Do not turn hypotheses into present-tense product claims.

## 11. Recommended next experiment: T04 Condition C

The smallest informative next step is one fresh C run against the existing frozen T04 task after human approval. First approve the specific pending decision through Contexer's normal review mechanism. Verify the isolated store reports an approved state and preserve reviewer/provenance fields. Start a fresh agent session and retain a sanitized retrieval receipt showing the exact approved decision before coding. Start from the frozen starter in the isolated T04 repo; do not include B's AGENTS.md in C. Match T04 A/B's Codex CLI version, model gpt-5.6-terra, high reasoning, tools, prompt, and default one-turn budget. Keep the frozen tests and grader unchanged.

Success for C requires evidence that the approved decision was delivered, all six frozen URL outputs pass, and each of the four patched network-boundary call counts is zero. Report the result even if it fails. Do not use a pending decision, installer output, or hook presence as a substitute for the delivery receipt or scored run.

## 12. Compact AI research watch

The CSV in research-watch/ai-research-watch.csv lists three primary research papers and the vendor benchmark separately. MemoryAgentBench recommends evaluating retrieval, test-time learning, long-range understanding, and selective forgetting across incremental interactions. AgentDojo motivates a synthetic injection/defense task with deterministic security and utility checks. Lost in the Middle motivates varying a decision's position in context. None demonstrates a Contexer effect.

## 13. Reproducibility and evidence

The existing public repository contains the earlier pilot package at [the uploaded bundle directory](https://github.com/faizahcontractor-ai/contexer-mvp-research/tree/main/contexer-mvp-research-upload-under-100%202). That bundle contains the original T01–T04 fixtures, scorers, results, and saved records. This Phase 2 folder contains sanitized source summaries, run artifacts, and the 6 November re-score outputs. The synthetic classifier source and pinned dependencies are copied into dataset/ and environment/.

For exact commands, network-mock restrictions, chart regeneration, and local requirements, see README.md, demo/README.md, and environment/README.md. Every numeric value in metrics.csv maps to a run or an explicit zero-run C status. The chart script plots per-case status and completed run counts only; it does not calculate a pooled performance estimate.

## 14. AI tool and independent verification

AI assistant used: ChatGPT running as Codex (GPT-6) for workspace audit, research synthesis, report and chart authoring, and review of saved experiment evidence. No new coding-agent experiment was launched.

Independent checks: read the underlying run records and deterministic scorer code; reran all eight saved A/B scorers, including T04 only through its patched boundaries; reran the synthetic classifier and compared its exact stdout with the saved sample-output.txt; computed the stored C decision status and text match directly; checked paper claims against the linked arXiv, NeurIPS, and ACL primary pages; and wrote metrics from those records, not from generated summaries alone. Reverification stdout is saved under logs/reverification/. Public benchmark values are explicitly attributed to Contexer's own report.

Agent outputs are evidence, not ground truth. The frozen tests and independent scorers determine the reported code outcomes.

## References

- Contexer public repository and documented features: [GitHub repository](https://github.com/bhargavamin/contexer)
- Contexer vendor-reported benchmark and limitations: [benchmark.md](https://github.com/bhargavamin/contexer/blob/main/docs/benchmark.md)
- Hu et al., “Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions,” ICLR 2026: [arXiv:2507.05257](https://arxiv.org/abs/2507.05257)
- Debenedetti et al., “AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents,” NeurIPS 2024 Datasets and Benchmarks: [official proceedings abstract](https://proceedings.nips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)
- Liu et al., “Lost in the Middle: How Language Models Use Long Contexts,” TACL 2024: [ACL Anthology](https://aclanthology.org/2024.tacl-1.9/)
