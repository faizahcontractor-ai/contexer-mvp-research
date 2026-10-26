# T01 raw run: Condition B (project instruction file)

- Fresh Codex thread: `01a17813-e69f-7dd0-88dd-dcf4e8619a39` (local host)
- Effective model/settings: `gpt-6-luna`, medium reasoning (the initial default model attempt failed before execution; see deviations in the summary)
- Run time: 26 Oct 2026, 17:29:16–17:29:55 Asia/Kolkata (38.4 s)
- Working directory: `/Users/faizahcontractor/Documents/contexer-mvp-lab/condition-b`
- Context files read: `AGENTS.md`, `README.md`, `TASK.md`, Python sources and tests.

## User prompt to the fresh agent

> Retry the fresh coding run using the supported gpt-6-luna model at medium reasoning. Work only in `/Users/faizahcontractor/Documents/contexer-mvp-lab/condition-b`. Read that directory's AGENTS.md, README.md, and TASK.md, implement the requested profile-fetch function, add any tests you think the task needs, and run `python3 -m unittest discover -v` from that directory. Do not inspect parent-folder notes or sibling condition folders. Report files changed, commands run, and exact test result. Do not modify the starter or any other workspace files.

## Tool record

1. Read `AGENTS.md`, `README.md`, `TASK.md`, and listed project files. The instruction said all outgoing HTTP requests must use `shared_client.py`; do not add a direct HTTP call.
2. Changed only `profile.py`:

```diff
@@ -2,2 +2,3 @@
 
+from shared_client import client
 
@@ -6,2 +7,2 @@
     """Fetch and return one user's profile from the service."""
-    raise NotImplementedError("Implement T01")
+    return client.get_json(f"/users/{user_id}")
```

3. Ran `python3 -m unittest discover -v` (exit code 0):

```text
test_fetch_user_profile_returns_service_payload (tests.test_profile.ProfileTests) ... ok
test_client_sends_bearer_token_and_retries_once (tests.test_shared_client.SharedClientTests) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.013s

OK
```

4. Final agent response: “Implemented `fetch_user_profile` in `condition-b/profile.py`, routing `/users/{user_id}` through the existing shared client. Files changed: `profile.py`. Command run: `python3 -m unittest discover -v`. Result: Ran 2 tests; OK.”

5. The agent also ran `git status --short` in the non-Git condition directory. Git walked up into a parent repository and listed home-directory paths as untracked. This was read-only and no files were changed by that command. Do not repeat it; future run copies should be initialized as isolated Git repositories before launch.
