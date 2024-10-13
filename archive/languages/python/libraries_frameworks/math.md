# Python `math` Module: Detailed Overview and Examples

The Python `math` module provides a wide range of mathematical functions and constants. It is part of the standard library, which means it is included with Python and does not require any additional installation. This module is ideal for performing mathematical operations and computations efficiently.

## Importing the `math` Module

To use the functions and constants in the `math` module, you first need to import it:

```python
import math
```

## Constants

### `math.pi`

Represents the mathematical constant π (pi), which is approximately 3.14159.

### Example

```python
import math

print(math.pi)  # Output: 3.141592653589793
```

### `math.e`

Represents the mathematical constant e, which is approximately 2.71828.

### Example

```python
import math

print(math.e)  # Output: 2.718281828459045
```

### `math.inf`

Represents positive infinity.

### Example

```python
import math

print(math.inf)  # Output: inf
```

### `math.nan`

Represents a "Not-a-Number" value.

### Example

```python
import math

print(math.nan)  # Output: nan
```

## Mathematical Functions

### `math.sqrt(x)`

Returns the square root of `x`.

### Example

```python
import math

print(math.sqrt(16))  # Output: 4.0
```

### `math.pow(x, y)`

Returns `x` raised to the power of `y`.

### Example

```python
import math

print(math.pow(2, 3))  # Output: 8.0
```

### `math.exp(x)`

Returns e raised to the power of `x`.

### Example

```python
import math

print(math.exp(2))  # Output: 7.38905609893065
```

### `math.log(x[, base])`

Returns the logarithm of `x` to the given `base`. If the base is not specified, it returns the natural logarithm (base `e`).

### Example

```python
import math

print(math.log(100))  # Output: 4.605170185988092
print(math.log(100, 10))  # Output: 2.0
```

### `math.log10(x)`

Returns the base-10 logarithm of `x`.

### Example

```python
import math

print(math.log10(100))  # Output: 2.0
```

### `math.sin(x)`

Returns the sine of `x` radians.

### Example

```python
import math

print(math.sin(math.pi / 2))  # Output: 1.0
```

### `math.cos(x)`

Returns the cosine of `x` radians.

### Example

```python
import math

print(math.cos(math.pi))  # Output: -1.0
```

### `math.tan(x)`

Returns the tangent of `x` radians.

### Example

```python
import math

print(math.tan(math.pi / 4))  # Output: 0.9999999999999999
```

### `math.factorial(x)`

Returns the factorial of `x`, where `x` must be a non-negative integer.

### Example

```python
import math

print(math.factorial(5))  # Output: 120
```

### `math.gcd(x, y)`

Returns the greatest common divisor of `x` and `y`.

### Example

```python
import math

print(math.gcd(48, 18))  # Output: 6
```

### `math.degrees(x)`

Converts angle `x` from radians to degrees.

### Example

```python
import math

print(math.degrees(math.pi))  # Output: 180.0
```

### `math.radians(x)`

Converts angle `x` from degrees to radians.

### Example

```python
import math

print(math.radians(180))  # Output: 3.141592653589793
```

## Trigonometric Functions

### `math.asin(x)`

Returns the arc sine of `x` in radians.

### Example

```python
import math

print(math.asin(1))  # Output: 1.5707963267948966
```

### `math.acos(x)`

Returns the arc cosine of `x` in radians.

### Example

```python
import math

print(math.acos(0))  # Output: 1.5707963267948966
```

### `math.atan(x)`

Returns the arc tangent of `x` in radians.

### Example

```python
import math

print(math.atan(1))  # Output: 0.7853981633974483
```

### `math.atan2(y, x)`

Returns the arc tangent of `y/x` in radians, with consideration of the sign of both arguments.

### Example

```python
import math

print(math.atan2(1, 1))  # Output: 0.7853981633974483
```

## Hyperbolic Functions

### `math.sinh(x)`

Returns the hyperbolic sine of `x`.

### Example

```python
import math

print(math.sinh(1))  # Output: 1.1752011936438014
```

### `math.cosh(x)`

Returns the hyperbolic cosine of `x`.

### Example

```python
import math

print(math.cosh(1))  # Output: 1.5430806348152437
```

### `math.tanh(x)`

Returns the hyperbolic tangent of `x`.

### Example

```python
import math

print(math.tanh(1))  # Output: 0.7615941559557649
```

## Conclusion

The Python `math` module provides a comprehensive set of functions and constants for performing mathematical operations. Whether you need basic arithmetic, advanced functions, or special mathematical constants, the `math` module is a valuable tool for handling numerical computations and mathematical tasks efficiently. By leveraging these functions, you can perform complex calculations and process mathematical data with ease.