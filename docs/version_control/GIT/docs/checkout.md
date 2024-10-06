# Git Checkout Commands

## Overview

The `git checkout` command is used to switch between branches or restore working tree files. This document covers the basic and advanced usage of `git checkout`.

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

## Creating and Switching to a New Branch

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

## Checking Out a Specific Commit

### `git checkout <commit>`

Switches to a specific commit, putting the repository in a "detached HEAD" state.

```sh
git checkout <commit>
```

#### Example

```sh
git checkout 1a2b3c4d
```

This command switches to the commit with the hash `1a2b3c4d`.

## Checking Out a File from a Specific Commit

### `git checkout <commit> -- <file>`

Restores a specific file from a particular commit to the working directory.

```sh
git checkout <commit> -- <file>
```

#### Example

```sh
git checkout 1a2b3c4d -- README.md
```

This command restores the `README.md` file from the commit with the hash `1a2b3c4d` to the working directory.

## Discarding Changes in Working Directory

### `git checkout -- <file>`

Reverts changes in the working directory to match the HEAD commit.

```sh
git checkout -- <file>
```

#### Example

```sh
git checkout -- README.md
```

This command discards changes in `README.md`, reverting it to the state of the last commit.

## Checking Out a Branch from a Remote Repository

### `git checkout -b <new-branch> <remote>/<branch>`

Creates a new branch tracking a remote branch and switches to it.

```sh
git checkout -b <new-branch> <remote>/<branch>
```

#### Example

```sh
git checkout -b feature-branch origin/feature-branch
```

This command creates a new branch named `feature-branch` tracking the `origin/feature-branch` remote branch and switches to it.

## Checking Out a Specific Tag

### `git checkout tags/<tag>`

Switches to a specific tag.

```sh
git checkout tags/<tag>
```

#### Example

```sh
git checkout tags/v1.0.0
```

This command switches to the `v1.0.0` tag.

## Undoing a Checkout

### `git checkout -`

Switches back to the previous branch.

```sh
git checkout -
```

#### Example

```sh
git checkout -
```

This command switches back to the branch you were previously on.

## Summary

The `git checkout` command is versatile and can be used to switch branches, create new branches, check out specific commits, and restore files. It is an essential command for navigating and managing your Git repository. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).