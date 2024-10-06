# Git Rebase Commands

## Overview

The `git rebase` command allows you to integrate changes from one branch into another. It is an alternative to merging and can create a cleaner project history by moving or combining a sequence of commits.

## Basic Rebase

### `git rebase <branch>`

Rebases the current branch onto the specified branch.

```sh
git rebase <branch>
```

#### Example

```sh
git rebase main
```

This command moves the commits from the current branch on top of the `main` branch.

## Interactive Rebase

### `git rebase -i <base>`

Starts an interactive rebase session, allowing you to edit, reorder, or squash commits.

```sh
git rebase -i <base>
```

#### Example

```sh
git rebase -i HEAD~3
```

This command starts an interactive rebase session for the last three commits.

## Rebase Onto Another Branch

### `git rebase --onto <newbase> <upstream> <branch>`

Rebases the `branch` starting from `upstream` onto `newbase`.

```sh
git rebase --onto <newbase> <upstream> <branch>
```

#### Example

```sh
git rebase --onto main feature~1 feature
```

This command rebases the `feature` branch onto `main`, starting from one commit before the tip of `feature`.

## Continue, Skip, and Abort Rebase

### `git rebase --continue`

Continues the rebase after resolving conflicts.

```sh
git rebase --continue
```

#### Example

```sh
git rebase --continue
```

This command continues the rebase process after you have resolved conflicts.

### `git rebase --skip`

Skips the current patch during a rebase.

```sh
git rebase --skip
```

#### Example

```sh
git rebase --skip
```

This command skips the current commit during the rebase.

### `git rebase --abort`

Aborts the rebase and resets the branch to the state before the rebase began.

```sh
git rebase --abort
```

#### Example

```sh
git rebase --abort
```

This command aborts the rebase process and returns the branch to its original state.

## Rebasing vs. Merging

### Rebasing

Rebasing rewrites the commit history by creating new commits for each commit in the original branch, but with a new base. This can result in a cleaner, linear project history.

#### Example

```sh
git checkout feature
git rebase main
```

This sequence moves the `feature` branch commits on top of the `main` branch.

### Merging

Merging preserves the commit history and creates a new merge commit that includes changes from both branches.

#### Example

```sh
git checkout main
git merge feature
```

This sequence merges the `feature` branch into the `main` branch, creating a merge commit.

## Summary

The `git rebase` command is a powerful tool for streamlining and cleaning up your commit history. It is particularly useful for integrating changes from one branch to another in a linear fashion. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
