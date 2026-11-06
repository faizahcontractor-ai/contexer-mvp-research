# T01 pilot results

Date: 26 October 2026. This is one exploratory run per condition, not a replicated study.

## Question

Does project guidance that says to use the shared HTTP helper change whether a coding agent uses it when implementing a profile fetcher?

## Conditions

- A: repository-only task context, no instruction file.
- B: same task and starter files, plus `AGENTS.md` with the predeclared decision.
- Both used fresh local Codex threads, `gpt-6-luna`, medium reasoning, and the same task wording. Each started from its own copy of `starter/`; the copies differed only by B's `AGENTS.md` before the run.
- A ran 17:29:11–17:29:45; B ran 17:29:16–17:29:55 (Asia/Kolkata). Thread IDs and run records are in `runs/`.

## Predeclared checks and outcomes

| Check | Condition A | Condition B |
|---|---:|---:|
| Functional suite (`unittest`, two tests) | 2/2 passed | 2/2 passed |
| Uses imported shared client and calls `get_json` | Pass | Pass |
| No direct HTTP module/call detected in `profile.py` | Pass | Pass |
| Overall decision compliance | Pass | Pass |

The independent scorer was run after both agent sessions. Its output was `functional_exit_code=0` and `decision_compliance=PASS` for each. The scorer was validated against two separate reference implementations: a shared-client reference passed both checks; a direct `urllib.request` implementation passed functional tests but failed the compliance audit. Thus the policy result is not inferred from the agent's own claim.

A and B reached the same decision-compliance outcome. The small single-task result does not show an instruction-file benefit. A followed the repository evidence and used `shared_client` even without `AGENTS.md`. A also URL-encodes the user ID; B does not. The task's executable case uses `u-123`, so both produce the expected path. Identifier escaping was not a predeclared check.

## Deviations and limitations

- The app's initial default `gpt-5.2-codex` selection was unsupported for this ChatGPT account. Both threads failed before any coding; they were retried in the same two threads with `gpt-6-luna` at medium reasoning. Only the successful retry counts as the run.
- The fixture tests mock `urllib.request.urlopen`; no external network call is made. They verify a fixed user ID and helper auth/retry behavior, not malformed IDs, URL encoding, failure propagation, or service edge cases.
- The hidden compliance scorer is a small AST audit scoped to `profile.py`; it can miss indirect or aliased network calls. It is an independent deterministic check, not a general security analyzer.
- `README.md` tells agents that `shared_client.py` exists and provides auth/retries. Condition A therefore tests whether repository evidence is enough, while B adds an explicit mandate; it is not a no-information baseline.
- Each condition has only one run. Model sampling variation cannot be estimated, and no token/cost data was exposed. The measured durations are wall-clock turn durations, not just coding time.
- The condition directories did not initially have their own `.git` repositories. Both agents ran read-only `git status` commands that walked into a parent repository and listed paths in the home directory. No files were changed. Future runs should have isolated Git roots and should not run Git commands outside them.
- This pilot tests project instructions, not Contexer. No Contexer condition was run because the local CLI trial had no agent integration or approved decision.
- Screenshots and a narrated demonstration remain outstanding.

## Reproduction

From each condition folder, run:

```sh
python3 -m unittest discover -v
python3 ../grader/score.py .
```

The original starter remains unchanged in `starter/`. The two scored outputs are in `condition-a/` and `condition-b/`.
