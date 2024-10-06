# Git Show Tutorial

## Overview

The `git show` command is used to display various types of information from Git repositories. It is commonly used to show details about commits, tags, and other objects in the repository. This command provides insights into changes made, including commit messages, diffs, and more.

## What is `git show`

`git show` is a Git command used to display information about various objects in a Git repository. It can show details about commits, tags, trees, and blobs, providing information such as commit messages, diffs, and metadata.

## Basic Syntax

```bash
git show [options] <object>
```

- **`<object>`**: The commit hash, tag, or other Git object you want to display.
- **`[options]`**: Additional options to modify the output.

## Using `git show` with Commits

By default, `git show` displays information about a specific commit, including the commit message and diff.

### Example: Show Details of a Commit

To display details of a specific commit:

```bash
git show <commit-hash>
```

### Example: Show Commit with Custom Formatting

To show a commit with a custom format for the commit message:

```bash
git show <commit-hash> --pretty=format:"%h - %an, %ar : %s"
```

## Using `git show` with Tags

You can also use `git show` to display details about a tag, including the commit it points to and any associated annotations.

### Example: Show Tag Details

To display information about a specific tag:

```bash
git show <tag-name>
```

## Using `git show` with Other Objects

`git show` can be used to display information about other Git objects, such as trees and blobs.

### Example: Show Tree Object

To show the contents of a tree object (e.g., a directory structure):

```bash
git show <tree-hash>
```

### Example: Show Blob Object

To display the contents of a blob object (i.e., file contents):

```bash
git show <blob-hash>
```

## Examples of Using `git show`

### Example 1: Show the Latest Commit

To display the details of the latest commit:

```bash
git show HEAD
```

### Example 2: Show a Commit with a Diff

To show a specific commit along with the diff of changes:

```bash
git show <commit-hash>
```

### Example 3: Show a Tag and Its Commit

To display a tag and the commit it points to:

```bash
git show v1.0.0
```

### Example 4: Show the Contents of a Specific File in a Commit

To view the contents of a file as it was in a specific commit:

```bash
git show <commit-hash>:path/to/file
```

### Example 5: Show a Commit with a Custom Output Format

To format the commit message and metadata:

```bash
git show <commit-hash> --pretty=format:"%h - %an, %ar : %s" --no-patch
```

## Common Use Cases

- **Inspecting Commits**: View detailed information about commits, including changes and commit messages.
- **Examining Tags**: Display information about tags and their associated commits.
- **Reviewing Changes**: Review the changes introduced by a specific commit or object.

## Summary

The `git show` command is a versatile tool for displaying detailed information about Git objects, including commits, tags, trees, and blobs. It allows you to view commit messages, diffs, and other metadata, making it useful for inspecting and reviewing changes in your repository.
