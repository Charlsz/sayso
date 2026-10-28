# Sayso

Sayso is an open-source [Agent Skill](https://agentskills.io/specification) for Cursor, Claude Code, Codex, and OpenCode. It helps the model decide what the reader needs to be able to do or know, then write to that. It does not guarantee a better answer. The October 27, 2026 comparison did not show a consistent improvement.

## Install

```bash
npx skills add Charlsz/sayso
```

That is the [skills CLI](https://github.com/vercel-labs/skills). Skill repositories on [skills.sh](https://skills.sh) install the same way. In a terminal it asks which agents to include. Cursor, Claude Code, Codex, and OpenCode are on that list, and the CLI picks the folder for each one you select. Run it in a project, or add `-g` for every project on this computer. It needs Node.js 22.20 or later.

Then start a new chat.

### Turn it on

#### Cursor

[Cursor](https://cursor.com/docs/skills) is the editor with Agent chat. In a new Agent chat, type `/sayso` and choose Sayso. That attaches it to one message. Option+Enter on a Mac, or Alt+Enter on Windows, keeps it on for the session as a Custom Mode. Cursor can also apply it when the task matches the description.

A global install stays on your machine. Cursor does not copy `~/.agents/skills/` to Cloud Agents, remote SSH sessions, or self-hosted workers. For a Cloud Agent, commit `.agents/skills/sayso/` in the repository. Skills in `~/.cursor/skills/` can be synced for Cloud Agents you start yourself: Settings → Agents → Context and Tools → Sync Skills for Cloud Agents. That sync does not include `~/.agents/skills/`, and automation runs do not load the synced copy.

#### Claude Code

[Claude Code](https://code.claude.com/docs/en/skills) is Anthropic's coding agent in the terminal and the desktop app. Type `/sayso`, or ask for the work and Claude can load the skill when the description matches. Claude Code notices a new skill during the current session. If the skills folder did not exist when the session started, run `/reload-skills`.

Claude on the web, and Cowork cloud sessions, do not read `~/.claude/skills/` on your machine. Those sessions use the skills enabled on your claude.ai account.

#### Codex

[Codex](https://developers.openai.com/codex/skills) is OpenAI's coding agent in the CLI, the IDE extension, and the ChatGPT desktop app. In the CLI or the IDE extension, type `$sayso`, or run `/skills` and choose Sayso. In the ChatGPT desktop app, type `@` and choose Sayso. Codex can also select it when the task matches the description. It picks up a newly copied skill on its own. If it does not appear, restart Codex.

#### OpenCode

[OpenCode](https://opencode.ai/docs/skills/) is the open-source coding agent. Type `@sayso` to load it, or ask normally and OpenCode can load it when the description matches. Start a new session after installing.

## Use it

Ask for the work the way you normally would: an explanation, a rewrite, an email, a summary, documentation, or a review. You can also invoke Sayso first, then ask.

The answer should not mention Sayso or walk through a checklist.

If an edit comes back colder, shorter, or more casual than the task deserves, that is a miss. So is a rewrite of a draft that was already doing its job, a technical claim stated more strongly than it holds, or a review that stops before a consequential bug.

## What it does

The audience and the task set the standard. A text, a professional email, a scientific note, a technical explanation, and a code review do not share one. Formal, technical, and scientific writing stay that way when the task calls for them. Someone's own words stay theirs. A draft that already does the job should be left alone. Casual, lowercase, and short are not the aim.

The instructions also keep facts, limits, uncertainty, attribution, and technical precision. Those safeguards matter. They do not by themselves make an explanation clearer or a review more complete. A correct answer can still hide the point, and a review that holds back can still miss a bug.

Sayso is not a model. It does not detect or remove "AI writing." Instructions can change a result. They cannot guarantee a correct answer, and they do not remove the limits of the model underneath. The comparisons in [`evals/`](evals/README.md) are where a "better answer" claim would have to come from.

## What's in the folder

| Path | What it is |
| --- | --- |
| `SKILL.md` | The instructions the agent loads |
| `references/voice.md` | Personal messages and writing in someone's voice |
| `references/professional.md` | Workplace email and other professional messages |
| `references/factual.md` | News, research, and other writing that has to stay faithful to sources |
| `references/technical-docs.md` | API and interface documentation |
| `references/code.md` | Code, review, and debugging |
| `evals/` | Cases for comparing answers with and without the skill |
| `docs/` | The static page |

The reference files are for the agent, and only when the task matches. You can ignore `evals/` if you only want to use the skill.

## Evaluations

The cases, the grading questions, and the comparison method are in [`evals/README.md`](evals/README.md). The `use` cases add context fit and clarity to the five questions. The prompts and pass/fail checks are in [`evals/evals.json`](evals/evals.json). Copy [`evals/runs/scorecard.md`](evals/runs/scorecard.md) for each session.

Give the model the prompt only. Run it with Sayso and without Sayso, on the same model, and repeat the pair before treating a difference as stable. One win is not proof. A small sample is not statistical significance. A run can show a better answer, a similar answer, or a worse one.

Check the suite, and the hand-written weak and better fixtures, with:

```bash
python evals/check_suite.py
```

That command uses Python's standard library. It does not call a model. The fixtures show that the objective checks can tell those written answers apart. They are not a Sayso result. [`evals/runs/2026-10-27-examples.json`](evals/runs/2026-10-27-examples.json) is one pass of the eight `examples` prompts, from before the skill was rewritten around the reader's job. Score it with `python evals/check_suite.py evals/runs/2026-10-27-examples.json`. On that day the checker passed 14 answers and failed both threshold answers, because those answers explained the exception without using the phrases the check looks for. That phrase list was later removed. Re-scoring the file does not replay the exit code. Read [`evals/runs/2026-10-27-examples.md`](evals/runs/2026-10-27-examples.md). Several answers were the same either way, and the threshold explanation written with the skill was harder to read.

[`evals/runs/2026-10-27-use.json`](evals/runs/2026-10-27-use.json) is one later pass of the eleven `use` prompts, after that rewrite. [`evals/runs/2026-10-27-use-trial2.json`](evals/runs/2026-10-27-use-trial2.json) repeats three of them. Read [`evals/runs/2026-10-27-use.md`](evals/runs/2026-10-27-use.md) before treating either file as a result. Most pairs were similarly usable. The hash explanation was longer with the skill both times it was tried. The first code review with the skill omitted a missing-file failure that the other review reported, and a second trial did not repeat that split. The first text-to-Sam session without the skill did not return the message; the second trial returned it unchanged on both sides. The checker exits 1 on both saved files. Part of the first exit was a phrase check, later corrected, and part of it was those disagreements. One file is not a repeated result.

[`evals/reports/2026-10-27-full37-summary.md`](evals/reports/2026-10-27-full37-summary.md) is one pass of all 37 prompts, one fresh session per condition. Sayso was loaded by reading the skill file. It did not show a consistent improvement. The answers are in [`evals/runs/2026-10-27-full37.json`](evals/runs/2026-10-27-full37.json).

To run a comparison in Cursor:

1. Start a new chat, invoke `/sayso`, and paste one `prompt` from `evals/evals.json`.
2. Start another new chat, do not invoke Sayso, and paste the same prompt.
3. Grade both answers on that case's assertions and dimensions in a copy of the scorecard.
4. Record the model, any setting you can see, the date, and how many runs you did.

[`evals/runs/2026-10-27-notes.md`](evals/runs/2026-10-27-notes.md) and [`evals/runs/2026-10-27-five-cases.md`](evals/runs/2026-10-27-five-cases.md) are two earlier passes from that date. Each is one run per condition, on prompts from before the `use` set. Read the conditions in those files before treating either as a result for the files you have now.

## Limits

- A model can ignore the skill, follow part of it, or rewrite something it should have left alone.
- Models do not respond to the same instructions in the same way.
- Sayso tells the model not to invent facts. It does not look facts up, and the model can still invent them.
- Sayso does not detect or remove "AI writing."
- There is nothing to configure.

## Contributing

### Tell us about a miss

1. Save the prompt and the answer.
2. Note the model if you know it, and what you wanted instead.
3. Open an issue: [github.com/Charlsz/sayso/issues](https://github.com/Charlsz/sayso/issues).

A useful report is a real task where Sayso made the answer worse, changed a voice it should have kept, dropped a limit or a bug, or rewrote a draft that was already good.

### Change the instructions

1. Fork the repo and make a branch.
2. For a mistake that shows up on many kinds of tasks, edit `SKILL.md`.
3. For a mistake that only shows up in one kind of task, edit the matching file in `references/`. If you add a new reference file, add one line in `SKILL.md` that says when to read it.
4. Before keeping the change, run the same prompt in two new chats on the same model: one with Sayso loaded, one without it. Read both. Keep the change if the Sayso answer is actually better.
5. Open a pull request. Include the prompt and both answers, or say that you could not run the comparison.

Keep `SKILL.md` short enough to read in one sitting. Add a case to `evals/evals.json` when you can describe the prompt, what a good result does, and a failure someone can see in the answer. Include tasks that should stay formal or highly structured, and tasks where the right move is to leave the draft alone. The comparison method is in [`evals/README.md`](evals/README.md).

### Check the format

The spec checker looks at the frontmatter and the folder name. It does not judge the writing.

```bash
uvx --from git+https://github.com/agentskills/agentskills#subdirectory=skills-ref skills-ref validate .
```

Run that from the `sayso` folder. On October 27, 2026, `uvx` was not installed, so `skills-ref` was installed with pip into a temporary environment and `skills-ref validate` was run on this directory. The checker reported: `Valid skill`. That check looks at the frontmatter and the folder name. It does not judge the instructions. Re-run it after changing the frontmatter.

## Site

`docs/` is a static page. To publish it, open the repository settings, choose Pages, and set the source to branch `main` and folder `/docs`. GitHub then serves it at [charlsz.github.io/sayso](https://charlsz.github.io/sayso/).

## License

[MIT](LICENSE). Copyright (c) 2026 Charlsz.
