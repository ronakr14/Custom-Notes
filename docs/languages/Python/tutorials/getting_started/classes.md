# Python Classes: Overview and Examples

This report provides a comprehensive overview of Python classes, including bound, unbound, and static methods, inheritance, monkey patching, new-style and old-style classes, class compositions, singleton classes, descriptors, dotted lookups, and data classes.

## Classes in Python

Classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

### Basic Class Definition

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

p = Person("Alice", 30)
print(p.greet())
```

## Bound, Unbound, and Static Methods

### Bound Methods

A bound method is a method that is associated with an instance of a class.

```python
class Example:
    def bound_method(self):
        return "This is a bound method."

e = Example()
print(e.bound_method())  # Bound method called on instance
```

### Unbound Methods

In Python 3, there are no true unbound methods. However, in Python 2, an unbound method is one that is not bound to an instance.

### Static Methods

Static methods do not depend on class or instance variables. They are defined using the `@staticmethod` decorator.

```python
class Example:
    @staticmethod
    def static_method():
        return "This is a static method."

print(Example.static_method())  # Static method called on class
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

### Example: Single Inheritance

```python
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

d = Dog()
print(d.speak())  # Inherited method
print(d.bark())   # Method of subclass
```

### Example: Multiple Inheritance

```python
class A:
    def method_a(self):
        return "Method A"

class B:
    def method_b(self):
        return "Method B"

class C(A, B):
    pass

c = C()
print(c.method_a())  # Method from class A
print(c.method_b())  # Method from class B
```

## Monkey Patching

Monkey patching refers to modifying or extending a module or class at runtime.

### Example: Monkey Patching

```python
class MyClass:
    def greet(self):
        return "Hello!"

def new_greet(self):
    return "Hi there!"

# Patch the greet method
MyClass.greet = new_greet

obj = MyClass()
print(obj.greet())  # Output: Hi there!
```

## New-Style and Old-Style Classes

### Old-Style Classes (Python 2 only)

Old-style classes do not inherit from `object`.

```python
class OldStyleClass:
    pass
```

### New-Style Classes

New-style classes inherit from `object`. They provide a more consistent object model.

```python
class NewStyleClass(object):
    pass
```

In Python 3, all classes are new-style classes.

## Class Compositions

Class composition is a design principle where one class contains an instance of another class.

### Example: Class Composition

```python
class Engine:
    def start(self):
        return "Engine starts"

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start() + " and Car starts"

c = Car()
print(c.start())
```

## Singleton Class

A singleton class ensures that only one instance of the class is created.

### Example: Singleton Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True
```

## Descriptors and Dotted Lookups

Descriptors are objects that define how attributes are accessed or modified. They are used to create managed attributes.

### Example: Descriptor

```python
class Descriptor:
    def __get__(self, instance, owner):
        return "Descriptor value"

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Output: Descriptor value
```

### Dotted Lookups

Dotted lookups refer to accessing attributes and methods using dot notation.

```python
class Example:
    def method(self):
        return "Method called"

e = Example()
print(e.method())  # Output: Method called
```

## Data Classes

Data classes are a feature introduced in Python 3.7 to simplify the creation of classes that are primarily used to store data.

### Example: Data Class

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p = Person(name="Alice", age=30)
print(p)           # Output: Person(name='Alice', age=30)
print(p.name)      # Output: Alice
print(p.age)       # Output: 30
```

## Conclusion

Understanding Python classes and their associated features—such as methods, inheritance, monkey patching, class types, composition, singletons, descriptors, and data classes—is essential for writing efficient and maintainable object-oriented code. These concepts provide powerful tools for structuring and managing complex systems in Python.