---
name: agents-md-charter
description: How Daniel likes AGENTS.md files written — a slim project charter, not documentation. Use when creating or editing an AGENTS.md or CLAUDE.md for any project.
---

# AGENTS.md Charter Style

An AGENTS.md is a slim charter that onboards an agent fast and points it where to go. It is not documentation. Agents are good at searching code, and implementation detail belongs in plan files — never duplicate either here.

Keep it to roughly one page with these sections:

1. **What we're after** — the endgame in a paragraph or two, plus the handful of concepts that drive the work. Written so a fresh agent understands *why* the project exists, not just what it is.
2. **Where to go** — one line per directory/doc pointing to plans, source modules, and the README. Pointers only, no descriptions of internals.
3. **Ground rules** — only the invariants that must never be violated (a few bullets, not a style guide).
4. **Vocabulary** — shared project terms so humans and agents use the same words. Homemade acronyms are encouraged (e.g. FFD = fat-finger detection); define each in one line.

CLAUDE.md should be one or two lines pointing at AGENTS.md — never a second copy of it.

When the project's goals shift, update the charter's endgame paragraph rather than appending history; history lives in plans and git.
