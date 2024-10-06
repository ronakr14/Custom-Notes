# Git Push Commands

## Overview

The `git push` command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repository. This document covers the basic and advanced usage of `git push`.

## Basic Push

### `git push`

Pushes the current branch to the configured upstream branch of the remote repository.

```sh
git push
```

#### Example

```sh
git push
```

This command pushes your current branch to its upstream branch on the remote repository.

### `git push <remote> <branch>`

Pushes a specific branch to a specific remote repository.

```sh
git push <remote> <branch>
```

#### Example

```sh
git push origin main
```

This command pushes the `main` branch to the `origin` remote.

## Setting Upstream Branch

### `git push -u <remote> <branch>`

Sets the upstream branch for the current branch and pushes the branch.

```sh
git push -u <remote> <branch>
```

#### Example

```sh
git push -u origin feature-branch
```

This command pushes the `feature-branch` to the `origin` remote and sets it as the upstream branch for the current branch.

## Force Push

### `git push --force`

Forces the push to the remote repository, overwriting the remote branch with your local branch.

```sh
git push --force
```

#### Example

```sh
git push --force origin main
```

This command forcefully pushes the `main` branch to the `origin` remote, overwriting any conflicting changes.

### `git push --force-with-lease`

Forces the push but only if the remote branch has not been updated since the last pull.

```sh
git push --force-with-lease
```

#### Example

```sh
git push --force-with-lease origin main
```

This command forcefully pushes the `main` branch to the `origin` remote but only if there are no new commits on the remote `main` branch.

## Pushing Tags

### `git push --tags`

Pushes all tags to the remote repository.

```sh
git push --tags
```

#### Example

```sh
git push --tags
```

This command pushes all your local tags to the remote repository.

## Deleting a Remote Branch

### `git push <remote> --delete <branch>`

Deletes a branch from the remote repository.

```sh
git push <remote> --delete <branch>
```

#### Example

```sh
git push origin --delete feature-branch
```

This command deletes the `feature-branch` from the `origin` remote.

## Pushing to Multiple Remotes

### `git push <remote1> <branch> && git push <remote2> <branch>`

Pushes a branch to multiple remote repositories.

```sh
git push <remote1> <branch> && git push <remote2> <branch>
```

#### Example

```sh
git push origin main && git push backup main
```

This command pushes the `main` branch to both the `origin` and `backup` remotes.

## Summary

The `git push` command is essential for transferring commits from your local repository to a remote repository. It can be used in various ways to suit different workflows, from basic pushing to force pushing and pushing tags. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
