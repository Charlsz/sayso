# 2026-10-27 five-case pass

One paired pass of five `judgment` prompts, run after the correctness and code-review instructions were already in `SKILL.md` and `references/code.md`. This is a different pass from `2026-10-27-notes.md`, which used the earlier instructions and all ten prompts. Each condition here was run once. That is not a repeated result, and it is not statistical significance. The `examples` suite, and the later get-user assertion about not confirming a behavior the function does not show, were not part of this grade.

- Date: October 27, 2026.
- Model: Grok 4.7, inherited by the session that ran the pair.
- Settings: temperature and other sampling settings were not exposed.
- Runs per condition: 1.
- Prompts: the `prompt` field only, for `precision-recall`, `get-user-review`, `preserve-voice`, `leave-unchanged-message`, and `professor-email`. Assertions were not sent.
- With Sayso: a fresh session was told to read `SKILL.md` and any reference that file pointed to for the task. That puts the skill in context. It does not measure whether a normal chat would load Sayso on its own.
- Without Sayso: a fresh session was told not to read the repository and not to apply a skill. Tool traces were not available, so that instruction was not independently verified.

No instruction was changed because of this pass. The outcomes below are what this one pair did.

## precision-recall

Both answers gave the two formulas, a threshold trade-off, a formal register, and a satellite flood example whose counts were labeled as constructed rather than measured.

With Sayso, precision was not described as rising with the threshold. The answer said precision has no monotone relation to the threshold, that one downward step can raise precision and recall together, and that a wider move to a more permissive threshold can lower precision while raising recall. It also said that inverse pattern does not hold for every adjacent pair of thresholds. The answer was long: it added a prevalence identity, an accuracy contrast, an F1 formula, and a note that pixel counts ignore spatial arrangement.

Without Sayso, the answer said lowering the threshold tends to lower precision and raising it tends to raise precision, then said that tendency is not an identity and that precision need not decrease at every step. The flood counts were labeled as constructed. The answer was shorter.

The earlier pass had said that raising a threshold typically increases precision, without the exception. This pass did not repeat that sentence. One run is not evidence that the instruction caused the difference. The length of the Sayso answer is a separate observation. `SKILL.md` already says not to turn a direct answer into an essay, so no further brevity rule was added.

## get-user-review

With Sayso, the review reported all three defects in the function:

- an HTTP error body can be parsed and cached, so a later call returns it as the user
- `id` is placed in the URL without encoding, so `/`, `?`, `#`, and dot segments can change the request
- two overlapping calls can both miss the cache before either write, and the last write wins

It also reported that `if (cached)` treats a stored falsy value as a miss, that callers receive the stored object and can mutate it, and that a cache key of only `id` would be wrong if the response depended on the viewer. On that last point, the answer said the function does not show whether the body varies by viewer.

Without Sayso, the review reported the cached HTTP error and the unescaped `id`, with a small patch for both. It did not report the overlapping requests.

The three defects this case is meant to catch were present on the Sayso side and the race was absent on the other side. The extra Sayso points are one run. The code reference already says to omit a problem the snippet does not support, so that sentence was not rewritten to chase this sample.

## preserve-voice

With Sayso:

> i've been working on this for a while and i finally got something that actually works. there's still a lot to fix but i'm happy with where it's going

The lowercase stayed. "its" became "it's". The openings changed from "been working" and "still a lot" to "i've been working" and "there's still a lot".

Without Sayso:

> I've been working on this for a while and I finally got something that actually works. Still a lot to fix, but I'm happy with where it's going.

That answer capitalized the note. Sayso stayed closer to the draft's formality. It still made a larger grammar edit than only correcting "its". The prompt asked for a grammar fix, and one run is not enough to treat the added words as a new failure mode.

## leave-unchanged-message

With Sayso, the message was returned unchanged:

> hey, i pushed the fix. the issue was caused by the cache not being invalidated after an update. should be good now, but let me know if you can still reproduce it.

Without Sayso, the same message was capitalized ("Hey, I pushed the fix...").

## professor-email

Both emails were capitalized and included the project-meeting conflict, the coursework, and a request to review the final project presentation. Neither invented a professor's name or a course number.

With Sayso, the body was three sentences and did not add a request for general feedback. Without Sayso, the email was longer and added "I'd really appreciate any feedback" and "Thank you for understanding."

The Sayso email stayed formal while the two personal notes stayed lowercase. That is one observation that the same instructions did not force one capitalization onto every task.
