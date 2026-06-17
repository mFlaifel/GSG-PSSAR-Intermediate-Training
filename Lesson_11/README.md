# Lesson 11 - Functions II: Scope & Advanced Design

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Explain local, global, enclosing, and built-in scope using the LEGB rule
- Predict which variable Python will use when names appear in different scopes
- Avoid unnecessary global state by passing data into functions and returning results
- Use `*args` and `**kwargs` for flexible function interfaces
- Recognize and fix the mutable default argument bug
- Add docstrings and type hints that make functions easier to understand and test

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Bridge from Lesson 09: functions as reusable units |
| 0:10-0:35 | Scope and the LEGB rule |
| 0:35-0:55 | Global state, pure functions, and side effects |
| 0:55-1:15 | Flexible inputs with `*args` and `**kwargs` |
| 1:15-1:35 | Mutable defaults, docstrings, and type hints |
| 1:35-2:00 | Mini-project and exercises |

---

## Part 1 - Bridge from Lesson 09 (10 min)

In Lesson 09 you learned how to define functions, pass arguments, return values, use keyword/default arguments, and write basic docstrings.

Today is not a repeat of those basics. The goal is to answer the next questions:

- Where do variables inside functions live?
- How can functions avoid depending on hidden outside data?
- How do we design function inputs when the number of values can change?
- How can documentation and type hints make functions easier to use?

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(20, 3)
print(total)  # 60
```

This function is clear because all needed data enters through parameters and the result leaves through `return`.

---

## Part 2 - Scope and the LEGB Rule (25 min)

**Scope** means where a name can be accessed.

### 2.1 Local Scope

A variable created inside a function is local to that function.

```python
def greet():
    message = "Hello from inside the function"
    print(message)

greet()

# print(message)  # NameError: message is not defined
```

`message` exists only while `greet()` is running.

### 2.2 Global Scope

A variable created outside all functions is global.

```python
course_name = "Python Advanced"

def show_course():
    print(course_name)

show_course()
```

Functions can read global values, but relying on them too much makes code harder to test.

### 2.3 Shadowing

A local variable can have the same name as a global variable. The local one wins inside the function.

```python
name = "Global Alice"

def show_name():
    name = "Local Bruno"
    print(name)

show_name()  # Local Bruno
print(name)  # Global Alice
```

This is called **shadowing**.

### 2.4 LEGB

When Python looks for a name, it searches in this order:

| Level | Meaning |
|-------|---------|
| L | Local: inside the current function |
| E | Enclosing: inside an outer function |
| G | Global: at the top level of the file |
| B | Built-in: names like `print`, `len`, `sum` |

```python
value = "global"

def outer():
    value = "enclosing"

    def inner():
        value = "local"
        print(value)

    inner()

outer()  # local
```

You do not need to memorize every edge case today. The key idea is that Python searches from the nearest scope outward.

---

## Part 3 - Global State, Pure Functions, and Side Effects (20 min)

Changing global variables from inside functions is possible, but it often makes code harder to reason about.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2
```

This works, but the function depends on outside state. A cleaner design passes the value in and returns the new value.

```python
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
counter = increment(counter)
print(counter)  # 2
```

This second version is easier to test:

```python
print(increment(10))  # 11
```

### Pure Functions

A **pure function**:

- Uses only its inputs
- Returns a result
- Does not change outside state
- Does not print, write files, or ask for input

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"
```

Pure functions are easier to debug because the same input always produces the same output.

---

## Part 4 - Flexible Inputs with `*args` and `**kwargs` (20 min)

### 4.1 `*args`

`*args` collects extra positional arguments into a tuple.

```python
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(10, 20, 30, 5))  # 65
```

Use `*args` when a function can receive any number of similar values.

### 4.2 `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def build_profile(name, **details):
    profile = {"name": name}

    for key, value in details.items():
        profile[key] = value

    return profile

