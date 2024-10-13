# HTML Programming Language Tutorial

## Overview

HTML (Hypertext Markup Language) is the standard language used to create and design web pages. It structures content on the web by using a series of elements and tags.

## Basic Structure

The basic structure of an HTML document includes the `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` elements.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is my first HTML page.</p>
</body>
</html>
```

## Headings and Paragraphs

### Headings

HTML provides six levels of headings, from `<h1>` (largest) to `<h6>` (smallest).

```html
<!DOCTYPE html>
<html>
<head>
    <title>Headings Example</title>
</head>
<body>
    <h1>This is a heading level 1</h1>
    <h2>This is a heading level 2</h2>
    <h3>This is a heading level 3</h3>
    <h4>This is a heading level 4</h4>
    <h5>This is a heading level 5</h5>
    <h6>This is a heading level 6</h6>
</body>
</html>
```

### Paragraphs

Paragraphs are defined using the `<p>` tag.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Paragraph Example</title>
</head>
<body>
    <p>This is a paragraph of text.</p>
    <p>Another paragraph with more text.</p>
</body>
</html>
```

## Links

Links are created using the `<a>` tag.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Links Example</title>
</head>
<body>
    <a href="https://www.example.com">Visit Example.com</a>
    <a href="mailto:someone@example.com">Send an Email</a>
</body>
</html>
```

## Images

Images are included using the `<img>` tag.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Images Example</title>
</head>
<body>
    <img src="image.jpg" alt="Description of Image" width="300" height="200">
    <p>Image above is an example of HTML image tag usage.</p>
</body>
</html>
```

## Lists

### Unordered Lists

```html
<!DOCTYPE html>
<html>
<head>
    <title>Unordered List Example</title>
</head>
<body>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
```

### Ordered Lists

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ordered List Example</title>
</head>
<body>
    <ol>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>
</body>
</html>
```

## Tables

Tables are defined using the `<table>` tag, with `<tr>` for rows, `<th>` for header cells, and `<td>` for data cells.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Table Example</title>
</head>
<body>
    <table border="1">
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
        </tr>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
        </tr>
    </table>
</body>
</html>
```

## Forms

Forms are used to collect user input. The `<form>` tag is used to create a form, with various input elements.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Form Example</title>
</head>
<body>
    <form action="/submit_form" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

## HTML5 Features

HTML5 introduces new elements and attributes for better web development.

### New Elements

- **`<header>`**: Represents introductory content or a set of navigational links.
- **`<footer>`**: Represents a footer for a document or section.
- **`<article>`**: Represents a self-contained composition in a document.
- **`<section>`**: Represents a generic section of a document.

### Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>HTML5 Example</title>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    <article>
        <h2>About Us</h2>
        <p>This is an article section.</p>
    </article>
    <section>
        <h2>Our Services</h2>
        <p>Details about our services.</p>
    </section>
    <footer>
        <p>Contact us at contact@example.com</p>
    </footer>
</body>
</html>
```

## Summary

This tutorial covers the basic concepts and syntax of HTML. HTML is the backbone of web development and is essential for creating structured web pages. For further learning, refer to the [MDN Web Docs for HTML](https://developer.mozilla.org/en-US/docs/Web/HTML).