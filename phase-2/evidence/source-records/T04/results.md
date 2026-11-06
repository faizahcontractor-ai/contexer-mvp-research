# T04 preliminary A/B pilot results

Completed: 26 October 2026. This is one fresh run per condition, a preliminary pilot rather than a conclusive benchmark.

## Comparison

| Measure | A: repository only | B: repository + `AGENTS.md` |
|---|---:|---:|
| Completed coding-agent runs | 1 | 1 |
| Agent process exit | 0 | 0 |
| Separately run functional suite | Pass (exit 0) | Pass (exit 0) |
| Independent scorer | Pass (exit 0) | Pass (exit 0) |
| Frozen URL output checks | 6/6 pass | 6/6 pass |
| Output compliance | Pass | Pass |
| Network compliance | Pass | Pass |
| Intercepted calls to each of the four patched boundaries | 0 | 0 |

Both implementations passed the preregistered checks. This pilot observed no difference in pass/fail outcome. With one run per condition, it cannot establish that project instructions have no effect or improve performance.

## Run controls and integrity

Both real runs used fresh Codex CLI sessions on `gpt-5.6-terra`, high reasoning effort, Codex CLI `0.163.0-alpha.10.2`, the same available tools, the exact same task prompt, and the same default one-turn budget. No explicit token cap was set. Condition B began with the same common starter bytes as A and the frozen project decision in its existing `AGENTS.md`; A had no `AGENTS.md`. The preregistration and grader hashes remained unchanged.

All helper calls in the agent-visible test commands and standalone test/scorer commands occurred inside the four preregistered mocks. The transcripts and scorer outputs show no helper invocation outside those mocks and no live URL request. The agent implementations added extra test inputs locally (three in A and two in B); these additions are retained in each final diff and were not added to the frozen independent scorer or used to alter the six scored examples.

Two A startup attempts failed before task execution: a mutually exclusive CLI flag combination, then an unsupported configured default model. They are documented in `runs/launch-attempts.md` and are not counted as experiment runs. The successful A attempt used the same supported model/settings as B. A standalone test wrapper also hit a zsh reserved-variable issue after the test process ran; the command was rerun and the successful output/exit code were saved.

## Evidence

Per-condition records: `runs/A-run-record.md`, `runs/B-run-record.md`.

For each condition, the directory also contains the raw JSONL transcript, final agent response, final diff against the common starter, standalone functional-test output and exit code, independent grader output and exit code, and agent process exit code. `runs/launch-attempts.md` records pre-run failures transparently.
