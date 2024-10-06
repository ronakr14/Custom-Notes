# Python Decorators and Generators: Overview and Examples

This report covers the concepts of decorators and generators in Python, explaining how they work and providing suitable examples for each.

## Decorators

Decorators are a way to modify or enhance the behavior of functions or methods. They are commonly used for logging, enforcing access control and authentication, instrumentation, caching, and more. Decorators are applied to functions or methods using the `@` symbol.

### Basic Decorator Example

A simple decorator that prints a message before and after a function is called.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
```

### Decorator with Arguments

A decorator that accepts arguments.

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Output:
```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

### Class Decorators

Decorators can also be applied to classes.

```python
def decorator(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            self._original = cls(*args, **kwargs)
        
        def __getattr__(self, name):
            return getattr(self._original, name)

        def __str__(self):
            return f"Decorated {self._original}"

    return NewClass

@decorator
class MyClass:
    def __str__(self):
        return "MyClass instance"

instance = MyClass()
print(instance)
```

Output:
```
Decorated MyClass instance
```

## Generators

Generators are a simple way to create iterators. They are written like regular functions but use the `yield` statement to return data one piece at a time, suspending the function's state between each `yield` and resuming from that state on the next call.

### Simple Generator Example

A generator function that yields numbers from 0 to 2.

```python
def simple_generator():
    yield 0
    yield 1
    yield 2

gen = simple_generator()
for value in gen:
    print(value)
```

Output:
```
0
1
2
```

### Generator for Fibonacci Sequence

A generator function to yield Fibonacci numbers.

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_gen = fibonacci(5)
for value in fib_gen:
    print(value)
```

Output:
```
0
1
1
2
3
```

### Generator Expressions

Generator expressions provide an easy way to create generators. They are similar to list comprehensions but use parentheses instead of square brackets.

```python
gen_expr = (x * x for x in range(5))
for value in gen_expr:
    print(value)
```

Output:
```
0
1
4
9
16
```

### Using `yield from`

The `yield from` statement allows a generator to delegate part of its operations to another generator.

```python
def generator1():
    yield from range(3)

def generator2():
    yield from generator1()
    yield from range(3, 6)

for value in generator2():
    print(value)
```

Output:
```
0
1
2
3
4
5
```

## Conclusion

Python decorators and generators are powerful tools for enhancing and simplifying code. Decorators allow you to modify or extend the behavior of functions and methods in a clean and readable way, while generators provide a memory-efficient way to iterate over large data sets or infinite sequences. Understanding and using these concepts can greatly improve the flexibility and efficiency of your Python programs.