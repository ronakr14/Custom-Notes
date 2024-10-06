# JavaScript Programming Language Tutorial

## Overview

JavaScript is a high-level, interpreted scripting language primarily used to create interactive effects within web browsers. It is a core technology of the World Wide Web, alongside HTML and CSS.

## Basic Syntax

### Hello World

A simple JavaScript code to display "Hello, World!" in the browser console.

```javascript
console.log("Hello, World!");
```

### Comments

- **Single-line comment:** `// This is a single-line comment`
- **Multi-line comment:**
  ```javascript
  /*
   * This is a multi-line comment
   */
  ```

## Variables and Data Types

### Variables

JavaScript uses `var`, `let`, and `const` to declare variables.

```javascript
let name = "John";
const age = 30;
```

### Data Types

JavaScript supports several data types:

- **String:** `"Hello"`
- **Number:** `42`
- **Boolean:** `true` or `false`
- **Object:** `{ key: "value" }`
- **Array:** `[1, 2, 3]`
- **Null:** `null`
- **Undefined:** `undefined`

### Example

```javascript
let name = "Alice";
let age = 25;
let isStudent = true;
let address = { city: "New York", zip: "10001" };
let numbers = [1, 2, 3, 4, 5];

console.log("Name:", name);
console.log("Age:", age);
console.log("Is Student:", isStudent);
console.log("Address:", address);
console.log("Numbers:", numbers);
```

## Operators

### Arithmetic Operators

```javascript
let a = 10;
let b = 5;

console.log("Addition:", a + b);
console.log("Subtraction:", a - b);
console.log("Multiplication:", a * b);
console.log("Division:", a / b);
console.log("Modulus:", a % b);
```

### Comparison Operators

```javascript
let x = 10;
let y = 20;

console.log("Equal:", x === y);
console.log("Not Equal:", x !== y);
console.log("Greater Than:", x > y);
console.log("Less Than:", x < y);
```

## Control Flow

### If-Else Statement

```javascript
let score = 85;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else {
    console.log("Grade: C");
}
```

### Switch Statement

```javascript
let day = 3;

switch (day) {
    case 1:
        console.log("Monday");
        break;
    case 2:
        console.log("Tuesday");
        break;
    case 3:
        console.log("Wednesday");
        break;
    default:
        console.log("Invalid day");
}
```

## Functions

### Function Declaration

```javascript
function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Alice"));
```

### Function Expression

```javascript
const square = function(x) {
    return x * x;
};

console.log(square(5));
```

### Arrow Functions

```javascript
const add = (a, b) => a + b;

console.log(add(10, 15));
```

## Objects and Arrays

### Objects

```javascript
const person = {
    name: "John",
    age: 30,
    greet() {
        console.log("Hello, my name is " + this.name);
    }
};

person.greet();
```

### Arrays

```javascript
const fruits = ["Apple", "Banana", "Cherry"];

fruits.forEach(fruit => {
    console.log(fruit);
});
```

## DOM Manipulation

### Selecting Elements

```javascript
const header = document.getElementById("header");
const items = document.querySelectorAll(".item");

console.log(header);
console.log(items);
```

### Modifying Elements

```javascript
const title = document.querySelector("h1");
title.textContent = "Welcome to JavaScript Tutorial!";
```

## Events

### Adding Event Listeners

```javascript
const button = document.querySelector("button");

button.addEventListener("click", () => {
    alert("Button clicked!");
});
```

### Event Handling

```javascript
function handleClick() {
    console.log("Button was clicked");
}

document.querySelector("button").addEventListener("click", handleClick);
```

## Asynchronous JavaScript

### Callbacks

```javascript
function fetchData(callback) {
    setTimeout(() => {
        callback("Data fetched");
    }, 1000);
}

fetchData(data => {
    console.log(data);
});
```

### Promises

```javascript
const fetchData = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data fetched");
        }, 1000);
    });
};

fetchData().then(data => {
    console.log(data);
});
```

### Async/Await

```javascript
const fetchData = async () => {
    return "Data fetched";
};

const displayData = async () => {
    const data = await fetchData();
    console.log(data);
};

displayData();
```

## Error Handling

### Try-Catch Block

```javascript
try {
    let result = riskyFunction(); // This function might throw an error
} catch (error) {
    console.log("An error occurred:", error.message);
}
```

### Throwing Errors

```javascript
function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

try {
    console.log(divide(10, 0));
} catch (error) {
    console.log("Error:", error.message);
}
```

## Summary

This tutorial covers the basic concepts and syntax of JavaScript programming. JavaScript is a versatile language used for web development to create dynamic and interactive web pages. For further learning, refer to the [MDN Web Docs for JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript).