# Basic Git Commands

## Overview

Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. This document covers the essential Git commands you'll need to manage your projects.

## Initializing a Repository

### `git init`

Initializes a new Git repository.

```sh
git init
```

#### Example

```sh
git init my-new-repo
cd my-new-repo
```

This creates a new directory `my-new-repo` with a Git repository initialized.

## Cloning a Repository

### `git clone`

Clones an existing repository.

```sh
git clone <repository-url>
```

#### Example

```sh
git clone https://github.com/user/repo.git
```

This command clones the repository from the specified URL to your local machine.

## Checking the Status

### `git status`

Displays the state of the working directory and the staging area.

```sh
git status
```

#### Example

```sh
git status
```

This command shows which changes have been staged, which haven't, and which files aren't being tracked by Git.

## Adding Changes

### `git add`

Adds changes to the staging area.

```sh
git add <file>
```

To add all changes:

```sh
git add .
```

#### Example

```sh
git add README.md
```

This command stages the changes made to `README.md`.

## Committing Changes

### `git commit`

Records changes to the repository.

```sh
git commit -m "Commit message"
```

#### Example

```sh
git commit -m "Add initial project files"
```

This command commits the staged changes with the message "Add initial project files".

## Viewing Commit History

### `git log`

Displays the commit history.

```sh
git log
```

#### Example

```sh
git log
```

This command shows a list of commits in reverse chronological order.

## Creating a Branch

### `git branch`

Lists, creates, or deletes branches.

To list branches:

```sh
git branch
```

To create a new branch:

```sh
git branch <branch-name>
```

#### Example

```sh
git branch new-feature
```

This command creates a new branch named `new-feature`.

## Switching Branches

### `git checkout`

Switches branches or restores working tree files.

To switch branches:

```sh
git checkout <branch-name>
```

#### Example

```sh
git checkout new-feature
```

This command switches to the `new-feature` branch.

## Merging Branches

### `git merge`

Merges one or more branches into the current branch.

```sh
git merge <branch-name>
```

#### Example

```sh
git merge new-feature
```

This command merges the `new-feature` branch into the current branch.

## Pulling Changes

### `git pull`

Fetches and integrates changes from a remote repository to the current branch.

```sh
git pull
```

#### Example

```sh
git pull origin main
```

This command fetches and merges changes from the `main` branch of the remote repository.

## Pushing Changes

### `git push`

Updates the remote repository with local commits.

```sh
git push
```

#### Example

```sh
git push origin main
```

This command pushes the local `main` branch to the remote repository.

## Summary

These basic Git commands will help you get started with version control for your projects. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
