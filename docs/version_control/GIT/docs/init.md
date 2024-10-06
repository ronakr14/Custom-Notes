# Git Init Commands

## Overview

The `git init` command is used to create a new Git repository. It initializes a new repository in the current directory, making it ready to track changes. This document covers the basic and advanced usage of `git init`.

## Basic Initialization

### `git init`

Initializes a new Git repository in the current directory.

```sh
git init
```

#### Example

```sh
mkdir my-new-project
cd my-new-project
git init
```

This command creates a new Git repository in the `my-new-project` directory.

## Initialization with a Specific Directory

### `git init <directory>`

Initializes a new Git repository in the specified directory. If the directory does not exist, it will be created.

```sh
git init <directory>
```

#### Example

```sh
git init my-new-project
```

This command creates a new Git repository in the `my-new-project` directory.

## Initialization with a Bare Repository

### `git init --bare`

Initializes a new bare Git repository. Bare repositories are used as remote repositories and do not contain a working directory.

```sh
git init --bare <directory>
```

#### Example

```sh
git init --bare /path/to/bare-repo.git
```

This command creates a new bare Git repository in the specified path.

## Initialization with a Specific Template

### `git init --template=<template_directory>`

Initializes a new Git repository with the specified template directory. This allows you to include custom configuration files or hooks.

```sh
git init --template=<template_directory>
```

#### Example

```sh
git init --template=/path/to/my-template
```

This command initializes a new Git repository using the custom template located at `/path/to/my-template`.

## Initialization with Configuration Options

### `git init -b <branch>`

Initializes a new Git repository with the specified initial branch name. This is useful for setting a default branch other than `main` or `master`.

```sh
git init -b <branch>
```

#### Example

```sh
git init -b main
```

This command initializes a new Git repository with the initial branch named `main`.

## Summary

The `git init` command is the starting point for creating a new Git repository. It sets up the necessary files and directories for version control. You can customize the initialization process with options such as creating a bare repository, specifying a template, or setting an initial branch name. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).