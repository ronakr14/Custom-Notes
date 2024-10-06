# Python `@dataclass` Decorator: Detailed Overview and Examples

The `@dataclass` decorator in Python, introduced in Python 3.7, provides a convenient way to create classes that are primarily used for storing data. It automatically generates special methods like `__init__()`, `__repr__()`, `__eq__()`, and `__hash__()` based on the class attributes. This reduces boilerplate code and simplifies class definitions.

## Basic Usage

To use the `@dataclass` decorator, you need to import it from the `dataclasses` module and apply it to your class.

### Example: Basic Data Class

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person(name="Alice", age=30)
print(p)  # Output: Person(name='Alice', age=30)
```

## Generated Methods

The `@dataclass` decorator automatically generates several methods:

### `__init__()`

The `__init__` method is automatically created, allowing you to instantiate the class with the specified attributes.

```python
@dataclass
class Person:
    name: str
    age: int

p = Person(name="Alice", age=30)
```

### `__repr__()`

The `__repr__` method provides a string representation of the object, useful for debugging.

```python
p = Person(name="Alice", age=30)
print(p)  # Output: Person(name='Alice', age=30)
```

### `__eq__()`

The `__eq__` method compares two instances of the class to check for equality based on their attributes.

```python
p1 = Person(name="Alice", age=30)
p2 = Person(name="Alice", age=30)
p3 = Person(name="Bob", age=25)

print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False
```

### `__hash__()`

The `__hash__` method allows instances of the data class to be used as dictionary keys or elements of sets.

```python
person_set = {Person(name="Alice", age=30), Person(name="Bob", age=25)}
print(len(person_set))  # Output: 2
```

## Customizing Data Classes

### Default Values

You can provide default values for attributes.

```python
@dataclass
class Person:
    name: str
    age: int = 0

p1 = Person(name="Alice")
p2 = Person(name="Bob", age=25)

print(p1)  # Output: Person(name='Alice', age=0)
print(p2)  # Output: Person(name='Bob', age=25)
```

### Default Factory

For mutable default values, such as lists or dictionaries, use `field(default_factory=...)` to avoid mutable default arguments.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)

team = Team(name="Developers")
print(team)  # Output: Team(name='Developers', members=[])
```

### Immutable Data Classes

To make a data class immutable, use the `frozen=True` parameter. This makes instances of the class hashable and their attributes read-only.

```python
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p1 = Point(1, 2)
print(p1.x)  # Output: 1
# p1.x = 3  # Raises dataclasses.FrozenInstanceError
```

### Custom Methods

You can still define custom methods within a data class.

```python
@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

r = Rectangle(width=5, height=10)
print(r.area())  # Output: 50
```

## Inheritance with Data Classes

Data classes support inheritance, allowing you to create subclasses with additional or modified attributes.

### Example: Inheritance

```python
from dataclasses import dataclass

@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

d = Dog(name="Buddy", breed="Golden Retriever")
print(d)  # Output: Dog(name='Buddy', breed='Golden Retriever')
```

## Conclusion

The `@dataclass` decorator in Python provides a powerful and convenient way to define classes that are primarily used to store data. By automatically generating common methods and supporting features like default values, immutable instances, and inheritance, `@dataclass` simplifies the creation and management of data-centric classes. This leads to cleaner, more readable code and reduces boilerplate in your Python programs.