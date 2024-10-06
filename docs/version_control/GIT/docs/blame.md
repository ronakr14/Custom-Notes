# Git Blame Tutorial

## Overview

The `git blame` command is used to display the last modification for each line in a file. It shows which commit and author are responsible for each line of a file, which can be helpful for tracking down the origin of changes and understanding the history of a file.

## What is Git Blame?

`git blame` annotates each line in a file with information about the last commit that modified that line. It provides a way to track who made changes to specific parts of a file and when those changes were made.

## Basic Usage

The basic syntax for `git blame` is:

```bash
git blame <file>
```

### Example

To see who last modified each line in `example.txt`:

```bash
git blame example.txt
```

This will output a list of lines with the commit hash, author, and date for each line in `example.txt`.

## Blame with Specific Commits

You can also use `git blame` to show annotations starting from a specific commit or branch.

### Example

To blame a file starting from a specific commit:

```bash
git blame <commit-hash> <file>
```

### Example

```bash
git blame abc1234 example.txt
```

This shows the blame annotations for `example.txt` starting from the commit `abc1234`.

## Blame with File History

To blame a file based on its history, use the `-L` option to limit the range of lines:

### Example

To blame lines 10 to 20 of `example.txt`:

```bash
git blame -L 10,20 example.txt
```

This restricts the blame output to lines 10 through 20.

## Blame with Custom Formatting

You can customize the output of `git blame` using the `-p` option to include more details:

### Example

To get a detailed output with commit information and author details:

```bash
git blame -p example.txt
```

The `-p` option provides a more detailed output with additional metadata for each line.

## Blame and Annotations

`git blame` can also be combined with `git log` to get additional information about changes:

### Example

To see detailed information about the commit that last modified a line:

1. First, use `git blame` to get the commit hash:

    ```bash
    git blame example.txt
    ```

2. Then, use `git log` to get more details about the commit:

    ```bash
    git log -p <commit-hash>
    ```

### Example

```bash
git blame example.txt
# Output might include:
# abc1234 (John Doe 2024-01-01 10:00:00 +0000 15) Line of code

git log -p abc1234
```

This shows the details of the commit `abc1234`, including changes made and the commit message.

## Useful Tips

- **Blame for Multiple Files**: You can pass multiple files to `git blame` to see annotations for several files at once.

    ```bash
    git blame file1.txt file2.txt
    ```

- **Blame Options**: Explore additional options with `git blame --help` to customize the output and functionality.

- **Performance**: For large files or repositories, blame operations might be slow. Use specific line ranges or commits to improve performance.

## Summary

The `git blame` command is a powerful tool for tracking changes in files and understanding the history of modifications. By using various options, you can customize the output, limit the blame to specific lines or commits, and get detailed information about changes. Understanding how to use `git blame` effectively can help you manage and troubleshoot your codebase more efficiently.