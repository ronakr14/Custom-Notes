# C++ Programming Language Tutorial

## Overview

C++ is a high-level programming language that includes object-oriented, procedural, and generic programming features. It is widely used for system/software development, game development, and performance-critical applications.

## Basic Syntax

### Hello World

A simple program to print "Hello, World!" to the console.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Comments

- **Single-line comment:** `// This is a single-line comment`
- **Multi-line comment:**
  ```cpp
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
- **bool**: Boolean type

### Example

```cpp
#include <iostream>

int main() {
    int age = 25;
    float height = 5.9f;
    double weight = 70.5;
    char initial = 'A';
    bool isStudent = true;

    std::cout << "Age: " << age << std::endl;
    std::cout << "Height: " << height << std::endl;
    std::cout << "Weight: " << weight << std::endl;
    std::cout << "Initial: " << initial << std::endl;
    std::cout << "Is Student: " << isStudent << std::endl;

    return 0;
}
```

## Control Flow

### If-Else Statement

```cpp
#include <iostream>

int main() {
    int number = 10;

    if (number > 0) {
        std::cout << "The number is positive." << std::endl;
    } else if (number < 0) {
        std::cout << "The number is negative." << std::endl;
    } else {
        std::cout << "The number is zero." << std::endl;
    }

    return 0;
}
```

### Switch Statement

```cpp
#include <iostream>

int main() {
    int day = 3;

    switch (day) {
        case 1:
            std::cout << "Monday" << std::endl;
            break;
        case 2:
            std::cout << "Tuesday" << std::endl;
            break;
        case 3:
            std::cout << "Wednesday" << std::endl;
            break;
        default:
            std::cout << "Invalid day" << std::endl;
    }

    return 0;
}
```

## Functions

### Function Declaration and Definition

```cpp
#include <iostream>

void greet() {
    std::cout << "Hello, welcome to C++ programming!" << std::endl;
}

int main() {
    greet();
    return 0;
}
```

### Function with Parameters

```cpp
#include <iostream>

int add(int a, int b) {
    return a + b;
}

int main() {
    int sum = add(5, 7);
    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
```

## Classes and Objects

### Defining a Class

```cpp
#include <iostream>

class Person {
public:
    std::string name;
    int age;

    void introduce() {
        std::cout << "Hi, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person1;
    person1.name = "Alice";
    person1.age = 30;

    person1.introduce();
    return 0;
}
```

## Inheritance and Polymorphism

### Inheritance Example

```cpp
#include <iostream>

class Animal {
public:
    void speak() {
        std::cout << "Animal makes a sound." << std::endl;
    }
};

class Dog : public Animal {
public:
    void speak() {
        std::cout << "Dog barks." << std::endl;
    }
};

int main() {
    Dog myDog;
    myDog.speak();  // Calls the Dog's speak method
    return 0;
}
```

### Polymorphism Example

```cpp
#include <iostream>

class Base {
public:
    virtual void show() {
        std::cout << "Base class" << std::endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        std::cout << "Derived class" << std::endl;
    }
};

int main() {
    Base* ptr;
    Derived derivedObj;
    ptr = &derivedObj;

    ptr->show();  // Calls Derived's show method
    return 0;
}
```

## Templates

### Function Templates

```cpp
#include <iostream>

template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << "Max of 3 and 7 is " << max(3, 7) << std::endl;
    std::cout << "Max of 3.5 and 2.1 is " << max(3.5, 2.1) << std::endl;
    return 0;
}
```

### Class Templates

```cpp
#include <iostream>

template <class T>
class MyArray {
private:
    T* arr;
    int size;

public:
    MyArray(int s) : size(s) {
        arr = new T[size];
    }

    void setValue(int index, T value) {
        if (index < size) {
            arr[index] = value;
        }
    }

    T getValue(int index) {
        if (index < size) {
            return arr[index];
        }
        return T();
    }

    ~MyArray() {
        delete[] arr;
    }
};

int main() {
    MyArray<int> intArray(5);
    intArray.setValue(0, 10);
    std::cout << "Value at index 0: " << intArray.getValue(0) << std::endl;

    MyArray<std::string> strArray(3);
    strArray.setValue(0, "Hello");
    std::cout << "Value at index 0: " << strArray.getValue(0) << std::endl;

    return 0;
}
```

## File I/O

### Reading from a File

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream infile("example.txt");
    std::string line;

    if (!infile) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    while (std::getline(infile, line)) {
        std::cout << line << std::endl;
    }

    infile.close();
    return 0;
}
```

### Writing to a File

```cpp
#include <iostream>
#include <fstream>

int main() {
    std::ofstream outfile("output.txt");

    if (!outfile) {
        std::cerr << "Error opening file." << std::endl;
        return 1;
    }

    outfile << "This is a test file." << std::endl;
    outfile.close();

    return 0;
}
```

## Standard Template Library (STL)

### Using `vector`

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    for (int num : numbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

### Using `map`

```cpp
#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> ageMap;

    ageMap["Alice"] = 30;
    ageMap["Bob"] = 25;

    for (const auto& pair : ageMap) {
        std::cout << pair.first << " is " << pair.second << " years old." << std::endl;
    }

    return 0;
}
```

## Summary

This tutorial covers the basic concepts and syntax of C++ programming. C++ is a versatile language that supports multiple programming paradigms and is widely used in various domains. For further learning, refer to [The C++ Programming Language](https://en.wikipedia.org/wiki/The_C%2B%2B_Programming_Language) by Bjarne Stroustrup.