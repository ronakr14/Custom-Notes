# Git Subtrees Tutorial

## Overview

Git subtrees allow you to include and manage the content of another repository within your own repository. Unlike submodules, subtrees are fully integrated into the parent repository, making them a flexible option for managing project dependencies.

## What is a Git Subtree?

A Git subtree allows you to include another Git repository as a subdirectory of your repository. This approach provides a way to manage dependencies or shared code without needing to clone or use submodules.

## Setting Up a Git Subtree

### Adding a Subtree

To add a new subtree, you use the `git subtree add` command. This command pulls the content of the specified repository and adds it to a subdirectory in your repository.

```bash
git subtree add --prefix=<subdirectory> <repository-url> <branch> --squash
```

- **`<subdirectory>`**: The directory where you want to add the subtree.
- **`<repository-url>`**: The URL of the repository you want to add.
- **`<branch>`**: The branch of the repository you want to use.
- **`--squash`**: Optional. Combines all commits into a single commit.

### Example

```bash
git subtree add --prefix=libs/some-library https://github.com/example/some-library.git main --squash
```

This command adds the `some-library` repository into the `libs/some-library` directory of your repository using the `main` branch and squashes the commits into a single commit.

### Updating a Subtree

To update the subtree with the latest changes from the upstream repository, use the `git subtree pull` command.

```bash
git subtree pull --prefix=<subdirectory> <repository-url> <branch> --squash
```

### Example

```bash
git subtree pull --prefix=libs/some-library https://github.com/example/some-library.git main --squash
```

This command updates the `libs/some-library` directory with the latest changes from the `main` branch of the `some-library` repository and squashes the commits.

### Removing a Subtree

To remove a subtree, you can simply delete the subdirectory and commit the changes.

```bash
rm -rf <subdirectory>
git add .
git commit -m "Remove subtree <subdirectory>"
```

### Example

```bash
rm -rf libs/some-library
git add .
git commit -m "Remove subtree libs/some-library"
```

## Basic Git Subtree Commands

Here are some basic commands for managing Git subtrees:

- **Add a Subtree:**

    ```bash
    git subtree add --prefix=<subdirectory> <repository-url> <branch> [--squash]
    ```

- **Pull Updates from a Subtree:**

    ```bash
    git subtree pull --prefix=<subdirectory> <repository-url> <branch> [--squash]
    ```

- **Push Changes to a Subtree:**

    ```bash
    git subtree push --prefix=<subdirectory> <repository-url> <branch>
    ```

- **Split a Subtree into a Separate Repository:**

    ```bash
    git subtree split --prefix=<subdirectory> --branch=<new-branch>
    ```

## Examples of Using Git Subtrees

### Example 1: Adding a Subtree

Suppose you want to add a library located at `https://github.com/example/lib.git` into your project under `libs/lib`. You can do this as follows:

```bash
git subtree add --prefix=libs/lib https://github.com/example/lib.git main --squash
```

### Example 2: Updating a Subtree

To update the `libs/lib` directory with the latest changes from the upstream repository:

```bash
git subtree pull --prefix=libs/lib https://github.com/example/lib.git main --squash
```

### Example 3: Pushing Changes to a Subtree

If you have made changes to the `libs/lib` subtree and want to push those changes back to the upstream repository:

```bash
git subtree push --prefix=libs/lib https://github.com/example/lib.git main
```

### Example 4: Splitting a Subtree

If you want to extract `libs/lib` into its own repository, use the `split` command:

```bash
git subtree split --prefix=libs/lib --branch=lib-extract
```

## Common Use Cases

- **Managing Dependencies**: Include external libraries or dependencies within your project.
- **Code Sharing**: Share common code across multiple projects.
- **Modularization**: Separate large projects into smaller, more manageable pieces.
- **Maintaining Legacy Code**: Include and maintain legacy codebases within a new project.

## Summary

Git subtrees provide a powerful way to manage and integrate external repositories into your project. They offer a more seamless experience compared to submodules by fully incorporating the external repository into your project's history. Use Git subtrees to handle dependencies, share code, and manage modular projects effectively.
