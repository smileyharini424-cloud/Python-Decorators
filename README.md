# Python Decorators

## Explanation

A decorator is a function that takes another function as an argument and adds extra functionality to it without modifying its original code.

Decorators are commonly used for logging, authentication, validation, and timing functions.

## Problem Statement

Write a Python program using a decorator to display messages before and after the execution of another function.

## Features

* Demonstrates decorators
* Uses nested functions
* Uses the `@` decorator syntax
* Adds functionality without modifying the original function
* Shows execution before and after a function

## How It Works

1. The `decorator` function accepts another function.
2. An inner `wrapper` function is created.
3. The wrapper executes code before the original function.
4. The original function is called.
5. The wrapper executes code after the original function.
6. The `@decorator` syntax applies the decorator to the target function.

## Technologies Used

* Python 3
* Functions
* Nested Functions
* Decorators

## Program Flow

Start → Define Decorator → Define Wrapper → Apply Decorator → Call Function → Execute Before Code → Execute Original Function → Execute After Code → End

## Sample Input

```text id="wq0g2r"
No user input required.
```

## Sample Output

```text id="a8n5kd"
Before function execution
Hello, Harini!
After function execution
```

## Key Learning

* Decorators extend the behavior of functions.
* The `@` symbol is used to apply a decorator.
* A wrapper function is commonly used inside decorators.
* Decorators allow functionality to be added without changing the original function.

## File Location

```text id="9f3m2a"
Python-Decorators/decorators.py
```

## Repository Structure

```text id="6k2p8v"
Python-Decorators/
│
├── decorators.py
└── README.md
```

## Author

V.Harini
