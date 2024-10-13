# Python String Formatting: Overview and Examples

String formatting in Python allows you to create formatted strings, which can be especially useful for generating output, logging, and creating user-friendly messages. Python provides several ways to format strings, each with its own use cases and advantages.

## 1. Old-Style Formatting (`%` Operator)

Old-style formatting uses the `%` operator to format strings. It is reminiscent of the `printf` style found in C.

### Basic Example

```python
name = "Alice"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)
```

Output:
```
Name: Alice, Age: 30
```

### Formatting with Padding and Alignment

```python
number = 42
formatted_string = "Number: %-10d" % number  # Left-aligned with padding
print(formatted_string)
```

Output:
```
Number: 42        
```

## 2. `str.format()` Method

The `str.format()` method provides more control and flexibility for string formatting. You can use curly braces `{}` as placeholders.

### Basic Example

```python
name = "Alice"
age = 30
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)
```

Output:
```
Name: Alice, Age: 30
```

### Positional and Keyword Arguments

```python
formatted_string = "Name: {0}, Age: {1}".format(name, age)
formatted_string = "Name: {name}, Age: {age}".format(name=name, age=age)
print(formatted_string)
```

Output:
```
Name: Alice, Age: 30
Name: Alice, Age: 30
```

### Formatting with Specifiers

```python
number = 1234.56789
formatted_string = "Number: {:.2f}".format(number)  # Two decimal places
print(formatted_string)
```

Output:
```
Number: 1234.57
```

### Padding and Alignment

```python
formatted_string = "{:<10} | {:^10} | {:>10}".format("left", "center", "right")
print(formatted_string)
```

Output:
```
left      |   center   |      right
```

## 3. f-Strings (Formatted String Literals)

Introduced in Python 3.6, f-strings provide a concise and readable way to format strings. They are prefixed with the letter `f` and allow embedded expressions inside curly braces `{}`.

### Basic Example

```python
name = "Alice"
age = 30
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)
```

Output:
```
Name: Alice, Age: 30
```

### Expressions Inside f-Strings

```python
import math
radius = 5
formatted_string = f"Area of circle with radius {radius} is {math.pi * radius**2:.2f}"
print(formatted_string)
```

Output:
```
Area of circle with radius 5 is 78.54
```

### Padding and Alignment with f-Strings

```python
formatted_string = f"|{'left':<10}|{'center':^10}|{'right':>10}|"
print(formatted_string)
```

Output:
```
|left      |  center  |     right|
```

## 4. String Template Class

The `string` module provides a `Template` class for simpler string substitutions.

### Basic Example

```python
from string import Template

template = Template("Name: $name, Age: $age")
formatted_string = template.substitute(name="Alice", age=30)
print(formatted_string)
```

Output:
```
Name: Alice, Age: 30
```

### Safe Substitution

```python
template = Template("Name: $name, Age: $age")
formatted_string = template.safe_substitute(name="Alice")  # Age is missing
print(formatted_string)  # Outputs: Name: Alice, Age: $age
```

## Conclusion

Python offers several ways to format strings, each with its own advantages:

- **Old-style formatting** (`%` operator) is familiar to those coming from C-style languages but is less flexible.
- **`str.format()`** method provides more control and is widely used in Python 2 and 3.
- **f-Strings** (formatted string literals) offer a concise and readable way to embed expressions and are the preferred method in Python 3.6 and later.
- **`string.Template`** provides a simpler way to substitute placeholders, useful for basic replacements.

Understanding these methods allows you to choose the most appropriate one for your needs, making your code more readable and maintainable.