# C Programming Language Tutorial

## Overview

C is a powerful, low-level programming language that is widely used for system programming and application development. It provides a good balance between high-level constructs and low-level operations, making it suitable for a wide range of programming tasks.

## Basic Syntax

### Hello World

A simple program to print "Hello, World!" to the console.

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

### Comments

- **Single-line comment:** `// This is a single-line comment`
- **Multi-line comment:**
  ```c
  /*
   * This is a multi-line comment
   */
  ```

## Data Types

### Primitive Data Types

- **int**: Integer type
- **float**: Floating-point type
- **double**: Double precision floating-point type
- **char**: Character type

### Example

```c
#include <stdio.h>

int main() {
    int age = 25;
    float height = 5.9;
    char initial = 'A';

    printf("Age: %d\n", age);
    printf("Height: %.1f\n", height);
    printf("Initial: %c\n", initial);

    return 0;
}
```

## Control Flow

### If-Else Statement

```c
#include <stdio.h>

int main() {
    int number = 10;

    if (number > 0) {
        printf("The number is positive.\n");
    } else if (number < 0) {
        printf("The number is negative.\n");
    } else {
        printf("The number is zero.\n");
    }

    return 0;
}
```

### Switch Statement

```c
#include <stdio.h>

int main() {
    int day = 3;

    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        default:
            printf("Invalid day\n");
    }

    return 0;
}
```

## Functions

### Function Declaration and Definition

```c
#include <stdio.h>

void greet() {
    printf("Hello, welcome to C programming!\n");
}

int main() {
    greet();
    return 0;
}
```

### Function with Parameters

```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int sum = add(5, 7);
    printf("Sum: %d\n", sum);
    return 0;
}
```

## Arrays

### Array Declaration and Initialization

```c
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    for (int i = 0; i < 5; i++) {
        printf("Number[%d]: %d\n", i, numbers[i]);
    }

    return 0;
}
```

## Pointers

### Pointer Basics

```c
#include <stdio.h>

int main() {
    int num = 10;
    int *ptr = &num;

    printf("Value of num: %d\n", num);
    printf("Address of num: %p\n", (void *)ptr);
    printf("Value at address ptr: %d\n", *ptr);

    return 0;
}
```

## Structures

### Defining and Using Structures

```c
#include <stdio.h>

struct Person {
    char name[50];
    int age;
};

int main() {
    struct Person person1;
    
    // Assign values
    strcpy(person1.name, "Alice");
    person1.age = 30;

    // Print values
    printf("Name: %s\n", person1.name);
    printf("Age: %d\n", person1.age);

    return 0;
}
```

## File I/O

### Reading from a File

```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "r");
    char buffer[100];

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), file)) {
        printf("%s", buffer);
    }

    fclose(file);
    return 0;
}
```

### Writing to a File

```c
#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "w");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fprintf(file, "This is a test file.\n");
    fclose(file);

    return 0;
}
```

## Summary

This tutorial covers the basic concepts and syntax of C programming. C is a versatile language that is foundational for understanding many other programming languages. For further learning, refer to [The C Programming Language](https://en.wikipedia.org/wiki/The_C_Programming_Language) by Kernighan and Ritchie.