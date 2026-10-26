# T01 run protocol

## Fixed task and decision

The agent task is in each condition's `TASK.md`. The predeclared decision is: all outgoing HTTP requests must use the existing `shared_client.py` helper, which provides authentication and retry behaviour; do not add a direct HTTP call.

## Conditions

- A is `condition-a/`: repo files and task only, no instruction file.
- B is `condition-b/`: identical starter plus `AGENTS.md` containing the decision.
- Each folder was copied from the same `starter/` snapshot before runs. The independent scorer lives in `grader/score.py`, outside both agent-visible copies.

## Measurements

Run `python3 -m unittest discover -v` in each condition for functional correctness. Then run `python3 ../grader/score.py .` from the condition directory (or pass the condition directory path) for the same tests plus AST-based decision-compliance audit. Keep raw transcript, diffs and scorer output separately for each condition. The compliance audit is not shown to the agent.

The starter suite is expected to have one failing test before implementation (`NotImplementedError` in `fetch_user_profile`) and one passing shared-client test. This confirms the task is open while the client fixture works.

## Agent settings

Use ChatGPT running Codex for both runs, one fresh session per condition, same configured model/reasoning/tool permissions and identical task text. Record model and settings shown by the host on run day; do not infer unavailable temperature or token values. Start each session in the corresponding condition directory, attach only that condition's repository context, and do not mention the decision in A. Run A and B in randomized order where scheduling permits.

## Scope and safety

The shared client test uses a fake in-memory transport. The profile functional test monkeypatches `urllib.request.urlopen`; it makes no network request. No credentials are present.
