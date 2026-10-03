# Skills

My personal skills for interface design, SQL, and Git workflows.

- [Interaction design](skills/interaction-design-v2/SKILL.md) guides custom interactions, visual hierarchy, progressive disclosure, and reviews through the audience's eyes.
- [SQL style](skills/sql-style/SKILL.md) defines compact analytical SQL, with separate rules for short queries and production reporting.
- [AGENTS.md charter](skills/agents-md-charter/SKILL.md) keeps project instructions focused on goals, pointers, invariants, and vocabulary.
- [Commit style](skills/commit-style/SKILL.md) groups changes by concept and writes commits as changelog entries.
- [Git style](skills/git-style/SKILL.md) organizes feature work and merges so first-parent history reads like a changelog.
- [Merge commit style](skills/merge-commit-style/SKILL.md) summarizes a feature branch as one useful changelog entry.
- [COW worktree](skills/cow-worktree/SKILL.md) creates isolated Git worktrees using APFS copy-on-write file clones, including pinned submodules. It requires macOS.

## Keep one source folder

For a fresh installation, clone the repository into `~/.agents`:

```bash
git clone https://github.com/dr-baker/skills.git ~/.agents
```

Keep the raw skill folders in `~/.agents/skills`. Link the skills you want into each agent's configured skills directory. For example:

```bash
mkdir -p ~/.codex/skills ~/.claude/skills
ln -s ~/.agents/skills/commit-style ~/.codex/skills/commit-style
ln -s ~/.agents/skills/commit-style ~/.claude/skills/commit-style
```

Create a link where that name is unused. Repeat for each desired skill and agent. Edits through a symlink change the same source file, and `git pull` updates that source.

Codex also discovers `~/.agents/skills` directly. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and invocation.

The `.gitignore` allows only named public skill folders. Other skills can live in the same source folder while staying local. To publish another skill, review its files and add its folder to that list before staging it.

## Use a skill

```text
$interaction-design-v2 Review this workflow through the audience's eyes.
$sql-style Optimize this query and verify that the results match.
$commit-style Split this diff into coherent commits.
```
