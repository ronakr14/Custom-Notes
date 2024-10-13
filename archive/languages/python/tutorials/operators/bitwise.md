# Python Bitwise Operators

Bitwise operators in Python perform operations on the binary representations of integers. These operators work at the bit level, providing a means to perform low-level operations efficiently.

## 1. Bitwise AND (`&`)

Performs a bitwise AND operation, which results in a binary number where each bit is set to `1` if both corresponding bits of the operands are `1`.

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

### Explanation:
- `0101` (5 in decimal)
- `0011` (3 in decimal)
- Result of `AND`: `0001` (1 in decimal)

## 2. Bitwise OR (`|`)

Performs a bitwise OR operation, which results in a binary number where each bit is set to `1` if at least one of the corresponding bits of the operands is `1`.

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

### Explanation:
- `0101` (5 in decimal)
- `0011` (3 in decimal)
- Result of `OR`: `0111` (7 in decimal)

## 3. Bitwise XOR (`^`)

Performs a bitwise XOR operation, which results in a binary number where each bit is set to `1` if exactly one of the corresponding bits of the operands is `1`.

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

### Explanation:
- `0101` (5 in decimal)
- `0011` (3 in decimal)
- Result of `XOR`: `0110` (6 in decimal)

## 4. Bitwise NOT (`~`)

Performs a bitwise NOT operation, which inverts all the bits of the operand. It results in the one's complement of the number.

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

### Explanation:
- `0101` (5 in decimal)
- `NOT` operation flips all bits: `1010`
- In Python, this results in `-6` due to two's complement representation.

## 5. Left Shift (`<<`)

Shifts the bits of the number to the left by the specified number of positions. This is equivalent to multiplying the number by `2` raised to the power of the shift amount.

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

### Explanation:
- `0101` (5 in decimal)
- Left shift by 1 position: `1010` (10 in decimal)

## 6. Right Shift (`>>`)

Shifts the bits of the number to the right by the specified number of positions. This is equivalent to integer division by `2` raised to the power of the shift amount.

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

### Explanation:
- `0101` (5 in decimal)
- Right shift by 1 position: `0010` (2 in decimal)

## 7. Bitwise Operations on Negative Numbers

Bitwise operations can also be applied to negative numbers, which are represented using two's complement in Python.

### Example:

```python
a = -5   # Binary: 11111111111111111111111111111111 (32-bit representation)
b = 3
print("Bitwise AND with negative number:", a & b)
print("Bitwise OR with negative number:", a | b)
print("Bitwise XOR with negative number:", a ^ b)
print("Bitwise NOT with negative number:", ~a)
```

### Output:

```
Bitwise AND with negative number: 1
Bitwise OR with negative number: -3
Bitwise XOR with negative number: -4
Bitwise NOT with negative number: 4
```

### Explanation:
- For `-5`, the two's complement binary representation affects the result of bitwise operations.

## Conclusion

Bitwise operators in Python provide a powerful way to perform low-level operations on integer data. Understanding these operators is essential for tasks that require efficient manipulation of data at the bit level, such as cryptography, networking, and low-level programming.

By practicing the examples provided, you can gain a deeper understanding of how to use bitwise operators effectively in your Python programs.