# Git Configuration Commands

## Overview

Git allows you to customize your settings by using configuration commands. These commands can be used to set user information, preferences, and other configurations that help tailor Git to your workflow.

## Setting User Information

### `git config --global user.name`

Sets the name you want attached to your commit transactions.

```sh
git config --global user.name "Your Name"
```

#### Example

```sh
git config --global user.name "Jane Doe"
```

This command sets your name to "Jane Doe" for all repositories on your machine.

### `git config --global user.email`

Sets the email you want attached to your commit transactions.

```sh
git config --global user.email "your.email@example.com"
```

#### Example

```sh
git config --global user.email "jane.doe@example.com"
```

This command sets your email to "jane.doe@example.com" for all repositories on your machine.

## Setting Editor

### `git config --global core.editor`

Sets the default text editor that Git will use when you need to enter a commit message.

```sh
git config --global core.editor "editor"
```

#### Example

```sh
git config --global core.editor "code --wait"
```

This command sets Visual Studio Code as the default editor for Git.

## Setting Default Branch Name

### `git config --global init.defaultBranch`

Sets the name of the initial branch created when you run `git init`.

```sh
git config --global init.defaultBranch main
```

#### Example

```sh
git config --global init.defaultBranch main
```

This command sets the default branch name to `main` for all new repositories.

## Aliases

### `git config --global alias.<alias-name>`

Creates shortcuts for Git commands.

```sh
git config --global alias.st status
```

#### Example

```sh
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
```

These commands create aliases so you can use `git co` instead of `git checkout`, `git br` instead of `git branch`, and `git ci` instead of `git commit`.

## Viewing Configuration

### `git config --list`

Displays the current configuration settings.

```sh
git config --list
```

#### Example

```sh
git config --list
```

This command lists all Git configuration settings currently in use.

### `git config <key>`

Displays the value for a specific configuration key.

```sh
git config <key>
```

#### Example

```sh
git config user.name
```

This command shows the current setting for `user.name`.

## Unsetting Configuration

### `git config --global --unset <key>`

Removes a configuration setting.

```sh
git config --global --unset <key>
```

#### Example

```sh
git config --global --unset user.name
```

This command removes the global setting for `user.name`.

## System, Global, and Local Configuration

Git configuration levels:

- **System**: Applies to every user on the system and all their repositories.
- **Global**: Applies to all of your repositories on your system.
- **Local**: Applies to the specific repository you are currently working in.

You can specify the level by using the `--system`, `--global`, or `--local` options:

```sh
git config --system <key> <value>
git config --global <key> <value>
git config --local <key> <value>
```

#### Example

```sh
git config --local core.ignorecase false
```

This command sets the `core.ignorecase` setting to `false` for the current repository.

## Summary

These Git configuration commands help you customize your Git environment to match your preferences and workflow. For more detailed information on each command, refer to the [official Git documentation](https://git-scm.com/doc).
