# Python Functions: Overview and Examples

This report covers various types of functions in Python, including regular functions, lambda functions, nested functions, recursive functions, iterable and dictionary unpacking in functions, list arguments in function calls, and higher-order functions like `map()`, `reduce()`, and `filter()`.

## Regular Functions

Functions in Python are defined using the `def` keyword. They can take arguments and return a value using the `return` keyword.

### Example: Simple Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Lambda Functions

Lambda functions are anonymous functions defined using the `lambda` keyword. They are typically used for short, simple operations.

### Example: Lambda Function

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

## Nested Functions

A nested function is a function defined inside another function. They are used to encapsulate functionality within a specific scope.

### Example: Nested Function

```python
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the outer function!")
```

## Recursive Functions

A recursive function is a function that calls itself to solve a problem.

### Example: Factorial Function

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

## Iterable and Dictionary Unpacking in Functions

You can unpack iterables and dictionaries when passing them as arguments to functions.

### Example: Iterable Unpacking

```python
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(sum_numbers(*numbers))  # Output: 6
```

### Example: Dictionary Unpacking

```python
def display_info(name, age):
    return f"Name: {name}, Age: {age}"

info = {'name': 'Alice', 'age': 30}
print(display_info(**info))  # Output: Name: Alice, Age: 30
```

## List Arguments in Function Call

You can pass a list of arguments to a function using the `*` operator.

### Example: List Arguments

```python
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(1, 2, 3, 4))  # Output: 24
```

## Higher-order Functions

### `map()` Function

The `map()` function applies a given function to all items in an iterable.

### Example: `map()`

```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

### `reduce()` Function

The `reduce()` function applies a given function cumulatively to the items of an iterable.

### Example: `reduce()`

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24
```

### `filter()` Function

The `filter()` function filters items in an iterable based on a given function.

### Example: `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4, 6]
```

## Conclusion

Python functions are versatile and powerful, enabling you to encapsulate logic, create reusable code, and perform complex operations succinctly. Regular functions, lambda functions, nested functions, and recursive functions offer various ways to implement functionality. Unpacking iterables and dictionaries, using list arguments, and leveraging higher-order functions like `map()`, `reduce()`, and `filter()` provide additional flexibility and efficiency in handling data. Understanding and mastering these concepts are essential for effective Python programming.