student = build_profile("Mona", city="Gaza", track="Python")
print(student)
```

Use `**kwargs` when optional named details may vary.

### 4.3 Combining Them

```python
def log_event(event_type, *messages, **metadata):
    print(f"Event: {event_type}")

    for message in messages:
        print(f"- {message}")

    for key, value in metadata.items():
        print(f"{key}: {value}")

log_event(
    "login",
    "User entered email",
    "User entered password",
    username="sara",
    success=True
)
```

Flexible functions are powerful, but they can become unclear if everything is optional. Prefer normal parameters unless flexibility is truly useful.

---

## Part 5 - Mutable Defaults, Docstrings, and Type Hints (20 min)

### 5.1 The Mutable Default Argument Bug

Avoid using a list or dictionary as a default value.

```python
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_item("bread"))  # ['bread']
print(add_item("milk"))   # ['bread', 'milk'] - surprising
```

Default values are created once, not each time the function is called.

Use `None` when the function needs a fresh list or dictionary.

```python
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []

    shopping_list.append(item)
    return shopping_list

print(add_item("bread"))  # ['bread']
print(add_item("milk"))   # ['milk']
```

### 5.2 Docstrings

A docstring explains what a function does, what it expects, and what it returns.

```python
def calculate_discount(price, discount_percent):
    """
    Return the final price after applying a percentage discount.

    price: original item price
    discount_percent: discount as a number from 0 to 100
    """
    discount = price * (discount_percent / 100)
    return price - discount
```

You can read a docstring with `help()`.

```python
help(calculate_discount)
```

### 5.3 Type Hints

Type hints document expected input and output types.

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    discount = price * (discount_percent / 100)
    return price - discount
```

Python does not enforce these types automatically. They help people, editors, and AI tools understand your code.

---

## Mini-Project - Shopping Cart Functions (25 min)

Build a small shopping cart calculator using clean functions.

### Requirements

1. Store cart items as dictionaries with `name`, `price`, and `quantity`
2. Write `item_subtotal(item)` to calculate one item's subtotal
3. Write `cart_total(cart)` to calculate the full cart total
4. Write `apply_discount(total, percent)` to return the discounted total
5. Write `format_receipt(cart, discount_percent)` to return a receipt string
6. Keep calculation functions pure where possible

### Starter Data

```python
cart = [
    {"name": "Notebook", "price": 4.50, "quantity": 3},
    {"name": "Pen", "price": 1.25, "quantity": 5},
    {"name": "Backpack", "price": 35.00, "quantity": 1},
]
```

### Starter Functions

```python
def item_subtotal(item):
    return item["price"] * item["quantity"]


def cart_total(cart):
    total = 0
    for item in cart:
        total += item_subtotal(item)
    return total


def apply_discount(total, percent=0):
    return total - (total * percent / 100)
```

Challenge: add type hints and docstrings to each function.

---

## Exercises

**Exercise 1 - Scope prediction**

Before running the code, predict the output:

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

**Exercise 2 - Pure grade function**

Write `calculate_grade(score)` that returns `"A"`, `"B"`, `"C"`, `"D"`, or `"F"` without printing.

**Exercise 3 - Flexible average**

Write `average(*numbers)` that returns the average of any number of values.

**Exercise 4 - Profile builder**

Write `build_profile(name, **details)` that returns a dictionary containing the name and all extra details.

**Exercise 5 - Refactor**

Take one function from Lesson 10 and improve it with a docstring, type hints, and cleaner separation between calculation and printing.

---

## Key Takeaways

- Variables created inside a function are local.
- Python resolves names using LEGB: Local, Enclosing, Global, Built-in.
- Passing data in and returning data out is usually cleaner than changing globals.
- `*args` collects positional arguments; `**kwargs` collects keyword arguments.
- Use `None` as the default when a function needs a fresh list or dictionary.
- Docstrings and type hints make functions easier to read, test, and reuse.

---

*Next lesson -> **Lesson 12: Lists & Tuples**  
Previous lesson -> **Lesson 10: Practice Lab - Python Basics***
