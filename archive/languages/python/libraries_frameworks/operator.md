# Python `operator` Module: Detailed Overview and Examples

The `operator` module in Python provides a set of efficient functions that correspond to standard operators. These functions are intended to be used as functional equivalents of operators and can be particularly useful for tasks involving functional programming, such as sorting, mapping, and reducing.

## Importing the `operator` Module

To use the functions from the `operator` module, you first need to import it:

```python
import operator
```

## Arithmetic Operators

### `operator.add(x, y)`

Returns the sum of `x` and `y`.

### Example

```python
import operator

result = operator.add(5, 3)
print(result)  # Output: 8
```

### `operator.sub(x, y)`

Returns the difference of `x` and `y`.

### Example

```python
import operator

result = operator.sub(5, 3)
print(result)  # Output: 2
```

### `operator.mul(x, y)`

Returns the product of `x` and `y`.

### Example

```python
import operator

result = operator.mul(5, 3)
print(result)  # Output: 15
```

### `operator.truediv(x, y)`

Returns the quotient of `x` divided by `y`. For integer division, use `operator.floordiv`.

### Example

```python
import operator

result = operator.truediv(5, 3)
print(result)  # Output: 1.6666666666666667
```

### `operator.floordiv(x, y)`

Returns the floor division of `x` divided by `y`.

### Example

```python
import operator

result = operator.floordiv(5, 3)
print(result)  # Output: 1
```

### `operator.mod(x, y)`

Returns the remainder of `x` divided by `y`.

### Example

```python
import operator

result = operator.mod(5, 3)
print(result)  # Output: 2
```

### `operator.pow(x, y)`

Returns `x` raised to the power of `y`.

### Example

```python
import operator

result = operator.pow(2, 3)
print(result)  # Output: 8
```

## Comparison Operators

### `operator.eq(x, y)`

Returns `True` if `x` is equal to `y`.

### Example

```python
import operator

result = operator.eq(5, 5)
print(result)  # Output: True
```

### `operator.ne(x, y)`

Returns `True` if `x` is not equal to `y`.

### Example

```python
import operator

result = operator.ne(5, 3)
print(result)  # Output: True
```

### `operator.lt(x, y)`

Returns `True` if `x` is less than `y`.

### Example

```python
import operator

result = operator.lt(5, 10)
print(result)  # Output: True
```

### `operator.le(x, y)`

Returns `True` if `x` is less than or equal to `y`.

### Example

```python
import operator

result = operator.le(5, 5)
print(result)  # Output: True
```

### `operator.gt(x, y)`

Returns `True` if `x` is greater than `y`.

### Example

```python
import operator

result = operator.gt(5, 3)
print(result)  # Output: True
```

### `operator.ge(x, y)`

Returns `True` if `x` is greater than or equal to `y`.

### Example

```python
import operator

result = operator.ge(5, 5)
print(result)  # Output: True
```

## Logical Operators

### `operator.and_(x, y)`

Returns the bitwise AND of `x` and `y`.

### Example

```python
import operator

result = operator.and_(5, 3)  # 5: 0101, 3: 0011
print(result)  # Output: 1 (0001 in binary)
```

### `operator.or_(x, y)`

Returns the bitwise OR of `x` and `y`.

### Example

```python
import operator

result = operator.or_(5, 3)  # 5: 0101, 3: 0011
print(result)  # Output: 7 (0111 in binary)
```

### `operator.xor(x, y)`

Returns the bitwise XOR of `x` and `y`.

### Example

```python
import operator

result = operator.xor(5, 3)  # 5: 0101, 3: 0011
print(result)  # Output: 6 (0110 in binary)
```

### `operator.not_(x)`

Returns the boolean NOT of `x`.

### Example

```python
import operator

result = operator.not_(True)
print(result)  # Output: False
```

### `operator.inv(x)`

Returns the bitwise inversion of `x`.

### Example

```python
import operator

result = operator.inv(5)  # 5: 0101
print(result)  # Output: -6 (Inverting bits)
```

## Object and Attribute Operators

### `operator.getitem(obj, key)`

Returns the item of `obj` at `key`. Equivalent to `obj[key]`.

### Example

```python
import operator

my_dict = {'a': 1, 'b': 2}
result = operator.getitem(my_dict, 'a')
print(result)  # Output: 1
```

### `operator.setitem(obj, key, value)`

Sets the item of `obj` at `key` to `value`. Equivalent to `obj[key] = value`.

### Example

```python
import operator

my_dict = {'a': 1}
operator.setitem(my_dict, 'b', 2)
print(my_dict)  # Output: {'a': 1, 'b': 2}
```

### `operator.delitem(obj, key)`

Deletes the item of `obj` at `key`. Equivalent to `del obj[key]`.

### Example

```python
import operator

my_dict = {'a': 1, 'b': 2}
operator.delitem(my_dict, 'b')
print(my_dict)  # Output: {'a': 1}
```

### `operator.getattr(obj, attr)`

Returns the attribute of `obj` with the name `attr`. Equivalent to `getattr(obj, attr)`.

### Example

```python
import operator

class MyClass:
    attr = 42

obj = MyClass()
result = operator.getattr(obj, 'attr')
print(result)  # Output: 42
```

### `operator.setattr(obj, attr, value)`

Sets the attribute of `obj` named `attr` to `value`. Equivalent to `setattr(obj, attr, value)`.

### Example

```python
import operator

class MyClass:
    pass

obj = MyClass()
operator.setattr(obj, 'attr', 42)
print(obj.attr)  # Output: 42
```

### `operator.delattr(obj, attr)`

Deletes the attribute of `obj` named `attr`. Equivalent to `delattr(obj, attr)`.

### Example

```python
import operator

class MyClass:
    attr = 42

obj = MyClass()
operator.delattr(obj, 'attr')
print(hasattr(obj, 'attr'))  # Output: False
```

## Callable Operators

### `operator.callable(obj)`

Checks if `obj` appears callable (i.e., it can be called like a function).

### Example

```python
import operator

result = operator.callable(print)
print(result)  # Output: True

result = operator.callable(42)
print(result)  # Output: False
```

## Conclusion

The `operator` module provides a set of functional equivalents for standard operators in Python. These functions can be used in a variety of contexts, including functional programming, data processing, and more. By understanding and using these functions, you can write more concise and functional code, enhancing readability and maintainability.