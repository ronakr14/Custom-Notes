# Git Pull Commands

## Overview

The `git pull` command is used to fetch and integrate changes from a remote repository into your local repository. This command combines `git fetch` and `git merge`, automatically merging the fetched changes into the current branch. This document covers the basic and advanced usage of `git pull`.

## Basic Pull

### `git pull`

Fetches changes from the configured upstream branch and merges them into the current branch.

```sh
git pull
```

#### Example

```sh
git pull
```

This command fetches and merges changes from the upstream branch of the current branch.

### `git pull <remote> <branch>`

Fetches changes from a specific remote branch and merges them into the current branch.

```sh
git pull <remote> <branch>
```

#### Example

```sh
git pull origin main
```

This command fetches and merges changes from the `main` branch of the `origin` remote into the current branch.

## Pull with Rebase

### `git pull --rebase`

Fetches changes from the configured upstream branch and rebases the current branch on top of them instead of merging.

```sh
git pull --rebase
```

#### Example

```sh
git pull --rebase
```

This command fetches changes from the upstream branch and rebases the current branch on top of them.

### `git pull --rebase <remote> <branch>`

Fetches changes from a specific remote branch and rebases the current branch on top of them.

```sh
git pull --rebase <remote> <branch>
```

#### Example

```sh
git pull --rebase origin main
```

This command fetches changes from the `main` branch of the `origin` remote and rebases the current branch on top of them.

## Specifying a Rebase Strategy

### `git pull --rebase=interactive`

Uses interactive rebase during the pull operation.

```sh
git pull --rebase=interactive
```

#### Example

```sh
git pull --rebase=interactive
```

This command fetches changes from the upstream branch and allows you to interactively rebase the current branch on top of them.

## Pull with Auto-stash

### `git pull --autostash`

Stashes local changes before pulling and re-applies them after the pull.

```sh
git pull --autostash
```

#### Example

```sh
git pull --autostash
```

This command stashes any local changes, pulls changes from the upstream branch, and then reapplies the stashed changes.

## Pulling Specific Commits

### `git pull --depth <depth>`

Fetches only the specified number of commits from the remote repository.

```sh
git pull --depth <depth>
```

#### Example

```sh
git pull --depth 1
```

This command fetches only the latest commit from the remote repository.

## Fetch and Merge

### `git fetch` and `git merge`

Fetches changes from a remote repository and merges them into the current branch in two separate steps.

```sh
git fetch <remote>
git merge <remote>/<branch>
```

#### Example

```sh
git fetch origin
git merge origin/main
```

This sequence of commands fetches changes from the `main` branch of the `origin` remote and merges them into the current branch.

## Summary

The `git pull` command is a convenient way to fetch and integrate changes from a remote repository. It can be customized to suit different workflows, such as using rebase instead of merge or stashing changes before pulling. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
