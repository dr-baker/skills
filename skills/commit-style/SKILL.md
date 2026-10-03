---
name: commit-style
description: Review a diff, split independent changes into separate commits, and write commit messages with a changelog-style feature name followed by clear technical details. Use when asked to commit changes, split a diff into multiple commits, or write messages in Daniel's style.
---

# Commit Style

Use this skill to do two things:

1. Group changes by concept.
- Split independent concepts into separate commits.
- Do not mix feature work, cleanup, refactors, bug fixes, styling, logging, or experiments unless one is required for the other.
- If part of the diff could be reverted independently, it should usually be its own commit.
- Do not hide mixed work under `misc`, `cleanup`, or `tweaks`.

2. Write clear, two-layer commit messages.
- Make the first line a short feature name or user-facing outcome that would make sense in a business changelog.
- Usually use lowercase for focused commits; capitalize proper names when needed.
- Use the body for technical detail that helps developers track behavior, constraints, tests, regressions, and follow-up work.
- Usually include a few bullets with the important details.
- Skip the body only if the commit is truly self-documenting.
- Do not use conventional-commit prefixes.

3. Prefer clear communication over internal shorthand.
- Name the user-facing capability or outcome in the first line, then name the implementation details in the body.
- Use concrete language in both layers: say what changed, where it changed, and why it matters when that context is useful.
- Replace vague phrases such as `updated`, `improved`, `current scale`, or `handled` with the specific behavior or outcome.
- Make each body bullet express one clear idea; include measurements or constraints there when they matter.

Prefer:

```text
reliable Codex text-field detection
correction learning in Codex
```

Avoid:

```text
made Codex focus resolution safe at current scale
updated focus handling
```

Default format:

```text
reliable Codex text-field detection

- prefer system-wide direct focus before bounded fallback traversal
- reject stale or ambiguous targets and cover the behavior with resolver tests
```

Before staging, tell the user how the changes are grouped. Then stage and commit each group deliberately.
