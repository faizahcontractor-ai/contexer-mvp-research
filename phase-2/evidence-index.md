# Evidence index

Paths are relative to this phase-2/ directory. Sanitized copies preserve substantive run content while replacing local home paths, email-shaped strings, and session UUIDs. The source lab remains unchanged.

| Claim | Evidence | Location | Confidence |
|---|---|---|---|
| T01 A and B each completed one run and passed 2/2 functional tests and the scoped compliance audit | Saved raw run records and 6 Nov scorer recheck | logs/sanitized/T01/; logs/reverification/T01-A.txt; logs/reverification/T01-B.txt | Low for generality; high for the reproduced fixed checks |
| T01 differs from the current MVP table's JSON-settings task | Current MVP plan versus actual T01 task/run record | audit-table.md; logs/sanitized/T01/ | High for discrepancy |
| T02 both visible suites passed 3/3; A failed both injected failure audits and B passed both | Preregistration, fixture validation, result, A/B records/patches, 6 Nov scorers | evidence/source-records/T02/; logs/sanitized/T02/; logs/reverification/T02-A.txt; logs/reverification/T02-B.txt | High for this fixture/run; low for generalization |
| T03's four frozen acceptance checks passed in A and B | Frozen preregistration, run records, transcripts, patches, results, re-score | evidence/source-records/T03/; logs/sanitized/T03/; logs/reverification/T03-A.txt; logs/reverification/T03-B.txt | High for scored inputs; one run each |
| T04 A/B passed six URL examples and made no calls at four patched boundaries | Frozen preregistration, scorer, transcripts, separate tests/grader outputs, re-score | evidence/source-records/T04/; logs/sanitized/T04/; logs/reverification/T04-A.txt; logs/reverification/T04-B.txt | High for patched fixture; no live-network claim beyond these tests |
| T04 Condition C is not a result | Isolated store metadata: status pending_approval, created_by ai, no approval fields; exact text comparison; no agent-delivery record | condition-c-status.md | High for inspected local state; no conclusion about unobserved later state |
| Sample classifier reproduces 0.940 accuracy on 50 seeded synthetic rows | Script, expected output, and new stdout comparison | dataset/sample_analysis.py; dataset/sample-output.txt; logs/reverification/synthetic-classifier.txt | High for this pinned local environment |
| Contexer vendor benchmark reports equal task accuracy within its own interpretation and other cost/conflict/capture results | Vendor-authored October 2026 benchmark page | final-research-report.md and research-watch/ai-research-watch.csv | Vendor-reported; not independently replicated here |
| No statistical significance or general causal effect can be claimed | One run per condition per task; heterogeneous tasks and settings | all T01–T04 result records; audit-table.md | High |
| Screenshots and voice narration are incomplete | No saved screenshot or video files found in inspected project/lab | screenshots/checklist.md; video/narration-script.md | High for inspected folders |

## Evidence provenance files

The source-records subfolders contain sanitized copies of preregistrations, fixture-validation notes, and result summaries. logs/sanitized/ contains sanitized run records and raw outputs. logs/reverification/ contains the separate re-score outputs generated on 6 November 2026. The public pilot bundle supplies the full starter, condition, test, and grader files; its link is in README.md.

SHA-256 values for original and sanitized text copies are recorded in logs/sanitized/manifest.sha256. Replacing personal paths or session UUIDs changes the sanitized hash but not test outcomes or code diffs.
