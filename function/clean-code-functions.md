# Functions in Clean Code

This note explains the main ideas from the **Functions** chapter of *Clean Code* by Robert C. Martin, using Python examples.

The big idea is simple:

> A good function is small, clear, focused, and easy to trust.

Functions are one of the most important tools for writing readable programs. A function should help the reader understand the code faster, not make them search through a maze.

---

## 1. Functions Should Be Small

Clean Code recommends keeping functions small. A small function is easier to read, test, reuse, and debug.

### Not clean

```python
def process_order(order):
    total = 0

    for item in order["items"]:
        total += item["price"] * item["quantity"]

    if order["customer_type"] == "vip":
        total = total * 0.9

    tax = total * 0.15
    final_total = total + tax

    print("Customer:", order["customer_name"])
    print("Subtotal:", total)
    print("Tax:", tax)
    print("Final total:", final_total)

    if final_total > 100:
        print("Free delivery")
    else:
        print("Delivery fee applies")
```

This function calculates totals, applies discounts, calculates tax, prints a receipt, and decides delivery rules. It does too much.

### Cleaner

```python
def calculate_subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, customer_type):
    if customer_type == "vip":
        return total * 0.9
    return total


def calculate_tax(total):
    return total * 0.15


def has_free_delivery(final_total):
    return final_total > 100
```

Now each function has one clear job.

---

## 2. Functions Should Do One Thing

A function should do one thing, do it well, and do it only.

If you can describe a function using the word **and**, it may be doing more than one thing.

### Not clean

```python
def validate_user_and_save(user):
    if not user["email"]:
        return False

    if len(user["password"]) < 8:
        return False

    users.append(user)
    return True
```

This function validates the user **and** saves the user.

### Cleaner

```python
def is_valid_user(user):
    return user["email"] != "" and len(user["password"]) >= 8


def save_user(user):
    users.append(user)
```

Usage:

```python
if is_valid_user(user):
    save_user(user)
```

The code now reads like English.

---

## 3. Use Descriptive Names

A function name should clearly explain what the function does.

Good names reduce the need for comments.

### Not clean

```python
def calc(x, y):
    return x * y
```

What does `calc` calculate? What are `x` and `y`?

### Cleaner

```python
def calculate_rectangle_area(width, height):
    return width * height
```

The name tells the reader exactly what the function does.

---

## 4. Keep the Same Level of Abstraction

A function should not mix high-level business steps with low-level implementation details.

### Not clean

```python
def register_student(student):
    if "@" not in student["email"]:
        raise ValueError("Invalid email")

    file = open("students.txt", "a")
    file.write(student["name"] + "," + student["email"] + "\n")
    file.close()

    print("Student registered successfully")
```

This mixes validation, file writing, and user output.

### Cleaner

```python
def register_student(student):
    validate_student(student)
    save_student(student)
    show_registration_success()
```

The high-level function explains the workflow. The details can live in smaller helper functions.

```python
def validate_student(student):
    if "@" not in student["email"]:
        raise ValueError("Invalid email")


def save_student(student):
    with open("students.txt", "a") as file:
        file.write(f"{student['name']},{student['email']}\n")


def show_registration_success():
    print("Student registered successfully")
```

---

## 5. Prefer Fewer Arguments

Functions are easier to understand when they take fewer arguments.

Clean Code generally prefers:

- 0 arguments when possible
- 1 argument when natural
- 2 arguments when needed
- 3 arguments only with care
- More than 3 arguments usually means you should rethink the design

### Not clean

```python
def create_user(first_name, last_name, email, password, age, city):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "age": age,
        "city": city,
    }
```

Too many separate values make the function harder to call correctly.

### Cleaner

```python
def create_user(user_data):
    return {
        "first_name": user_data["first_name"],
        "last_name": user_data["last_name"],
        "email": user_data["email"],
        "password": user_data["password"],
        "age": user_data["age"],
        "city": user_data["city"],
    }
```

Usage:

```python
user_data = {
    "first_name": "Mona",
    "last_name": "Ali",
    "email": "mona@example.com",
    "password": "securepass",
    "age": 22,
    "city": "Gaza",
}

user = create_user(user_data)
```

In larger Python programs, you may use a class or dataclass instead of a dictionary.

---

## 6. Avoid Flag Arguments

A flag argument is a `True` or `False` value that changes what a function does.

Flag arguments often mean the function is doing two different things.

### Not clean

```python
def format_name(first_name, last_name, uppercase):
    full_name = f"{first_name} {last_name}"

    if uppercase:
        return full_name.upper()

    return full_name
```

The function has two modes.

### Cleaner

```python
def format_name(first_name, last_name):
    return f"{first_name} {last_name}"


def format_uppercase_name(first_name, last_name):
    return format_name(first_name, last_name).upper()
```

Each function now has a clearer purpose.

---

## 7. Avoid Side Effects

A side effect happens when a function changes something outside itself in a surprising way.

