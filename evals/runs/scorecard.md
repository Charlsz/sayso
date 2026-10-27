# Scorecard

Copy this file to `evals/runs/<date>-<model>.md` for each comparison. Fill one copy per session. Add a section per repeated run rather than averaging runs together.

## Session

- Date:
- Model:
- Settings (temperature, reasoning effort, or "not exposed"):
- Runs per condition in this file:
- Skill: path or commit used, and whether `/sayso` was invoked or `SKILL.md` was pasted
- Prompt source: `evals/evals.json` field `prompt` only

A higher pass count on one run is something to read. It is not proof. Do not report statistical significance for a small sample.

## Dimension marks

Use `better`, `same`, or `worse` for the Sayso answer relative to the answer without it. Leave a cell blank when the case does not list that dimension. Quote the contrasting lines in Notes.

| Case | Correctness | Task completion | Voice | Intervention | Restraint | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| dishwasher-film |  |  |  |  |  |  |
| sister-text |  |  |  |  |  |  |
| reschedule-interview |  |  |  |  |  |  |
| norovirus-brief |  |  |  |  |  |  |
| actigraphy-abstract |  |  |  |  |  |  |
| retry-after-docs |  |  |  |  |  |  |
| password-reset-review |  |  |  |  |  |  |
| status-note |  |  |  |  |  |  |
| casual-message |  |  |  |  |  |  |
| preserve-voice |  |  |  |  |  |  |
| professor-email |  |  |  |  |  |  |
| precision-recall |  |  |  |  |  |  |
| project-advice |  |  |  |  |  |  |
| process-thread |  |  |  |  |  |  |
| satellite-summary |  |  |  |  |  |  |
| get-user-review |  |  |  |  |  |  |
| leave-unchanged-message |  |  |  |  |  |  |
| flood-paragraph |  |  |  |  |  |  |

## Assertion counts

Grade every assertion on the cases you ran. `pass` = 1, `fail` = 0. Omit `unclear` and say why.

| Case | Assertion (short quote) | With Sayso | Without Sayso | Evidence quote |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

- With Sayso, passes / graded:
- Without Sayso, passes / graded:
- Dimension marks, better / same / worse:

## Read next

Name the cases where the two answers disagree. Say whether the disagreement is correctness, a missing requirement, voice, an extra edit, or restraint that dropped something needed.
