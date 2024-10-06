# Python Comments and Documentation

Comments and documentation are essential for making code readable and maintainable. They help explain the purpose of code, provide context, and can be used to disable code during testing or debugging.

## 1. Single-Line Comments

Single-line comments in Python start with the `#` symbol. Everything after `#` on the same line is considered a comment and is ignored by the interpreter.

### Example:

```python
# This is a single-line comment
print("Hello, World!")  # This comment is inline with code
```

### Output:

```
Hello, World!
```

## 2. Multi-Line Comments

Multi-line comments can be created using a series of single-line comments or using triple quotes. Triple quotes are more commonly used for multi-line comments.

### Example:

```python
# This is a multi-line comment
# It spans multiple lines
# Each line starts with a hash symbol

"""
This is another way to create multi-line comments.
It uses triple quotes and can span multiple lines.
"""
print("Multi-line comments in Python")
```

### Output:

```
Multi-line comments in Python
```

## 3. Docstrings

Docstrings (documentation strings) are a special kind of comment used to document modules, classes, functions, and methods. They are written using triple quotes and are the first statement in a module, class, function, or method.

### 3.1 Module Docstrings

Module docstrings describe the contents of a module.

### Example:

```python
"""
This module demonstrates the use of docstrings.
It includes examples of module, class, and function docstrings.
"""

def example_function():
    """This function prints a simple message."""
    print("Hello from example_function!")
```

### 3.2 Class Docstrings

Class docstrings describe the purpose and behavior of a class.

### Example:

```python
class ExampleClass:
    """
    This class demonstrates the use of class docstrings.
    
    Attributes:
        attr1 (str): Description of attribute 1.
        attr2 (int): Description of attribute 2.
    """

    def __init__(self, attr1, attr2):
        """
        The constructor for ExampleClass.

        Parameters:
           attr1 (str): Description of attribute 1.
           attr2 (int): Description of attribute 2.
        """
        self.attr1 = attr1
        self.attr2 = attr2
```

### 3.3 Function and Method Docstrings

Function and method docstrings describe what the function or method does, its parameters, and return values.

### Example:

```python
def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b
```

### Example of a method docstring in a class:

```python
class MathOperations:
    """
    A class to perform basic math operations.
    """

    def multiply(self, a, b):
        """
        Multiplies two numbers.

        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The product of the two numbers.
        """
        return a * b
```

## 4. Accessing Docstrings

Docstrings can be accessed using the `__doc__` attribute of a module, class, function, or method.

### Example:

```python
def example_function():
    """This function prints a simple message."""
    print("Hello from example_function!")

print(example_function.__doc__)
```

### Output:

```
This function prints a simple message.
```

## Conclusion

Comments and documentation are critical for writing clear and maintainable code. Single-line comments and multi-line comments help explain specific parts of the code, while docstrings provide comprehensive documentation for modules, classes, and functions. Using comments and docstrings effectively can greatly enhance the readability and usability of your code.

By practicing the examples provided, you can gain a deeper understanding of how to use comments and docstrings in Python to document your code effectively.