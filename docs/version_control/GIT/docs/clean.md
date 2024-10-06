# Git Clean Tutorial

## Overview

The `git clean` command is used to remove untracked files and directories from your working directory. This can be useful for cleaning up your working directory by removing files that are not under version control. This document covers the basics of using `git clean` with examples.

## What is Git Clean?

The `git clean` command is used to remove untracked files and directories from your working directory. Untracked files are files that are not added to the Git index and are not being tracked by Git. This command is helpful for cleaning up your working directory and ensuring that it only contains files that are part of your project.

## Basic Usage

The basic usage of `git clean` is to remove untracked files from your working directory. By default, `git clean` will not remove any files unless you specify the `-f` or `--force` option.

### Example

```bash
git clean -f
```

This will remove all untracked files from your working directory.

## Dry Run

Before actually removing files, you can perform a dry run to see which files would be removed without actually deleting them. This is done using the `-n` or `--dry-run` option.

### Example

```bash
git clean -n
```

This will list all untracked files that would be removed, but it will not actually delete them.

## Force Clean

To forcefully remove untracked files, use the `-f` or `--force` option.

### Example

```bash
git clean -f
```

This will remove all untracked files from your working directory.

## Remove Untracked Directories

To remove untracked directories in addition to untracked files, use the `-d` option.

### Example

```bash
git clean -fd
```

This will remove all untracked files and directories from your working directory.

## Interactive Mode

Interactive mode allows you to review and approve each file or directory before it is removed. This is done using the `-i` or `--interactive` option.

### Example

```bash
git clean -i
```

This will prompt you to confirm each file and directory before it is removed.

## Useful Tips

- **Combine Options**: You can combine multiple options to customize the behavior of `git clean`. For example, to perform a dry run and include directories, use `git clean -nd`.
- **Be Cautious**: The `git clean` command is powerful and can permanently delete files. Always perform a dry run first if you are unsure about which files will be removed.
- **Exclude Files**: You can exclude certain files from being removed by creating a `.gitignore` file and listing the files or directories to be ignored.

## Summary

The `git clean` command is a powerful tool for removing untracked files and directories from your working directory. By using options such as `-n` for a dry run, `-f` to force removal, `-d` to include directories, and `-i` for interactive mode, you can effectively manage and clean your working directory. Always exercise caution when using this command to avoid accidentally deleting important files.
