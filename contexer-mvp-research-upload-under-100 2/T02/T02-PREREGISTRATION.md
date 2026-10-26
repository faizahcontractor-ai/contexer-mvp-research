# T02 preregistration: atomic report replacement

Preregistered before the T02 agent runs. The preregistration and scorer were frozen before either session started.

## Task prompt

Implement `write_report(path, content)` so generated report text is saved at the requested destination, replacing any existing contents. Follow the project structure and add tests.

This exact task is in each condition's `TASK.md`. Do not add the engineering decision to the task prompt.

## Decision for Condition B

Report files must be written atomically: create a temporary file with `tempfile.NamedTemporaryFile` in the destination's directory, write the complete new content, then publish it with `os.replace`. Do not open the existing destination for a truncating write. If writing or replacement fails, preserve the previous destination contents and clean up any temporary file.

## Conditions

- A: a fresh coding-agent session with `condition-a/`, which contains the repository and task only.
- B: a fresh session with the same task and repository files plus `AGENTS.md` containing only the decision above.
- Each condition has its own initialized Git repository root. No files are staged or committed. This prevents Git commands from escaping to a parent repository while preserving the starter files.
- Use the same agent host, model/version, tools, task wording, and available time/token budget. Record unavailable budget fields as unavailable. Do not mention the decision in A.

## Predeclared checks

Functional tests visible to both agents: (1) writing to a new destination yields exact content; (2) writing over an existing destination yields exact new content.

Independent compliance audit, kept outside both condition repositories: (1) intercept the replacement operation and verify its source is a temporary sibling of the destination; (2) verify the complete new content is present in that temporary file before publication; (3) inject a partial temporary-file write failure and verify the prior destination content remains unchanged, no replacement is attempted, and the temporary file is removed; (4) inject a replacement failure and verify the prior destination content remains unchanged and the temporary file is removed; (5) require that both temporary-file writing and the replacement path are actually used, so a direct truncating write cannot pass by ignoring the injected failures. The scorer exits nonzero if either the functional suite or any compliance check fails.

## Run status

One fresh run per condition is complete. See `results/T02-results.md` and `runs/` for the observed results, raw run records, and code diffs. This is a preliminary pilot, not a conclusive benchmark. Condition C, screenshots, and narration remain outstanding.
