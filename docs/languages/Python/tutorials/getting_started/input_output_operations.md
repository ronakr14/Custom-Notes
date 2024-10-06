# Python Basic Input and Output Operations

Python provides various functions for basic input and output operations. These operations allow users to interact with programs by entering data and receiving feedback.

## Input Operations

### `input()` Function

The `input()` function reads a line from the user's input, typically via the keyboard, and returns it as a string.

#### Example 1: Reading a String

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

#### Example 2: Reading an Integer

To read an integer, you need to convert the input string to an integer using `int()`.

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

#### Example 3: Reading a Float

To read a floating-point number, use the `float()` function.

```python
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")
```

## Output Operations

### `print()` Function

The `print()` function outputs data to the standard output (usually the console).

#### Example 1: Printing a String

```python
print("Hello, world!")
```

#### Example 2: Printing Variables

You can print multiple variables by separating them with commas.

```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
```

#### Example 3: Formatted String Literals (f-strings)

Using f-strings (available in Python 3.6 and later) for formatted output.

```python
name = "Bob"
age = 30
print(f"Name: {name}, Age: {age}")
```

#### Example 4: String Formatting with `format()`

You can use the `format()` method for string formatting.

```python
name = "Charlie"
age = 35
print("Name: {}, Age: {}".format(name, age))
```

## Advanced Input and Output

### Reading Multiple Inputs

You can read multiple inputs in a single line using the `split()` method.

#### Example 1: Reading Two Integers

```python
x, y = map(int, input("Enter two integers separated by space: ").split())
print(f"x: {x}, y: {y}")
```

### Writing to a File

You can write data to a file using the `write()` method of a file object.

#### Example 2: Writing to a Text File

```python
with open("output.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("This is a new line.")
```

### Reading from a File

You can read data from a file using the `read()` method.

#### Example 3: Reading a Text File

```python
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
```

## Conclusion

Basic input and output operations in Python are essential for creating interactive programs. The `input()` function allows for user input, while the `print()` function provides output capabilities. For more advanced needs, Python also supports file operations, enabling reading from and writing to files. Mastery of these operations is fundamental for effective programming in Python.