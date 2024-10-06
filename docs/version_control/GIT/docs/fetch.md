# Git Fetch Commands

## Overview

The `git fetch` command downloads objects and refs from another repository. This command is essential for updating your local repository with the latest changes from a remote repository without merging them into your local branch. This document covers the basic and advanced usage of `git fetch`.

## Basic Fetch

### `git fetch`

Fetches updates from the default remote repository (usually `origin`).

```sh
git fetch
```

#### Example

```sh
git fetch
```

This command fetches updates from the `origin` remote repository without merging them into your local branch.

### `git fetch <remote>`

Fetches updates from a specific remote repository.

```sh
git fetch <remote>
```

#### Example

```sh
git fetch origin
```

This command fetches updates from the `origin` remote repository.

## Fetching Specific Branches

### `git fetch <remote> <branch>`

Fetches updates from a specific branch of a remote repository.

```sh
git fetch <remote> <branch>
```

#### Example

```sh
git fetch origin main
```

This command fetches updates from the `main` branch of the `origin` remote repository.

## Fetching All Branches

### `git fetch --all`

Fetches updates from all configured remotes and their branches.

```sh
git fetch --all
```

#### Example

```sh
git fetch --all
```

This command fetches updates from all remote repositories and their branches configured in your local repository.

## Pruning Deleted Branches

### `git fetch --prune`

Prunes (removes) tracking references that no longer exist on the remote.

```sh
git fetch --prune
```

#### Example

```sh
git fetch --prune
```

This command removes any tracking branches that have been deleted on the remote repository.

## Fetching Tags

### `git fetch --tags`

Fetches all tags from the remote repository.

```sh
git fetch --tags
```

#### Example

```sh
git fetch --tags
```

This command fetches all tags from the remote repository.

## Fetching with Depth

### `git fetch --depth <depth>`

Fetches only the specified number of commits from the remote repository.

```sh
git fetch --depth <depth>
```

#### Example

```sh
git fetch --depth 1
```

This command fetches only the latest commit from the remote repository.

## Specifying Refspecs

### `git fetch <remote> <refspec>`

Fetches a specific refspec from a remote repository.

```sh
git fetch <remote> <refspec>
```

#### Example

```sh
git fetch origin refs/heads/main:refs/remotes/origin/main
```

This command fetches the `main` branch from the `origin` remote and updates the corresponding remote-tracking branch in your local repository.

## Fetching All Remote Branches

### `git fetch <remote> +refs/heads/*:refs/remotes/<remote>/*`

Fetches all branches from a remote repository and updates the corresponding remote-tracking branches.

```sh
git fetch <remote> +refs/heads/*:refs/remotes/<remote>/*
```

#### Example

```sh
git fetch origin +refs/heads/*:refs/remotes/origin/*
```

This command fetches all branches from the `origin` remote and updates the corresponding remote-tracking branches in your local repository.

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

The `git fetch` command is a powerful tool for updating your local repository with the latest changes from a remote repository without merging them immediately. This allows you to review changes before integrating them into your work. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
