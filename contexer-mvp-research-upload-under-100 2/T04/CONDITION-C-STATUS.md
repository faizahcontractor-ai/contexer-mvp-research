# T04 Condition C setup status

**As of 26 October 2026 — setup only; no coding-agent experiment has run.**

The isolated runtime is `condition-c/runtime-home/` and the separate repository is `condition-c/repo/`. The Codex profile authenticated using its isolated `HOME` and `CODEX_HOME`; the isolated config registers the Contexer MCP server and hooks. The common T04 starter is present in the repository, and no B `AGENTS.md` was copied into it.

One decision was created and inspected through the Contexer MCP integration:

- ID: `8aa46b44-c427-4cda-a20e-4b8abb5b70b2`
- Status: `pending_approval`
- `created_by`: `ai`
- Origin: `captured by the assistant`
- Approval provenance: none; it remains pending.
- Stored text matched the frozen Condition B decision exactly.

Exact text:

> For valid absolute HTTP(S) URLs, `normalize_service_url(url: str) -> str` must make no network calls and must only remove exactly one final `/` from the URL path when present. Preserve the scheme and authority exactly, preserve the rest of the path exactly, and leave query and fragment untouched. Do not normalize or trim any other part of the URL. A root path `/` becomes an empty path; multiple trailing path slashes lose only the final one.

The read-only `contexer review --json` check returned one item for the isolated repository and confirmed its pending status. The credential file and local Contexer store are intentionally not included in this submission. To continue, run `contexer review` with `HOME` and `CODEX_HOME` set to the isolated runtime, inspect this ID and the exact wording, and approve only this item. After approval, independently verify the store state and verify that a fresh agent receives the approved decision before any T04 code task is launched.

This setup does not demonstrate Condition C effectiveness: no approved decision was delivered to a coding agent, and no C result exists.
