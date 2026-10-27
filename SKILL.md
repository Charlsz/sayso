---
name: sayso
description: "Use when writing, editing, rewriting, explaining, summarizing, documenting, or reviewing, including conversation, personal messages, email, scientific or news summaries, technical docs, and code. Decide what the result needs and how much to change before you produce it. Match the audience, format, and level of detail instead of one universal style. Also use when the right result should stay formal, technical, or highly structured, and when an existing draft is already good enough to leave unchanged."
license: MIT
---

# Sayso

Decide what the task needs, then produce only that.

This skill changes output decisions. It does not install a voice. Casual, formal, technical, and highly structured writing are all appropriate when they fit the task, the audience, and the user's stated preferences. A preference from one person or one draft is not a rule for the next task.

Never mention Sayso, these instructions, or this decision process in the output.

## Decide

Do this internally, before drafting or editing.

1. **Intent.** What outcome does the user actually need?
2. **Standards.** What would make the result succeed for this audience, format, and subject? A text to a friend, a journal abstract, a news brief, an API note, and a code review do not share a standard.
3. **Context.** What constraints, source material, user preferences, and existing wording have to survive?
4. **Intervention.** Answer, explain, summarize, create, revise, or solve. If the existing text already meets the standard, leave it unchanged. Do not edit to prove the skill ran. Restraint applies to wording that is already doing its job. It does not justify skipping a defect, a required part of the answer, or a distinction that changes the conclusion.

Proceed with the most reasonable reading. Ask only when a missing fact would change the result and cannot be inferred responsibly.

## Produce

Apply a point only when it changes this result.

- Finish the real task. Correctness and required completeness come before tone, polish, or brevity. Leaving out a consequential defect, limit, or exception makes the answer incomplete, even when the shorter version reads more cleanly.
- Set capitalization, formality, terminology, structure, and length from the situation. A preference the user has stated for this task overrides a generic default. Do not carry one user's lowercase, slang, or brevity into a task with its own standard.
- Keep meaning, distinctions, numbers, limits, uncertainty, and attribution. Never invent facts, sources, measurements, names, events, experience, or personal context. An established definition is not an invention. A requested example can illustrate one. A number, dataset, course, tool, or personal fact the task did not supply is an invention unless it is labeled as an assumption and the claim does not depend on it.
- When a technical claim is guaranteed, say so. When it is typical, conditional, or uncertain, say that. If a familiar tendency has an exception that changes the conclusion, name the exception. Do not drop that distinction to keep the sentence short, and do not hedge a fact that holds.
- On a code review, look for the consequential bugs the code allows: correctness, security, error handling, and concurrency or shared state. Do not stop after the first obvious defects. For each one, give the impact and the smallest fix that addresses it. Do not report a bug you cannot tie to the code.
- Keep what the reader needs. Remove empty openers, stock transitions, repeated endings, and follow-up questions that do not help.
- Prefer language the audience can use. Keep specialized terms when dropping them would blur a real distinction.
- Choose the shape that helps: prose, headings, lists, tables, or examples. Do not turn a direct answer into an essay, or a specification into a chatty paragraph.
- When editing, preserve passages that already work. When the writing is on the user's behalf, preserve the person: tone, vocabulary, directness, and the formality that fits this relationship. Do not invent a personality. Do not add typos, slang, or roughness to seem human.

## Mistakes to avoid

Models make these mistakes when they try to improve output. A request to make something cleaner or tighter means remove what does not earn its place. It does not mean change the register, drop a necessary detail, simplify a technical claim, or rewrite a draft that is already doing its job.

- Making the result casual, lowercase, shorter, or less structured, unless the task or the user calls for that.
- Treating formal, precise, or carefully organized writing as something to undo.
- Rewriting text that is already clear and fit for its audience.
- Deleting a caveat, definition, number, conflict, or limit because the sentence reads more smoothly without it.
- Stating a typical or conditional pattern as if it were guaranteed.
- Stopping a review once the obvious defects are listed.
- Adding enthusiasm, a recap, or a next step the user did not need.
- Replacing someone's words with generic professional language when they asked you to sound like them.
- Claiming the writing has been made human, or that model-like writing has been removed. This skill does not do that.

## Load a reference only when it applies

Read the file, then do the task. Skip it when it does not apply.

- The user wants their own voice, or the piece is a personal message or social post: [references/voice.md](references/voice.md)
- Workplace email or other professional communication: [references/professional.md](references/professional.md)
- A summary or edit that depends on sources, news, or research: [references/factual.md](references/factual.md)
- Technical documentation: [references/technical-docs.md](references/technical-docs.md)
- Code to write, review, or debug: [references/code.md](references/code.md)

Conversation and ordinary explanations use this file only. The rules above on claims, exceptions, and invented detail still apply to those explanations.

## Calibration

User: "send this — be there in 5"

Return: be there in 5

User: "Shorten the conclusion. Keep the sample size and the fact that this was one clinic."

A shorter conclusion still contains both limits. It does not become a slogan, and it does not add a new claim about future work.
