# Python Basics

## Overview

Python is a high-level, interpreted programming language known for its simplicity and readability. This document covers the basics of Python programming, including syntax, data types, and control structures.

## Hello World

The classic first program in any language is to print "Hello, World!" to the console.

```python
print("Hello, World!")
```

## Variables and Data Types

### Variables

Variables store data that can be used and manipulated in your programs.

```python
x = 10
name = "Alice"
```

#### Example

```python
age = 25
print(age)  # Output: 25
```

### Data Types

Python supports several data types, including integers, floats, strings, and booleans.

- **Integer**: `int`
- **Float**: `float`
- **String**: `str`
- **Boolean**: `bool`

#### Example

```python
integer_num = 10
float_num = 10.5
string_value = "Hello"
boolean_value = True

print(type(integer_num))  # Output: <class 'int'>
print(type(float_num))    # Output: <class 'float'>
print(type(string_value)) # Output: <class 'str'>
print(type(boolean_value))# Output: <class 'bool'>
```

## Operators

### Arithmetic Operators

- **Addition**: `+`
- **Subtraction**: `-`
- **Multiplication**: `*`
- **Division**: `/`
- **Modulus**: `%`
- **Exponentiation**: `**`
- **Floor Division**: `//`

#### Example

```python
a = 10
b = 3

print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333...
print(a % b)  # Output: 1
print(a ** b) # Output: 1000
print(a // b) # Output: 3
```

### Comparison Operators

- **Equal to**: `==`
- **Not equal to**: `!=`
- **Greater than**: `>`
- **Less than**: `<`
- **Greater than or equal to**: `>=`
- **Less than or equal to**: `<=`

#### Example

```python
x = 10
y = 20

print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True
```

## Control Structures

### Conditional Statements

Use `if`, `elif`, and `else` for decision-making.

```python
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
```

#### Example

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# Output: Odd
```

### Loops

#### `for` Loop

Iterate over a sequence (e.g., list, tuple, string).

```python
for i in range(5):
    print(i)
```

#### Example

```python
for i in [1, 2, 3, 4, 5]:
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
```

#### `while` Loop

Repeat while a condition is true.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

#### Example

```python
num = 1
while num <= 5:
    print(num)
    num += 1
# Output:
# 1
# 2
# 3
# 4
# 5
```

## Functions

Functions group reusable code. Use the `def` keyword to define a function.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

#### Example

```python
def add(x, y):
    return x + y

result = add(10, 5)
print(result)  # Output: 15
```

## Lists

Lists store multiple items in a single variable. Lists are ordered and mutable.

```python
fruits = ["apple", "banana", "cherry"]
```

#### Example

```python
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1
print(numbers[1:3])# Output: [2, 3]
```

## Dictionaries

Dictionaries store key-value pairs. They are unordered and mutable.

```python
person = {"name": "Alice", "age": 25}
```

#### Example

```python
student = {"name": "John", "grade": "A"}
print(student["name"])  # Output: John
```

## Summary

This document covers fundamental Python concepts, including variables, data types, operators, control structures, functions, lists, and dictionaries. Python’s simplicity and readability make it a great choice for both beginners and experienced developers. For more in-depth information, refer to the [official Python documentation](https://docs.python.org/3/).