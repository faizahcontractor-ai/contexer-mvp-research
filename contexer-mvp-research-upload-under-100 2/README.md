# Contexer MVP research pilot

This repository contains the preregistered fixtures, A/B pilot records, raw run artifacts, and a consolidated report for a small synthetic study of coding-agent compliance with engineering decisions.

## Current status — 26 October 2026

- T01–T04 each have one completed repository-only run (A) and one completed project-instruction run (B). These are preliminary pilots, not a powered or conclusive benchmark.
- T02 is the only task with different A/B outcomes on a preregistered compliance audit. A failed both atomic-failure checks; B passed both.
- T01, T03, and T04 passed their preregistered checks in both conditions.
- No Condition C coding-agent run has taken place. The isolated T04 Contexer decision exists with status `pending_approval`; it has not been approved or shown to a coding agent.
- Screenshots and a narrated demonstration remain outstanding. The original milestone date, 23 October 2026, preceded the preparation of the later pilot records.

Read [REPORT.md](REPORT.md) for the research question, methods, evidence, findings, limitations, and conclusions. See each task's preregistration, fixture validation, results, and `runs/` directory for its underlying evidence.

## Repository contents

- `T01/`–`T04/`: frozen task definitions, A/B fixtures, deterministic graders, controls, run records, diffs, test outputs, and transcripts where saved.
- `RUN-PROTOCOL.md`: common run principles.
- `planning/`: copies of the original onboarding plan and README. Their earlier status statements are retained as provenance; the consolidated report reflects the later T03/T04 records.
- `T04/CONDITION-C-STATUS.md`: current isolated Condition C preparation and approval state.

The isolated Codex runtime, authentication file, local Contexer store database, and nested `.git` directories are intentionally excluded. They contain local credentials/runtime state and are not needed to reproduce the synthetic A/B scoring. Condition C's pending decision text and ID are documented without uploading the local store.

## Reproduction

Each task directory contains its preregistration and scorer. Follow that task's documented command and mock requirements. In particular, T04's helper must only be exercised through the preregistered network mocks; no live network request is needed or permitted.

The results are observations from saved one-run-per-condition pilots. Do not treat the reports or agent responses as ground truth: use the frozen tests, independent graders, and raw records.
