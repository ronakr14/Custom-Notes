# Python Indexing and Slicing

Indexing and slicing are powerful features in Python that allow you to access and manipulate sequences such as lists, tuples, and strings. Understanding these concepts is essential for efficient data handling.

## Indexing

Indexing allows you to access individual elements of a sequence. Python uses zero-based indexing, meaning the first element has an index of 0, the second element has an index of 1, and so on.

### Example 1: Indexing a List

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry
print(fruits[-1]) # Output: elderberry
```

- `fruits[0]` accesses the first element.
- `fruits[2]` accesses the third element.
- `fruits[-1]` accesses the last element (negative indexing starts from the end).

### Example 2: Indexing a String

```python
word = "Python"
print(word[0])   # Output: P
print(word[3])   # Output: h
print(word[-1])  # Output: n
```

## Slicing

Slicing allows you to access a subset of elements from a sequence. The basic syntax is `sequence[start:stop:step]`.

- `start` is the index where the slice begins (inclusive).
- `stop` is the index where the slice ends (exclusive).
- `step` is the interval between elements in the slice (optional).

### Example 3: Slicing a List

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])    # Output: [2, 3, 4]
print(numbers[:4])     # Output: [0, 1, 2, 3]
print(numbers[5:])     # Output: [5, 6, 7, 8, 9]
print(numbers[::2])    # Output: [0, 2, 4, 6, 8]
print(numbers[1:7:2])  # Output: [1, 3, 5]
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

### Example 4: Slicing a String

```python
text = "slicing"
print(text[1:4])    # Output: lic
print(text[:3])     # Output: sli
print(text[3:])     # Output: cing
print(text[::2])    # Output: sicn
print(text[::-1])   # Output: gnicils
```

## Advanced Slicing Techniques

### Example 5: Slicing with Negative Indices

```python
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(data[-7:-2])   # Output: [30, 40, 50, 60, 70]
print(data[-3:])     # Output: [70, 80, 90]
print(data[:-5])     # Output: [10, 20, 30, 40]
print(data[-5:-1:2]) # Output: [50, 70]
```

### Example 6: Multi-dimensional Slicing

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])         # Output: [1, 2, 3] (first row)
print(matrix[1][2])      # Output: 6 (element in the second row, third column)
print([row[1] for row in matrix]) # Output: [2, 5, 8] (second column)
```

## Conclusion

Indexing and slicing are fundamental techniques in Python that enable efficient and concise manipulation of sequences. Mastery of these concepts can significantly improve your ability to work with lists, strings, and other iterable objects in Python.

