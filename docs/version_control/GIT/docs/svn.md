# Git-SVN Tutorial

## Overview

Git-SVN is a Git command-line tool that allows you to interact with Subversion (SVN) repositories using Git. It provides a way to use Git as a client for SVN, allowing you to leverage Git's features while working with SVN repositories.

## What is Git-SVN?

Git-SVN is a Git extension that allows you to work with Subversion repositories using Git. It enables you to clone, fetch, commit, and merge changes between Git and SVN repositories, making it easier to work with SVN while benefiting from Git's powerful features.

## Installing Git-SVN

### Installation on Windows

1. **Install Git**: Download and install Git from the [official Git website](https://git-scm.com/downloads).

2. **Install Git-SVN**: Git-SVN is included with Git for Windows. If you have Git installed, you should already have Git-SVN available.

3. **Verify Installation**: Open a command prompt and run:

    ```bash
    git svn --version
    ```

### Installation on macOS/Linux

1. **Install Git**: Use your package manager to install Git.

    - **macOS**: 

      ```bash
      brew install git
      ```

    - **Linux**:

      ```bash
      sudo apt-get install git
      ```

2. **Install Git-SVN**: Git-SVN is included with Git on most systems. If it's not installed, you can install it separately.

    - **macOS**:

      ```bash
      brew install git-svn
      ```

    - **Linux**:

      ```bash
      sudo apt-get install git-svn
      ```

3. **Verify Installation**:

    ```bash
    git svn --version
    ```

## Basic Git-SVN Commands

### Cloning an SVN Repository

To clone an SVN repository into a Git repository:

```bash
git svn clone <svn-repository-url> --no-minimize-url --authors-file=authors.txt
```

- **`<svn-repository-url>`**: The URL of the SVN repository.
- **`--no-minimize-url`**: Prevents URL minimization.
- **`--authors-file=authors.txt`**: (Optional) Maps SVN authors to Git authors.

### Fetching Changes from SVN

To fetch the latest changes from SVN into your Git repository:

```bash
git svn fetch
```

### Committing Changes to SVN

To commit your local changes to the SVN repository:

```bash
git svn dcommit
```

### Viewing SVN Logs

To view SVN logs:

```bash
git svn log
```

### Creating a Branch in SVN

To create a new branch in SVN:

```bash
git svn branch <branch-name>
```

### Merging SVN Branches

To merge changes from one SVN branch into another:

```bash
git svn rebase
```

## Examples of Using Git-SVN

### Example 1: Cloning an SVN Repository

Clone an SVN repository into a local Git repository:

```bash
git svn clone http://svn-server/repository/trunk --no-minimize-url
```

### Example 2: Fetching Changes

Fetch the latest changes from the SVN repository:

```bash
git svn fetch
```

### Example 3: Committing Changes

Commit your local changes to the SVN repository:

```bash
git svn dcommit
```

### Example 4: Viewing Logs

View the SVN logs:

```bash
git svn log
```

### Example 5: Creating a Branch

Create a new branch in the SVN repository:

```bash
git svn branch feature/new-feature
```

### Example 6: Merging Branches

Merge changes from the `feature/new-feature` branch into the `trunk`:

```bash
git svn rebase
```

## Common Use Cases

- **Migrating to Git**: Use Git-SVN to migrate a project from SVN to Git while maintaining SVN history.
- **Hybrid Workflow**: Use Git for local development and SVN for centralized version control in larger teams.
- **Working with Legacy Systems**: Integrate Git with legacy SVN systems to benefit from Git features without abandoning existing workflows.

## Summary

Git-SVN is a powerful tool for integrating Git with Subversion, allowing you to use Git's features while working with SVN repositories. By using commands like `git svn clone`, `git svn fetch`, and `git svn dcommit`, you can effectively manage your codebase and synchronize changes between Git and SVN.
