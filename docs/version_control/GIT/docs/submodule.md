# Git Submodule Tutorial

## Overview

Git submodules allow you to include and manage repositories within other repositories. This is useful for including libraries or other dependencies in your project. This document will cover the basics of using git submodules with examples.

## Table of Contents

1. [Adding a Submodule](#adding-a-submodule)
2. [Cloning a Repository with Submodules](#cloning-a-repository-with-submodules)
3. [Initializing and Updating Submodules](#initializing-and-updating-submodules)
4. [Working with Submodules](#working-with-submodules)
    - [Checking the Status of Submodules](#checking-the-status-of-submodules)
    - [Pulling Changes in Submodules](#pulling-changes-in-submodules)
    - [Committing Changes in Submodules](#committing-changes-in-submodules)
5. [Removing a Submodule](#removing-a-submodule)
6. [Useful Tips](#useful-tips)

---

## Adding a Submodule

To add a submodule to your repository, use:

```bash
git submodule add <repository-url> <path>
```

### Example

```bash
git submodule add https://github.com/example/library.git libs/library
```

This will add the `library` repository as a submodule in the `libs/library` directory.

## Cloning a Repository with Submodules

When cloning a repository that contains submodules, use:

```bash
git clone --recurse-submodules <repository-url>
```

### Example

```bash
git clone --recurse-submodules https://github.com/example/project.git
```

This will clone the `project` repository and initialize all its submodules.

## Initializing and Updating Submodules

If you clone a repository without using `--recurse-submodules`, you need to initialize and update the submodules manually:

```bash
git submodule init
git submodule update
```

Or, you can use a single command:

```bash
git submodule update --init
```

### Example

```bash
git submodule update --init
```

This will initialize and update all submodules in the repository.

## Working with Submodules

### Checking the Status of Submodules

To check the status of submodules, use:

```bash
git submodule status
```

### Example

```bash
git submodule status
```

This will show the current commit for each submodule.

### Pulling Changes in Submodules

To pull the latest changes in all submodules, use:

```bash
git submodule update --remote
```

### Example

```bash
git submodule update --remote
```

This will pull the latest changes from the submodules' remote repositories.

### Committing Changes in Submodules

When you make changes in a submodule, you need to commit them within the submodule directory and then commit the updated submodule reference in the main repository.

#### Example

1. Change to the submodule directory and commit changes:

    ```bash
    cd libs/library
    git add .
    git commit -m "Update library"
    ```

2. Change back to the main repository and commit the submodule reference update:

    ```bash
    cd ../..
    git add libs/library
    git commit -m "Update library submodule reference"
    ```

## Removing a Submodule

To remove a submodule, you need to delete the submodule entry from the `.gitmodules` file, the submodule's directory, and the submodule entry in the `.git/config` file.

### Example

1. Edit `.gitmodules` and remove the submodule entry:

    ```plaintext
    [submodule "libs/library"]
        path = libs/library
        url = https://github.com/example/library.git
    ```

2. Remove the submodule's directory and the `.git/config` entry:

    ```bash
    git rm -f libs/library
    rm -rf .git/modules/libs/library
    git commit -m "Remove library submodule"
    ```

## Useful Tips

- **Syncing Submodules**: To ensure your submodules are in sync with the repository, use:

    ```bash
    git submodule sync
    ```

- **Branch Tracking**: To track a specific branch in a submodule, use:

    ```bash
    git config -f .gitmodules submodule.<path>.branch <branch>
    ```

    Example:

    ```bash
    git config -f .gitmodules submodule.libs/library.branch main
    ```

- **Recurse Option**: Many Git commands accept the `--recurse-submodules` option to perform actions recursively in submodules.

## Summary

Git submodules are powerful for managing dependencies in your repositories. By understanding how to add, clone, update, and remove submodules, you can effectively manage projects that depend on other repositories.