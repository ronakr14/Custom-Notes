# Git Log Commands

## Overview

The `git log` command is used to view the commit history of a Git repository. It provides a detailed log of commits, including commit messages, author information, and dates. This document covers the basic and advanced usage of `git log`.

## Basic Log

### `git log`

Displays the commit history of the current branch.

```sh
git log
```

#### Example

```sh
git log
```

This command shows the commit history with details like commit hash, author, date, and commit message.

## One-Line Log

### `git log --oneline`

Displays the commit history with each commit on a single line, showing the commit hash and message.

```sh
git log --oneline
```

#### Example

```sh
git log --oneline
```

This command provides a simplified view of the commit history with a short commit hash and message.

## Log with Graph

### `git log --graph`

Displays the commit history as a graph with a visual representation of branch and merge history.

```sh
git log --graph
```

#### Example

```sh
git log --graph
```

This command shows the commit history with a graphical representation of branches and merges.

## Log with Details

### `git log --stat`

Displays the commit history with a summary of changes for each commit, including modified files and the number of changes.

```sh
git log --stat
```

#### Example

```sh
git log --stat
```

This command shows the commit history along with a summary of changes for each commit.

## Log with Formatting

### `git log --pretty=format:"<format>"`

Customizes the log output using a specified format.

```sh
git log --pretty=format:"<format>"
```

#### Example

```sh
git log --pretty=format:"%h - %an, %ar : %s"
```

This command customizes the log output to show the commit hash, author name, relative date, and commit message.

## Log for a Specific File

### `git log <file>`

Displays the commit history for a specific file.

```sh
git log <file>
```

#### Example

```sh
git log src/main.py
```

This command shows the commit history for `src/main.py`, including all changes made to the file.

## Log for a Date Range

### `git log --since="<date>" --until="<date>"`

Displays the commit history within a specific date range.

```sh
git log --since="<date>" --until="<date>"
```

#### Example

```sh
git log --since="2024-01-01" --until="2024-06-30"
```

This command shows commits made between January 1, 2024, and June 30, 2024.

## Log for a Specific Author

### `git log --author="<author>"`

Displays the commit history for commits made by a specific author.

```sh
git log --author="<author>"
```

#### Example

```sh
git log --author="John Doe"
```

This command shows commits made by the author "John Doe."

## Log with Search

### `git log --grep="<pattern>"`

Displays commits that match a specified search pattern in the commit message.

```sh
git log --grep="<pattern>"
```

#### Example

```sh
git log --grep="bug fix"
```

This command shows commits with messages containing the pattern "bug fix."

## Summary

The `git log` command is a powerful tool for viewing and analyzing the commit history of a Git repository. It provides various options for customizing the log output, filtering by date, author, or file, and formatting the results. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).