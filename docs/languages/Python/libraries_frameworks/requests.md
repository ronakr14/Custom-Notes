# Python `requests` Module Report

The `requests` module in Python is a popular and user-friendly library for making HTTP requests. It provides a simple and intuitive API for sending HTTP requests and handling responses. This report covers installation, basic usage, and practical examples to help you understand how to use the `requests` library effectively.

## Introduction

The `requests` library is designed to simplify the process of sending HTTP requests and handling responses. It abstracts the complexities of HTTP protocols and provides a clean and elegant API. It supports various HTTP methods, including GET, POST, PUT, DELETE, and more.

## Installation

To install the `requests` library, you can use pip:

```bash
pip install requests
```

## Basic Usage

Here’s a basic overview of how to use the `requests` library to make HTTP requests and handle responses.

### Example Code

```python
import requests

# Sending a simple GET request
response = requests.get('https://www.example.com')

# Print the status code
print(response.status_code)

# Print the response content
print(response.text)
```

## Examples

### Sending a GET Request

To send a GET request, use the `requests.get()` method. This is commonly used to retrieve data from a URL.

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Sending a POST Request

To send a POST request with data, use the `requests.post()` method. This is typically used to submit data to a server.

```python
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response = requests.post(url, json=data)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Handling Query Parameters

To include query parameters in your request, pass them as a dictionary to the `params` argument.

```python
import requests

params = {'q': 'python requests', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=params)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Handling Form Data

For sending form data, use the `data` argument. This is useful for submitting forms.

```python
import requests

url = 'https://httpbin.org/post'
form_data = {'username': 'user', 'password': 'pass'}

response = requests.post(url, data=form_data)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Handling JSON Data

To send JSON data in a POST request, use the `json` argument. This automatically sets the `Content-Type` to `application/json`.

```python
import requests

url = 'https://httpbin.org/post'
json_data = {'key1': 'value1', 'key2': 'value2'}

response = requests.post(url, json=json_data)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Handling Headers

You can pass custom headers using the `headers` argument. This is useful for setting authorization tokens or custom content types.

```python
import requests

url = 'https://httpbin.org/headers'
headers = {'Authorization': 'Bearer your_token'}

response = requests.get(url, headers=headers)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Handling Cookies

To send cookies with your request, use the `cookies` argument. This can be useful for maintaining sessions.

```python
import requests

url = 'https://httpbin.org/cookies'
cookies = {'session_id': 'abc123'}

response = requests.get(url, cookies=cookies)

print('Status Code:', response.status_code)
print('Response JSON:', response.json())
```

### Error Handling

Handling errors is crucial for robust applications. The `requests` library provides various ways to handle exceptions.

#### Example: Basic Error Handling

```python
import requests
from requests.exceptions import HTTPError, RequestException

url = 'https://jsonplaceholder.typicode.com/posts/1'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    print('Response JSON:', response.json())
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except RequestException as err:
    print(f'Error occurred: {err}')
```

## Conclusion

The `requests` library provides a simple and powerful way to make HTTP requests in Python. It supports various HTTP methods, handles parameters, headers, cookies, and provides facilities for robust error handling. With its intuitive API, `requests` is an excellent choice for interacting with web services and APIs.

For more detailed information and advanced usage, refer to the [Requests documentation](https://docs.python-requests.org/en/latest/).
