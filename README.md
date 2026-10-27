# Sayso

Sayso is an open-source [Agent Skill](https://agentskills.io/specification) that helps a model decide what a task needs before it writes.

A capable answer can still be generic, padded, repetitive, or shaped for the wrong situation. Sayso is a short set of instructions for those decisions. A text to a friend, a professional email, a scientific abstract, a news brief, a technical document, and a code review do not share one standard. Formal, technical, and highly structured writing stay that way when the task calls for them. A draft that is already good should be left alone.

Sayso does not install a house style, and it does not turn every answer into something shorter or more casual. Correctness comes before polish. A tendency is not a guarantee, and a review does not stop once the obvious bugs are listed. It is an experiment. Instructions can improve judgment. They cannot guarantee a correct answer, and they do not remove the limits of the model underneath.

You do not need Python, Node, or an API key to use it.

## Install

The skill is this folder. The folder has to be named `sayso`, and `SKILL.md` has to sit directly inside it. Your agent loads skills from its own skills folder. Cloning this repository, or opening it in an editor, does not install the skill.

These steps come from [Cursor's skills docs](https://cursor.com/docs/skills) and the [Codex skills docs](https://developers.openai.com/codex/skills). They were not click-tested inside each app.

### On your computer (Cursor and Codex)

This puts Sayso on every local project for both Cursor and Codex.

Windows, in PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
git clone https://github.com/Charlsz/sayso.git "$env:USERPROFILE\.agents\skills\sayso"
```

macOS and Linux:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Charlsz/sayso.git ~/.agents/skills/sayso
```

If you already have the files, copy them instead of cloning. Run this from your copy of the repo, not from inside the skills folder. The folder you run it in is the one that contains `SKILL.md`:

```powershell
$dest = "$env:USERPROFILE\.agents\skills\sayso"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
Copy-Item -Recurse -Force .\* $dest
```

```bash
mkdir -p ~/.agents/skills/sayso
cp -R . ~/.agents/skills/sayso
```

The last folder in the path still has to be named `sayso`.

Check that this file exists:

- Windows: `%USERPROFILE%\.agents\skills\sayso\SKILL.md`
- macOS and Linux: `~/.agents/skills/sayso/SKILL.md`

Then start a **new** chat.

- In Cursor, type `/sayso` and choose Sayso. That attaches it to one message. Option+Enter on a Mac, or Alt+Enter on Windows, keeps it on for the session as a Custom Mode.
- In Codex CLI or the IDE extension, type `$` or run `/skills` and choose Sayso. Codex can also select it when the task matches the description.

Codex picks up a newly copied skill on its own. If it does not appear, restart Codex. The usual miss is a folder named something other than `sayso`, or `SKILL.md` nested one level too deep (`sayso/sayso/SKILL.md`).

### For one project only

From that project's root:

```bash
mkdir -p .agents/skills
git clone https://github.com/Charlsz/sayso.git .agents/skills/sayso
```

Commit `.agents/skills/sayso` if teammates should get the same skill from the repo. Cursor also reads `.cursor/skills/sayso/` in a project. Either location works for Cursor. Codex reads `.agents/skills/`.

### Cursor Cloud Agents

A copy in `~/.agents/skills/` stays on your machine. Cursor's docs say it does not copy that folder to Cloud Agents, remote SSH sessions, or self-hosted workers. For a Cloud Agent, commit the skill in the repository at `.agents/skills/sayso/` or `.cursor/skills/sayso/`. Skills in `~/.cursor/skills/` can be synced for Cloud Agents you start yourself: Settings → Agents → Context and Tools → Sync Skills for Cloud Agents. That sync does not include `~/.agents/skills/`, and the same docs say automation runs do not load the synced copy.

### Other agents

Any agent that supports the Agent Skills format can use this folder. Put it where that agent looks for skills, and keep the folder name `sayso`. Check that agent's own docs for the path. A path that is not listed above has not been verified for Sayso.

## Use it

Ask for the work the way you normally would: an explanation, a rewrite, an email, a summary, documentation, or a review. You can also invoke Sayso first, then ask.

The answer should not mention Sayso or walk through a checklist. In Cursor, Option+Enter on a Mac, or Alt+Enter on Windows, keeps the selected skill on for the session as a Custom Mode.

If an edit comes back colder, shorter, or more casual than the task deserves, that is a miss. So is a rewrite of a draft that was already doing its job, a technical claim stated more strongly than it holds, or a review that stops before a consequential bug.

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

The reference files are for the agent, and only when the task matches. You can ignore `evals/` if you only want to use the skill.

## Evaluations

The cases, the five grading questions, and the comparison method are in [`evals/README.md`](evals/README.md). The prompts and pass/fail checks are in [`evals/evals.json`](evals/evals.json). Copy [`evals/runs/scorecard.md`](evals/runs/scorecard.md) for each session.

Give the model the prompt only. Run it with Sayso and without Sayso, on the same model, and repeat the pair before treating a difference as stable. One win is not proof. A small sample is not statistical significance.

To run a comparison in Cursor:

1. Start a new chat, invoke `/sayso`, and paste one `prompt` from `evals/evals.json`.
2. Start another new chat, do not invoke Sayso, and paste the same prompt.
3. Grade both answers on that case's assertions and dimensions in a copy of the scorecard.
4. Record the model, any setting you can see, the date, and how many runs you did.

[`evals/runs/2026-10-27-notes.md`](evals/runs/2026-10-27-notes.md) and [`evals/runs/2026-10-27-five-cases.md`](evals/runs/2026-10-27-five-cases.md) are two separate passes from that date. Each is one run per condition. Read the conditions in those files before treating either as a result for the files you have now.

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

## License

[MIT](LICENSE). Copyright (c) 2026 Charlsz.
