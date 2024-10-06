# Java Programming Language Tutorial

## Overview

Java is a high-level, object-oriented programming language known for its portability across platforms, robustness, and ease of use. It is widely used for building enterprise-scale applications, Android apps, and web applications.

## Basic Syntax

### Hello World

A simple program to print "Hello, World!" to the console.

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Comments

- **Single-line comment:** `// This is a single-line comment`
- **Multi-line comment:**
  ```java
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
- **boolean**: Boolean type

### Example

```java
public class DataTypes {
    public static void main(String[] args) {
        int age = 25;
        float height = 5.9f;
        double weight = 70.5;
        char initial = 'A';
        boolean isStudent = true;

        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        System.out.println("Weight: " + weight);
        System.out.println("Initial: " + initial);
        System.out.println("Is Student: " + isStudent);
    }
}
```

## Control Flow

### If-Else Statement

```java
public class IfElseExample {
    public static void main(String[] args) {
        int number = 10;

        if (number > 0) {
            System.out.println("The number is positive.");
        } else if (number < 0) {
            System.out.println("The number is negative.");
        } else {
            System.out.println("The number is zero.");
        }
    }
}
```

### Switch Statement

```java
public class SwitchExample {
    public static void main(String[] args) {
        int day = 3;

        switch (day) {
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            default:
                System.out.println("Invalid day");
        }
    }
}
```

## Methods

### Method Declaration and Definition

```java
public class MethodsExample {
    public static void greet() {
        System.out.println("Hello, welcome to Java programming!");
    }

    public static void main(String[] args) {
        greet();
    }
}
```

### Method with Parameters

```java
public class AddExample {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        int sum = add(5, 7);
        System.out.println("Sum: " + sum);
    }
}
```

## Classes and Objects

### Defining a Class

```java
public class Person {
    String name;
    int age;

    void introduce() {
        System.out.println("Hi, my name is " + name + " and I am " + age + " years old.");
    }

    public static void main(String[] args) {
        Person person1 = new Person();
        person1.name = "Alice";
        person1.age = 30;

        person1.introduce();
    }
}
```

## Inheritance and Polymorphism

### Inheritance Example

```java
public class Animal {
    public void speak() {
        System.out.println("Animal makes a sound.");
    }
}

public class Dog extends Animal {
    @Override
    public void speak() {
        System.out.println("Dog barks.");
    }

    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.speak();  // Calls the Dog's speak method
    }
}
```

### Polymorphism Example

```java
public class Base {
    public void show() {
        System.out.println("Base class");
    }
}

public class Derived extends Base {
    @Override
    public void show() {
        System.out.println("Derived class");
    }

    public static void main(String[] args) {
        Base obj = new Derived();
        obj.show();  // Calls Derived's show method
    }
}
```

## Interfaces and Abstract Classes

### Interface Example

```java
interface Drawable {
    void draw();
}

public class Circle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing a circle.");
    }

    public static void main(String[] args) {
        Circle circle = new Circle();
        circle.draw();
    }
}
```

### Abstract Class Example

```java
abstract class Animal {
    abstract void makeSound();

    void sleep() {
        System.out.println("This animal sleeps.");
    }
}

public class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Meow");
    }

    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.makeSound();
        cat.sleep();
    }
}
```

## Exception Handling

### Try-Catch Block

```java
public class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            int[] numbers = {1, 2, 3};
            System.out.println(numbers[5]); // This will throw an ArrayIndexOutOfBoundsException
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception caught: " + e.getMessage());
        } finally {
            System.out.println("This block is always executed.");
        }
    }
}
```

## File I/O

### Reading from a File

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileReadExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("example.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
```

### Writing to a File

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class FileWriteExample {
    public static void main(String[] args) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("output.txt"))) {
            bw.write("This is a test file.");
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
```

## Java Collections Framework

### Using `ArrayList`

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}
```

### Using `HashMap`

```java
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, Integer> map = new HashMap<>();
        map.put("Alice", 30);
        map.put("Bob", 25);

        for (String key : map.keySet()) {
            System.out.println(key + " is " + map.get(key) + " years old.");
        }
    }
}
```

## Summary

This tutorial covers the basic concepts and syntax of Java programming. Java is a versatile language that supports object-oriented principles and provides a rich set of libraries for various applications. For further learning, refer to the [Java Tutorials by Oracle](https://docs.oracle.com/javase/tutorial/).