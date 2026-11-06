# Reproducible demo

## Deterministic local re-score

Obtain and extract the pilot bundle from the link in ../README.md. In the extracted bundle root, run:

    PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T03/grader/score.py T03/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T03/grader/score.py T03/condition-b
    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-a
    PYTHONDONTWRITEBYTECODE=1 python3 T04/grader/score.py T04/condition-b

T02-A is expected to exit nonzero because the independent compliance audits detect the recorded failure-safety violations. Treat that as an observed result. Do not change the frozen tests or grader to make it pass.

T04's scorer calls the URL helper only while the four network boundaries are monkeypatched. Do not call the helper outside the scorer's mocks and do not make any live network request.

## Regenerate the charts and classifier output

From the onboarding-contexer root:

    python3 phase-2/charts/plot_results.py
    .venv/bin/python phase-2/dataset/sample_analysis.py

The script regenerates SVGs from phase-2/metrics.csv; it reports per-case checks and completed run counts and does not compute an aggregate effect. The classifier output is unrelated to the A/B agent comparison.

## Reproducing a coding-agent comparison

The saved raw outputs are historical and are not a substitute for new runs. To reproduce a pair, start fresh sessions and clean copies of the frozen task starter, keep the same model/version, tools, prompt, and budget within A/B, and add only the existing AGENTS.md to B. Use the exact graders and task prompts from the pilot bundle. Save the full transcripts, diffs, model/settings, test output, and grader output. Condition C is not currently reproducible as a scored comparison: the isolated T04 decision is pending approval and has no verified delivery receipt. Do not launch C until those two requirements are met.
