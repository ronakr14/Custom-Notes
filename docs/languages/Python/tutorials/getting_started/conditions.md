# Python Conditional Statements

Conditional statements in Python allow you to execute different blocks of code based on certain conditions. They are fundamental for making decisions in your programs and controlling the flow of execution.

## 1. `if` Statement

The `if` statement evaluates a condition and executes a block of code if the condition is `True`.

### Basic Syntax:

```python
if condition:
    # Code block to execute
```

### Example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### Output:

```
x is greater than 5
```

### Explanation:
- The condition `x > 5` is `True`, so the code block inside the `if` statement is executed.

## 2. `if-else` Statement

The `if-else` statement allows you to execute one block of code if the condition is `True`, and a different block if the condition is `False`.

### Basic Syntax:

```python
if condition:
    # Code block to execute if condition is True
else:
    # Code block to execute if condition is False
```

### Example:

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

### Output:

```
x is 5 or less
```

### Explanation:
- The condition `x > 5` is `False`, so the code block in the `else` statement is executed.

## 3. `if-elif-else` Statement

The `if-elif-else` statement allows you to check multiple conditions in sequence. If the first condition is `False`, the next `elif` condition is checked, and so on. If none of the conditions are `True`, the `else` block is executed.

### Basic Syntax:

```python
if condition1:
    # Code block to execute if condition1 is True
elif condition2:
    # Code block to execute if condition1 is False and condition2 is True
else:
    # Code block to execute if all conditions are False
```

### Example:

```python
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but not greater than 10")
else:
    print("x is 5 or less")
```

### Output:

```
x is greater than 5 but not greater than 10
```

### Explanation:
- The first condition `x > 10` is `False`, so the `elif` condition `x > 5` is checked and found to be `True`. The corresponding code block is executed.

## 4. Nested Conditional Statements

You can nest `if`, `elif`, and `else` statements inside each other to handle more complex conditions.

### Example:

```python
x = 15
if x > 10:
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is greater than 10 but not greater than 20")
else:
    print("x is 10 or less")
```

### Output:

```
x is greater than 10 but not greater than 20
```

### Explanation:
- The outer `if` condition `x > 10` is `True`, so the nested `if-else` statement is evaluated. The nested condition `x > 20` is `False`, so the corresponding `else` block is executed.

## 5. Ternary Operator (Conditional Expression)

Python supports a shorthand for `if-else` statements known as the ternary operator. It allows you to assign values based on a condition in a single line.

### Basic Syntax:

```python
value = true_value if condition else false_value
```

### Example:

```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```

### Output:

```
Even
```

### Explanation:
- The condition `x % 2 == 0` checks if `x` is even. Since it is true, `result` is assigned `"Even"`.

## 6. Conditional Statements with Multiple Conditions

You can combine multiple conditions using logical operators like `and`, `or`, and `not`.

### Example:

```python
x = 15
y = 20
if x > 10 and y < 25:
    print("Both conditions are met")
else:
    print("One or both conditions are not met")
```

### Output:

```
Both conditions are met
```

### Explanation:
- Both conditions `x > 10` and `y < 25` are `True`, so the code block inside the `if` statement is executed.

## Conclusion

Conditional statements in Python are powerful tools for making decisions and controlling the flow of execution in your programs. By understanding how to use `if`, `if-else`, and `if-elif-else` statements, as well as nested conditions and the ternary operator, you can write more dynamic and flexible code.