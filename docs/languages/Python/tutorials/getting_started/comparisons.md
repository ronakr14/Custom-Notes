# Python Comparisons

Comparison operators in Python are used to compare values and determine the relationship between them. They return boolean values (`True` or `False`) based on the result of the comparison.

## 1. Comparison Operators

### 1.1. Equal to (`==`)

Checks if two values are equal.

#### Syntax:

```python
a == b
```

#### Example:

```python
a = 10
b = 10
print(a == b)  # True

c = 5
print(a == c)  # False
```

#### Output:

```
True
False
```

### 1.2. Not equal to (`!=`)

Checks if two values are not equal.

#### Syntax:

```python
a != b
```

#### Example:

```python
a = 10
b = 5
print(a != b)  # True

c = 10
print(a != c)  # False
```

#### Output:

```
True
False
```

### 1.3. Greater than (`>`)

Checks if the value on the left is greater than the value on the right.

#### Syntax:

```python
a > b
```

#### Example:

```python
a = 15
b = 10
print(a > b)  # True

c = 20
print(a > c)  # False
```

#### Output:

```
True
False
```

### 1.4. Less than (`<`)

Checks if the value on the left is less than the value on the right.

#### Syntax:

```python
a < b
```

#### Example:

```python
a = 5
b = 10
print(a < b)  # True

c = 3
print(a < c)  # False
```

#### Output:

```
True
False
```

### 1.5. Greater than or equal to (`>=`)

Checks if the value on the left is greater than or equal to the value on the right.

#### Syntax:

```python
a >= b
```

#### Example:

```python
a = 10
b = 10
print(a >= b)  # True

c = 15
print(a >= c)  # False
```

#### Output:

```
True
False
```

### 1.6. Less than or equal to (`<=`)

Checks if the value on the left is less than or equal to the value on the right.

#### Syntax:

```python
a <= b
```

#### Example:

```python
a = 5
b = 5
print(a <= b)  # True

c = 3
print(a <= c)  # False
```

#### Output:

```
True
False
```

## 2. Chained Comparisons

Python allows chaining multiple comparison operators to form more complex conditions.

### Example:

```python
x = 10
print(5 < x < 15)  # True
print(15 < x < 20)  # False
```

#### Output:

```
True
False
```

### Explanation:
- The first comparison `5 < x < 15` checks if `x` is between `5` and `15`.
- The second comparison `15 < x < 20` checks if `x` is between `15` and `20`.

## 3. Comparison with Strings

Comparison operators can also be used with strings, where they compare lexicographically.

### Example:

```python
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # True

str3 = "apple"
print(str1 == str3)  # True
```

#### Output:

```
True
True
```

### Explanation:
- Strings are compared based on their lexicographic order (alphabetical order), so `"apple"` is less than `"banana"`.

## 4. Comparison with Lists and Other Data Structures

Comparison operators can be used to compare lists and other data structures, typically comparing them element-wise.

### Example:

```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]

print(list1 == list2)  # True
print(list1 != list3)  # True
print(list1 < list3)   # True
```

#### Output:

```
True
True
True
```

### Explanation:
- `list1` is equal to `list2` because they contain the same elements in the same order.
- `list1` is not equal to `list3` because the elements differ.
- The comparison `list1 < list3` checks the lists element-wise and determines that `[1, 2, 3]` is less than `[1, 2, 4]`.

## Conclusion

Python comparison operators are essential for evaluating relationships between values. They allow you to make decisions and control the flow of execution in your programs. By understanding and using these operators effectively, you can write more flexible and dynamic code.