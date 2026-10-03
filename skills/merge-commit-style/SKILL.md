---
name: merge-commit-style
description: Writes feature-branch merge commit messages as changelog entries in Daniel's commit style — a plain changelog-style subject with no prefix, an optional user-facing summary, and short technical bullets drawn from the actual branch commits. Use when merging a branch, writing or editing a merge commit message, or summarizing a branch for a merge.
---

# Merge Commit Style

A merge commit is the changelog entry for its branch. In first-parent history, merges are the headline entries and direct-to-main commits are the small ones — both should read the same way. This skill applies the same rules as `$commit-style`, scaled up to a whole branch.

## Subject

- Make the first line a short feature name or user-facing outcome that would make sense in a business changelog — the same shape `$commit-style` uses for a single commit.
- No prefixes. Not `feat:`, not `merge:`, not `Merge branch 'x'`. The graph already shows it is a merge; the subject's only job is to name what landed.
- Usually lowercase; capitalize proper names when needed.
- Summarize the branch as a whole, not its largest commit and not one symptom.

Prefer:

```text
project templates
provider health visibility
smarter wrist filtering
```

Avoid:

```text
Merge branch 'feature/templates'
feat: add project templates
misc branch updates
fix template bug
```

## Body

- If the branch changes UX, open with one plain sentence describing the user-visible outcome. Skip this when there is no user-facing change.
- Then 2-4 technical bullets that summarize the branch by concept — what changed, what became possible, what was separated, what workflow improved.
- Group the branch's commits into themes; do not list every commit.
- Use concrete language: say what changed, where, and why it matters. Replace vague words like `updated`, `improved`, or `handled` with the specific behavior.
- One clear idea per bullet; put measurements or constraints there when they matter.

```text
project templates

Users can preview and choose a starter template before creating a project.

- add template discovery from configured template paths
- show template names and metadata in the creation flow
- validate missing metadata and unsupported template versions
```

## Workflow

1. Identify the base branch and feature branch, and find the merge base.
2. Read the commits unique to the branch:

```bash
git log --reverse --format='%h %s%n%b' $(git merge-base <base-ref> <branch-ref>)..<branch-ref>
```

3. Group the commits into 2-4 conceptual themes.
4. Write the subject and body per the rules above.
5. State base, branch, and the chosen message, then merge with `--no-ff`:

```bash
git merge --no-ff <branch-ref> -m "<subject>" -m "<body>"
```

## Hasty merges

When the user wants to merge quickly to test on main, skip all ceremony: write one good message on your own judgment and merge immediately. Do not present options or ask for approval. The message can be amended right after the merge (`git commit --amend`) if the summary needs improving once things settle.

## Proposing options

Only when the user explicitly asks for ideas or options: give a one-line read of the branch shape, 3-5 candidate messages in final format, and a brief recommendation.
