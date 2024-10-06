# Git Hooks Tutorial

## Overview

Git hooks are scripts that Git automatically executes before or after certain events, such as commits or merges. They allow you to automate tasks, enforce rules, and integrate custom workflows into your Git process.

## What are Git Hooks?

Git hooks are scripts located in the `.git/hooks` directory of a Git repository. They can be triggered by various Git commands and events. Hooks can be used to perform automated tasks, enforce coding standards, or integrate with other tools.

## Types of Git Hooks

Git provides several types of hooks, each associated with a specific event:

- **Pre-commit**: Runs before a commit is created.
- **Post-commit**: Runs after a commit is created.
- **Pre-receive**: Runs on the server before changes are accepted.
- **Post-receive**: Runs on the server after changes are accepted.
- **Pre-push**: Runs before changes are pushed to a remote repository.
- **Update**: Runs on the server when a branch is updated.
- **Prepare-commit-msg**: Runs before the commit message editor is opened.
- **Commit-msg**: Runs after the commit message is entered.
- **Post-merge**: Runs after a merge is completed.
- **Pre-rebase**: Runs before a rebase starts.
- **Post-checkout**: Runs after a `git checkout` command.

## Setting Up Git Hooks

To set up a Git hook, follow these steps:

1. **Navigate to the Hooks Directory:**

    ```bash
    cd .git/hooks
    ```

2. **Create or Edit a Hook Script:**

    Git hooks are typically written in shell script, but you can use other scripting languages like Python or Perl.

    ```bash
    touch pre-commit
    chmod +x pre-commit
    ```

3. **Write the Hook Script:**

    Edit the hook script to include the commands you want to run. For example, you can use `nano`, `vim`, or any text editor.

    ```bash
    nano pre-commit
    ```

4. **Add Your Script Content:**

    Add the commands or script logic you need. Save and exit the editor.

    ```bash
    #!/bin/sh
    echo "Running pre-commit hook"
    ```

## Examples of Git Hooks

### Pre-commit Hook

The `pre-commit` hook runs before a commit is made. It’s often used to run tests or lint code.

#### Example: Linting Code

```bash
#!/bin/sh
# pre-commit hook to lint code before committing

# Run a linter (e.g., eslint for JavaScript)
eslint .

# Check if linting passed
if [ $? -ne 0 ]; then
    echo "Linting failed. Commit aborted."
    exit 1
fi
```

### Commit-msg Hook

The `commit-msg` hook checks the commit message before the commit is finalized. It can be used to enforce commit message conventions.

#### Example: Enforce Commit Message Format

```bash
#!/bin/sh
# commit-msg hook to enforce commit message format

MESSAGE_FILE=$1
MESSAGE=$(cat $MESSAGE_FILE)

if ! echo "$MESSAGE" | grep -q "^\[ISSUE-\[0-9\]+\] "; then
    echo "Commit message must start with '[ISSUE-<number>] '"
    exit 1
fi
```

### Post-commit Hook

The `post-commit` hook runs after a commit is created. It can be used to notify or log commit details.

#### Example: Notify on Commit

```bash
#!/bin/sh
# post-commit hook to send a notification after commit

# Get the latest commit hash
LATEST_COMMIT=$(git log -1 --format="%H")

# Send a notification (e.g., using a webhook)
curl -X POST -H 'Content-type: application/json' --data '{"text":"New commit made: '"$LATEST_COMMIT"'"}' https://your-webhook-url
```

## Common Use Cases

- **Code Quality**: Run linters, formatters, or tests before committing to ensure code quality.
- **Commit Message Validation**: Enforce conventions for commit messages to maintain consistency.
- **Automated Notifications**: Send notifications or alerts when commits or merges occur.
- **Deployment**: Trigger deployment scripts or processes after successful commits or pushes.

## Summary

Git hooks are powerful tools that allow you to automate various tasks and enforce rules within your Git workflow. By configuring hooks like `pre-commit`, `commit-msg`, and `post-commit`, you can improve code quality, maintain consistency, and integrate with other tools. Customize your Git hooks to fit your development process and enhance productivity.
