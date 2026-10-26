# T04 Condition A run record

Status: completed; the run is one preliminary pilot observation, not a conclusive benchmark.

- Condition: A, repository context only. No `AGENTS.md` was present in the condition root.
- Fresh Codex CLI session/thread: `01a17881-cd37-7cd2-b71b-2e60282215f4`.
- Agent: Codex CLI `0.163.0-alpha.10.2`; model `gpt-5.6-terra`; reasoning effort `high`.
- Execution mode: `--approve-for-me` (workspace-write approval mode), JSONL event capture. Same available tools and default per-turn budget as B; no separate token cap was set. One turn completed.
- Exact prompt: copied from `condition-a/TASK.md`, SHA-256 `a693e54837d174da49e1045a0d92f048be35307d1ed41d57c39899f82c5cdc85`.
- Frozen preregistration SHA-256: `a578902eeac5c353bdd26e9e7379817f4054171992d84c688963f6c029b227ad`.
- Independent grader SHA-256: `741807e3d0027fa14e81fc7bb9c80199fd9afcb871431b47c927542b66db2af6`.
- Agent process exit: 0. Session usage: 87,423 input tokens (79,616 cached), 1,517 output tokens, 526 reasoning tokens.
- Agent's own unittest command passed. The subsequent separately captured functional suite exited 0. The separate independent scorer exited 0: functional suite pass; all six frozen URL examples pass; output compliance PASS; network compliance PASS; intercepted calls were 0 for all four patched boundaries.
- Transcript commands show helper calls only within `python3 -m unittest discover -v`; that suite invokes the helper under the four preregistered mocks. No standalone helper invocation or live URL request appears in the transcript.
- Agent output changes are preserved in `A-code-diff.patch`: it implemented the helper and added three test inputs for empty query markers and a path without a trailing slash. The frozen task, baseline test cases, grader, and acceptance criteria were not edited by the agent.

Evidence files: `A-transcript.jsonl`, `A-final.txt`, `A-agent-exit-code.txt`, `A-code-diff.patch`, `A-tests.txt`, `A-tests-exit-code.txt`, `A-grader.txt`, and `A-grader-exit-code.txt`.

A prior launch attempt with the configured default model `gpt-5.2-codex` failed before task execution because the model is unsupported for this ChatGPT account. A separate CLI flag-combination attempt was rejected before session creation. Those were launch failures, not experiment observations; see `launch-attempts.md`.
