# Numeric Data Types in Python

Python provides several built-in numeric data types to handle various kinds of numerical data. These data types are primarily used for arithmetic operations and to perform mathematical calculations.

## 1. Integer (`int`)

Integers are whole numbers that can be positive, negative, or zero, without a fractional part.

### Example:

```python
# Declaring integer variables
a = 10
b = -5
c = 0

# Performing arithmetic operations
sum_ab = a + b  # Addition
diff_ab = a - b  # Subtraction
prod_ab = a * b  # Multiplication
quot_ab = a // b  # Floor Division

print("Sum:", sum_ab)
print("Difference:", diff_ab)
print("Product:", prod_ab)
print("Quotient:", quot_ab)
```

### Output:

```
Sum: 5
Difference: 15
Product: -50
Quotient: -2
```

## 2. Float (`float`)

Float represents real numbers that contain a decimal point. They are used for representing fractional values.

### Example:

```python
# Declaring float variables
x = 10.5
y = -3.2
z = 0.0

# Performing arithmetic operations
sum_xy = x + y  # Addition
diff_xy = x - y  # Subtraction
prod_xy = x * y  # Multiplication
quot_xy = x / y  # Division

print("Sum:", sum_xy)
print("Difference:", diff_xy)
print("Product:", prod_xy)
print("Quotient:", quot_xy)
```

### Output:

```
Sum: 7.3
Difference: 13.7
Product: -33.6
Quotient: -3.28125
```

## 3. Complex (`complex`)

Complex numbers consist of a real part and an imaginary part. In Python, they are written in the form `a + bj`, where `a` is the real part and `b` is the imaginary part.

### Example:

```python
# Declaring complex variables
p = 2 + 3j
q = 1 - 4j

# Performing arithmetic operations
sum_pq = p + q  # Addition
diff_pq = p - q  # Subtraction
prod_pq = p * q  # Multiplication
quot_pq = p / q  # Division

print("Sum:", sum_pq)
print("Difference:", diff_pq)
print("Product:", prod_pq)
print("Quotient:", quot_pq)
```

### Output:

```
Sum: (3-1j)
Difference: (1+7j)
Product: (14-5j)
Quotient: (-0.6470588235294118+0.5882352941176471j)
```

## Conclusion

Python's numeric data types provide a robust way to handle various types of numerical data. Understanding how to use `int`, `float`, and `complex` types effectively is crucial for performing mathematical operations and numerical computations in Python.

By practicing the examples provided, you can gain a deeper understanding of how these numeric data types work and how to apply them in your Python programs.