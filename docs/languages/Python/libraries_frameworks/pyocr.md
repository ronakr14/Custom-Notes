# Python pyocr Module: A Comprehensive Guide

The `pyocr` module is a Python library for Optical Character Recognition (OCR). It provides a unified interface to several OCR engines, such as Tesseract and CuneiForm, allowing you to extract text from images and PDFs. This guide covers the key features and functionalities of the `pyocr` module with detailed examples.

## Introduction to pyocr

`pyocr` is a library that provides an interface for various OCR engines, enabling you to extract text from images and other documents. It abstracts away the complexities of different OCR engines, providing a consistent API for text extraction.

## Installation

To use `pyocr`, you need to install it via pip. Additionally, you need to install the OCR engines it supports, such as Tesseract.

### Installing pyocr

```bash
pip install pyocr
```

### Installing Tesseract

`pyocr` commonly uses Tesseract as its OCR engine. Install Tesseract by following the instructions for your operating system:

- **Windows**: Download and install the Tesseract executable from [GitHub](https://github.com/tesseract-ocr/tesseract/releases).
- **macOS**: Install using Homebrew:

  ```bash
  brew install tesseract
  ```

- **Linux**: Install using your package manager:

  ```bash
  sudo apt-get install tesseract-ocr
  ```

## Basic Usage

Once installed, you can use `pyocr` to extract text from images.

### Importing pyocr

```python
import pyocr
import pyocr.builders
```

### Getting the OCR Tool

`pyocr` supports multiple OCR tools. You can get the OCR tool available on your system with the following code:

```python
tools = pyocr.get_available_tools()
tool = tools[0]  # Select the first available tool
print(f'Using OCR tool: {tool.get_name()}')
```

## Using OCR Engines

`pyocr` provides a unified interface to OCR engines. The following examples use Tesseract as the OCR engine.

### Text Extraction from an Image

```python
from PIL import Image
import pyocr
import pyocr.builders

# Get the OCR tool
tools = pyocr.get_available_tools()
tool = tools[0]

# Open an image file
image = Image.open('sample_image.png')

# Perform OCR
text = tool.image_to_string(image, builder=pyocr.builders.TextBuilder())
print('Extracted text:', text)
```

### Extracting Text from a PDF

```python
from pdf2image import convert_from_path
import pyocr
import pyocr.builders

# Get the OCR tool
tools = pyocr.get_available_tools()
tool = tools[0]

# Convert PDF pages to images
pages = convert_from_path('sample_document.pdf')

# Perform OCR on each page
for page_number, page in enumerate(pages):
    text = tool.image_to_string(page, builder=pyocr.builders.TextBuilder())
    print(f'Page {page_number + 1} text:', text)
```

## Handling Different File Formats

`pyocr` can handle various image formats, including PNG, JPEG, and TIFF. Make sure to install any necessary libraries for handling these formats, such as `Pillow`.

### Extracting Text from Different Image Formats

```python
from PIL import Image
import pyocr
import pyocr.builders

# Get the OCR tool
tools = pyocr.get_available_tools()
tool = tools[0]

# Open different image formats
image_formats = ['sample_image.png', 'sample_image.jpg', 'sample_image.tiff']
for image_file in image_formats:
    image = Image.open(image_file)
    text = tool.image_to_string(image, builder=pyocr.builders.TextBuilder())
    print(f'Text from {image_file}:', text)
```

## Error Handling

Handling errors gracefully ensures the robustness of your OCR application.

### Handling Common Errors

```python
import pyocr
import pyocr.builders
from PIL import Image
import sys

try:
    # Get the OCR tool
    tools = pyocr.get_available_tools()
    if not tools:
        raise RuntimeError('No OCR tools found')
    tool = tools[0]

    # Open an image file
    image = Image.open('sample_image.png')

    # Perform OCR
    text = tool.image_to_string(image, builder=pyocr.builders.TextBuilder())
    print('Extracted text:', text)

except FileNotFoundError as e:
    print(f'File not found: {e}', file=sys.stderr)
except RuntimeError as e:
    print(f'Runtime error: {e}', file=sys.stderr)
except Exception as e:
    print(f'An unexpected error occurred: {e}', file=sys.stderr)
```

## Conclusion

The `pyocr` module provides a straightforward interface for Optical Character Recognition, allowing you to extract text from various file formats using different OCR engines. With the examples provided, you should be able to set up `pyocr`, perform OCR on images and PDFs, and handle common errors effectively. This module is a powerful tool for integrating OCR capabilities into your Python applications.