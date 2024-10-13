# Python Type Hints: Detailed Overview and Examples

Type hints, introduced in PEP 484, are a feature in Python that allow you to annotate the types of variables, function parameters, and return values. They help improve code readability, provide better tooling support, and aid in catching type-related errors during development.

## What are Type Hints?

Type hints are a way to specify the expected types of variables, function parameters, and return values. They do not enforce type checking at runtime but are used by tools such as linters and IDEs to provide type checking and code suggestions.

### Basic Syntax

Type hints use the `typing` module and are added as comments or annotations to your code.

```python
# Example of type hints in a function signature
def add(a: int, b: int) -> int:
    return a + b
```

## Function Annotations

### Annotating Function Parameters and Return Types

#### Example: Function with Type Hints

```python
def greet(name: str) -> str:
    return f'Hello, {name}!'
```

In this example, `name` is expected to be a `str`, and the function is expected to return a `str`.

### Using Type Hints with Default Values

#### Example: Function with Default Parameter

```python
def repeat(message: str, times: int = 1) -> str:
    return message * times
```

Here, `message` is a `str`, `times` is an `int` with a default value of `1`, and the function returns a `str`.

## Type Hinting for Variables

### Annotating Variable Types

#### Example: Variable Annotations

```python
from typing import List

# Annotating a list of integers
numbers: List[int] = [1, 2, 3, 4, 5]
```

In this example, `numbers` is a list where each element is of type `int`.

## Complex Data Types

### Using Typing for Collections

#### Example: Annotating Lists, Tuples, and Dictionaries

```python
from typing import List, Tuple, Dict

def process_data(data: List[int]) -> Tuple[int, int]:
    return min(data), max(data)

def user_info() -> Dict[str, str]:
    return {'name': 'Alice', 'age': '30'}
```

In this example, `process_data` takes a list of integers and returns a tuple of two integers. `user_info` returns a dictionary with string keys and values.

### Union Types

#### Example: Using `Union` for Multiple Possible Types

```python
from typing import Union

def stringify(value: Union[int, float]) -> str:
    return str(value)
```

Here, `value` can be either an `int` or a `float`, and the function returns a `str`.

## Type Aliases

### Creating Custom Type Aliases

#### Example: Defining Type Aliases

```python
from typing import List, Dict

# Define a type alias for a list of dictionaries
UserList = List[Dict[str, str]]

def get_users() -> UserList:
    return [{'name': 'Alice', 'email': 'alice@example.com'}]
```

In this example, `UserList` is an alias for a list of dictionaries with string keys and values.

## Optional Types

### Using `Optional` for Nullable Types

#### Example: Optional Type Hint

```python
from typing import Optional

def find_item(id: int) -> Optional[str]:
    items = {1: 'apple', 2: 'banana'}
    return items.get(id)
```

Here, `find_item` returns either a `str` or `None` if the item is not found.

## Type Hinting for Classes

### Annotating Methods and Attributes

#### Example: Type Hints in Classes

```python
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def birthday(self) -> None:
        self.age += 1
```

In this example, `name` and `age` are annotated as `str` and `int`, respectively. The `birthday` method does not return any value (`None`).

## Generics

### Using Generics for Type Safety

#### Example: Defining a Generic Class

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()
```

In this example, `Stack` is a generic class that can hold items of any type.

## Type Checking with `mypy`

### Using `mypy` for Static Type Checking

You can use `mypy` to perform static type checking based on the type hints provided in your code.

#### Example: Running `mypy`

1. Install `mypy` using pip:

   ```bash
   pip install mypy
   ```

2. Run `mypy` on your script:

   ```bash
   mypy script.py
   ```

`mypy` will analyze your code and report any type errors or inconsistencies.

## Summary

Type hints in Python provide a way to annotate the types of variables, function parameters, and return values, enhancing code readability and enabling better tooling support. By using type hints, you can make your code more robust, maintainable, and easier to understand. With tools like `mypy`, you can perform static type checking to catch type-related errors before runtime. Whether you are working with simple data types or complex class structures, type hints offer a flexible and powerful way to manage types in your Python code.