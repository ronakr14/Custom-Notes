# Git Bisect Tutorial

## Overview

The `git bisect` command is a powerful tool for identifying the commit that introduced a bug or issue in a Git repository. By performing a binary search through the commit history, `git bisect` helps you efficiently locate the specific commit where a problem first appeared.

## What is `git bisect`

`git bisect` is a command used to perform a binary search through your commit history to find the commit that introduced a specific bug or issue. The process involves marking commits as good or bad and narrowing down the search until the problematic commit is identified.

## Basic Syntax

```bash
git bisect start
git bisect bad [commit]
git bisect good [commit]
git bisect run <test-script>
git bisect reset
```

- **`git bisect start`**: Start the bisecting process.
- **`git bisect bad [commit]`**: Mark the current commit or a specified commit as bad (contains the issue).
- **`git bisect good [commit]`**: Mark the current commit or a specified commit as good (does not contain the issue).
- **`git bisect run <test-script>`**: Automatically test each commit with the provided script to identify the bad commit.
- **`git bisect reset`**: End the bisect session and return to the original branch.

## How to Use `git bisect`

### Step 1: Start Bisecting

Begin the bisecting process:

```bash
git bisect start
```

### Step 2: Mark the Bad Commit

Specify the commit that is known to have the bug:

```bash
git bisect bad
```

### Step 3: Mark the Good Commit

Specify a commit that is known to be good (where the bug did not exist):

```bash
git bisect good <commit>
```

### Step 4: Test Each Commit

Git will checkout a commit between the good and bad commits for you to test. You need to check if the bug exists in this commit and then mark it accordingly:

- If the bug is present in the commit, mark it as bad:

    ```bash
    git bisect bad
    ```

- If the bug is not present, mark it as good:

    ```bash
    git bisect good
    ```

Repeat this process until Git identifies the exact commit that introduced the issue.

### Step 5: End Bisect Session

Once the problematic commit is identified, end the bisect session and return to the original branch:

```bash
git bisect reset
```

## Examples of Using `git bisect`

### Example 1: Basic Manual Bisecting

1. **Start Bisecting**:

    ```bash
    git bisect start
    ```

2. **Mark Bad Commit**:

    ```bash
    git bisect bad
    ```

3. **Mark Good Commit**:

    ```bash
    git bisect good <commit>
    ```

4. **Test Commits**: 
   
    Test each commit Git checks out and mark as `bad` or `good`.

5. **End Bisect Session**:

    ```bash
    git bisect reset
    ```

### Example 2: Automated Bisecting with a Test Script

If you have a test script that can automatically determine if a commit is good or bad, you can use `git bisect run` to automate the process.

1. **Create a Test Script**:

    ```bash
    #!/bin/bash
    # test.sh
    make test
    ```

2. **Run Bisect with Script**:

    ```bash
    git bisect start
    git bisect bad
    git bisect good <commit>
    git bisect run ./test.sh
    ```

3. **Git will automatically test commits and identify the problematic commit.**

### Example 3: Finding the Commit That Introduced a Bug

1. **Start Bisecting**:

    ```bash
    git bisect start
    ```

2. **Mark the Current Commit as Bad**:

    ```bash
    git bisect bad
    ```

3. **Mark a Known Good Commit**:

    ```bash
    git bisect good <good-commit-hash>
    ```

4. **Test and Mark Commits**:

    Mark each commit as `good` or `bad` until the problematic commit is found.

5. **End Bisect Session**:

    ```bash
    git bisect reset
    ```

## Common Use Cases

- **Debugging**: Identifying the commit that introduced a bug or issue in the code.
- **Code Review**: Finding when a specific feature or change was added.
- **Regression Testing**: Tracking down when a regression or unwanted change occurred.

## Summary

The `git bisect` command is a powerful tool for locating the commit that introduced a bug or issue by performing a binary search through the commit history. By marking commits as good or bad and using automated testing scripts, you can efficiently identify problematic changes and resolve issues in your repository.
