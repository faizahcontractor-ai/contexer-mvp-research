# Existing-work audit

Audited 6 November 2026. Sources inspected: onboarding-contexer/README.md and MVP-experiment.md; the lab README, run protocol, codebase flow, T01–T04 preregistrations, fixture-validation records, result summaries, run records, patches, transcripts, scorers, and the isolated T04 Contexer decision metadata. The parent Git status and history were inspected read-only.

| Requirement | Existing evidence | Status | Missing work |
|---|---|---|---|
| Reuse original onboarding work | Pinned requirements, sample_analysis.py, sample output, isolated Contexer CLI evidence, local toy Git repo, original README and MVP plan | Reused; classifier rerun matched archived output | Existing installation evidence is historical and machine-specific; only sanitized excerpts are retained here |
| Runnable synthetic code comparison | T01–T04 starter fixtures, tests, graders, A/B outputs | Four task pairs exist; deterministic graders were rerun on 6 Nov | No replicated trials; T01's actual task does not match the T01 row in the current MVP table |
| Five concrete cases | T01 shared-client case; T02 partial-write and replace-failure cases; T03 label validation; T04 URL/no-network | Five scored outcome slices reviewed across four task pairs | T02's two failure checks are not independent agent runs |
| Condition A | Per-task repository-only fixtures and saved results | One completed run per task | Small sample, task-specific configurations |
| Condition B | Per-task AGENTS.md fixtures and saved results | One completed run per task | Small sample; token/time budget fields are missing for T01–T03 |
| Condition C | Isolated T04 Codex config and repo; one Contexer store entry matching the body of T04 B's decision | Setup exists; store status is pending_approval | Approval and approval provenance; proof of retrieval to a fresh agent; scored C run |
| Baseline/Contexer three-way comparison | No scored C run | Not measured | Complete approved C run under comparable T04 settings |
| Synthetic classifier smoke run | sample_analysis.py, pinned requirements, archived sample-output.txt | Reproduced exactly: 0.940 accuracy on 50 synthetic test rows | This is not a comparison of A/B/C and not evidence of Contexer impact |
| Research memo/report | New Phase 2 files | Prepared from saved evidence and cited sources | Mentor review is not recorded |
| Metrics and charts | metrics.csv, script, SVG charts | Generated from saved scorer outputs | No justified aggregate performance estimate |
| Sanitized raw logs | Copies under logs/sanitized with transformation manifest | Prepared; local source files are unchanged | Public release of Phase 2 package still needs upload |
| Screenshots | No saved benchmark screenshots found | Outstanding; checklist prepared | Capture manually from genuine runs/results |
| Narrated video | No recording found | Outstanding; script and shot list prepared | Record and review manually |
| Public package | Public repository has an earlier pilot bundle nested under a folder with a duplicated “2” suffix | Existing A/B package is public; Phase 2 is not yet published | Upload the phase-2/ directory; correct the nested presentation later if desired |
| Git state/history | onboarding-contexer resolves to the parent “New project” repository; it has no separate Git history. The toy-repo has its own three-commit history. Parent status contains pre-existing deletions and unrelated untracked files. | Preserved; no stage or commit performed | Create a separate repository root only if future project workflow needs it |

## Discrepancies and interpretation

The current MVP-experiment.md table defines its first task as JSON settings updates using the standard library. The saved T01 pilot instead implements a profile fetcher through shared_client.py. The T01 run protocol and raw evidence support the profile-fetch observation, but the current plan does not preregister that as T01. The report therefore labels it an exploratory pilot and does not treat it as a faithful execution of the current T01 table row.

The README and several run documents were written at different stages. Earlier statements that T03–T04 had not run are superseded by the later T03/T04 result records, which each document one A and one B run. This does not alter their frozen task checks.

The lab's T04 fixture-validation note says “no agent run has started” in the pre-run section; later T04 run records and T04-RESULTS.md document the subsequent A/B runs. The section is retained as historical fixture validation, not current run status.

The Phase 2 package leaves all prior results and frozen checks unchanged. Re-scoring on 6 November is recorded separately under logs/reverification/.

## Final Phase 2 checklist

| Requirement | Status | Evidence / remaining action |
|---|---|---|
| At least five concrete outcome cases reviewed | PASS | Five outcome slices across four A/B task pairs; the two T02 failure checks are explicitly not counted as separate agent runs. |
| Failure cases included | PASS | T02-A failed both injected failure-safety audits; operational T04 launch failures are preserved. |
| Every case traceable to run evidence | PASS | See evidence-index.md and sanitized run records; T02 subcases point to the same A/B runs. |
| A/B/C definitions and fairness documented | PARTIAL | A/B paired within task; C has no run, so no three-way empirical comparison. T01–T03 lack explicit comparable budgets; T04 settings are documented. |
| Baseline-equivalent cases identified | PASS | A matched B on T01, T03, and T04's scored checks. This does not establish equality with Contexer. |
| Baseline better than Contexer / Contexer better than baseline identified | NOT MEASURED | No scored C result; neither direction can be claimed. |
| Small-dataset limitations documented | PASS | See report section 8; no significance or general causal inference. |
| Founder memo and evidence-backed versus hypothetical recommendations | PASS | research-memo.md separates observed findings from hypotheses. |
| Compact AI research watch | PASS | Four relevant sources with caveats and proposed tests. |
| Dataset, script, environment files | PASS | Synthetic classifier source/output and pinned direct/full dependency files included. The classifier is not agent evidence. |
| Metrics CSV and regenerable charts | PASS | metrics.csv; charts/plot_results.py and two validated SVGs. No pooled performance estimate. |
| Sanitized raw logs | PASS | 44 source records copied with transformation hashes; no runtime credentials or local store copied. Automated string scan found no local home paths, email-shaped strings, or credential assignments in the Phase 2 tree. |
| Screenshots | OUTSTANDING | Genuine captures must be made manually using screenshots/checklist.md. |
| Narrated video | OUTSTANDING | video/narration-script.md is a script only; recording is not complete. |
| Final report and reproducible demo | PASS | final-research-report.md and demo/README.md; demo includes the T04 mock-only restriction. |
| Public Phase 2 publication | OUTSTANDING | Earlier A/B bundle is public; the 75-file Phase 2 folder and archive are ready locally. GitHub integration returned HTTP 403 “Resource not accessible by integration” on the additive tree write, so no remote files or commits changed. Upload the local archive manually. |
| No fabricated evidence or unsupported claims | PASS | C, screenshots, recording, significance, and mentor review are marked missing/not measured. |
| No secrets/private runtime state included | PASS | Sanitized log set and final tree scan; isolated runtime store and credentials excluded. |
