# Python Mathematical Operators

Python provides a range of mathematical operators for performing arithmetic operations, comparisons, and more. These operators can be used with various data types, including integers, floating-point numbers, and complex numbers.

## 1. Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations.

### 1.1 Addition (`+`)

Adds two numbers.

### Example:

```python
a = 10
b = 5
result = a + b
print("Addition:", result)
```

### Output:

```
Addition: 15
```

### 1.2 Subtraction (`-`)

Subtracts one number from another.

### Example:

```python
a = 10
b = 5
result = a - b
print("Subtraction:", result)
```

### Output:

```
Subtraction: 5
```

### 1.3 Multiplication (`*`)

Multiplies two numbers.

### Example:

```python
a = 10
b = 5
result = a * b
print("Multiplication:", result)
```

### Output:

```
Multiplication: 50
```

### 1.4 Division (`/`)

Divides one number by another, resulting in a floating-point number.

### Example:

```python
a = 10
b = 3
result = a / b
print("Division:", result)
```

### Output:

```
Division: 3.3333333333333335
```

### 1.5 Floor Division (`//`)

Divides one number by another and returns the largest integer less than or equal to the result.

### Example:

```python
a = 10
b = 3
result = a // b
print("Floor Division:", result)
```

### Output:

```
Floor Division: 3
```

### 1.6 Modulus (`%`)

Returns the remainder of the division.

### Example:

```python
a = 10
b = 3
result = a % b
print("Modulus:", result)
```

### Output:

```
Modulus: 1
```

### 1.7 Exponentiation (`**`)

Raises one number to the power of another.

### Example:

```python
a = 2
b = 3
result = a ** b
print("Exponentiation:", result)
```

### Output:

```
Exponentiation: 8
```

## 2. Comparison Operators

Comparison operators are used to compare values and return boolean results.

### 2.1 Equal to (`==`)

Checks if two values are equal.

### Example:

```python
a = 10
b = 5
result = (a == b)
print("Equal to:", result)
```

### Output:

```
Equal to: False
```

### 2.2 Not equal to (`!=`)

Checks if two values are not equal.

### Example:

```python
a = 10
b = 5
result = (a != b)
print("Not equal to:", result)
```

### Output:

```
Not equal to: True
```

### 2.3 Greater than (`>`)

Checks if one value is greater than another.

### Example:

```python
a = 10
b = 5
result = (a > b)
print("Greater than:", result)
```

### Output:

```
Greater than: True
```

### 2.4 Less than (`<`)

Checks if one value is less than another.

### Example:

```python
a = 10
b = 5
result = (a < b)
print("Less than:", result)
```

### Output:

```
Less than: False
```

### 2.5 Greater than or equal to (`>=`)

Checks if one value is greater than or equal to another.

### Example:

```python
a = 10
b = 10
result = (a >= b)
print("Greater than or equal to:", result)
```

### Output:

```
Greater than or equal to: True
```

### 2.6 Less than or equal to (`<=`)

Checks if one value is less than or equal to another.

### Example:

```python
a = 10
b = 10
result = (a <= b)
print("Less than or equal to:", result)
```

### Output:

```
Less than or equal to: True
```

## 3. Assignment Operators

Assignment operators are used to assign values to variables with operations.

### 3.1 Addition Assignment (`+=`)

Adds and assigns the result to the variable.

### Example:

```python
a = 10
a += 5
print("Addition Assignment:", a)
```

### Output:

```
Addition Assignment: 15
```

### 3.2 Subtraction Assignment (`-=`)

Subtracts and assigns the result to the variable.

### Example:

```python
a = 10
a -= 5
print("Subtraction Assignment:", a)
```

### Output:

```
Subtraction Assignment: 5
```

### 3.3 Multiplication Assignment (`*=`)

Multiplies and assigns the result to the variable.

### Example:

```python
a = 10
a *= 5
print("Multiplication Assignment:", a)
```

### Output:

```
Multiplication Assignment: 50
```

### 3.4 Division Assignment (`/=`)

Divides and assigns the result to the variable.

### Example:

```python
a = 10
a /= 5
print("Division Assignment:", a)
```

### Output:

```
Division Assignment: 2.0
```

### 3.5 Floor Division Assignment (`//=`)

Floor divides and assigns the result to the variable.

### Example:

```python
a = 10
a //= 3
print("Floor Division Assignment:", a)
```

### Output:

```
Floor Division Assignment: 3
```

### 3.6 Modulus Assignment (`%=`)

Applies modulus and assigns the result to the variable.

### Example:

```python
a = 10
a %= 3
print("Modulus Assignment:", a)
```

### Output:

```
Modulus Assignment: 1
```

### 3.7 Exponentiation Assignment (`**=`)

Raises to the power and assigns the result to the variable.

### Example:

```python
a = 2
a **= 3
print("Exponentiation Assignment:", a)
```

### Output:

```
Exponentiation Assignment: 8
```

## 4. Bitwise Operators

Bitwise operators perform operations on the binary representations of integers.

### 4.1 AND (`&`)

Performs a bitwise AND operation.

### Example:

```python
a = 5    # Binary: 0101
b = 3    # Binary: 0011
result = a & b
print("Bitwise AND:", result)
```

### Output:

```
Bitwise AND: 1
```

### 4.2 OR (`|`)

Performs a bitwise OR operation.

### Example:

```python
a = 5    # Binary: 0101
b = 3    # Binary: 0011
result = a | b
print("Bitwise OR:", result)
```

### Output:

```
Bitwise OR: 7
```

### 4.3 XOR (`^`)

Performs a bitwise XOR operation.

### Example:

```python
a = 5    # Binary: 0101
b = 3    # Binary: 0011
result = a ^ b
print("Bitwise XOR:", result)
```

### Output:

```
Bitwise XOR: 6
```

### 4.4 NOT (`~`)

Performs a bitwise NOT operation (one's complement).

### Example:

```python
a = 5    # Binary: 0101
result = ~a
print("Bitwise NOT:", result)
```

### Output:

```
Bitwise NOT: -6
```

### 4.5 Left Shift (`<<`)

Shifts the bits of a number to the left.

### Example:

```python
a = 5    # Binary: 0101
result = a << 1
print("Left Shift:", result)
```

### Output:

```
Left Shift: 10
```

### 4.6 Right Shift (`>>`)

Shifts the bits of a number to the right.

### Example:

```python
a = 5    # Binary: 0101
result = a >> 1
print("Right Shift:", result)
```

### Output:

```
Right Shift: 2
```

## Conclusion

Python provides a rich set of mathematical operators for performing arithmetic, comparison, assignment, and bitwise operations. Understanding these operators and their usage can greatly enhance your ability to manipulate and analyze data in Python.

By practicing the examples provided, you can gain a deeper understanding of how to use these operators effectively in your programming tasks.