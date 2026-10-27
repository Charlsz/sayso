# Evaluations

This suite checks whether Sayso changes a result. A convincing skill file is not evidence. One paired run is not evidence that the skill caused the difference. A single win is not proof, and a small sample is not statistical significance.

`evals.json` is the source of the cases. Give the model the `prompt` only. Do not paste `assertions`, `dimensions`, `failure_modes`, or notes into the session, and do not say which condition you are running.

Each case has:

- `suite`: `core` for the original comparison set, or `judgment` for the ten-prompt batch.
- `prompt`: the user request, unchanged.
- `expected_output`: what a successful result does.
- `constraints`: facts and limits that have to survive.
- `failure_modes`: likely ways a model misses.
- `dimensions`: which of the five questions below the case is meant to inform.
- `assertions`: checks a person can mark pass or fail from the output, with a quote as evidence.

The `judgment` prompts are stored as run. They were not rewritten to hint at the desired answer.

## Five questions

Grade these separately. A case can be better on one and worse on another.

| Dimension | Question | A miss looks like |
| --- | --- | --- |
| Correctness and factual grounding | Are the claims true, and are invented details kept out? | A typical pattern stated as a guarantee. A name, number, course, tool, or measurement the prompt did not supply, presented as real. |
| Task completion and important omissions | Is the requested work done, including the part that is easy to skip? | A review that stops after the obvious bugs. A summary that drops a limit. An explanation that skips a required formula or example. |
| Voice and context preservation | Does the register match this task and, when asked, this person? | Lowercase casual prose rewritten into professional sentences. A formal email or a scientific paragraph made chatty. One person's habits applied to a different task. |
| Appropriate intervention | Was the change the task asked for, and only that? | A clear message capitalized or rewritten. A grammar fix that also changes the voice. |
| Useful restraint | Did restraint remove low-value edits without suppressing a needed point? | An already-good draft rewritten. Or a real defect, exception, or required detail left out so the answer would stay short. |

## How to compare

Use the same model and the same settings for every condition in a session. Run each prompt at least once with Sayso and once without it. Repeat the pair before treating a difference as stable. Record the run count. Do not pool runs from different models and call them one result.

1. **With Sayso.** In a new Cursor chat, invoke `/sayso`, then paste the prompt. If you are not in Cursor, start a clean session that has read `SKILL.md` and any reference that file points to.
2. **Without Sayso.** In a new chat that has not loaded the skill, paste the same prompt. Do not mention Sayso.

Save both outputs. Copy [`runs/scorecard.md`](runs/scorecard.md) to a new file for the session and fill it in.

## Scoring

For each assertion, mark `pass` or `fail` and quote the line that justifies it. Use `unclear` only when the output does not let you tell, and leave `unclear` out of the counts.

For each dimension listed on the case, mark Sayso `better`, `same`, or `worse` than the other answer. Quote both lines when they differ.

Then record:

- assertion passes with Sayso, and assertion passes without it
- how many dimension marks were better, same, and worse

Read the pairs where those counts disagree. The count is a way to compare repeated runs. It is not a quality score, and it does not support a significance claim.

Assertions that pass in both columns do not show that the skill works. Assertions that fail only on the Sayso side are regressions. The useful signal is a check that passes with the skill and fails without it, across more than one run, and that still looks right when you read the answers.

## What a previous run showed

[`runs/2026-10-27-notes.md`](runs/2026-10-27-notes.md) records one paired pass of all ten `judgment` prompts, from before the correctness and code-review instructions were added. [`runs/2026-10-27-five-cases.md`](runs/2026-10-27-five-cases.md) records one later paired pass of five of those prompts, after those instructions were in the files. Both are observations from a single run per condition. Neither is a score for every later edit, and neither was repeated.

## What is not here

There is no scoring script, no leaderboard, and no claim that a model improved by a measured amount. Add a case when a real miss shows up. Do not add a harness before a repeated miss shows that a harness is worth maintaining.
