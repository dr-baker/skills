---
name: git-style
description: Daniel's git workflow across all projects — first-parent history should read like a changelog, with multi-commit features built on branches in copy-on-write worktrees and landed as no-ff merges, while small single-concept work commits straight to main. Use when starting substantive feature or implementation work in a git repo, creating a branch or worktree, committing, merging, or deciding how work should land.
---

# Git Style

The goal: `git log --first-parent main` reads like a changelog. Big features appear as one merge entry each; small fixes appear as single commits. Someone skimming history should understand what happened to the product without opening a diff.

## Where work happens

- Work that will take several commits, could break main, or runs alongside other work: build it on a branch in an isolated worktree. Use `$cow-worktree` to create it.
- Small single-concept changes: commit directly on main.
- When unsure, start on a branch — it can always be merged early.

## Landing work

- Write commits with `$commit-style` — each one a coherent, changelog-quality chunk.
- Merge feature branches with `--no-ff` using a `$merge-commit-style` message, so the feature clumps under one readable entry.
- Do not fast-forward a feature branch into main; that scatters the clump across first-parent history.
- For substantial branches, review the diff and commit list and run verification before merging.

## Testing branch work

- If the project can be run from the worktree (CLI tools, servers, scripts, anything with a runnable entry point), ask the user whether to run it from the worktree before reaching for a merge.
- Xcode projects usually cannot be tested sensibly from a worktree, so merging a branch early into main to test in the real app is a legitimate move there, not a shortcut to apologize for: still use `--no-ff` and a real merge message, then keep iterating — amend the merge message or land follow-ups as new commits or a fresh branch. Never let message ceremony or review ceremony delay a merge the user wants now; say the review was skipped and move on.

## Delegation

Orchestration is harness-specific — use whatever worker or subagent tooling is available. Workers implement inside the worktree and commit with `$commit-style`; give them the worktree path, exact scope, and `do not merge`. Review and merge authority stays with the main agent.

## Per-project variance

These are defaults, deliberately loose. A project's AGENTS.md or CLAUDE.md may override any of it — protected main, PR-based flow, different branch policy. Project instructions win.
