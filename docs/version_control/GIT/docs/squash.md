# Git Squash Tutorial

## Overview

Git squash allows you to combine multiple commits into a single commit. This is particularly useful for cleaning up your commit history before merging a feature branch into the main branch. This document will cover the basics of using git squash with examples.

## What is Git Squash?

Git squash is the process of combining multiple commits into one. This helps to simplify the commit history and make it more readable.

## Interactive Rebase for Squashing Commits

The most common way to squash commits is by using an interactive rebase. This allows you to choose which commits to squash and how to combine them.

### Example: Squashing the Last Two Commits

1. Start an interactive rebase for the last two commits:

    ```bash
    git rebase -i HEAD~2
    ```

2. In the interactive rebase editor, you will see something like this:

    ```plaintext
    pick abc1234 Commit message 1
    pick def5678 Commit message 2
    ```

3. Change the second `pick` to `squash` (or `s`):

    ```plaintext
    pick abc1234 Commit message 1
    squash def5678 Commit message 2
    ```

4. Save and close the editor. Another editor will open to combine the commit messages. Edit as necessary, then save and close.

5. Your commits are now squashed into one.

### Example: Squashing Multiple Commits

1. Start an interactive rebase for the last four commits:

    ```bash
    git rebase -i HEAD~4
    ```

2. In the interactive rebase editor, you will see something like this:

    ```plaintext
    pick abc1234 Commit message 1
    pick def5678 Commit message 2
    pick ghi9101 Commit message 3
    pick jkl1121 Commit message 4
    ```

3. Change all but the first `pick` to `squash` (or `s`):

    ```plaintext
    pick abc1234 Commit message 1
    squash def5678 Commit message 2
    squash ghi9101 Commit message 3
    squash jkl1121 Commit message 4
    ```

4. Save and close the editor. Another editor will open to combine the commit messages. Edit as necessary, then save and close.

5. Your commits are now squashed into one.

## Using `commit --squash`

The `--squash` option can be used with `git commit` to combine changes into a previous commit without immediately amending the commit.

### Example

1. Make some changes and stage them:

    ```bash
    git add file1.txt
    ```

2. Use `commit --squash` to prepare to squash these changes into a previous commit:

    ```bash
    git commit --squash <commit-hash>
    ```

3. Complete the squash by performing a rebase:

    ```bash
    git rebase -i HEAD~2
    ```

4. Follow the interactive rebase steps as described earlier to finalize the squash.

## Squashing Commits During a Merge

When merging a feature branch into the main branch, you can squash all commits into a single commit.

### Example

1. Check out the main branch:

    ```bash
    git checkout main
    ```

2. Merge the feature branch with the `--squash` option:

    ```bash
    git merge --squash feature-branch
    ```

3. Commit the squashed changes:

    ```bash
    git commit -m "Merge feature-branch with squash"
    ```

This will combine all the commits from `feature-branch` into a single commit on `main`.

## Useful Tips

- **Backup Important Changes**: Before performing a rebase or squash, ensure you have backups of important work or work on a separate branch.
- **Interactive Rebase**: Use `git rebase -i` for greater control over how commits are squashed and merged.
- **Use Descriptive Commit Messages**: When combining commit messages during a squash, make sure to create a comprehensive and descriptive message that accurately reflects the changes.

## Summary

Git squash is a powerful tool for cleaning up commit history and making it more readable. By understanding how to use interactive rebase, `commit --squash`, and squashing during merges, you can maintain a cleaner and more manageable repository.