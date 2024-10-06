# Python `functools` Module: Detailed Overview and Examples

The `functools` module in Python provides higher-order functions that act on or return other functions. These utilities help with common functional programming patterns and can make your code more concise and expressive.

## Key Functions and Methods

### 1. `functools.partial`

#### Description

`functools.partial` allows you to fix a certain number of arguments of a function and generate a new function.

#### Syntax

```python
functools.partial(func, /, *args, **keywords)
```

#### Example

```python
import functools

def multiply(x, y):
    return x * y

# Create a new function that multiplies by 2
double = functools.partial(multiply, 2)

print(double(5))  # Output: 10
```

### 2. `functools.reduce`

#### Description

`functools.reduce` applies a binary function cumulatively to the items of a sequence, from left to right, to reduce the sequence to a single value.

#### Syntax

```python
functools.reduce(function, iterable[, initializer])
```

#### Example

```python
import functools

# Sum all elements in a list
result = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result)  # Output: 15
```

### 3. `functools.lru_cache`

#### Description

`functools.lru_cache` is a decorator that caches the results of function calls with least-recently-used (LRU) eviction.

#### Syntax

```python
functools.lru_cache(maxsize=128, typed=False)
```

#### Example

```python
import functools

@functools.lru_cache(maxsize=100)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

### 4. `functools.singledispatch`

#### Description

`functools.singledispatch` is a decorator that transforms a function into a single-dispatch generic function.

#### Syntax

```python
@functools.singledispatch
def func(arg, *args, **kw):
    ...
```

#### Example

```python
import functools

@functools.singledispatch
def process(value):
    print(f"Default: {value}")

@process.register(int)
def _(value):
    print(f"Integer: {value}")

@process.register(str)
def _(value):
    print(f"String: {value}")

process(10)    # Output: Integer: 10
process("hi")  # Output: String: hi
process([1, 2, 3])  # Output: Default: [1, 2, 3]
```

### 5. `functools.update_wrapper` and `functools.wraps`

#### Description

`functools.update_wrapper` is used to update a wrapper function to look more like the wrapped function by copying attributes. `functools.wraps` is a decorator that applies `update_wrapper` to the wrapper function.

#### Syntax

```python
functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
```

#### Example

```python
import functools

def my_decorator(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = f(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    return f"Hello, {name}"

print(say_hello("Alice"))
print(say_hello.__name__)  # Output: say_hello
```

### 6. `functools.total_ordering`

#### Description

`functools.total_ordering` is a class decorator that fills in missing comparison methods (`<`, `<=`, `>`, `>=`) based on `__eq__` and one other method.

#### Syntax

```python
@functools.total_ordering
class MyClass:
    ...
```

#### Example

```python
import functools

@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1 > person2)  # Output: True
print(person1 <= person2)  # Output: False
```

### 7. `functools.cached_property`

#### Description

`functools.cached_property` transforms a method into a property whose value is computed once and then cached as a normal attribute for the life of the instance.

#### Syntax

```python
class MyClass:
    @functools.cached_property
    def my_property(self):
        ...
```

#### Example

```python
import functools

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @functools.cached_property
    def area(self):
        print("Computing area")
        return 3.14159 * self.radius * self.radius

c = Circle(10)
print(c.area)  # Output: Computing area 314.159
print(c.area)  # Output: 314.159
```

## Conclusion

The `functools` module in Python provides a variety of higher-order functions that can greatly simplify and enhance your code. From partial application of functions with `partial` to memoization with `lru_cache`, and method overloading with `singledispatch`, the module offers powerful tools for functional programming and optimization. By leveraging these utilities, you can write more concise, readable, and efficient Python code.