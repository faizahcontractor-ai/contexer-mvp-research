# Contexer MVP experiment report

**Report date:** 26 October 2026

**Study status:** Four preliminary A/B task pilots complete; Condition C not run; milestone evidence package incomplete.

## Executive summary

This study asks whether a project instruction file carrying a predeclared engineering decision changes a coding agent's compliance and task correctness compared with repository context alone. Four small, synthetic Python tasks were preregistered and evaluated with executable tests and deterministic independent graders. Each task has one run in each A/B condition, so there are four observed runs per condition across four different tasks, but only one observation per condition for any individual task.

The results are mixed. Both conditions passed T01's functional and shared-client checks, T03's label checks, and T04's URL-output and mocked-network checks. On T02, both passed the three visible functional tests, while A failed both injected atomic-write failure audits and B passed both. This is a task-specific pilot observation; it does not establish a general or causal effect. No statistical significance is claimed.

Condition C is not an outcome in this study. A separate, isolated T04 Contexer store contains one decision with ID `8aa46b44-c427-4cda-a20e-4b8abb5b70b2`, status `pending_approval`. It was not approved and has not been delivered to a coding-agent run. Screenshots and narrated demonstration are also outstanding.

## Research questions

**Primary A/B question:** On small, deterministic engineering tasks in a synthetic Python repository, does giving a coding agent an approved project decision in `AGENTS.md` improve compliance with that decision compared with repository context alone, without reducing task correctness?

**Planned Contexer extension:** When a comparable agent integration is available, does a stored, approved Contexer decision produce comparable or better compliance than the project instruction file, when surfaced to the same coding agent with otherwise comparable settings?

The current A/B runs compare repository context with a project instruction file. They do not test Contexer’s decision lifecycle, retrieval quality, or opt-in Git guard.

## Background and public functionality review

Contexer's public project describes recording engineering decisions with approval/history and supplying relevant guidance to coding agents. It also describes an opt-in commit guard. Its October 2026 benchmark reports 1,242 sessions on 38 synthetic coding tasks in one repository. At 150 rules it reports 109/114 correct tasks for Contexer and 108/114 for both a full `CLAUDE.md` and decision documents. It reports $0.076 per session for Contexer versus $0.109 for `CLAUDE.md`, and records that a newly stated rule was captured for the next session in 6/24 Contexer runs versus 24/24 with a maintained `CLAUDE.md`. These are vendor-reported findings, not an independent replication and not results of this MVP. The benchmark is motivation for testing retrieval and compliance on a separate fixture, not evidence for this pilot's outcome.

MemoryAgentBench evaluates accurate retrieval, test-time learning, long-range understanding, and selective forgetting in incremental multi-turn interactions. It is relevant background for evaluating agent memory, but it does not directly test engineering-rule compliance or human approval of architecture decisions.

Sources:

