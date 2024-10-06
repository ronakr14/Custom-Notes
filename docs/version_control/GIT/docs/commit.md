# Git Commit Commands

## Overview

The `git commit` command is used to save changes to the local repository. It records changes to the repository's history with a message describing the changes. This document covers the basic and advanced usage of `git commit`.

## Basic Commit

### `git commit -m "<message>"`

Commits the staged changes with a message describing the changes.

```sh
git commit -m "<message>"
```

#### Example

```sh
git add .
git commit -m "Add new feature to the project"
```

This command commits all staged changes with the message "Add new feature to the project."

## Commit with a Detailed Message

### `git commit`

Opens the default text editor to write a detailed commit message.

```sh
git commit
```

#### Example

```sh
git add .
git commit
```

This command opens the text editor for you to write a more detailed commit message.

## Commit Only Specific Files

### `git commit <file> -m "<message>"`

Commits only the specified file with a message describing the changes.

```sh
git commit <file> -m "<message>"
```

#### Example

```sh
git commit src/main.py -m "Fix bug in main.py"
```

This command commits only `src/main.py` with the message "Fix bug in main.py."

## Amend the Last Commit

### `git commit --amend`

Modifies the last commit. You can add new changes or update the commit message.

```sh
git commit --amend
```

#### Example

```sh
# Make additional changes
git add src/main.py
git commit --amend
```

This command allows you to modify the last commit, either by adding new changes or changing the commit message.

## Commit with a Specific Author

### `git commit --author="Name <email>" -m "<message>"`

Commits with a specified author name and email.

```sh
git commit --author="Name <email>" -m "<message>"
```

#### Example

```sh
git commit --author="John Doe <john@example.com>" -m "Update documentation"
```

This command commits with the author information provided, which can be different from the global Git configuration.

## Skip the Staging Area

### `git commit -a -m "<message>"`

Commits all changes in tracked files, skipping the staging area.

```sh
git commit -a -m "<message>"
```

#### Example

```sh
git commit -a -m "Automatically commit all changes"
```

This command commits all tracked changes without having to explicitly use `git add`.

## Commit with a GPG Signature

### `git commit -S -m "<message>"`

Commits the changes with a GPG signature, verifying the commit's authenticity.

```sh
git commit -S -m "<message>"
```

#### Example

```sh
git commit -S -m "Signed commit with GPG key"
```

This command signs the commit with your GPG key, providing an additional layer of verification.

## Summary

The `git commit` command is essential for recording changes in the Git repository. It allows you to provide descriptive messages, amend previous commits, and perform commits with specific author information or signatures. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).