---
name: house-skills
description: How Daniel's skills are organized — the canonical git-tracked home, symlink rules, and procedures for adding, editing, moving, or retiring a skill. Use when creating or installing a skill, editing an existing skill's file, or deciding where a skill should live.
---

# House Skills

One canonical copy per skill. Harness directories contain symlinks, never copies — stale copies drifting apart was the historical failure mode.

## Layout

- `~/.agents/skills/` — canonical home for every skill. `~/.agents` is the checkout of `https://github.com/dr-baker/skills`. All edits land here (editing through a harness symlink is fine — same file).
- The public repo tracks only the skill folders explicitly allowed in `~/.agents/.gitignore`. Other skills stay in the same canonical folder, local and ignored. Add a folder to the public allowlist only when Daniel asks to publish it.
- `~/.claude/skills/` and `~/.codex/skills/` — symlink farms pointing into the home. Real directories are allowed only for harness internals:
  - Claude: `create-agent`, `subagents`
  - Codex: `codex-primary-runtime`, `usage-codex`, and `model-subagents` (its `runs/` dir is live runner infrastructure with absolute paths in logs — never move it)
- `~/Developer/pi Config/skills/` — symlinks into the home; kept so pi finds its skills.
- `~/.agents/skills-archive/` — retired skills. Archive rather than delete unless told otherwise.
- `~/.agents/.local-history/pre-public-2026-10-02/git/` — the original local Git metadata, preserved before adopting the public repo's history. Keep it local. Read its history with `git --git-dir="$HOME/.agents/.local-history/pre-public-2026-10-02/git" log`.

## Procedures

**Add a skill:** create `~/.agents/skills/<name>/SKILL.md`, then link it into each harness that should see it:

```bash
ln -s ../../.agents/skills/<name> ~/.claude/skills/<name>
ln -s ../../.agents/skills/<name> ~/.codex/skills/<name>
```

**Edit a skill:** follow the symlink and edit the canonical file. Never copy a skill directory into a harness dir.

**Retire a skill:** move the canonical dir into `~/.agents/skills-archive/` and remove the harness symlinks.

**Scripts inside skills** must reference their own files via `~/.agents/skills/<name>/...` paths.

**Commit** public skill changes in `~/.agents` using `$commit-style`, then push that repo when publication is authorized. Unpublished skills are ignored by the public repo; never force-add them to bypass the allowlist.
