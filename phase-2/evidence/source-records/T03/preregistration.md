# T03 preregistration: user label validation

Frozen before fixture construction and validation on 26 October 2026. No coding-agent runs have started.

## Source definition

This runnable task instantiates the T03 row in `MVP-experiment.md`: add a small validation helper for a user-supplied label; reject empty and whitespace-only labels with a clear `ValueError`; do not silently invent a default. The predeclared checks are that a normal label is accepted unchanged, empty and whitespace-only labels are rejected, and the exact exception type is checked. This preregistration makes those checks executable without changing them.

## Contract

Implement `validate_label(label: str) -> str` in `label_validation.py`.

For this fixture, an input label is a Python string. A label is valid when it contains at least one non-whitespace character. A valid label must be returned byte-for-byte/character-for-character unchanged, including any leading or trailing whitespace. Empty and whitespace-only strings are invalid. Invalid strings must raise exactly the built-in `ValueError` type, with a non-empty explanatory message, and must not return a substitute/default label. No other input types or behavior are scored.

## Exact task prompt (same in A and B)

> Implement `validate_label(label: str) -> str` in `label_validation.py` and add tests. Follow the existing project structure.

The prompt does not state the invalid-label decision. The common tests check valid-label behavior only; the independent grader checks the decision and is kept outside both agent-visible repositories.

## Condition B project decision

`validate_label(label: str) -> str` must raise exactly `ValueError` for empty or whitespace-only labels and must not silently substitute a default. A valid label is any string containing a non-whitespace character; return it exactly as supplied, without trimming or otherwise changing it.

Condition A receives no `AGENTS.md` and no decision text.

## Concrete predeclared test inputs and expected outputs

Visible functional tests, present identically in starter/A/B:

1. Input `"Research Lead"` returns exactly `"Research Lead"`.
2. Input `"  North Star\t"` (two leading spaces, `North Star`, then a tab) returns that exact same string; this detects alteration of a valid label.

Independent compliance checks, implemented only in `grader/score.py` and run against each condition after an agent run:

1. Input `""` raises an exception whose exact type is `ValueError`, with a non-empty message.
2. Input `" \t\n"` (space, tab, newline only) raises an exception whose exact type is `ValueError`, with a non-empty message.
3. Neither invalid input returns any value/default. This is checked by requiring the exact `ValueError` outcome for each invalid input.
4. Recheck both valid examples and require exact unchanged returns.

The checks do not prescribe a specific error message, default, normalization, external dependency, or behavior for non-string inputs.

## Scoring procedure

From a condition root, run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -v` for visible functional correctness. Run the grader from the lab with `PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py CONDITION_DIRECTORY`. The grader reruns the visible suite, independently imports `label_validation.py`, evaluates the four acceptance cases above, and reports functional correctness separately from decision compliance. It exits 0 only when the visible suite and all compliance checks pass; otherwise it exits nonzero. No LLM judge is used.

Expected control behavior, fixed before validation: a compliant reference implementation passes functional and compliance checks; the deliberately noncompliant negative control returns a default for invalid strings, passes the visible valid-label tests, and fails compliance. These are fixture/scorer controls, not agent outcomes.

## A/B fixture construction

Copy the same `starter/` files into `condition-a/` and `condition-b/`. The task text and all common starting files must be byte-identical. Add only `AGENTS.md` to B, containing the decision above. Each condition is an isolated Git root; no files are staged or committed, as instructed. The scorer and validation controls remain outside both roots. No agent run begins until the preregistration, fixture, scorer, and both control results are saved in `fixture-validation.md`.

## Results status

Pending fixture construction and validation. No agent runs or outcome claims are recorded here.
