# Git Diff Tutorial

## Overview

The `git diff` command is used to show changes between commits, commit and working tree, etc. It is a versatile command that can compare branches, commits, and changes in the working directory. This document will cover various usages of `git diff` with examples.

## Table of Contents

1. [Basic Syntax](#basic-syntax)
2. [Comparing Working Directory and Index](#comparing-working-directory-and-index)
3. [Comparing Staged Changes](#comparing-staged-changes)
4. [Comparing Working Directory and Last Commit](#comparing-working-directory-and-last-commit)
5. [Comparing Between Commits](#comparing-between-commits)
6. [Comparing Branches](#comparing-branches)
7. [Diffing Specific Files](#diffing-specific-files)
8. [Diffing with Different Output Formats](#diffing-with-different-output-formats)
9. [Ignoring Whitespace Changes](#ignoring-whitespace-changes)
10. [Useful Tips](#useful-tips)

---

## Basic Syntax

The basic syntax of `git diff` is:

```bash
git diff [options] [<commit>] [<commit>]
```

## Comparing Working Directory and Index

To see the changes that you have made but not yet staged, use:

```bash
git diff
```

### Example

```bash
git diff
```

This will show the changes in the working directory that are not staged for the next commit.

## Comparing Staged Changes

To see the changes that are staged for the next commit, use:

```bash
git diff --cached
```

### Example

```bash
git diff --cached
```

This will show the changes that have been staged but not yet committed.

## Comparing Working Directory and Last Commit

To see the changes between the working directory and the last commit, use:

```bash
git diff HEAD
```

### Example

```bash
git diff HEAD
```

This will show the changes in the working directory compared to the latest commit.

## Comparing Between Commits

To see the changes between two commits, use:

```bash
git diff <commit1> <commit2>
```

### Example

```bash
git diff commit1 commit2
```

This will show the changes between `commit1` and `commit2`.

## Comparing Branches

To see the changes between two branches, use:

```bash
git diff <branch1> <branch2>
```

### Example

```bash
git diff main feature-branch
```

This will show the differences between the `main` branch and the `feature-branch`.

## Diffing Specific Files

To see the changes for a specific file, use:

```bash
git diff <file>
```

### Example

```bash
git diff README.md
```

This will show the changes in `README.md`.

## Diffing with Different Output Formats

`git diff` supports different output formats. The most common are:

- **Patch format** (default): Shows the changes as a patch.
- **Name-only format**: Shows the names of the changed files.
- **Name-status format**: Shows the names and statuses (added, modified, deleted) of the changed files.

### Examples

#### Patch Format

```bash
git diff
```

#### Name-Only Format

```bash
git diff --name-only
```

#### Name-Status Format

```bash
git diff --name-status
```

## Ignoring Whitespace Changes

To ignore whitespace changes, use:

```bash
git diff -w
```

### Example

```bash
git diff -w
```

This will ignore whitespace changes in the diff output.

## Useful Tips

- **Color Diff Output**: Use `--color` to force color diff output:

    ```bash
    git diff --color
    ```

- **Word Diff**: Use `--word-diff` to show changes word by word:

    ```bash
    git diff --word-diff
    ```

- **Context Lines**: Use `-U<n>` to show `<n>` lines of context around changes:

    ```bash
    git diff -U3
    ```

## Summary

The `git diff` command is an essential tool for understanding changes in your Git repository. By using the various options and formats available, you can tailor the output to your needs and gain better insight into the differences between commits, branches, and your working directory.