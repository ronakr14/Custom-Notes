# Scala Programming Language Tutorial

## Overview

Scala is a high-level programming language that combines functional programming with object-oriented programming. It is known for its concise syntax, powerful type inference, and strong support for concurrent programming.

## Basic Syntax

### Hello World

A simple Scala program to print "Hello, World!" to the console.

```scala
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, World!")
  }
}
```

### Comments

- **Single-line comment:** `// This is a single-line comment`
- **Multi-line comment:**
  ```scala
  /*
   * This is a multi-line comment
   */
  ```

## Data Types

### Primitive Data Types

- **Int:** Integer type
- **Double:** Double precision floating-point type
- **Char:** Character type
- **Boolean:** Boolean type

### Example

```scala
object DataTypes {
  def main(args: Array[String]): Unit = {
    val age: Int = 25
    val height: Double = 5.9
    val initial: Char = 'A'
    val isStudent: Boolean = true

    println(s"Age: $age")
    println(s"Height: $height")
    println(s"Initial: $initial")
    println(s"Is Student: $isStudent")
  }
}
```

## Control Flow

### If-Else Statement

```scala
object IfElseExample {
  def main(args: Array[String]): Unit = {
    val score: Int = 85

    if (score >= 90) {
      println("Grade: A")
    } else if (score >= 80) {
      println("Grade: B")
    } else {
      println("Grade: C")
    }
  }
}
```

### Match Expression

```scala
object MatchExample {
  def main(args: Array[String]): Unit = {
    val day: Int = 3

    day match {
      case 1 => println("Monday")
      case 2 => println("Tuesday")
      case 3 => println("Wednesday")
      case _ => println("Invalid day")
    }
  }
}
```

## Functions

### Function Definition

```scala
object FunctionsExample {
  def greet(name: String): String = {
    s"Hello, $name!"
  }

  def main(args: Array[String]): Unit = {
    println(greet("Alice"))
  }
}
```

### Function with Multiple Parameters

```scala
object AddExample {
  def add(a: Int, b: Int): Int = {
    a + b
  }

  def main(args: Array[String]): Unit = {
    println(add(5, 7))
  }
}
```

## Classes and Objects

### Defining a Class

```scala
class Person(val name: String, val age: Int) {
  def introduce(): Unit = {
    println(s"Hi, my name is $name and I am $age years old.")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val person1 = new Person("Alice", 30)
    person1.introduce()
  }
}
```

### Companion Object

```scala
class Circle(val radius: Double) {
  def area(): Double = {
    math.Pi * radius * radius
  }
}

object Circle {
  def apply(radius: Double): Circle = new Circle(radius)
}

object Main {
  def main(args: Array[String]): Unit = {
    val circle = Circle(5.0)
    println(s"Area of the circle: ${circle.area()}")
  }
}
```

## Inheritance and Polymorphism

### Inheritance Example

```scala
class Animal {
  def speak(): Unit = {
    println("Animal makes a sound.")
  }
}

class Dog extends Animal {
  override def speak(): Unit = {
    println("Dog barks.")
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val myDog = new Dog()
    myDog.speak()
  }
}
```

### Polymorphism Example

```scala
object PolymorphismExample {
  def makeSound(animal: Animal): Unit = {
    animal.speak()
  }

  def main(args: Array[String]): Unit = {
    val dog = new Dog()
    makeSound(dog) // Calls Dog's speak method
  }
}
```

## Collections

### List

```scala
object ListExample {
  def main(args: Array[String]): Unit = {
    val fruits = List("Apple", "Banana", "Cherry")

    fruits.foreach(fruit => println(fruit))
  }
}
```

### Map

```scala
object MapExample {
  def main(args: Array[String]): Unit = {
    val ages = Map("Alice" -> 30, "Bob" -> 25)

    ages.foreach { case (name, age) => println(s"$name is $age years old.") }
  }
}
```

## Pattern Matching

### Basic Pattern Matching

```scala
object PatternMatchingExample {
  def main(args: Array[String]): Unit = {
    val number: Any = 10

    number match {
      case 1 => println("One")
      case 2 => println("Two")
      case _ => println("Other")
    }
  }
}
```

### Matching on Type

```scala
object TypeMatchingExample {
  def process(value: Any): Unit = {
    value match {
      case s: String => println(s"String: $s")
      case i: Int => println(s"Integer: $i")
      case _ => println("Other type")
    }
  }

  def main(args: Array[String]): Unit = {
    process("Hello")
    process(42)
    process(3.14)
  }
}
```

## Exception Handling

### Try-Catch Block

```scala
object ExceptionHandlingExample {
  def main(args: Array[String]): Unit = {
    try {
      val result = 10 / 0
    } catch {
      case e: ArithmeticException => println("Cannot divide by zero")
    } finally {
      println("This block is always executed.")
    }
  }
}
```

## Concurrency

### Using Futures

```scala
import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration._

object FutureExample {
  def main(args: Array[String]): Unit = {
    val future = Future {
      Thread.sleep(1000)
      "Hello from the future!"
    }

    val result = Await.result(future, 2.seconds)
    println(result)
  }
}
```

### Using Actors

```scala
import akka.actor.{Actor, ActorSystem, Props}

class HelloActor extends Actor {
  def receive: Receive = {
    case "Hello" => println("Hello, World!")
    case _ => println("Unknown message")
  }
}

object ActorExample {
  def main(args: Array[String]): Unit = {
    val system = ActorSystem("HelloActorSystem")
    val helloActor = system.actorOf(Props[HelloActor], "helloActor")

    helloActor ! "Hello"
    helloActor ! "Goodbye"
  }
}
```

## Summary

This tutorial covers the fundamental concepts and syntax of Scala programming. Scala combines object-oriented and functional programming paradigms, making it a powerful language for a variety of applications. For further learning, refer to the [Scala Documentation](https://docs.scala-lang.org/).