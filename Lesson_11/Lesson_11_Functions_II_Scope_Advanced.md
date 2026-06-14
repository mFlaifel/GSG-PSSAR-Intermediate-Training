# Lesson 11 - Functions II: Scope & Advanced Concepts

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Explain local scope, global scope, and why scope matters
- Use positional, keyword, and default arguments correctly
- Avoid the mutable default argument bug
- Use `*args` and `**kwargs` for flexible function inputs
- Write useful docstrings for your functions
- Design cleaner functions that are easier to test and reuse

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Review of function basics |
| 0:10-0:35 | Scope: local, global, and built-in names |
| 0:35-1:00 | Arguments: positional, keyword, default |
| 1:00-1:20 | `*args` and `**kwargs` |
| 1:20-1:40 | Docstrings and clean function design |
| 1:40-2:00 | Mini-project and exercises |

---

## Part 1 - Quick Review: What Functions Give Us (10 min)

In Lesson 09, you learned that functions let us package logic into reusable blocks.

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(20, 3)
print(total)  # 60
```

A function normally has:

- A name
- Optional inputs, called parameters
- A body
- An optional returned result

Today we go deeper: where variables live, how arguments are passed, and how to design functions that stay clear as programs grow.

---

## Part 2 - Scope (25 min)

**Scope** means: where a variable can be accessed.

### 2.1 Local Scope

A variable created inside a function is local to that function.

```python
def greet():
    message = "Hello from inside the function"
    print(message)

greet()

# This would cause an error:
# print(message)
```

`message` only exists while `greet()` is running.

---

### 2.2 Global Scope

A variable created outside all functions is global.

```python
course_name = "Python Intermediate"

def show_course():
    print(course_name)

show_course()
```

Functions can read global variables, but depending on them too much makes code harder to test and debug.

---

### 2.3 Local Variables Can Shadow Global Variables

```python
name = "Global Alice"

def show_name():
    name = "Local Bruno"
    print(name)

show_name()  # Local Bruno
print(name)  # Global Alice
```

The local `name` does not change the global `name`. It shadows it inside the function.

---

### 2.4 Changing Global Variables

Python requires the `global` keyword if a function wants to reassign a global variable.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # 2
```

This works, but it is usually not the cleanest design. Prefer passing data in and returning new data out.

```python
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
counter = increment(counter)
print(counter)  # 2
```

This version is easier to test because the function depends only on its input.

---

### 2.5 The LEGB Rule

When Python sees a name, it looks in this order:

| Level | Meaning |
|-------|---------|
| L | Local: inside the current function |
| E | Enclosing: inside outer functions |
| G | Global: module-level variables |
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

You do not need to memorize every detail today. The key idea is: Python searches from the nearest scope outward.

---

## Part 3 - Function Arguments (25 min)

### 3.1 Positional Arguments

Arguments are matched by position.

```python
def introduce(name, role):
    print(f"{name} is a {role}.")

introduce("Sara", "developer")
```

Order matters. If you switch the values, the meaning changes.

```python
introduce("developer", "Sara")  # confusing output
```

---

### 3.2 Keyword Arguments

Keyword arguments are matched by parameter name.

```python
introduce(role="developer", name="Sara")
```

This is clearer when a function has several arguments.

```python
def create_user(username, email, is_admin=False):
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Admin: {is_admin}")

create_user(
    username="maria",
    email="maria@example.com",
    is_admin=True
)
```

---

### 3.3 Default Arguments

Default arguments are used when the caller does not provide a value.

```python
def calculate_price(price, tax_rate=0.15):
    return price + (price * tax_rate)

print(calculate_price(100))       # 115.0
print(calculate_price(100, 0.20)) # 120.0
```

Put required parameters first, then parameters with defaults.

```python
def send_message(to, message, urgent=False):
    if urgent:
        print("URGENT!")
    print(f"To: {to}")
    print(message)
```

---

### 3.4 The Mutable Default Argument Bug

Avoid using a list or dictionary as a default value.

```python
# Bad pattern
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_item("bread"))  # ['bread']
print(add_item("milk"))   # ['bread', 'milk'] - surprising!
```

Default values are created once, not each time the function is called.

Use `None` instead:

```python
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

print(add_item("bread"))  # ['bread']
print(add_item("milk"))   # ['milk']
```

