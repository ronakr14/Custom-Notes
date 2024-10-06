# Git-TFS Tutorial

## Overview

Git-TFS is a tool that allows you to interact with Team Foundation Server (TFS) and Azure DevOps Server (formerly TFS) from Git. It provides a way to use Git as a client for TFS, allowing you to leverage Git features while working with TFS repositories.

## What is Git-TFS?

Git-TFS is an open-source tool that integrates Git with TFS and Azure DevOps Server. It enables Git users to work with TFS repositories, perform operations like cloning, fetching, and pushing changes, and interact with TFS branches and work items.

## Installing Git-TFS

### Installation on Windows

1. **Download Git-TFS**: You can download Git-TFS binaries from the [Git-TFS releases page](https://github.com/git-tfs/git-tfs/releases).

2. **Install Git-TFS**: Extract the downloaded files and add the directory to your system's `PATH` environment variable.

3. **Verify Installation**: Open a command prompt and run:

    ```bash
    git tfs --version
    ```

### Installation on macOS/Linux

1. **Install via Homebrew (macOS)**:

    ```bash
    brew install git-tfs
    ```

2. **Install via Package Manager (Linux)**: Use your distribution's package manager or follow [manual installation instructions](https://github.com/git-tfs/git-tfs/wiki/Installation) provided on the Git-TFS GitHub page.

3. **Verify Installation**:

    ```bash
    git tfs --version
    ```

## Basic Git-TFS Commands

### Cloning a TFS Repository

To clone a TFS repository into a Git repository:

```bash
git tfs clone http://tfs-server:8080/tfs/DefaultCollection $/TeamProject/Repository
```

### Fetching Changes from TFS

To fetch the latest changes from TFS into your Git repository:

```bash
git tfs fetch
```

### Pushing Changes to TFS

To push your local changes to the TFS repository:

```bash
git tfs push
```

### Checking Out a TFS Branch

To check out a TFS branch:

```bash
git tfs checkout $/TeamProject/BranchName
```

### Creating a New TFS Branch

To create a new branch in TFS:

```bash
git tfs branch $/TeamProject/NewBranch
```

### Merging TFS Branches

To merge changes from one TFS branch into another:

```bash
git tfs merge $/TeamProject/SourceBranch $/TeamProject/TargetBranch
```

### Viewing TFS Changesets

To view TFS changesets:

```bash
git tfs changeset <changeset-id>
```

### Resolving Conflicts

To resolve conflicts between Git and TFS:

```bash
git tfs checkin --resolve
```

## Examples of Using Git-TFS

### Example 1: Cloning a TFS Repository

Clone a TFS repository into a local Git repository:

```bash
git tfs clone http://tfs-server:8080/tfs/DefaultCollection $/MyProject
```

### Example 2: Fetching Changes

Fetch the latest changes from TFS:

```bash
git tfs fetch
```

### Example 3: Pushing Changes

Push your local commits to TFS:

```bash
git tfs push
```

### Example 4: Checking Out a Branch

Check out a specific branch from TFS:

```bash
git tfs checkout $/MyProject/FeatureBranch
```

### Example 5: Merging Branches

Merge changes from a feature branch into the main branch:

```bash
git tfs merge $/MyProject/FeatureBranch $/MyProject/MainBranch
```

### Example 6: Viewing Changesets

View details of a specific changeset:

```bash
git tfs changeset 1234
```

## Common Use Cases

- **Integrating Git with TFS**: Leverage Git features while working with TFS repositories.
- **Managing Branches**: Create, check out, and merge branches between Git and TFS.
- **Fetching and Pushing Changes**: Synchronize changes between local Git repositories and TFS.
- **Conflict Resolution**: Resolve conflicts that arise from interactions between Git and TFS.

## Summary

Git-TFS is a powerful tool for integrating Git with TFS, allowing you to use Git's features while working with TFS repositories. By using commands like `git tfs clone`, `git tfs fetch`, and `git tfs push`, you can effectively manage your codebase and synchronize changes between Git and TFS.