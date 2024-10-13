# Linux Shell Scripting

## Overview

Shell scripting in Linux allows you to automate tasks and execute commands in a sequence. Shell scripts are written in various shell languages, such as Bash, and can simplify repetitive tasks and system administration.

## Basic Concepts

### Shebang

The shebang (`#!`) specifies the interpreter for the script.

```sh
#!/bin/bash
```

#### Example

```sh
#!/bin/bash
# This line tells the system to use the Bash shell to interpret the script
```

### Making a Script Executable

To make a script executable, use the `chmod` command:

```sh
chmod +x <script_name>
```

#### Example

```sh
chmod +x myscript.sh
# Makes 'myscript.sh' executable
```

### Running a Script

To run a script, specify its path:

```sh
./<script_name>
```

#### Example

```sh
./myscript.sh
# Executes 'myscript.sh'
```

## Basic Script Elements

### Variables

Variables store data and can be used throughout the script.

```sh
variable_name=value
```

#### Example

```sh
#!/bin/bash
name="Alice"
echo "Hello, $name"
# Output: Hello, Alice
```

### Comments

Comments are added with the `#` symbol and are ignored by the shell.

```sh
# This is a comment
```

#### Example

```sh
#!/bin/bash
# This script displays a message
echo "Hello, World!"
```

### Control Structures

#### Conditional Statements

Use `if`, `then`, `elif`, and `else` for conditional execution.

```sh
if [ condition ]; then
    commands
elif [ other_condition ]; then
    other_commands
else
    else_commands
fi
```

#### Example

```sh
#!/bin/bash
if [ -f "file.txt" ]; then
    echo "file.txt exists."
else
    echo "file.txt does not exist."
fi
```

#### Loops

Loops iterate over a set of commands.

##### `for` Loop

```sh
for variable in list; do
    commands
done
```

###### Example

```sh
#!/bin/bash
for i in 1 2 3 4 5; do
    echo "Number $i"
done
```

##### `while` Loop

```sh
while [ condition ]; do
    commands
done
```

###### Example

```sh
#!/bin/bash
count=1
while [ $count -le 5 ]; do
    echo "Count $count"
    ((count++))
done
```

### Functions

Functions group commands and can be called multiple times.

```sh
function_name() {
    commands
}
```

#### Example

```sh
#!/bin/bash
greet() {
    echo "Hello, $1"
}

greet "Alice"
# Output: Hello, Alice
```

## Advanced Topics

### Command-Line Arguments

Access arguments passed to the script using `$1`, `$2`, etc.

```sh
#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
```

#### Example

```sh
./myscript.sh arg1 arg2
# Output:
# First argument: arg1
# Second argument: arg2
```

### Redirection and Pipes

- **Redirection**: `>` to write output to a file, `<` to read from a file.

```sh
echo "Hello" > file.txt
cat < file.txt
```

- **Pipes**: `|` to pass the output of one command as input to another.

```sh
ls | grep "pattern"
```

#### Example

```sh
#!/bin/bash
ps aux | grep "bash"
# Lists all processes and filters those with "bash"
```

### Error Handling

Check the exit status of commands using `$?`.

```sh
command
if [ $? -ne 0 ]; then
    echo "Command failed"
fi
```

#### Example

```sh
#!/bin/bash
mkdir mydir
if [ $? -ne 0 ]; then
    echo "Failed to create directory"
fi
```

## Summary

Shell scripting is a powerful way to automate tasks and manage system operations. Understanding variables, control structures, loops, functions, and handling input/output will enable you to write effective scripts. For more detailed information, refer to the [Bash manual](https://www.gnu.org/software/bash/manual/) or other shell scripting resources.