Examples of side effects:

- Changing a global variable
- Modifying a list passed into the function
- Writing to a file
- Printing to the screen
- Sending a network request

Side effects are not always bad, but they should be obvious from the function name.

### Not clean

```python
users = []


def is_valid_user(user):
    if user["email"] != "":
        users.append(user)
        return True
    return False
```

The name says the function checks validity, but it also saves the user. That is surprising.

### Cleaner

```python
def is_valid_user(user):
    return user["email"] != ""


def add_user(users, user):
    users.append(user)
```

Now checking and changing data are separate.

---

## 8. Separate Commands from Queries

A function should either:

- Answer a question
- Do an action

It should not do both at the same time.

### Query example

```python
def is_passing_grade(grade):
    return grade >= 50
```

This answers a question.

### Command example

```python
def print_pass_status(student_name):
    print(f"{student_name} passed")
```

This performs an action.

### Not clean

```python
def save_user_and_return_status(users, user):
    users.append(user)
    return "saved"
```

This changes data and returns a status message.

### Cleaner

```python
def save_user(users, user):
    users.append(user)


def user_saved_message():
    return "saved"
```

---

## 9. Prefer Exceptions Over Error Codes

Returning error codes can make the main logic harder to read.

### Not clean

```python
def divide(a, b):
    if b == 0:
        return "ERROR"
    return a / b


result = divide(10, 0)

if result == "ERROR":
    print("Cannot divide by zero")
else:
    print(result)
```

The caller must remember to check for the error string.

### Cleaner

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


try:
    result = divide(10, 0)
    print(result)
except ValueError as error:
    print(error)
```

The normal path stays clean, and the error path is handled separately.

---

## 10. Do Not Repeat Yourself

Repeated logic should usually become a function.

### Not clean

```python
price1 = 100
discount1 = price1 * 0.2
final_price1 = price1 - discount1

price2 = 250
discount2 = price2 * 0.2
final_price2 = price2 - discount2

price3 = 80
discount3 = price3 * 0.2
final_price3 = price3 - discount3
```

### Cleaner

```python
def apply_twenty_percent_discount(price):
    return price - (price * 0.2)


final_price1 = apply_twenty_percent_discount(100)
final_price2 = apply_twenty_percent_discount(250)
final_price3 = apply_twenty_percent_discount(80)
```

The rule lives in one place.

---

## 11. Write Functions That Are Easy to Test

A clean function is usually easy to test because it has clear input and clear output.

### Easy to test

```python
def calculate_final_price(price, discount_rate):
    return price - (price * discount_rate)
```

Test:

```python
def test_calculate_final_price():
    assert calculate_final_price(100, 0.2) == 80
```

### Harder to test

```python
def print_final_price(price, discount_rate):
    final_price = price - (price * discount_rate)
    print(final_price)
```

This function prints instead of returning. To test it, you must capture the printed output.

When possible, return values from functions and print at the edge of the program.

---

## 12. Comments Are Not a Fix for Confusing Functions

If a function needs a long comment to explain what it does, try improving the function first.

### Not clean

```python
# This function checks if the student has a grade greater than or equal to 50,
# and if yes it returns True, otherwise it returns False.
def check(x):
    return x >= 50
```

### Cleaner

```python
def is_passing_grade(grade):
    return grade >= 50
```

The name explains the idea.

---

## Quick Checklist for Clean Functions

Before finishing a function, ask:

- Does the function do one thing?
- Is the function small?
- Is the name clear?
- Are the parameter names clear?
- Can I reduce the number of arguments?
- Does the function avoid surprising side effects?
- Does it return a useful value when needed?
- Is repeated logic moved into a function?
- Can this function be tested easily?

---

## Final Example: Refactoring a Messy Function

### Before

```python
def handle_student(name, grade):
    if grade >= 50:
        status = "passed"
    else:
        status = "failed"

    print(name + " has " + status)

    with open("students.txt", "a") as file:
        file.write(name + "," + str(grade) + "," + status + "\n")
```

Problems:

- It decides pass/fail status
- It prints a message
- It writes to a file
- It mixes several levels of detail

### After

```python
def get_student_status(grade):
    if grade >= 50:
        return "passed"
    return "failed"


def format_student_result(name, status):
    return f"{name} has {status}"


def save_student_result(name, grade, status):
    with open("students.txt", "a") as file:
        file.write(f"{name},{grade},{status}\n")


def handle_student(name, grade):
    status = get_student_status(grade)
    message = format_student_result(name, status)

    print(message)
    save_student_result(name, grade, status)
```

This version is longer in number of lines, but each part is easier to understand, test, and change.

---

## Summary

Clean functions make code easier to read and safer to change.

The most important rules are:

- Keep functions small
- Make each function do one thing
- Use clear names
- Avoid too many arguments
- Avoid hidden side effects
- Separate actions from questions
- Remove duplicated logic
- Prefer readable code over clever code

When functions are clean, the program tells a clear story.
