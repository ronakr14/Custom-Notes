# Git Branch Commands

## Overview

The `git branch` command is used to manage branches in a Git repository. Branches allow you to work on separate features or fixes independently from the main codebase. This document covers the basic and advanced usage of `git branch`.

## Listing Branches

### `git branch`

Lists all local branches in the repository.

```sh
git branch
```

#### Example

```sh
git branch
```

This command lists all local branches and highlights the current branch with an asterisk.

### `git branch -r`

Lists all remote branches.

```sh
git branch -r
```

#### Example

```sh
git branch -r
```

This command lists all branches available on the remote repository.

### `git branch -a`

Lists all local and remote branches.

```sh
git branch -a
```

#### Example

```sh
git branch -a
```

This command lists all local and remote branches in the repository.

## Creating Branches

### `git branch <branch>`

Creates a new branch with the specified name.

```sh
git branch <branch>
```

#### Example

```sh
git branch feature-branch
```

This command creates a new branch named `feature-branch`.

## Deleting Branches

### `git branch -d <branch>`

Deletes a local branch safely, preventing deletion if it contains unmerged changes.

```sh
git branch -d <branch>
```

#### Example

```sh
git branch -d feature-branch
```

This command deletes the `feature-branch` if it has been fully merged into the current branch.

### `git branch -D <branch>`

Forcefully deletes a local branch, regardless of its merge status.

```sh
git branch -D <branch>
```

#### Example

```sh
git branch -D feature-branch
```

This command forcefully deletes the `feature-branch`, even if it has unmerged changes.

## Renaming Branches

### `git branch -m <old-branch> <new-branch>`

Renames a local branch.

```sh
git branch -m <old-branch> <new-branch>
```

#### Example

```sh
git branch -m old-feature-branch new-feature-branch
```

This command renames the local branch from `old-feature-branch` to `new-feature-branch`.

### `git branch -m <new-branch>`

Renames the current branch.

```sh
git branch -m <new-branch>
```

#### Example

```sh
git branch -m new-branch
```

This command renames the current branch to `new-branch`.

## Switching Branches

### `git checkout <branch>`

Switches to the specified branch.

```sh
git checkout <branch>
```

#### Example

```sh
git checkout main
```

This command switches to the `main` branch.

### `git switch <branch>`

Switches to the specified branch (alternative to `git checkout`).

```sh
git switch <branch>
```

#### Example

```sh
git switch main
```

This command switches to the `main` branch using the `git switch` command.

## Creating and Switching Branches

### `git checkout -b <branch>`

Creates a new branch and switches to it.

```sh
git checkout -b <branch>
```

#### Example

```sh
git checkout -b feature-branch
```

This command creates a new branch named `feature-branch` and switches to it.

### `git switch -c <branch>`

Creates a new branch and switches to it (alternative to `git checkout -b`).

```sh
git switch -c <branch>
```

#### Example

```sh
git switch -c feature-branch
```

This command creates a new branch named `feature-branch` and switches to it using the `git switch` command.

## Tracking Remote Branches

### `git branch --track <branch> <remote>/<branch>`

Creates a new local branch that tracks a remote branch.

```sh
git branch --track <branch> <remote>/<branch>
```

#### Example

```sh
git branch --track feature-branch origin/feature-branch
```

This command creates a new local branch `feature-branch` that tracks the `origin/feature-branch` remote branch.

## Summary

The `git branch` command is crucial for managing branches within your Git repository. It allows you to create, delete, rename, and list branches, as well as switch between them and track remote branches. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).