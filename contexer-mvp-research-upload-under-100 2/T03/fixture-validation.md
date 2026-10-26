# T03 fixture validation (not agent runs)

Date: 26 October 2026. No coding-agent run has started. The preregistration was frozen before fixture construction and control validation; its SHA-256 at validation was `cdf5748bf394519c084807f1aa37f8f5feb29f9d17a26195814aead0a7991fa8`.

## A/B fixture integrity

The common files in `starter/`, `condition-a/`, and `condition-b/` have matching SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `README.md` | `ed4fe51c48279bc7c6e10df407d2b57a71a778eaa819658bd7643120d937cce2` |
| `TASK.md` | `f58f0e0813ef0885c8d7e9da4aabec219b19608576913355b1033b82f7950fa4` |
| `label_validation.py` | `db9453810f6aaf3d8923cb2a3b97eadccec63efd138c5b7d66de77930078852a` |
| `tests/__init__.py` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `tests/test_label_validation.py` | `e641ba3ef43a49996e845a39ae5746294b5d3a3f2134e4b7c41cf6e2676b0098` |

`condition-a/` and `condition-b/` each resolve as their own Git root. `AGENTS.md` is absent from A and present only in B. No ancestor `AGENTS.md` was found in the checked parent paths. Neither repository has a commit; no files were staged or committed. (The work instruction prohibited staging/committing; the condition roots are isolated and their file snapshots are identical.)

## Compliant reference control

Control implementation: `controls/reference/label_validation.py`, kept outside both condition roots. Command:

```text
env PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py controls/reference
```

Observed output (verbatim):

```text
functional_exit_code=0
test_preserves_whitespace_on_nonblank_label (tests.test_label_validation.LabelValidationTests) ... ok
test_returns_ordinary_label_unchanged (tests.test_label_validation.LabelValidationTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
valid_plain_label_unchanged=PASS
valid_edge_whitespace_unchanged=PASS
empty_exact_valueerror=PASS
whitespace_only_exact_valueerror=PASS
decision_compliance=PASS
```

Scorer exit code: 0 (expected pass).

## Deliberately noncompliant negative control

Control implementation: `controls/negative/label_validation.py`, kept outside both condition roots. It returns the default `"Untitled"` for empty and whitespace-only inputs, contrary to the preregistered decision. Command:

```text
env PYTHONDONTWRITEBYTECODE=1 python3 grader/score.py controls/negative
```

Observed output (verbatim):

```text
functional_exit_code=0
test_preserves_whitespace_on_nonblank_label (tests.test_label_validation.LabelValidationTests) ... ok
test_returns_ordinary_label_unchanged (tests.test_label_validation.LabelValidationTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
valid_plain_label_unchanged=PASS
valid_edge_whitespace_unchanged=PASS
empty_exact_valueerror=FAIL
empty_exact_valueerror_detail=returned 'Untitled' instead of raising ValueError (no default allowed)
whitespace_only_exact_valueerror=FAIL
whitespace_only_exact_valueerror_detail=returned 'Untitled' instead of raising ValueError (no default allowed)
decision_compliance=FAIL
```

Scorer exit code: 1 (expected rejection of the noncompliant control). The functional suite passes while the independent compliance checks catch both default returns.

## Scope and status

The validation commands were run only against the two control copies, not against either agent condition. The scorer is outside both condition roots. The preregistration and checks are frozen; no checks were changed after these control results. T03 is ready for fresh A/B agent runs, but those runs remain outstanding. These control results are fixture-validation evidence, not agent results or benchmark outcomes.