- [Contexer public repository and README](https://github.com/bhargavamin/contexer)
- [Contexer benchmark methodology and reported results](https://github.com/bhargavamin/contexer/blob/main/docs/benchmark.md)
- Hu, Wang, and McAuley, [Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257), arXiv:2507.05257v4, revised 28 June 2026.

## Design and methods

### Task environment

Four small, dependency-free synthetic Python repositories were used. The task-specific files, tests, expected behavior, and compliance checks are saved beside each task's preregistration. Acceptance checks were defined before the corresponding agent runs. Reference and negative controls validated the graders for T03 and T04; T01 and T02 also have recorded scorer validation evidence.

### Conditions

- **A — repository only:** The agent receives the task repository, ordinary project material, and task prompt, without an instruction file containing the predeclared decision.
- **B — project decision file:** The same task and common starter content, plus the predeclared decision in `AGENTS.md`.
- **C — Contexer:** Planned only. It requires an approved decision and evidence that a fresh, comparable coding-agent session actually received it.

A and B used separate fresh sessions and condition-specific roots. For T02–T04, records document isolated Git roots; T01 predates that isolation correction and its `git status` command walked into a parent repository. The command was read-only, but this is a setup limitation. T02 and T03 were run concurrently. No task had an explicit token/time cap. All tasks used the same model/settings within a task, but the model and reasoning settings differ across tasks as the CLI/model setup changed.

### Scoring

Functional correctness and decision compliance were recorded separately. Executable tests and independent deterministic graders—not an LLM judge or agent self-report—determine the reported pass outcomes. Raw transcripts, diffs, grader/test outputs, run metadata, and launch failures are retained where available under each task's `runs/` directory. A missing measurement is not inferred or imputed.

### Preregistered task contracts

| Task | Engineering decision in B | Predeclared checks |
|---|---|---|
| **T01 — shared HTTP client** | Route outgoing requests through the existing `shared_client.py` helper, which supplies authentication/retry behavior; do not add direct HTTP calls. | Profile fetcher returns expected service payload; independent audit checks shared-client import/use and selected direct HTTP imports/calls. |
| **T02 — atomic report writes** | Write to a temporary sibling and replace atomically; do not truncate the prior report before new content is ready. | Three visible report-writing tests; injected partial-write and replacement-failure audits verify the previous destination remains intact and temporary files are handled. |
| **T03 — label validation** | Return any nonblank valid label unchanged; empty and whitespace-only labels raise exactly `ValueError`; do not invent a default. | Two valid strings (including surrounding whitespace) return byte-for-byte unchanged; empty and whitespace-only inputs raise the exact exception type and no value/default is returned. |
| **T04 — URL path normalization** | Make no network calls; preserve scheme, authority, all path content except removing exactly one final slash; leave query and fragment unchanged. | Six frozen URL inputs/outputs; monkeypatched audit intercepts `urllib.request.urlopen`, `http.client.HTTPConnection.request`, `socket.create_connection`, and `socket.socket.connect`. All helper calls run inside the mocks. |

Full exact task prompts, interfaces, examples, and scoring procedures are in `T02/T02-PREREGISTRATION.md`, `T03/T03-PREREGISTRATION.md`, and `T04/T04-PREREGISTRATION.md`, plus the T01 records and fixture. T03/T04 fixture checks are not counted as agent outcomes.

## Results

| Task | Condition A | Condition B | Pilot interpretation |
|---|---|---|---|
| **T01** | 1 run; functional 2/2; shared-client audit PASS; selected direct-HTTP audit PASS | 1 run; functional 2/2; both audits PASS | Same scored outcome. A URL-encodes the user ID and B does not; this was not a preregistered case. |
| **T02** | 1 run; functional 3/3; partial-write audit FAIL; replacement-failure audit FAIL | 1 run; functional 3/3; both injected-failure audits PASS | Only observed A/B difference on a preregistered compliance outcome. A used a truncating write; B used a temporary sibling and `os.replace`. |
| **T03** | 1 run; grader exit 0; all four preregistered checks PASS; agent suite 5 tests | 1 run; grader exit 0; all four preregistered checks PASS; agent suite 4 tests | Same scored outcome. A added a non-string `TypeError` case; B added Unicode whitespace coverage; neither extension changed frozen checks. |
| **T04** | 1 run; six outputs PASS; network compliance PASS; 0 intercepted calls at each of four boundaries | 1 run; same checks PASS; 0 intercepted calls at each of four boundaries | Same scored outcome. Both runs stayed within the registered mocks; no live URL request was recorded. |

### Run comparability details

- **T01:** Fresh local Codex threads, `gpt-6-luna`, medium reasoning. Both initially encountered an unsupported default model before coding, then completed one run each with the supported model. The run records show 34.3 seconds for A and 38.4 seconds for B; these are total turn durations. Token/cost caps were not exposed. Its starter README already described the shared client and auth/retry behavior, so A had repository evidence and was not a no-information baseline. A and B were not separate Git roots at launch.
- **T02:** Fresh projectless Codex sessions, requested `gpt-6-luna`, medium reasoning, byte-identical task prompt, separate Git roots. Sessions ran concurrently; no explicit cap or consumed-token metadata. Both passed visible tests; the A/B contrast is the two injected-failure audits.
- **T03:** Fresh local Codex sessions, `gpt-6-luna`, medium reasoning, same task prompt, separate roots, common starter hashes recorded. Sessions ran concurrently; no explicit budget or token-use metadata. Agent-added tests differed, but the independent grader applied identical frozen checks.
- **T04:** Fresh Codex CLI `0.163.0-alpha.10.2` sessions, `gpt-5.6-terra`, high reasoning, byte-identical task prompt and available tools, default one-turn budget, no explicit token cap. The preregistration and grader hashes are recorded in both run records. Two A launch failures before task execution and one test-wrapper issue are preserved in `T04/runs/launch-attempts.md`; they are not counted as runs.

## Interpretation and conclusions

1. The four paired pilot observations do not show a uniform advantage for `AGENTS.md`. T01, T03, and T04 had the same preregistered pass/fail outcome in A and B.
2. T02 shows a meaningful task-specific difference: the B implementation passed the predeclared atomic-failure audits while A's implementation did not, although both passed the three visible functional tests.
3. Because there is one run per condition per task, model sampling variability is unknown. Task-specific differences, limited checks, unblinded conditions, and absent token/time caps prevent a causal or broad performance claim. The result is not statistically significant evidence.
4. No conclusion about Contexer versus `AGENTS.md` is possible. The T04 Condition C decision is unapproved; no fresh coding agent has been given it and no C run exists.
5. The correct next research step is to review and explicitly approve the single isolated T04 decision through Contexer's normal review flow, then independently verify the approved state and prove a fresh agent receives the exact decision before coding. Only then should a preregistered, matched C run be considered.

## Limitations

- **Very small sample:** one run per condition for each of four different tasks; no repeatability estimate or statistical power.
- **Synthetic scope:** small Python fixtures do not establish behavior on production repositories, other languages, broader engineering work, teams, or long-term decision drift.
- **Task-specific coverage:** each grader covers only a defined set of behaviors. T01's static audit can miss indirect or aliased network calls; T04 mocks four known network boundaries, not every possible outbound mechanism.
- **Repository context differs in strength:** T01's README already advertised the shared client, making A more informed than a repository with no relevant guidance.
- **Unequal task settings:** model/reasoning settings differ across tasks; they are held constant within each A/B pair, not across all tasks.
- **Budget controls are incomplete:** explicit token/time caps were not configured; token/cost use is mostly unavailable. T02/T03 ran concurrently, so timing is not a controlled comparative outcome.
- **T01 isolation flaw:** its condition folders were not independent Git roots when agents ran. The observed `git status` walked into a parent repository but made no writes.
- **Condition C untested:** a pending decision is not an approved decision and MCP tool access is not proof that the coding agent received the decision.
- **Evidence presentation incomplete:** screenshots and narrated demonstration remain outstanding.
- **Status-note drift:** the copied planning documents preserve earlier “T03–T04 outstanding” statements. Those are historical and superseded by the saved T03/T04 run records; the current status is summarized in this report.

## AI tool use and verification

ChatGPT, running as Codex (GPT-6), supported literature review, experiment design, fixture/scorer work, troubleshooting, report preparation, and the T01–T04 agent sessions. Individual A/B run records identify the model and reasoning effort used for each task. Agent outputs were treated as evidence, not ground truth. Scores came from saved functional tests and deterministic independent graders. The T01 scorer was also rerun read-only against the saved implementations as documented in the local experiment notes. No new tests were run while preparing this submission report; it summarizes the existing saved records.

## Evidence map

- `results/T01-results.md`, `runs/condition-a.md`, `runs/condition-b.md`, `condition-a/`, `condition-b/`, and `grader/` — T01.
- `T02/T02-PREREGISTRATION.md`, `T02/results/T02-results.md`, `T02/runs/`, `T02/grader/`, `T02/fixture-validation.md` — T02.
- `T03/T03-PREREGISTRATION.md`, `T03/results/T03-results.md`, `T03/runs/`, `T03/grader/`, `T03/fixture-validation.md` — T03.
- `T04/T04-PREREGISTRATION.md`, `T04/T04-RESULTS.md`, `T04/runs/`, `T04/grader/`, `T04/fixture-validation.md`, `T04/CONDITION-C-STATUS.md` — T04 and current C status.
- `planning/` — copies of the earlier onboarding documents retained as provenance, not the final status authority.
