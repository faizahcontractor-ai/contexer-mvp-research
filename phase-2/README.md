# Contexer extended research — Phase 2

Status date: 6 November 2026. This package extends the existing onboarding research; it does not replace the earlier MVP plan or raw records.

## What this package establishes

The saved synthetic lab has four completed A/B pilot task pairs: one run per condition for T01–T04. The evidence was independently re-scored on 6 November 2026. The only observed A/B difference is T02: both agents passed the visible functional tests, but A failed both frozen failure-safety audits while B passed them. T01, T03, and T04 passed the scored checks in both A and B. These eight runs are exploratory observations, not a powered study.

The T04 Contexer decision is pending_approval. No approval provenance or coding-agent delivery record exists, so C has no outcome and is not compared as if it had run.

The package reviews five concrete outcome slices across four task pairs. T02's partial-write and replacement-failure checks are separate preregistered failure cases, not independent agent runs.

## Conditions

- A — repository context and task only.
- B — the same task and starter plus its project decision in AGENTS.md.
- C — the T04 task with the corresponding decision delivered through the isolated Contexer/Codex setup. The decision is still pending approval; no scored C run exists.

The task-specific model and agent settings are recorded in the report. T01–T03 used Codex with gpt-6-luna at medium reasoning; T04 used Codex CLI 0.163.0-alpha.10.2 with gpt-5.6-terra at high reasoning. Results are compared only within each task. No cross-task aggregate is reported.

## Package map

- research-memo.md — concise founder-facing memo.
- final-research-report.md — methods, case review, conclusions, limitations, and next experiment.
- audit-table.md — existing-evidence audit and discrepancies.
- metrics.csv — traceable task and case-level measurements.
- charts/ — two per-case SVG charts and the script that regenerates them.
- research-watch/ai-research-watch.csv — compact primary-source research watch.
- evidence/source-records/ — sanitized copies of preregistration, fixture-validation, and result documents.
- logs/sanitized/ — sanitized run records, diffs, transcripts, launch attempts, and output evidence.
- logs/reverification/ — outputs from the offline deterministic re-scoring performed on 6 November 2026.
- dataset/ and environment/ — seeded synthetic classifier source, expected output, and pinned requirements.
- screenshots/checklist.md and video/narration-script.md — required manual evidence that was not captured.
- demo/README.md — reproducible commands for the saved A/B fixtures.

The previously uploaded public pilot bundle contains the full T01–T04 runnable fixtures, graders, controls, and result records. It is currently nested in the repository at [the pilot bundle directory](https://github.com/faizahcontractor-ai/contexer-mvp-research/tree/main/contexer-mvp-research-upload-under-100%202). Upload this Phase 2 material as a sibling phase-2/ directory. Local Contexer runtime state and credentials are not included.

The current Phase 2 package contains 76 deliverable files; a clean archive can exclude two macOS .DS_Store metadata files. Publication was attempted through the connected GitHub integration, but its Git Trees and file-content writes returned HTTP 403 (“Resource not accessible by integration”); no remote files or commits were changed. Public release remains outstanding. The local archive can be uploaded manually.

## Reproduce the deterministic analysis

From the root of the onboarding-contexer repository:

    python3 phase-2/charts/plot_results.py

This regenerates the per-case SVGs from phase-2/metrics.csv. It does not call an AI service or a network.

For the historical A/B scorers, use a local clone of the public pilot bundle. From the extracted pilot-bundle directory:

    PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T03/grader/score.py T03/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T03/grader/score.py T03/condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-b

T04's scorer exercises URL helpers only while the preregistered network boundaries are monkeypatched. Do not call the helper outside those mocks, and do not make a live network request. Scorer exit 1 for T02-A is the expected recorded compliance failure, not a broken reproduction.

The synthetic classifier uses pandas 2.2.3 and scikit-learn 1.6.1. See environment/README.md. It is a toolchain smoke test, not a Contexer outcome.

## Status limits

Condition C, screenshots, and video recording are incomplete. The report does not claim a baseline-versus-Contexer result, statistical significance, or that the MVP deadline was met. See audit-table.md and final-research-report.md for the complete status.

No genuine screenshot or video files are included. Capture screenshots manually from real benchmark commands using screenshots/checklist.md, and record the narrated evaluation using video/narration-script.md. Do not treat the checklist or script as completed media evidence. See PHASE-2-SUBMISSION-STATUS.md for the deadline checklist and final readiness status.
