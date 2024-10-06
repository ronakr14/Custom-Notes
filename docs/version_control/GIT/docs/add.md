# Git Add Commands

## Overview

The `git add` command is used to add changes in the working directory to the staging area. This is the first step in the Git workflow to prepare changes for the next commit. This document covers the basic and advanced usage of `git add`.

## Adding All Changes

### `git add .`

Adds all changes (new, modified, and deleted files) in the current directory and subdirectories to the staging area.

```sh
git add .
```

#### Example

```sh
git add .
```

This command stages all changes in the repository for the next commit.

### `git add -A`

Adds all changes (new, modified, and deleted files) in the entire working directory to the staging area.

```sh
git add -A
```

#### Example

```sh
git add -A
```

This command stages all changes in the repository, including those outside the current directory.

## Adding Specific Files

### `git add <file>`

Adds changes in a specific file to the staging area.

```sh
git add <file>
```

#### Example

```sh
git add README.md
```

This command stages changes in the `README.md` file for the next commit.

### `git add <directory>`

Adds changes in a specific directory to the staging area.

```sh
git add <directory>
```

#### Example

```sh
git add src/
```

This command stages changes in the `src/` directory for the next commit.

## Adding Changes Interactively

### `git add -i`

Starts an interactive mode for adding changes to the staging area.

```sh
git add -i
```

#### Example

```sh
git add -i
```

This command opens an interactive prompt where you can choose which changes to add to the staging area.

### `git add -p`

Adds changes in a patch mode, allowing you to select specific changes to add.

```sh
git add -p
```

#### Example

```sh
git add -p
```

This command opens an interactive prompt to review and stage changes hunk by hunk.

## Adding All Tracked Files

### `git add -u`

Adds changes in all tracked files to the staging area, excluding new files.

```sh
git add -u
```

#### Example

```sh
git add -u
```

This command stages changes (modifications and deletions) in all tracked files.

## Adding Ignored Files

### `git add -f`

Forces the addition of ignored files to the staging area.

```sh
git add -f <file>
```

#### Example

```sh
git add -f .env
```

This command forces the addition of the `.env` file, even if it is listed in the `.gitignore`.

## Dry Run

### `git add --dry-run`

Shows what would be added to the staging area without actually adding the files.

```sh
git add --dry-run <file>
```

#### Example

```sh
git add --dry-run .
```

This command shows what would be staged for commit without actually staging any changes.

## Summary

The `git add` command is a fundamental part of the Git workflow, allowing you to prepare changes for the next commit. It offers various options to add specific files, directories, and changes interactively or selectively. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).