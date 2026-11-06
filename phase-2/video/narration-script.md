# Narrated evaluation and failure-investigation video

**Recording status: not recorded.** This file is a script, not video evidence.

Suggested length: 4–6 minutes. Record genuine terminal output with credentials and unrelated windows hidden.

## Shot list and narration

1. **Scope:** “This review covers four small synthetic A/B task pairs, one completed run per condition per task. It has no scored Contexer Condition C run.”
2. **Conditions:** Explain A as repository-only and B as the same task plus static AGENTS.md guidance. State clearly that B is not Contexer.
3. **T02 failure:** Run PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-a. Point out that the visible tests pass, while both injected failure-safety audits fail.
4. **T02 comparison:** Run PYTHONDONTWRITEBYTECODE=1 python3 T02/grader/score.py T02/condition-b. Explain that this saved run passed both audits. Avoid claiming a general causal effect from one run per condition.
5. **T04:** Run the two T04 scorer commands from demo/README.md. Explain the six exact URL checks and four patched network boundaries; no live request is permitted.
6. **Results and limits:** Show the metrics CSV and per-case charts. State that A and B matched on T01, T03 and T04, and differed on the T02 safety checks. Explain that five outcome slices represent four task pairs and are not five independent runs.
7. **Condition C and next step:** Show pending_approval status. Explain that approval provenance, verified delivery to a fresh agent, and a scored run are absent.
8. **Close:** State that the sample is too small for statistical or broad superiority claims; screenshots, this recording, publication, and mentor review remain outstanding.

Save an authentic recording plus an unedited copy, note its date and any edits, and review it for secrets and personal information before publishing. Until then, narration remains outstanding.
