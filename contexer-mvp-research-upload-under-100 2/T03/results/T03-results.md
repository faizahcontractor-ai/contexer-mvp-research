# T03 preliminary A/B result

## Results

| Measure | A — repository only | B — `AGENTS.md` |
|---|---:|---:|
| Completed runs | 1 | 1 |
| Agent-reported functional tests | 5/5 passed | 4/4 passed |
| Independent grader functional suite | Passed (5 tests) | Passed (4 tests) |
| Valid-label unchanged checks | Pass | Pass |
| Empty exact-`ValueError` check | Pass | Pass |
| Whitespace-only exact-`ValueError` check | Pass | Pass |
| Overall decision compliance | Pass | Pass |
| Independent grader exit code | 0 | 0 |

Both implementations passed all preregistered checks. A added a TypeError check for non-string input, which is outside the preregistered scored inputs. B added Unicode whitespace coverage beyond the specified concrete case. Neither extension changes the frozen scoring checks. A's and B's agent-written test counts differ; the independent scorer applies the same frozen checks to both.

## Comparability and limitations

Both sessions were fresh local Codex sessions requesting `gpt-6-luna` with medium reasoning effort, the same session prompt apart from repository path, and the same available tools. The sessions ran concurrently. No explicit token/time cap was set and token use is unavailable. Each condition is its own Git root; common starting files were hash-identical. No commit was created or files staged, following the explicit instruction for this work. This is one run per condition, so it is a preliminary pilot only; no causal or statistical conclusion is supported.

No Contexer Condition C was tested. Raw full session transcripts, code diffs, and per-condition scoring outputs are in `runs/`.

## Evidence provenance

- Frozen preregistration: `T03-PREREGISTRATION.md`; SHA-256 `cdf5748bf394519c084807f1aa37f8f5feb29f9d17a26195814aead0a7991fa8`.
- Fixture/control validation before runs: `fixture-validation.md`.
- Agent session IDs: A `01a17850-2e56-7e41-8a73-c00dbdda0115`; B `01a17850-2479-7e53-a262-85f79754a7d9`.

