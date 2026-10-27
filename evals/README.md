# Evaluations

This suite checks whether Sayso changes a result. A convincing skill file is not evidence. One paired run is not evidence that the skill caused the difference. A single win is not proof, and a small sample is not statistical significance.

`evals.json` is the source of the cases. Give the model the `prompt` only. Do not paste `assertions`, `checks`, `dimensions`, `failure_modes`, or notes into the session, and do not say which condition you are running.

Each case has:

- `suite`: `core` for the original comparison set, `judgment` for the ten-prompt batch, `examples` for the later cases built from known failure modes, or `use` for the set that asks whether the answer is usable for its reader. The `use` prompts are not the calibration examples in `SKILL.md`. [`runs/2026-10-27-use.md`](runs/2026-10-27-use.md) is the one scored pass of that set.
- `prompt`: the user request, unchanged.
- `expected_output`: what a successful result does.
- `constraints`: facts and limits that have to survive.
- `failure_modes`: likely ways a model misses.
- `dimensions`: which of the questions below the case is meant to inform. `use` cases can also list context fit and clarity.
- `assertions`: checks a person can mark pass or fail from the output, with a quote as evidence. Naturalness and voice stay here. They are not automatic.
- `checks`: optional objective patterns, such as a required phrase, a forbidden cliché, or text that should stay unchanged. A passing check is not a passing review of the whole answer. A case with no `checks` is graded by a person.
- `covers`: which of the ten themes a newer case is for. Older cases are mapped in `check_suite.py`.

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

## Use suite

`use` cases add two questions to the five above, when the case lists them.

| Dimension | Question | A miss looks like |
| --- | --- | --- |
| Context fit | Does the result match this reader, this relationship, and this kind of task? | A lab note turned into a chat. A recommendation with no recommendation. |
| Clarity | Can the reader use the answer without rereading it? | A correct explanation packed into one sentence the reader cannot follow. A point buried under framing. |

A case can be better on clarity and worse on correctness. Record that split. Do not collapse it into one score.

Objective `checks` on these cases look for facts and required distinctions, not for one approved sentence. A phrase list that failed correct answers on `threshold-sentence` was removed after the October 27 examples pass. That recorded exit code stands. Re-scoring the file does not replay it.

The first scoring of [`runs/2026-10-27-use.json`](runs/2026-10-27-use.json) also punished wording. `hey` matched inside `They`, and the retry check missed an answer that had already described a duplicate order. `excludes_word` matches a forbidden word on its own. The retry check now accepts phrases such as `already have been placed` and `same order`. The missing-file check no longer treats every `exception` as that bug. The notes record the first exit and the exit after those edits. Re-scoring does not replay the first one.

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

## Objective checks

From the repository root:

```bash
python evals/check_suite.py
```

The script uses only the Python standard library. It checks that every case has the fields above, that the ten themes are covered, and that each hand-written pair in [`fixtures.json`](fixtures.json) behaves as labeled: the weak answer fails at least one check, and the better answer passes. Those pairs were written to test the checks. They are not model output, and they are not a comparison of Sayso with a baseline.

To score answers you actually collected, save a file like this and pass its path:

```json
{
  "date": "2026-10-28",
  "model": "the model name you can see",
  "settings": "temperature, or not exposed",
  "runs": 1,
  "with_sayso": {"editor-tools-rewrite": "the answer"},
  "without_sayso": {"editor-tools-rewrite": "the answer"}
}
```

```bash
python evals/check_suite.py evals/runs/your-run.json
```

The script scores `checks` only. Grade `assertions` and the dimensions on the scorecard. Missing answers are reported and are not filled in. The script does not call an API. [`runs/2026-10-27-examples.json`](runs/2026-10-27-examples.json) is one scored pass of the eight `examples` prompts. The checker passed 14 of those answers and failed both threshold answers. [`runs/2026-10-27-use.json`](runs/2026-10-27-use.json) and [`runs/2026-10-27-use-trial2.json`](runs/2026-10-27-use-trial2.json) are the later `use` pass. Both still exit 1 after the check edits. Read the notes before treating a fail as a wrong answer or a pass as a good one.

The checks are brittle on purpose. A good paraphrase can fail a substring, and a bad answer can pass one. Read the answer when the script and the prose disagree.

## What a previous run showed

[`runs/2026-10-27-notes.md`](runs/2026-10-27-notes.md) records one paired pass of all ten `judgment` prompts, from before the correctness and code-review instructions were added. [`runs/2026-10-27-five-cases.md`](runs/2026-10-27-five-cases.md) records one later paired pass of five of those prompts, after those instructions were in the files. Both are observations from a single run per condition. Neither is a score for every later edit, and neither was repeated. The `examples` cases were added after those notes. One later assertion on `get-user-review`, about not stating an unseen behavior as a confirmed bug, was not part of either grade. [`runs/2026-10-27-examples.md`](runs/2026-10-27-examples.md) is a separate one-run pass of the `examples` prompts only.

The calibration left in `SKILL.md` is a text that should be returned unchanged and a shortened conclusion that has to keep two limits. The older illustrations, including the `getUser` review and the prototype note, are not in the skill file anymore. A later pass on those older prompts is still not a held-out test of the rewrite. The `use` prompts were written so they would not copy either the remaining calibration or those removed illustrations. [`runs/2026-10-27-use.md`](runs/2026-10-27-use.md) is one pass of that set, plus a second trial of three prompts. It did not show a consistent improvement.

[`reports/2026-10-27-full37-summary.md`](reports/2026-10-27-full37-summary.md) is one later pass of all 37 cases. Each condition ran once, in a fresh session, with Sayso loaded by reading `SKILL.md`. It did not show a consistent improvement. The answers are in [`runs/2026-10-27-full37.json`](runs/2026-10-27-full37.json).

## What is not here

There is no leaderboard and no claim that a model improved by a measured amount. The script does not grade naturalness, and it does not replace reading both answers.
