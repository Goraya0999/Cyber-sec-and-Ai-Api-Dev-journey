# Python Decorator Functions

## What is a Decorator?

A **decorator** is a Python function that adds extra functionality to another function **without modifying the original function's source code**.

Instead of changing the original function, a decorator wraps it inside another function and executes additional code before or after the original function.

Decorators promote **code reuse**, **clean code**, and **separation of concerns**.

---

# Why Do We Need Decorators?

Without decorators, if the same functionality (such as logging, authentication, timing, or validation) is needed for multiple functions, the code must be written repeatedly.

Decorators solve this problem by allowing one reusable function to enhance many different functions.

---

# Real-Life Analogy

Imagine you have a simple gift box.

```text
Gift Box
```

Now you wrap it with decorative paper.

```text
Wrapping Paper
      │
      ▼
+------------------+
|    Gift Box      |
+------------------+
```

The gift inside has not changed.

Only its appearance has improved.

A decorator works in exactly the same way.

* Gift Box → Original Function
* Wrapping Paper → Decorator
* Wrapped Gift → Decorated Function

---

# How a Decorator Works

A decorator receives a function as an argument.

It creates a new function called a **wrapper**.

The wrapper executes:

1. Code before the original function.
2. The original function.
3. Code after the original function.

Finally, the decorator returns the wrapper function.

---

# Execution Flow

```text
Original Function
        │
        ▼
Decorator Receives Function
        │
        ▼
Wrapper Function Created
        │
        ▼
Wrapper Returned
        │
        ▼
Original Function Replaced
        │
        ▼
Function Called
        │
        ▼
Wrapper Executes
        │
        ├── Before Code
        │
        ├── Original Function
        │
        └── After Code
```

---

# Decorator Syntax

```python
@decorator_name
def function_name():
    ...
```

---

# Syntax Breakdown

## `@`

The decorator operator.

It tells Python to apply the decorator to the function immediately after the function is created.

---

## `def`

Defines a function.

---

## `()`

Contains the function parameters.

---

## `:`

Starts the function body.

---

## `return`

Returns the wrapper function from the decorator.

---

# Basic Decorator Example

```python
def border(func):

    def wrapper():
        print("++++++++++")
        func()
        print("++++++++++")

    return wrapper


@border
def greet():
    print("Hello")


greet()
```

---

# Output

```text
++++++++++
Hello
++++++++++
```

---

# Step-by-Step Execution

### Step 1

Python creates the `greet()` function.

```text
greet()
```

---

### Step 2

Python sees the decorator.

```python
@border
```

---

### Step 3

Python executes:

```python
greet = border(greet)
```

The original function is replaced with the wrapper returned by the decorator.

---

### Step 4

When `greet()` is called:

```python
greet()
```

Python actually calls:

```python
wrapper()
```

---

### Step 5

The wrapper executes.

```text
Print "++++++++++"
        │
        ▼
Call greet()
        │
        ▼
Print "Hello"
        │
        ▼
Print "++++++++++"
```

---

# What Happens Behind the Scenes?

Using a decorator:

```python
@border
def greet():
    print("Hello")
```

is exactly the same as writing:

```python
def greet():
    print("Hello")

greet = border(greet)
```

The `@` syntax is simply a shorter and cleaner way to apply a decorator.

---

# Decorator Structure

```text
Decorator
│
├── Receives Function
│
├── Creates Wrapper
│
├── Executes Extra Code
│
├── Calls Original Function
│
├── Executes More Code
│
└── Returns Wrapper
```

---

# Components of a Decorator

## Decorator Function

Receives another function as an argument.

```python
def border(func):
```

---

## Wrapped Function

The original function being decorated.

```python
def greet():
```

---

## Wrapper Function

Contains the additional behavior.

```python
def wrapper():
```

---

## Function Call

Executes the original function.

```python
func()
```

---

## Returning the Wrapper

Returns the new enhanced function.

```python
return wrapper
```

---

# Advantages

* Promotes code reuse.
* Keeps functions clean.
* Avoids duplicate code.
* Makes programs easier to maintain.
* Separates additional behavior from business logic.
* Easy to apply to multiple functions.

---

# Common Use Cases

* Logging
* Authentication
* Authorization
* Input validation
* Error handling
* Performance measurement
* Caching
* Database transactions
* API routing (FastAPI)
* Flask route registration

---

# FastAPI Example

FastAPI uses decorators to register API endpoints.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
```

Here:

* `@app.get("/")` is the decorator.
* `home()` is the decorated function.
* FastAPI automatically registers `home()` as the handler for the `GET /` endpoint.

---

# Important Notes

* A decorator always receives a function.
* A decorator usually returns another function.
* The wrapper controls what happens before and after the original function.
* The original function does not need to be modified.
* The `@` symbol is only syntactic sugar for applying a decorator.
* Decorators are heavily used in frameworks such as FastAPI, Flask, and Django.
