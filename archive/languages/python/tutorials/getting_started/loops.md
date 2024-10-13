# Python Loops

Loops in Python are used to execute a block of code repeatedly based on a condition or for iterating over a sequence. They are essential for performing repetitive tasks efficiently.

## 1. `for` Loop

The `for` loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.

### Basic Syntax:

```python
for variable in sequence:
    # Code block to execute
```

### Example:

#### Iterating over a List

```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

### Output:

```
apple
banana
cherry
```

### Explanation:
- The `for` loop iterates over each item in the `fruits` list and prints it.

#### Iterating over a Range

```python
for i in range(5):
    print(i)
```

### Output:

```
0
1
2
3
4
```

### Explanation:
- The `range(5)` generates numbers from `0` to `4`, and the loop prints each number.

#### Iterating over a Dictionary

```python
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(key, value)
```

### Output:

```
name Alice
age 25
city New York
```

### Explanation:
- The `items()` method returns key-value pairs of the dictionary, which are iterated and printed.

## 2. `while` Loop

The `while` loop in Python continues to execute a block of code as long as a specified condition is `True`.

### Basic Syntax:

```python
while condition:
    # Code block to execute
```

### Example:

#### Basic `while` Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Output:

```
0
1
2
3
4
```

### Explanation:
- The loop continues as long as `count` is less than `5`. The `count` variable is incremented in each iteration.

#### `while` Loop with `break`

```python
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1
```

### Output:

```
0
1
2
3
4
```

### Explanation:
- The `while True` loop runs indefinitely but is terminated by the `break` statement when `count` reaches `5`.

#### `while` Loop with `continue`

```python
count = 0
while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```

### Output:

```
1
3
```

### Explanation:
- The `continue` statement skips the rest of the code in the loop for even values of `count`, so only odd numbers are printed.

## 3. Nested Loops

Loops can be nested within each other to perform more complex iterations.

### Example:

#### Nested `for` Loops

```python
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

### Output:

```
i=0, j=0
i=0, j=1
i=0, j=2
i=1, j=0
i=1, j=1
i=1, j=2
i=2, j=0
i=2, j=1
i=2, j=2
```

### Explanation:
- The outer loop runs 3 times, and for each iteration of the outer loop, the inner loop runs 3 times.

## 4. Loop Control Statements

### 4.1. `break`

The `break` statement terminates the loop prematurely.

### Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Output:

```
0
1
2
3
4
```

### Explanation:
- The loop breaks when `i` equals `5`, so only numbers from `0` to `4` are printed.

### 4.2. `continue`

The `continue` statement skips the current iteration and moves to the next iteration.

### Example:

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### Output:

```
1
3
5
7
9
```

### Explanation:
- Even numbers are skipped due to the `continue` statement, so only odd numbers are printed.

### 4.3. `pass`

The `pass` statement is a placeholder that does nothing and is used when a statement is syntactically required but no action is needed.

### Example:

```python
for i in range(3):
    pass  # No operation performed
```

### Explanation:
- The `pass` statement does nothing; the loop executes without performing any actions.

## Conclusion

Loops in Python are powerful constructs for executing repetitive tasks and iterating over sequences. By understanding the `for` and `while` loops, as well as loop control statements like `break`, `continue`, and `pass`, you can write efficient and effective code for various programming tasks.