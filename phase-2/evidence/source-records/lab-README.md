# Contexer MVP lab

This isolated folder contains the first runnable T01 comparison. It is separate from the existing onboarding workspace.

- `starter/`: unchanged initial fixture
- `condition-a/`: repository-only agent output
- `condition-b/`: same fixture plus `AGENTS.md`, then agent output
- `grader/score.py`: independent functional and AST compliance scorer, kept outside agent-visible copies
- `runs/`: fresh-session prompts, diffs, commands, and raw test output
- `results/T01-results.md`: measurements, limitations, and deviations
- `RUN-PROTOCOL.md`: reproduction instructions

Both conditions passed the two functional tests and the independent compliance audit. This is one task and one run per condition; it is an exploratory pilot, not evidence of a general instruction-file effect. Contexer condition C, screenshots, and narration remain outstanding.
