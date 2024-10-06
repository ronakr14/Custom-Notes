# Git Filter Tutorial

## Overview

`git filter` is a powerful command used to filter and rewrite Git history. This can be particularly useful for tasks such as removing sensitive information, modifying commit messages, or adjusting file structures. The primary tools for filtering in Git are `git filter-branch` and `git filter-repo`.

## What is Git Filter?

Git filtering tools are used to rewrite or filter the commit history of a Git repository. This allows you to modify commits, such as removing sensitive information, changing commit messages, or altering file paths.

- **`git filter-branch`**: A legacy tool for filtering and rewriting Git history.
- **`git filter-repo`**: A more recent and faster tool for filtering Git repositories, recommended for new projects.

## Installing Git Filter Tools

### Installing `git filter-repo`

1. **Install via Package Manager**:

    - **macOS**: 

      ```bash
      brew install git-filter-repo
      ```

    - **Linux**: 

      ```bash
      sudo apt-get install git-filter-repo
      ```

2. **Install via Python Package**:

    ```bash
    pip install git-filter-repo
    ```

### Installing `git filter-branch`

`git filter-branch` is included with Git, so no additional installation is required.

## Using `git filter-branch`

`git filter-branch` is used to rewrite history in a Git repository. Use it with caution, as it rewrites commit history, which can affect all clones of the repository.

### Basic Syntax

```bash
git filter-branch --filter <filter> <branch>
```

### Example: Removing a File from History

To remove a file from all commits:

```bash
git filter-branch --tree-filter 'rm -f path/to/file' HEAD
```

### Example: Changing Author Information

To change author information in all commits:

```bash
git filter-branch --env-filter '
OLD_EMAIL="old-email@example.com"
NEW_EMAIL="new-email@example.com"
NEW_NAME="New Name"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$NEW_NAME"
    export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$NEW_NAME"
    export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags
```

## Using `git filter-repo`

`git filter-repo` is a newer and more efficient tool compared to `git filter-branch`. It is recommended for most filtering tasks.

### Basic Syntax

```bash
git filter-repo --<filter> <options>
```

### Example: Removing a File from History

To remove a file from all commits:

```bash
git filter-repo --path path/to/file --invert-paths
```

### Example: Changing Author Information

To change author information in all commits:

```bash
git filter-repo --commit-callback '
if commit.author_email == b"old-email@example.com":
    commit.author_email = b"new-email@example.com"
    commit.author_name = b"New Name"
if commit.committer_email == b"old-email@example.com":
    commit.committer_email = b"new-email@example.com"
    commit.committer_name = b"New Name"
'
```

## Examples of Using Git Filter

### Example 1: Removing a File

Remove a file from the entire history of a Git repository:

```bash
git filter-repo --path path/to/file --invert-paths
```

### Example 2: Changing Email Addresses

Change all instances of an old email address to a new email address:

```bash
git filter-repo --commit-callback '
if commit.author_email == b"old-email@example.com":
    commit.author_email = b"new-email@example.com"
if commit.committer_email == b"old-email@example.com":
    commit.committer_email = b"new-email@example.com"
'
```

### Example 3: Renaming a Repository

Rename a repository from `old-repo` to `new-repo`:

```bash
git filter-repo --path old-repo --to-subdirectory-filter new-repo
```

## Common Use Cases

- **Removing Sensitive Data**: Permanently delete sensitive files or data from the repository history.
- **Changing Author Information**: Correct or update author names and email addresses.
- **Reorganizing Repository Structure**: Change the directory structure or rename repositories.
- **Splitting Repositories**: Split a repository into multiple repositories.

## Summary

Git filtering tools like `git filter-branch` and `git filter-repo` are powerful tools for rewriting and filtering Git history. They allow you to perform tasks such as removing sensitive information, changing commit metadata, and modifying repository structure. `git filter-repo` is generally preferred for new projects due to its efficiency and improved performance.
