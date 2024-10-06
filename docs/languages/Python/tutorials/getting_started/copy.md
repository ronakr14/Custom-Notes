# Python Different Types of Copies: Detailed Overview and Examples

In Python, copying objects can be done in several ways, depending on whether you need a shallow copy or a deep copy. Understanding these concepts is crucial for managing mutable objects and avoiding unintended side effects in your code.

## Shallow Copy vs. Deep Copy

### Shallow Copy

A shallow copy creates a new object but inserts references into it to the objects found in the original. It means that while the new object is distinct from the original, the contents (i.e., objects referenced) are shared.

#### Example: Shallow Copy with Lists

```python
import copy

original_list = [1, [2, 3], 4]

# Create a shallow copy of the list
shallow_copied_list = copy.copy(original_list)

# Modify the nested list
shallow_copied_list[1][0] = 'changed'

print('Original list:', original_list)       # Output: [1, ['changed', 3], 4]
print('Shallow copied list:', shallow_copied_list)  # Output: [1, ['changed', 3], 4]
```

In this example, modifying the nested list in the shallow copy also affects the original list because both lists share the same nested objects.

### Deep Copy

A deep copy creates a new object and recursively copies all objects found in the original, resulting in a completely independent copy. Changes to the deep copy do not affect the original object.

#### Example: Deep Copy with Lists

```python
import copy

original_list = [1, [2, 3], 4]

# Create a deep copy of the list
deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list
deep_copied_list[1][0] = 'changed'

print('Original list:', original_list)       # Output: [1, [2, 3], 4]
print('Deep copied list:', deep_copied_list)  # Output: [1, ['changed', 3], 4]
```

In this example, modifying the nested list in the deep copy does not affect the original list because they are completely independent.

## Copying Built-in Data Types

### Copying Simple Data Types

Simple data types like integers and strings are immutable, so copying them does not require special handling. Assigning them to a new variable creates a new reference.

#### Example: Copying Integers and Strings

```python
a = 10
b = a  # Copying integer

s1 = 'hello'
s2 = s1  # Copying string

print(a, b)  # Output: 10 10
print(s1, s2)  # Output: hello hello
```

### Copying Mutable Data Types

Mutable data types like lists, dictionaries, and sets require careful handling when copying.

#### Example: Copying Lists

```python
original_list = [1, 2, 3]

# Shallow copy
shallow_copied_list = original_list.copy()

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

print('Original list:', original_list)
print('Shallow copied list:', shallow_copied_list)
print('Deep copied list:', deep_copied_list)
```

### Example: Copying Dictionaries

```python
original_dict = {'a': 1, 'b': [2, 3]}

# Shallow copy
shallow_copied_dict = original_dict.copy()

# Deep copy
deep_copied_dict = copy.deepcopy(original_dict)

# Modify the nested list
shallow_copied_dict['b'][0] = 'changed'

print('Original dict:', original_dict)
print('Shallow copied dict:', shallow_copied_dict)
print('Deep copied dict:', deep_copied_dict)
```

## Copying Custom Objects

### Implementing Custom Copy Methods

You can control how custom objects are copied by implementing `__copy__` and `__deepcopy__` methods.

#### Example: Custom Copy Methods

```python
import copy

class CustomObject:
    def __init__(self, data):
        self.data = data

    def __copy__(self):
        # Create a shallow copy
        new_copy = type(self)(self.data)
        return new_copy

    def __deepcopy__(self, memo):
        # Create a deep copy
        new_copy = type(self)(copy.deepcopy(self.data, memo))
        return new_copy

# Create an instance of CustomObject
original_obj = CustomObject([1, 2, 3])

# Shallow copy
shallow_copied_obj = copy.copy(original_obj)

# Deep copy
deep_copied_obj = copy.deepcopy(original_obj)

# Modify the data in the shallow copy
shallow_copied_obj.data[0] = 'changed'

print('Original object data:', original_obj.data)
print('Shallow copied object data:', shallow_copied_obj.data)
print('Deep copied object data:', deep_copied_obj.data)
```

## When to Use Each Type of Copy

- **Shallow Copy**: Use when you need a new object with the same references to mutable objects as the original.
- **Deep Copy**: Use when you need a completely independent copy of the original object and its nested objects.

## Summary

Understanding the difference between shallow and deep copies is crucial for effective resource management and avoiding unintended side effects in your code. Shallow copies duplicate the outer container but share nested objects, while deep copies create a completely independent copy of the entire object hierarchy. By utilizing Python’s `copy` module and custom copy methods, you can manage complex data structures and ensure your programs behave as expected.