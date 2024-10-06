# Git LFS (Large File Storage) Tutorial

## Overview

Git Large File Storage (LFS) is an extension for Git that improves the handling of large files in repositories. Instead of storing large files directly in the Git repository, Git LFS replaces them with text pointers inside the repository and stores the actual file contents on a remote server.

## What is Git LFS?

Git LFS (Large File Storage) helps manage large files in Git repositories by replacing large files with small pointer files in the repository and storing the actual file content on a remote server. This reduces the size of the Git repository and speeds up operations like cloning and fetching.

## Installation

To use Git LFS, you first need to install it. Follow these steps:

### On macOS

```bash
brew install git-lfs
```

### On Windows

Download the installer from the [Git LFS releases page](https://git-lfs.github.com/) and follow the installation instructions.

### On Linux

Use the package manager specific to your distribution:

```bash
# Debian/Ubuntu
sudo apt-get install git-lfs

# Fedora
sudo dnf install git-lfs

# CentOS
sudo yum install git-lfs
```

After installation, you need to initialize Git LFS in your repository:

```bash
git lfs install
```

## Basic Commands

### Track Files

To track files with Git LFS, specify the file patterns to be managed by LFS:

```bash
git lfs track "*.psd"
```

This command adds the specified file pattern to `.gitattributes`, which tells Git LFS to manage files matching this pattern.

### Untrack Files

To stop tracking files with Git LFS, use:

```bash
git lfs untrack "*.psd"
```

This command removes the specified file pattern from `.gitattributes`.

### Add Files

Add files to the Git repository as usual:

```bash
git add path/to/largefile.psd
```

### Commit Files

Commit the changes to the repository:

```bash
git commit -m "Add large file using Git LFS"
```

### Push Changes

Push your changes to the remote repository:

```bash
git push origin main
```

Git LFS will upload the large files to the LFS cache on the server.

### Pull Changes

To fetch the large files stored in LFS, use:

```bash
git pull
```

### Clone Repository

When cloning a repository with LFS files, use:

```bash
git clone <repository-url>
```

Git LFS will automatically download the large files after cloning.

## Examples

### Example 1: Tracking and Committing a Large File

1. **Initialize Git LFS**:

    ```bash
    git lfs install
    ```

2. **Track a Large File**:

    ```bash
    git lfs track "*.zip"
    ```

3. **Add and Commit the File**:

    ```bash
    git add largefile.zip
    git commit -m "Add large zip file using Git LFS"
    ```

4. **Push to Remote**:

    ```bash
    git push origin main
    ```

5. **Verify LFS Tracking**:

    ```bash
    git lfs ls-files
    ```

### Example 2: Untracking a File

1. **Untrack a File**:

    ```bash
    git lfs untrack "*.zip"
    ```

2. **Remove the File from Git LFS**:

    Remove the file from the repository and re-add it if needed:

    ```bash
    git rm --cached largefile.zip
    git add largefile.zip
    git commit -m "Remove large file from Git LFS"
    ```

3. **Push Changes**:

    ```bash
    git push origin main
    ```

## Common Use Cases

- **Managing Large Binary Files**: Ideal for large files like images, videos, datasets, and compiled binaries.
- **Reducing Repository Size**: Keeps the repository size manageable by storing large files on a remote server.
- **Improving Clone and Fetch Performance**: Reduces the time required to clone or fetch repositories with large files.

## Summary

Git LFS is a valuable tool for managing large files in Git repositories, improving performance, and reducing repository size. By tracking large files with Git LFS, you can efficiently handle large assets while keeping your Git repository lightweight and responsive.
