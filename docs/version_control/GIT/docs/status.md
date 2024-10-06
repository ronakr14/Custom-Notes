# Git Status Commands

## Overview

The `git status` command is used to display the state of the working directory and the staging area. It shows which changes have been staged, which haven't, and which files are not being tracked by Git. This document covers the basic and advanced usage of `git status`.

## Basic Status

### `git status`

Displays the state of the working directory and the staging area.

```sh
git status
```

#### Example

```sh
git status
```

This command provides a summary of changes in the working directory and staging area, including modified, added, and untracked files.

## Status with Verbose Output

### `git status -v`

Provides verbose output, showing additional details about the changes.

```sh
git status -v
```

#### Example

```sh
git status -v
```

This command displays additional details about changes in the files, such as the differences in the content of modified files.

## Status with Short Format

### `git status -s`

Displays a concise, short format of the status output.

```sh
git status -s
```

#### Example

```sh
git status -s
```

This command provides a brief overview of the status with a shorter format, showing just the file status and changes.

## Status with Porcelain Format

### `git status --porcelain`

Displays the status in a machine-readable format, which is useful for scripting.

```sh
git status --porcelain
```

#### Example

```sh
git status --porcelain
```

This command outputs the status in a stable and easy-to-parse format for use in scripts or automated processes.

## Status of Specific Files

### `git status <file>`

Displays the status of a specific file.

```sh
git status <file>
```

#### Example

```sh
git status src/main.py
```

This command shows the status of `src/main.py`, indicating whether it has been modified, staged, or is untracked.

## Status with Path Limiting

### `git status <path>`

Displays the status of files within a specific path.

```sh
git status <path>
```

#### Example

```sh
git status docs/
```

This command shows the status of files within the `docs/` directory, including any changes or untracked files in that directory.

## Summary

The `git status` command is essential for tracking the state of the working directory and staging area. It provides various formats for viewing changes, from a basic overview to detailed or machine-readable outputs. Understanding the status of files helps manage and review changes effectively. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).