# Git Worktree Command

### Overview
The `git worktree` command allows you to manage multiple working directories attached to a single Git repository. This is useful for working on different branches simultaneously without needing to clone the repository multiple times.

## Basic Commands
### Adding a Worktree
To add a new worktree, use the following command:

```sh
git worktree add <path> <branch>
```
- `<path>`: The directory where the new worktree will be created.
- `<branch>`: The branch to be checked out in the new worktree.

Example
```sh
git worktree add ../new-feature-branch feature
```
This command will create a new directory `../new-feature-branch` and check out the `feature` branch in that directory.

### Listing Worktrees
To list all worktrees associated with the repository, use:

```sh
git worktree list
```
Example
```sh
$ git worktree list
/Users/username/project              a1b2c3d [master]
/Users/username/new-feature-branch   e4f5g6h [feature]
```
### Removing a Worktree
To remove a worktree, use the following command:

```sh
git worktree remove <path>
```
- `<path>`: The path to the worktree directory you want to remove.
Example
```sh
git worktree remove ../new-feature-branch
```
This command will remove the `../new-feature-branch` worktree.

### Pruning Worktrees
To remove references to worktrees that no longer exist, use:

```sh
git worktree prune
```
Example
```sh
git worktree prune
```
This command will clean up any stale references to deleted worktrees.

## Advanced Usage
### Creating and Checking Out a New Branch
You can create a new branch and check it out in a new worktree simultaneously:

```sh
git worktree add <path> -b <new-branch>
```
- `<path>`: The directory where the new worktree will be created.
- `<new-branch>`: The name of the new branch to be created.
Example
```sh
git worktree add ../bugfix -b bugfix-123
```
This command will create a new directory `../bugfix`, create a new branch `bugfix-123`, and check it out in that directory.

### Detached Worktree
You can also create a detached worktree, which is useful for checking out a specific commit without creating a branch:

```sh
git worktree add <path> <commit>
```
- `<path>`: The directory where the new worktree will be created.
- `<commit>`: The commit hash to check out.
Example
```sh
git worktree add ../detached-worktree a1b2c3d4
```
This command will create a new directory `../detached-worktree` and check out the commit `a1b2c3d4` in a detached HEAD state.

## Benefits of Using Git Worktree
- **Simultaneous Branch Development**: Work on multiple branches without switching back and forth.
- **Resource Efficiency**: Avoid the overhead of cloning the repository multiple times.
- **Context Isolation**: Keep changes isolated to their respective directories, reducing the risk of accidental changes.
## Summary
The `git worktree` command is a powerful tool for managing multiple working directories in a single repository. It simplifies workflows that require simultaneous work on different branches, making it easier to handle feature development, bug fixes, and code reviews.

For more information, refer to the [official Git documentation](https://git-scm.com/docs/git-worktree).