---
name: cow-worktree
description: Use when starting implementation work that should happen in an isolated copy-on-write Git worktree under agent_features/.worktrees.
---

# COW Worktree

Before editing files, create an isolated worktree with the bundled skill script.
Do not look for this helper in the target repo's `scripts/` folder.

Default policy unless the user explicitly says otherwise:

- Start from committed `HEAD`.
- Allow dirty source checkouts.
- Ignore staged, unstaged, untracked, and ignored source changes.
- Require copy-on-write creation.
- Fail if copy-on-write is unavailable.
- Work only inside the created worktree.
- Do not merge.

Run the installed helper:

```bash
~/.agents/skills/cow-worktree/scripts/create-cow-worktree --branch <branch-name> --worktree agent_features/.worktrees/<slug>
```

The script defaults to:

```text
dirty-policy=head
clone-mode=require
base=HEAD
```

If the source checkout is dirty, tell the user:

```text
Source checkout has uncommitted changes; the worktree starts from HEAD and ignores them.
```

After creation, `cd` into the worktree and do all work there. Final response must include the worktree path, branch/base, and verification run.
