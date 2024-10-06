# Set Data Type in Python

Sets are an unordered collection of unique elements. They are commonly used to eliminate duplicate values and perform mathematical set operations like union, intersection, and difference.

## 1. Creating Sets

Sets can be created using curly braces `{}` or the `set()` function.

### Example:

```python
# Using curly braces
set1 = {1, 2, 3, 4, 5}

# Using the set() function
set2 = set([3, 4, 5, 6, 7])

print("Set1:", set1)
print("Set2:", set2)
```

### Output:

```
Set1: {1, 2, 3, 4, 5}
Set2: {3, 4, 5, 6, 7}
```

## 2. Adding and Removing Elements

Elements can be added to a set using the `add()` method and removed using the `remove()` or `discard()` methods.

### Example:

```python
set1 = {1, 2, 3}

# Adding elements
set1.add(4)
set1.add(5)

# Removing elements
set1.remove(2)  # Raises KeyError if element not found
set1.discard(3)  # Does not raise an error if element not found

print("Updated Set:", set1)
```

### Output:

```
Updated Set: {1, 4, 5}
```

## 3. Set Operations

### 3.1 Union

The union of two sets is a set containing all elements from both sets.

### Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
# or using the | operator
union_set_operator = set1 | set2

print("Union:", union_set)
print("Union (operator):", union_set_operator)
```

### Output:

```
Union: {1, 2, 3, 4, 5}
Union (operator): {1, 2, 3, 4, 5}
```

### 3.2 Intersection

The intersection of two sets is a set containing only the elements that are in both sets.

### Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
# or using the & operator
intersection_set_operator = set1 & set2

print("Intersection:", intersection_set)
print("Intersection (operator):", intersection_set_operator)
```

### Output:

```
Intersection: {3}
Intersection (operator): {3}
```

### 3.3 Difference

The difference between two sets is a set containing the elements that are in the first set but not in the second.

### Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
# or using the - operator
difference_set_operator = set1 - set2

print("Difference:", difference_set)
print("Difference (operator):", difference_set_operator)
```

### Output:

```
Difference: {1, 2}
Difference (operator): {1, 2}
```

### 3.4 Symmetric Difference

The symmetric difference between two sets is a set containing elements that are in either of the sets but not in both.

### Example:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
# or using the ^ operator
symmetric_difference_set_operator = set1 ^ set2

print("Symmetric Difference:", symmetric_difference_set)
print("Symmetric Difference (operator):", symmetric_difference_set_operator)
```

### Output:

```
Symmetric Difference: {1, 2, 4, 5}
Symmetric Difference (operator): {1, 2, 4, 5}
```

## 4. Set Membership

You can check if an element is in a set using the `in` keyword.

### Example:

```python
set1 = {1, 2, 3, 4, 5}

print(3 in set1)  # True
print(6 in set1)  # False
```

### Output:

```
True
False
```

## Conclusion

Sets in Python are a powerful data type for managing collections of unique elements and performing mathematical set operations. Understanding how to create, modify, and utilize sets is essential for efficient programming in Python.

By practicing the examples provided, you can gain a deeper understanding of how sets work and how to apply these techniques in your Python projects.