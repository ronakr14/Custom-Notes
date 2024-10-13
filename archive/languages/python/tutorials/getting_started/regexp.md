# Python Regular Expressions: Detailed Overview and Examples

Regular expressions (regex) are sequences of characters that define search patterns, primarily used for string matching and manipulation. Python's `re` module provides a powerful interface for working with regular expressions.

## Importing the `re` Module

To use regular expressions in Python, you need to import the `re` module:

```python
import re
```

## Basic Operations

### Searching for Patterns

#### Example

```python
import re

# Define a pattern
pattern = r'\d+'

# Search for the pattern in a string
result = re.search(pattern, 'The price is 100 dollars')
print(result.group())  # Output: 100
```

### Finding All Matches

#### Example

```python
import re

# Define a pattern
pattern = r'\d+'

# Find all matches in a string
result = re.findall(pattern, 'The price is 100 dollars and the tax is 20 dollars')
print(result)  # Output: ['100', '20']
```

### Splitting Strings

#### Example

```python
import re

# Define a pattern
pattern = r'\s+'

# Split a string by the pattern
result = re.split(pattern, 'This is a test')
print(result)  # Output: ['This', 'is', 'a', 'test']
```

### Replacing Patterns

#### Example

```python
import re

# Define a pattern
pattern = r'\d+'

# Replace the pattern with a new string
result = re.sub(pattern, 'XXX', 'The price is 100 dollars')
print(result)  # Output: The price is XXX dollars
```

## Regular Expression Patterns

### Special Characters

- `.`: Matches any character except a newline.
- `^`: Matches the start of a string.
- `$`: Matches the end of a string.
- `*`: Matches 0 or more repetitions of the preceding pattern.
- `+`: Matches 1 or more repetitions of the preceding pattern.
- `?`: Matches 0 or 1 repetition of the preceding pattern.
- `{m}`: Matches exactly m repetitions of the preceding pattern.
- `{m,n}`: Matches between m and n repetitions of the preceding pattern.

### Character Classes

- `[abc]`: Matches any one of the characters a, b, or c.
- `[^abc]`: Matches any character except a, b, or c.
- `[a-z]`: Matches any lowercase letter.
- `[A-Z]`: Matches any uppercase letter.
- `[0-9]`: Matches any digit.

### Predefined Character Classes

- `\d`: Matches any digit; equivalent to `[0-9]`.
- `\D`: Matches any non-digit; equivalent to `[^0-9]`.
- `\w`: Matches any word character (alphanumeric plus underscore); equivalent to `[a-zA-Z0-9_]`.
- `\W`: Matches any non-word character; equivalent to `[^a-zA-Z0-9_]`.
- `\s`: Matches any whitespace character (space, tab, newline).
- `\S`: Matches any non-whitespace character.

### Anchors

- `\b`: Matches a word boundary.
- `\B`: Matches a non-word boundary.

## Compiling Regular Expressions

You can compile a regular expression pattern into a regex object for repeated use.

#### Example

```python
import re

# Compile a pattern
pattern = re.compile(r'\d+')

# Use the compiled pattern
result = pattern.search('The price is 100 dollars')
print(result.group())  # Output: 100
```

## Grouping and Capturing

### Using Groups

#### Example

```python
import re

# Define a pattern with groups
pattern = r'(\d+)\s+(\w+)'

# Search for the pattern in a string
result = re.search(pattern, '100 dollars')
print(result.group(1))  # Output: 100
print(result.group(2))  # Output: dollars
```

### Named Groups

#### Example

```python
import re

# Define a pattern with named groups
pattern = r'(?P<price>\d+)\s+(?P<currency>\w+)'

# Search for the pattern in a string
result = re.search(pattern, '100 dollars')
print(result.group('price'))  # Output: 100
print(result.group('currency'))  # Output: dollars
```

## Lookahead and Lookbehind

### Positive Lookahead

#### Example

```python
import re

# Define a pattern with positive lookahead
pattern = r'\d+(?=\sdollars)'

# Search for the pattern in a string
result = re.search(pattern, '100 dollars')
print(result.group())  # Output: 100
```

### Negative Lookahead

#### Example

```python
import re

# Define a pattern with negative lookahead
pattern = r'\d+(?!\sdollars)'

# Search for the pattern in a string
result = re.search(pattern, '100 euros')
print(result.group())  # Output: 100
```

### Positive Lookbehind

#### Example

```python
import re

# Define a pattern with positive lookbehind
pattern = r'(?<=\d\s)euros'

# Search for the pattern in a string
result = re.search(pattern, '100 euros')
print(result.group())  # Output: euros
```

### Negative Lookbehind

#### Example

```python
import re

# Define a pattern with negative lookbehind
pattern = r'(?<!100\s)euros'

# Search for the pattern in a string
result = re.search(pattern, '200 euros')
print(result.group())  # Output: euros
```

## Practical Examples

### Example 1: Email Validation

```python
import re

# Define a pattern for email validation
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Validate an email
email = 'example@example.com'
if re.match(pattern, email):
    print('Valid email')
else:
    print('Invalid email')
```

### Example 2: Phone Number Validation

```python
import re

# Define a pattern for phone number validation
pattern = r'^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$'

# Validate a phone number
phone_number = '+1 (123) 456-7890'
if re.match(pattern, phone_number):
    print('Valid phone number')
else:
    print('Invalid phone number')
```

### Example 3: URL Extraction

```python
import re

# Define a pattern for URL extraction
pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

# Extract URLs from a string
text = 'Visit https://example.com and http://example.org for more information.'
urls = re.findall(pattern, text)
print(urls)  # Output: ['https://example.com', 'http://example.org']
```

## Conclusion

The `re` module in Python provides a powerful set of tools for working with regular expressions. By mastering the various patterns and techniques outlined in this report, you can effectively search, manipulate, and validate strings in your Python programs. Regular expressions are a versatile tool that can help you handle a wide range of text processing tasks efficiently.