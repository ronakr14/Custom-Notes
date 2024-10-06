# Git Send Email Tutorial

## Overview

The `git send-email` command is used to send patches via email. This is particularly useful for contributing to projects that use mailing lists for code reviews and patch submissions. The command allows you to send patches created with `git format-patch` directly to an email address.

## What is `git send-email`?

`git send-email` is a Git command that facilitates sending patches via email. It is used in workflows where patches need to be reviewed or submitted via mailing lists. It integrates with Git’s patch management and email configuration tools to send patches directly from the command line.

## Setting Up `git send-email`

Before using `git send-email`, you need to configure your email settings. This involves setting up the email server and user credentials in your Git configuration.

### Configure Email Settings

1. **Set the Email Address**:

    ```bash
    git config --global user.email "your-email@example.com"
    ```

2. **Configure the SMTP Server**:

    Add your SMTP server details to your Git configuration. Replace placeholders with actual values:

    ```bash
    git config --global sendemail.smtpserver "smtp.example.com"
    git config --global sendemail.smtpuser "your-username"
    git config --global sendemail.smtppass "your-password"
    ```

3. **Optional: Configure Other Email Settings**:

    ```bash
    git config --global sendemail.smtpport "587"
    git config --global sendemail.smtpssl "true"
    ```

## Sending Patches

Once you have configured `git send-email`, you can send patches via email.

### Basic Syntax

```bash
git send-email [options] <patch-files>
```

### Example: Sending a Patch via Email

1. **Create a Patch File**:

    First, create a patch file using `git format-patch`:

    ```bash
    git format-patch -1 HEAD
    ```

    This generates a patch file named `0001-<commit-message>.patch`.

2. **Send the Patch File via Email**:

    Use `git send-email` to send the patch:

    ```bash
    git send-email 0001-<commit-message>.patch
    ```

    By default, `git send-email` will prompt for recipient email addresses and other details.

### Example: Sending Multiple Patches

To send multiple patches, specify the patch files:

```bash
git send-email 0001-patch1.patch 0002-patch2.patch
```

You can also use a pattern to match multiple patch files:

```bash
git send-email *.patch
```

## Examples

### Example 1: Sending a Single Patch

1. **Create a Patch**:

    ```bash
    git format-patch -1 HEAD
    ```

2. **Send the Patch**:

    ```bash
    git send-email 0001-Add-new-feature.patch
    ```

3. **Follow the Prompts**:

    Enter the recipient email address and any other required information.

### Example 2: Sending Patches to a Mailing List

1. **Create Multiple Patches**:

    ```bash
    git format-patch HEAD~3..HEAD
    ```

2. **Send Patches to a Mailing List**:

    ```bash
    git send-email --to="patches@project.org" *.patch
    ```

## Common Use Cases

- **Contributing to Open Source Projects**: Many projects use mailing lists for code reviews and patch submissions.
- **Submitting Patches for Review**: Sending patches for review and discussion before merging them into the main codebase.
- **Archiving Changes**: Sending patches as part of an email thread for record-keeping or documentation.

## Summary

`git send-email` is a powerful tool for sending patches via email, particularly in workflows involving mailing lists and code reviews. By configuring your email settings and using the command, you can streamline the process of sharing changes with collaborators and maintaining a clean and organized codebase.