This is one of the most common intermediate Python mistakes.

---

## Part 4 - `*args` and `**kwargs` (20 min)

### 4.1 `*args`: Many Positional Arguments

`*args` collects extra positional arguments into a tuple.

```python
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 2, 3))       # 6
print(add_all(10, 20, 30, 5)) # 65
```

Use `*args` when the number of inputs can vary.

---

### 4.2 `**kwargs`: Many Keyword Arguments

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def show_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

show_profile(name="Ali", city="Gaza", role="student")
```

Output:

```text
name: Ali
city: Gaza
role: student
```

---

### 4.3 Combining Normal Arguments with `*args` and `**kwargs`

```python
def log_event(event_type, *messages, **metadata):
    print(f"Event: {event_type}")

    for message in messages:
        print(f"- {message}")

    for key, value in metadata.items():
        print(f"{key}: {value}")

log_event(
    "login",
    "User entered password",
    "Password accepted",
    username="mona",
    success=True
)
```

Use this feature carefully. Flexible functions are powerful, but they can become unclear if every input is optional and unnamed.

---

## Part 5 - Docstrings and Clean Function Design (20 min)

### 5.1 Docstrings

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

You can view a function's docstring with `help()`.

```python
help(calculate_discount)
```

---

### 5.2 Type Hints

Type hints make the expected data clearer.

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    discount = price * (discount_percent / 100)
    return price - discount
```

Python does not enforce these types automatically, but they help humans, editors, and AI tools understand your code.

---

### 5.3 Clean Function Checklist

A clean function should usually:

- Do one clear job
- Have a descriptive name
- Use clear parameter names
- Return a result instead of printing when possible
- Avoid changing global state
- Be small enough to understand quickly

Compare:

```python
def process(x):
    print(x * 0.15 + x)
```

Better:

```python
def calculate_price_with_tax(price, tax_rate=0.15):
    return price + (price * tax_rate)
```

The second version tells the reader what the function means.

---

## Mini-Project - Shopping Cart Calculator (20 min)

Build a small shopping cart program using functions.

### Requirements

1. Store cart items as dictionaries with `name`, `price`, and `quantity`
2. Write a function to calculate one item subtotal
3. Write a function to calculate the whole cart total
4. Write a function to apply a discount
5. Write a function to print a receipt

### Starter Data

```python
cart = [
    {"name": "Notebook", "price": 4.50, "quantity": 3},
    {"name": "Pen", "price": 1.25, "quantity": 5},
    {"name": "Backpack", "price": 35.00, "quantity": 1},
]
```

### Suggested Solution

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


def print_receipt(cart, discount_percent=0):
    print("RECEIPT")
    print("-" * 30)

    for item in cart:
        subtotal = item_subtotal(item)
        print(f'{item["name"]}: {item["quantity"]} x {item["price"]:.2f} = {subtotal:.2f}')

    total = cart_total(cart)
    final_total = apply_discount(total, discount_percent)

    print("-" * 30)
    print(f"Total: {total:.2f}")
    print(f"Discount: {discount_percent}%")
    print(f"Final total: {final_total:.2f}")


print_receipt(cart, discount_percent=10)
```

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

**Exercise 2 - Default argument**

Write a function `create_email(username, domain="example.com")` that returns an email address.

```python
print(create_email("sara"))              # sara@example.com
print(create_email("sara", "gsg.org"))   # sara@gsg.org
```

**Exercise 3 - Flexible average**

Write `average(*numbers)` that returns the average of any number of values.

**Exercise 4 - Profile builder**

Write `build_profile(name, **details)` that returns a dictionary containing the name and all extra details.

**Exercise 5 - Refactor**

Take a long piece of code from a previous lesson and split it into at least three clean functions.

---

## Key Takeaways

- Variables created inside a function are local.
- Avoid relying heavily on global variables.
- Keyword arguments improve readability.
- Use `None` as the default when the function needs a new list or dictionary.
- `*args` collects positional arguments; `**kwargs` collects keyword arguments.
- Good functions are small, named clearly, and easy to test.

---

*Next lesson -> **Lesson 12: Lists & Tuples**  
Previous lesson -> **Lesson 10: Practice Lab - Python Basics***
