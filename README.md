# Skills

Two skills I use for interface design and SQL. Each is a self-contained folder with a `SKILL.md` file.

- [Interaction design](skills/interaction-design-v2/SKILL.md) guides custom interactions, visual hierarchy, progressive disclosure, and reviews through the audience's eyes.
- [SQL style](skills/sql-style/SKILL.md) defines compact analytical SQL, with separate rules for short queries and production reporting.

## Install in Codex

Ask Codex:

```text
Use $skill-installer to install both skills from https://github.com/dr-baker/skills:
skills/interaction-design-v2 and skills/sql-style.
```

See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for local discovery and installation.

## Use a skill

Invoke either skill explicitly:

```text
$interaction-design-v2 Review this workflow through the audience's eyes.
$sql-style Optimize this query and verify that the results match.
```

For other agents that support `SKILL.md`, add the desired skill folder to the agent's configured skills directory.
