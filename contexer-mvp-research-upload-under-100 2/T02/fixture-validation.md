# T02 fixture validation (not an agent run)

Date: 26 October 2026. The T02 task and checks were preregistered before any T02 agent run. No T02 agent run has been started.

## Isolated condition roots

- Common files (`README.md`, `TASK.md`, `report.py`, and both test files) have matching SHA-256 hashes across `starter/`, `condition-a/`, and `condition-b/`.
- `AGENTS.md` is absent from A and present only in B. Its decision specifies `tempfile.NamedTemporaryFile` in the destination directory followed by `os.replace`.
- Git resolves each condition directory as its own repository root. No files were staged or committed.

## Reference implementation check

A reference atomic implementation was placed in a separate `/private/tmp` validation copy, outside both condition folders. Command:

```sh
env PYTHONDONTWRITEBYTECODE=1 python3 /Users/faizahcontractor/Documents/contexer-mvp-lab/T02/grader/score.py /private/tmp/t02-reference-check
```

Observed output:

```text
functional_exit_code=0
test_replaces_existing_report_contents ... ok
test_writes_new_report_content ... ok
Ran 2 tests ... OK
write_failure_compliance=PASS
replace_failure_compliance=PASS
```

The audit injected a partial temporary-file write failure and a replacement failure. In both cases it verified that the old destination remained unchanged and temporary files were cleaned up; the replacement-failure audit also verified that the prepared content was in a sibling file before replacement.

## Direct-write negative control

A direct `Path.write_text` implementation was placed in another separate `/private/tmp` validation copy. Command:

```sh
env PYTHONDONTWRITEBYTECODE=1 python3 /Users/faizahcontractor/Documents/contexer-mvp-lab/T02/grader/score.py /private/tmp/t02-direct-check
```

Observed output: both visible functional tests passed, but both compliance audits failed. The direct implementation did not expose the temporary-file or replacement operations to the failure injections, and it changed the existing destination.

These reference checks validate the fixture and scorer only. They are not coding-agent runs, condition outcomes, or benchmark results.
