# Git Attributes Tutorial

## Overview

Git attributes are used to define specific behaviors for files in your Git repository. These behaviors can include text encoding, merge strategies, and custom handling of files. Git attributes are configured using the `.gitattributes` file in the repository. This document covers the basics of using git attributes with examples.

## What are Git Attributes?

Git attributes allow you to specify how Git should handle certain files in your repository. This can include settings for text file normalization, merge conflict resolution, and other file-specific behaviors. Attributes are defined in the `.gitattributes` file.

## Creating and Configuring `.gitattributes`

To use Git attributes, you need to create a `.gitattributes` file in the root directory of your repository. You can then define attributes for files and directories within this file.

### Example: Creating a `.gitattributes` File

1. Create a `.gitattributes` file in the root directory of your repository:

    ```bash
    touch .gitattributes
    ```

2. Open the file in your text editor and define attributes:

    ```bash
    *.txt text
    ```

## Text Attributes

Text attributes control how text files are handled, such as normalizing line endings.

### Example: Normalizing Line Endings

1. Add a text attribute to ensure consistent line endings:

    ```bash
    *.txt text eol=lf
    ```

    This ensures that all `.txt` files use LF (line feed) line endings.

2. To apply these changes to existing files, you may need to run:

    ```bash
    git add --renormalize .
    ```

## Merge Strategies

Merge strategies define how Git should handle merge conflicts for specific files.

### Example: Custom Merge Driver

1. Define a custom merge driver in `.gitattributes`:

    ```bash
    *.md merge=union
    ```

2. Configure the merge driver in the `.git/config` file:

    ```bash
    [merge "union"]
        name = "Union Merge"
        driver = cat %A %O %B > %A
    ```

    This example uses a "union" merge strategy for `.md` files, concatenating the changes from both branches.

## Exporting Attributes

Attributes can also be used to control file export behavior.

### Example: Excluding Files from Export

1. Exclude files from export with `export-ignore`:

    ```bash
    *.log export-ignore
    ```

    This prevents `.log` files from being included in exported archives (e.g., zip files).

## Custom Attributes

Custom attributes allow you to define arbitrary attributes that can be used by scripts or tools.

### Example: Defining and Using Custom Attributes

1. Define a custom attribute in `.gitattributes`:

    ```bash
    *.custom filter=myfilter
    ```

2. Configure the filter in `.git/config`:

    ```bash
    [filter "myfilter"]
        clean = myfilter-clean
        smudge = myfilter-smudge
    ```

    This example uses a custom filter for files with the `.custom` extension, with specified clean and smudge scripts.

## Useful Tips

- **Check Attributes**: Use `git check-attr` to view the attributes applied to specific files.

    ```bash
    git check-attr --all <file>
    ```

- **Global Attributes**: You can also configure global attributes by placing the `.gitattributes` file in your home directory, but this is less common.

- **Documentation**: Refer to the [Git Attributes Documentation](https://git-scm.com/docs/gitattributes) for more detailed information on available attributes and options.

## Summary

Git attributes provide powerful ways to control how files are handled in your repository. By configuring attributes in the `.gitattributes` file, you can manage text file normalization, custom merge strategies, export behavior, and custom handling of files. Understanding and utilizing these attributes can help you maintain a consistent and manageable codebase.
