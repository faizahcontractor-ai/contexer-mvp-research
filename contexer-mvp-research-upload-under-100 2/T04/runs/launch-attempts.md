# T04 launch and wrapper attempts

These events occurred before/around the completed A/B runs. They are not counted as coding-agent observations.

1. Initial A CLI invocation was rejected before a model session because `--sandbox` and `--approve-for-me` are mutually exclusive. Tool output: `error: the argument '--sandbox <SANDBOX_MODE>' cannot be used with '--approve-for-me'`. No task ran and no fixture file changed.
2. A fresh A launch using configured default model `gpt-5.2-codex` created thread `01a17881-20bb-7a62-880a-0062494d2f6e` but failed before task execution. CLI reported: `The 'gpt-5.2-codex' model is not supported when using Codex with a ChatGPT account.` The model catalog was checked and both real conditions then used supported `gpt-5.6-terra` at high reasoning effort. The failed launch transcript was superseded in the temporary A transcript path by the final A transcript; this note preserves its observed error and thread ID, but the raw launch output is not available as a separate file.
3. The first standalone A test wrapper used zsh's read-only special variable name `status`; the test command ran, but the wrapper stopped while saving its exit code (`zsh:8: read-only variable: status`). The test was rerun with a non-reserved variable name; the persisted standalone output and exit code are from that successful rerun. This was a wrapper issue, not a test failure.

The completed fresh A and B transcripts, outputs, diffs, and run records are preserved separately. No failed coding-agent implementation was discarded.
