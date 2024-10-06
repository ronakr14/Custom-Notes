# Python Operators Precedence

Operators precedence determines the order in which different operators are evaluated in an expression. Understanding operator precedence is crucial for writing correct and predictable code. 

## Operator Precedence Order

Here’s a summary of Python operator precedence from highest to lowest:

1. **Parentheses** `()`
2. **Exponentiation** `**`
3. **Unary Plus and Minus**, **Bitwise NOT** `+x`, `-x`, `~x`
4. **Multiplication**, **Division**, **Floor Division**, **Modulus** `*`, `/`, `//`, `%`
5. **Addition**, **Subtraction** `+`, `-`
6. **Bitwise Shift Operators** `<<`, `>>`
7. **Bitwise AND** `&`
8. **Bitwise XOR** `^`
9. **Bitwise OR** `|`
10. **Comparison Operators** `==`, `!=`, `>`, `<`, `>=`, `<=`
11. **Boolean NOT** `not`
12. **Boolean AND** `and`
13. **Boolean OR** `or`
14. **Assignment Operators** `=`, `+=`, `-=`, `*=`, `/=`, etc.

## 1. Parentheses `()`

Parentheses have the highest precedence and are used to explicitly define the order of operations.

### Example:

```python
result = (3 + 5) * 2
print("Parentheses:", result)
```

### Output:

```
Parentheses: 16
```

### Explanation:
- The expression inside parentheses `(3 + 5)` is evaluated first, resulting in `8`.
- Then, `8 * 2` is evaluated to give `16`.

## 2. Exponentiation `**`

Exponentiation has higher precedence than multiplication and division.

### Example:

```python
result = 2 ** 3 ** 2
print("Exponentiation:", result)
```

### Output:

```
Exponentiation: 512
```

### Explanation:
- Exponentiation is evaluated from right to left, so `3 ** 2` is evaluated first, which is `9`.
- Then, `2 ** 9` results in `512`.

## 3. Unary Plus and Minus, Bitwise NOT `+x`, `-x`, `~x`

Unary operations are evaluated before binary operations.

### Example:

```python
result = -5 + 3
print("Unary Minus:", result)

result = ~5
print("Bitwise NOT:", result)
```

### Output:

```
Unary Minus: -2
Bitwise NOT: -6
```

### Explanation:
- `-5 + 3` evaluates to `-2`.
- Bitwise NOT of `5` is `-6` due to two's complement representation.

## 4. Multiplication, Division, Floor Division, Modulus `*`, `/`, `//`, `%`

These operators have higher precedence than addition and subtraction.

### Example:

```python
result = 4 + 3 * 2
print("Multiplication:", result)

result = 10 / 2 - 3
print("Division:", result)

result = 10 // 3 % 2
print("Floor Division and Modulus:", result)
```

### Output:

```
Multiplication: 10
Division: 2.0
Floor Division and Modulus: 1
```

### Explanation:
- `3 * 2` is evaluated first, resulting in `6`, then `4 + 6` results in `10`.
- `10 / 2` is evaluated first, resulting in `5.0`, then `5.0 - 3` results in `2.0`.
- `10 // 3` results in `3`, then `3 % 2` results in `1`.

## 5. Addition, Subtraction `+`, `-`

These operators have lower precedence than multiplication and division.

### Example:

```python
result = 5 + 3 - 2
print("Addition and Subtraction:", result)
```

### Output:

```
Addition and Subtraction: 6
```

### Explanation:
- Addition and subtraction are evaluated from left to right, so `5 + 3` results in `8`, then `8 - 2` results in `6`.

## 6. Bitwise Shift Operators `<<`, `>>`

Bitwise shift operators shift bits to the left or right.

### Example:

```python
result = 2 << 1
print("Left Shift:", result)

result = 4 >> 1
print("Right Shift:", result)
```

### Output:

```
Left Shift: 4
Right Shift: 2
```

### Explanation:
- `2 << 1` shifts `2` left by 1 position, resulting in `4`.
- `4 >> 1` shifts `4` right by 1 position, resulting in `2`.

## 7. Bitwise AND `&`

Bitwise AND has lower precedence than shift operators.

### Example:

```python
result = 6 & 3
print("Bitwise AND:", result)
```

### Output:

```
Bitwise AND: 2
```

### Explanation:
- `6` (binary `0110`) AND `3` (binary `0011`) results in `2` (binary `0010`).

## 8. Bitwise XOR `^`

Bitwise XOR has the same precedence level as Bitwise AND.

### Example:

```python
result = 6 ^ 3
print("Bitwise XOR:", result)
```

### Output:

```
Bitwise XOR: 5
```

### Explanation:
- `6` (binary `0110`) XOR `3` (binary `0011`) results in `5` (binary `0101`).

## 9. Bitwise OR `|`

Bitwise OR has the same precedence level as Bitwise XOR.

### Example:

```python
result = 6 | 3
print("Bitwise OR:", result)
```

### Output:

```
Bitwise OR: 7
```

### Explanation:
- `6` (binary `0110`) OR `3` (binary `0011`) results in `7` (binary `0111`).

## 10. Comparison Operators `==`, `!=`, `>`, `<`, `>=`, `<=`

Comparison operators have lower precedence than arithmetic operators.

### Example:

```python
result = 5 > 3 and 2 < 4
print("Comparison Operators:", result)
```

### Output:

```
Comparison Operators: True
```

### Explanation:
- Both `5 > 3` and `2 < 4` are `True`, so `True and True` results in `True`.

## 11. Boolean NOT `not`

The `not` operator has higher precedence than `and` and `or`.

### Example:

```python
result = not (5 > 3) and 2 < 4
print("Boolean NOT:", result)
```

### Output:

```
Boolean NOT: False
```

### Explanation:
- `not (5 > 3)` evaluates to `False`, so `False and 2 < 4` results in `False`.

## 12. Boolean AND `and`

The `and` operator has higher precedence than `or`.

### Example:

```python
result = True and False or True
print("Boolean AND and OR:", result)
```

### Output:

```
Boolean AND and OR: True
```

### Explanation:
- `True and False` is `False`, and `False or True` is `True`.

## 13. Boolean OR `or`

The `or` operator has the lowest precedence among boolean operators.

### Example:

```python
result = False or True
print("Boolean OR:", result)
```

### Output:

```
Boolean OR: True
```

### Explanation:
- `False or True` results in `True`.

## 14. Assignment Operators `=`, `+=`, `-=`, etc.

Assignment operators have the lowest precedence among operators.

### Example:

```python
a = 5
a += 3
print("Assignment Operator:", a)
```

### Output:

```
Assignment Operator: 8
```

### Explanation:
- `a += 3` is evaluated as `a = a + 3`, resulting in `8`.

## Conclusion

Understanding operator precedence in Python is crucial for writing correct expressions and avoiding unexpected results. By practicing and applying these principles, you can ensure that your code behaves as intended and maintains clarity in complex expressions.