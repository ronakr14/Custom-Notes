# Git Stash Commands

## Overview

The `git stash` command temporarily shelves (or stashes) changes you've made to your working directory so you can work on something else and then come back and re-apply them later. This is useful when you want to switch branches but aren't ready to commit your current work.

## Basic Stashing

### `git stash`

Saves your local modifications away and reverts the working directory to match the HEAD commit.

```sh
git stash
```

#### Example

```sh
git stash
```

This command stashes your changes, allowing you to work from a clean state.

### `git stash save "message"`

Saves your local modifications with a custom message.

```sh
git stash save "message"
```

#### Example

```sh
git stash save "WIP: working on feature"
```

This command stashes your changes with the message "WIP: working on feature".

## Listing Stashes

### `git stash list`

Shows the list of stashes you have stored.

```sh
git stash list
```

#### Example

```sh
$ git stash list
stash@{0}: WIP on main: 4c5b3e7 Add new feature
stash@{1}: WIP on main: 1a2b3c4 Fix bug
```

This command lists all stashes, showing their index, message, and commit reference.

## Applying Stashes

### `git stash apply`

Applies the changes from a stash to your working directory without removing it from the stash list.

```sh
git stash apply [stash]
```

#### Example

```sh
git stash apply stash@{0}
```

This command applies the changes from `stash@{0}` to your working directory.

### `git stash pop`

Applies the changes from a stash to your working directory and removes it from the stash list.

```sh
git stash pop [stash]
```

#### Example

```sh
git stash pop stash@{0}
```

This command applies the changes from `stash@{0}` to your working directory and removes it from the stash list.

## Creating a Branch from a Stash

### `git stash branch`

Creates and checks out a new branch starting from the commit at which the stash was originally created, then applies the changes from the stash and drops it.

```sh
git stash branch <branch-name> [stash]
```

#### Example

```sh
git stash branch new-feature-branch stash@{0}
```

This command creates a new branch `new-feature-branch` starting from the commit at which `stash@{0}` was created, applies the stash, and removes it from the stash list.

## Dropping Stashes

### `git stash drop`

Removes a single stash from the stash list.

```sh
git stash drop [stash]
```

#### Example

```sh
git stash drop stash@{0}
```

This command removes `stash@{0}` from the stash list.

### `git stash clear`

Removes all stashes from the stash list.

```sh
git stash clear
```

#### Example

```sh
git stash clear
```

This command clears all stashes from the stash list.

## Stashing Untracked or Ignored Files

### `git stash -u`

Includes untracked files in the stash.

```sh
git stash -u
```

#### Example

```sh
git stash -u
```

This command stashes your changes, including untracked files.

### `git stash -a`

Includes all untracked and ignored files in the stash.

```sh
git stash -a
```

#### Example

```sh
git stash -a
```

This command stashes your changes, including all untracked and ignored files.

## Summary

The `git stash` command is a powerful tool for temporarily setting aside changes in your working directory. It allows you to switch branches and work on something else without losing your current work. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
