# Phase 2 Submission Status — 6 November 2026

## Completed

- Audited the existing onboarding project, lab structure, preregistrations, fixtures, result records, transcripts, diffs, scorers, Condition C store status, and Git state. Historical files and experiment results were not changed.
- Reviewed five concrete scored outcome slices across four task pairs. The two T02 failure checks are separate scoring cases from the same A/B runs, not additional agent runs.
- Verified four completed A/B task pairs: one successful A and one successful B run for T01, T02, T03, and T04 (eight completed agent runs total).
- Re-ran the saved deterministic A/B scorers on 6 November. Outputs are in logs/reverification/. T04 scoring remained within its preregistered monkeypatches; no live network request was made.
- Re-ran the seeded synthetic classifier in the pinned environment. Its stdout exactly matched the saved output: 0.940 accuracy, 47/50 test rows correct, and confusion matrix [[24, 1], [2, 23]]. This is a classifier smoke test, not agent or Contexer evidence.
- Prepared the founder memo, final research report, evidence index, audit table, metrics CSV, chart generator and SVGs, sanitized run records with SHA-256 manifest, compact research watch, dataset and environment files, and reproducible demo instructions.
- Prepared the screenshot checklist and narrated-video script. These are instructions, not captured media.
- Updated the parent README and MVP plan with dated status notes that preserve their earlier text and clarify what later T01–T04 records supersede.

## Partial

- **A/B/C comparison:** A/B observations are documented within each task. C was not scored, so no three-condition empirical comparison exists.
- **Baseline comparison:** A matched B on the scored T01, T03, and T04 outcomes; A failed two T02 failure-safety audits that B passed. Since C has no result, no baseline-versus-Contexer comparison can be made.
- **Fairness across the full set:** Comparisons are within-task. T01–T03 and T04 used different model/CLI settings; T01–T03 lack explicit comparable token/time budgets. These limitations are recorded in the report.
- **Public GitHub release:** The Phase 2 package is prepared locally, but the connected GitHub integration rejected both attempted write methods with HTTP 403 (“Resource not accessible by integration”). No Phase 2 files or commits were added remotely.

## Outstanding Manual Actions

- Capture genuine screenshots of the actual scorer runs, meaningful T02 failure, A/B contrast, metrics, and reproduction demo. Follow screenshots/checklist.md; it is not evidence of completed captures.
- Record the narrated evaluation and failure investigation using video/narration-script.md. No video has been recorded.
- Upload/publish the Phase 2 folder to the public GitHub repository. Publication remains outstanding.
- Obtain mentor review; no review is recorded.
- Condition C remains unmeasured. Its T04 decision is pending approval with no approval provenance or delivery receipt. Do not count setup as a run. A C run would require human approval and verified delivery before coding.

## Key Findings

- **T01:** A and B each passed 2/2 functional tests and the scoped shared-client compliance audit. The saved profile-fetch task differs from the current MVP table's JSON-settings task, so T01 remains exploratory relative to that plan.
- **T02:** A and B each passed 3/3 visible functional tests. A failed both the injected partial-write and replacement-failure safety audits; B passed both.
- **T03:** A and B passed all four frozen acceptance checks for unchanged valid labels and exact ValueError behavior on empty and whitespace-only labels.
- **T04:** A and B each passed six frozen URL output examples and recorded zero calls at each of four monkeypatched network boundaries.
- In this one-run-per-condition pilot, the only observed A/B difference was T02. B is the static AGENTS.md instruction condition; it is not Contexer.

### Quantitative evidence trace

