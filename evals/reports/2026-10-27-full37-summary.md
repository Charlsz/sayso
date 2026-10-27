# Sayso full comparison, 27 October 2026 — summary

One fresh session per case per condition, 37 cases, same model. This is exploratory evidence from a single run. It is not proof that Sayso improves outputs in general, and it is not statistical significance.

## Setup

- Model: Grok 4.7, inherited by each session. No finer version string was reported. Temperature was not available.
- Started about 7:45 p.m. America/Chicago (UTC-5) on 27 October 2026 and finished the same evening.
- With Sayso: the session read `SKILL.md` and followed it, including whichever reference that file led it to open. Transcripts show `SKILL.md` was read in all 37 sessions. No baseline session read a file.
- Without Sayso: the same prompt, with an instruction not to read files and not to apply a skill, because the skill sits in the workspace. The sessions were not told to imitate or avoid Sayso.
- Raw answers: `evals/runs/2026-10-27-full37.json`. Checker output: `evals/reports/2026-10-27-full37-checks.txt`.
- The skill, references, prompts, fixtures, assertions, and checks were not edited for this run.

## Result

| Overall | Count | Denominator |
| --- | ---: | ---: |
| Sayso win | 10 | 37 |
| Tie | 24 | 37 |
| Sayso regression | 1 | 37 |
| Unclear | 2 | 37 |

A win here means the Sayso answer was more useful on the dimensions that mattered for that prompt. It does not mean every dimension was better. Ten of 37 is not a majority, and 24 of 37 were ties.

By suite: core 1 win, 5 ties, 1 regression, 1 unclear (8). Judgment 5 wins, 5 ties (10). Examples 2 wins, 6 ties (8). Use 2 wins, 8 ties, 0 regressions, 1 unclear (11).

Automated checks, only the 18 cases that have them: Sayso 18 pass / 0 fail. Baseline 17 pass / 1 fail. The fail is `load-note-review`, and the human grade does not treat that fail as a clean baseline miss. Nineteen cases have no automated checks. Checker exit code: 1.

## Strongest places Sayso helped

- `precision-recall` (12). Sayso said precision can rise or fall when the threshold rises. The other answer said raising the threshold tends to raise precision and that the two measures move in opposite directions.
- `get-user-review` (16). Sayso reported the cached HTTP error, the unescaped id, and overlapping calls that both miss the cache. The other review stopped after the first two.
- `leave-unchanged-message` (17) and `preserve-voice` (10). Sayso kept the lowercase. The other answer capitalized.
- `export-flag` (37). Both said to leave the flag off until legal reviews the columns. The other answer then added a rollout to those two customers after legal signs off. The notes do not say that.

## Where Sayso was worse

- `status-note` (8). The note was already tight. Sayso joined the first two facts with "so", which states a cause the note did not state. The other answer tightened punctuation and left the facts side by side.

`order-retry` (30) is a tie. Sayso's paragraph is 116 words and the other is 92. Both distinguish a timeout from a reset, and both warn that a retry can place the order twice. The extra sentences tell the engineer to reuse an idempotency key.

`load-note-review` (34) is unclear rather than a win or a regression. Sayso covered an unreadable path and the cache key, and it was much longer (445 words against 137). The shorter review did not say a missing file is unhandled. Completeness and concision moved in opposite directions.

## Equally good

The ship note, the text to Sam, the gasket email, the Toledo summary, the meeting notes, the prototype line, the editor rewrite, the flood methods note, the threshold sentences, and the satellite summary were usable on both sides. Several of those pairs are nearly the same text. Identical output is not evidence that the skill changed anything.

## Limitations

One run per condition. Sessions were told to read the skill. That is not the same as a normal chat selecting Sayso from its description. Some sessions opened a reference the task did not clearly require (`flood-cloud` and `assay-notebook` opened `technical-docs.md`). Those choices did not produce a visible miss in the answers. Grading compared the two answers. It can favor a difference that another reader would call a tie.

## Next step

Gather another full round before changing the skill. The wins are concentrated in a few judgment cases, and the one regression is a single added "so". Neither pattern is stable enough, from this sample alone, to justify an edit.
