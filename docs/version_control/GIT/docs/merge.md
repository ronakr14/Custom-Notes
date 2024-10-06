# Git Merge Commands

## Overview

The `git merge` command is used to integrate changes from one branch into another. It combines the changes made in different branches and helps in synchronizing work. This document covers the basic and advanced usage of `git merge`.

## Basic Merge

### `git merge <branch>`

Merges the specified branch into the current branch.

```sh
git merge <branch>
```

#### Example

```sh
git checkout main
git merge feature-branch
```

This command merges changes from `feature-branch` into the `main` branch.

## Merge with Fast-Forward

### `git merge --ff <branch>`

Performs a fast-forward merge if possible. This is the default behavior when the current branch is a direct ancestor of the branch being merged.

```sh
git merge --ff <branch>
```

#### Example

```sh
git checkout main
git merge --ff feature-branch
```

This command performs a fast-forward merge if `main` is a direct ancestor of `feature-branch`.

## Merge with No Fast-Forward

### `git merge --no-ff <branch>`

Performs a merge with a merge commit, even if a fast-forward merge is possible. This is useful for preserving the history of the branch being merged.

```sh
git merge --no-ff <branch>
```

#### Example

```sh
git checkout main
git merge --no-ff feature-branch
```

This command creates a merge commit even if the `feature-branch` can be fast-forwarded into `main`.

## Merge with Commit Message

### `git merge --no-commit <branch>`

Merges the specified branch into the current branch but does not automatically create a commit. This allows you to review changes before committing.

```sh
git merge --no-commit <branch>
```

#### Example

```sh
git checkout main
git merge --no-commit feature-branch
```

This command merges `feature-branch` into `main` without committing the merge, allowing you to review and modify changes before committing.

## Merge with Strategy

### `git merge -s <strategy> <branch>`

Uses a specific merge strategy to combine changes. Common strategies include `recursive`, `ours`, and `theirs`.

```sh
git merge -s <strategy> <branch>
```

#### Example

```sh
git checkout main
git merge -s ours feature-branch
```

This command uses the `ours` strategy to merge `feature-branch` into `main`, favoring the current branch's changes.

## Merge with Message

### `git merge -m "<message>" <branch>`

Merges the specified branch and includes a custom commit message for the merge commit.

```sh
git merge -m "<message>" <branch>
```

#### Example

```sh
git checkout main
git merge -m "Merge feature-branch into main" feature-branch
```

This command merges `feature-branch` into `main` with the specified commit message.

## Resolve Merge Conflicts

### Handling Conflicts

If conflicts arise during a merge, Git will pause the merge process and mark the conflicting files. You need to manually resolve these conflicts and then complete the merge.

#### Example

```sh
git merge feature-branch
# Resolve conflicts in the files
git add <resolved-file>
git commit
```

This process involves resolving conflicts in files marked by Git, staging the resolved files, and then committing the merge.

## Summary

The `git merge` command is a key tool for integrating changes from one branch into another. It provides options for fast-forward merges, preserving history, and using specific merge strategies. Handling merge conflicts is a common part of the merging process, requiring manual resolution before finalizing the merge. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).