| Quantity reported | Trace |
|---|---|
| Eight completed agent runs; one A and one B for T01–T04 | Individual run records under logs/sanitized/T01–T04/ and source results under evidence/source-records/T01–T04/ |
| T01 2/2 tests and compliance pass | logs/reverification/T01-A.txt and T01-B.txt |
| T02 3/3 visible tests each; A fails two audits, B passes both | logs/reverification/T02-A.txt and T02-B.txt; T02 preregistration and results under evidence/source-records/T02/ |
| T03 four frozen acceptance checks pass in both conditions | logs/reverification/T03-A.txt and T03-B.txt; T03 preregistration under evidence/source-records/T03/ |
| T04 six examples pass and each of four patched boundaries records zero calls in A and B | logs/reverification/T04-A.txt and T04-B.txt; frozen T04 preregistration under evidence/source-records/T04/ |
| Classifier accuracy 0.940, 50 test rows, 47 correct, confusion matrix [[24,1],[2,23]] | dataset/sample_analysis.py, dataset/sample-output.txt, and logs/reverification/synthetic-classifier.txt |
| One C run-count value of zero | condition-c-status.md: decision is pending_approval, no delivery proof, no scored run. This zero is only a run count, not a C performance score. |

External benchmark/paper quantities in the report and research watch are attributed to their cited public sources; they are not T01–T04 measurements.

## Deadline Checklist

| # | Requirement | Status | Evidence / note |
|---:|---|---|---|
| 1 | Five concrete cases reviewed | PASS | Five outcome slices across four task pairs; the T02 subcases share the same runs. |
| 2 | Failure case included | PASS | T02-A failed both frozen injected failure-safety audits. |
| 3 | A/B comparison | PASS | One completed A and B run per task, with within-task settings and outcomes reported. |
| 4 | C condition | OUTSTANDING | No approved decision delivery and no scored C run. |
| 5 | Baseline comparison | PARTIAL | A/B only; no Contexer comparison is possible without C. |
| 6 | Small-dataset limitations | PASS | Explicitly documented; no general/statistical conclusion. |
| 7 | Founder memo | PASS | research-memo.md. |
| 8 | Evidence-backed recommendations | PASS | Separated from experimental hypotheses in the memo/report. |
| 9 | AI research watch | PASS | Compact, linked watch with caveats and proposed tests. |
| 10 | Dataset | PASS | Seeded synthetic classifier script and saved output; not agent evidence. |
| 11 | Python/reproduction scripts | PASS | Classifier and chart generator included; experiment commands documented. |
| 12 | Environment files | PASS | Pinned direct requirements and full lock included. |
| 13 | Metrics CSV | PASS | Traceable 39-row machine-readable CSV. |
| 14 | Comparison charts | PASS | Two SVG charts and regenerating source; no pooled effect. |
| 15 | Sanitized logs | PASS | Sanitized run evidence, re-score outputs, and validated hash manifest. |
| 16 | Screenshots | OUTSTANDING | No genuine image captures are present; manual checklist provided. |
| 17 | Narrated video | OUTSTANDING | No recording is present; narration script provided. |
| 18 | Final research report | PASS | final-research-report.md. |
| 19 | Reproducible demo | PASS | demo/README.md and exact T02/T04 commands in this status file. |
| 20 | Public GitHub publication | OUTSTANDING | GitHub integration write returned 403; manual upload remains necessary. |

## Limitations

Condition C has no scored run. The T04 decision remains pending_approval and there is no verified delivery receipt to a fresh agent. The dataset is four synthetic task pairs, one A/B run each, with five outcome slices; it is too small and heterogeneous for general statistical conclusions, significance claims, or claims of overall superiority. T01 also differs from its current plan row. The classifier's 0.940 result is not Contexer or coding-agent evidence.

## Reproduction

From the extracted public pilot-bundle root, reproduce the key T02 audits:

    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-b

The first command is expected to exit nonzero because the frozen A implementation fails both compliance audits.

Reproduce the frozen T04 outputs and mocked no-network audit:

    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-b

The T04 grader runs the functional suite and independent checks using the preregistered mocks. Do not invoke the helper outside those mocks or make live network requests. See demo/README.md for the full A/B re-score commands and local classifier/chart reproduction.

## Final Status

**READY WITH MANUAL ITEMS**

The evidence-based research package is prepared. Genuine screenshots, video recording, GitHub publication, and mentor review remain manual items. Condition C is explicitly unmeasured and is not represented as a completed experiment.
