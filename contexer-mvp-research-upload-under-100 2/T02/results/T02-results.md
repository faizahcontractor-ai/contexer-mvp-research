# T02 A/B result record

## Verified outcome

| Measure | A — repository only | B — `AGENTS.md` decision |
|---|---:|---:|
| Completed agent runs | 1 | 1 |
| Visible functional tests | 3/3 passed | 3/3 passed |
| Injected partial-write failure audit | FAIL | PASS |
| Injected replacement-failure audit | FAIL | PASS |
| Independent scorer exit | 1 (functional passed; compliance failed) | 0 |

A implemented a direct truncating write. Its functional tests passed, but the scorer verified that it did not use an intercepted temporary-file write or replacement path; the prior destination changed under both injected failures. B used a sibling `NamedTemporaryFile`, `os.replace`, and cleanup, passing both failure-injection checks. These are observations from one run per condition, not evidence of statistical significance or a general causal effect.

## Comparability and provenance

Both runs used fresh projectless Codex sessions on the local host, requested model `gpt-6-luna`, reasoning effort `medium`, the same generic session prompt and byte-identical `TASK.md`; the only condition difference was that B's repository included `AGENTS.md` with the preregistered decision. Each worked inside its own Git root. No explicit token/time budget was set, and consumed-token metadata was unavailable. Agent run records and exact code diffs are in `runs/condition-a.md`, `runs/condition-b.md`, and their corresponding `.patch` files. Session IDs link to the full tool transcripts.

## Limitations

- One run per condition; no repeatability estimate or statistical inference.
- The two conditions were run concurrently, and no explicit token/time cap was configured.
- No blinded evaluation; the scorer was deterministic and independent of agent-visible files.
- This compares repository-only context with a project instruction file. It does not test Contexer condition C.
- Screenshots and narrated demonstration remain outstanding.
