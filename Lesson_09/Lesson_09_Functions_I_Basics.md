# Lesson 09 — Functions I: Basics

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Learning Objectives

By the end of this lesson you will be able to:

- Define and call your own functions using `def`
- Use parameters to pass information into a function
- Use `return` to send a result back from a function
- Explain the DRY principle and why it matters
- Use Python's most important built-in functions
- Write clean, readable functions with proper naming conventions

---

## Part 1 — What Is a Function? (15 min)

A **function** is a named, reusable block of code that performs a specific task.

You have already been using functions:

```python
print("Hello")          # built-in function
len("Python")           # built-in function
int("42")               # built-in function
name = input("Name: ")  # built-in function
```

But you can also create your own.

### Why Functions Matter

**Without functions:**

```python
# Calculating the area of 3 rectangles
w1, h1 = 5, 3
print(f"Area 1: {w1 * h1}")

w2, h2 = 8, 4
print(f"Area 2: {w2 * h2}")

w3, h3 = 6, 6
print(f"Area 3: {w3 * h3}")
```

**With a function:**

```python
def rectangle_area(width, height):
    return width * height

print(f"Area 1: {rectangle_area(5, 3)}")
print(f"Area 2: {rectangle_area(8, 4)}")
print(f"Area 3: {rectangle_area(6, 6)}")
```

The logic lives in **one place**. If the calculation changes, you change it once.

---

## Part 2 — Defining and Calling Functions (30 min)

### 2.1 Basic Syntax

```python
def function_name(parameter1, parameter2):
    """Optional docstring describing what the function does."""
    # function body
    return result
```

- `def` — keyword to define a function
- `function_name` — use `snake_case` by convention
- `parameters` — inputs the function expects (optional)
- `return` — sends a value back (optional)
- The body must be **indented**

---

### 2.2 A Function with No Parameters

```python
def greet():
    print("Hello! Welcome to the Python course.")

# Calling the function
greet()    # Hello! Welcome to the Python course.
greet()    # called again — same output
greet()    # and again
```

---

### 2.3 A Function with Parameters

```python
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

greet_user("Alice")    # Hello, Alice! Welcome to the Python course.
greet_user("Bruno")    # Hello, Bruno! Welcome to the Python course.
greet_user("Carla")    # Hello, Carla! Welcome to the Python course.
```

The `name` parameter is a **local variable** — it only exists inside the function.

---

### 2.4 Multiple Parameters

```python
def introduce(first_name, last_name, age):
    print(f"Name: {first_name} {last_name}")
    print(f"Age : {age}")
    print()

introduce("Maria", "Silva", 22)
introduce("João", "Oliveira", 35)
```

---

### 2.5 The `return` Statement

`return` sends a value back to whoever called the function.

```python
def add(a, b):
    result = a + b
    return result

# Store the returned value
total = add(10, 5)
print(total)         # 15

# Use directly in an expression
print(add(3, 4) * 2)    # 14
```

**Without `return`, a function returns `None`:**

```python
def no_return():
    x = 5 + 3

value = no_return()
print(value)         # None
```

---

### 2.6 Returning Multiple Values

Python functions can return multiple values as a tuple:

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple (min, max)

low, high = min_max([3, 7, 1, 9, 4])
print(f"Min: {low}, Max: {high}")       # Min: 1, Max: 9
```

---

### 2.7 `return` Exits the Function

Once `return` is hit, the function ends immediately.

```python
def classify_number(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"   # only reached if n == 0

print(classify_number(5))    # positive
print(classify_number(-3))   # negative
print(classify_number(0))    # zero
```

---

## Part 3 — DRY and Functions (15 min)

In Lesson 03 you studied the **DRY principle** (Don't Repeat Yourself) as a design philosophy. You saw it applied to data (the `DISCOUNT_RATES` dictionary) and to code structure. Now you can use the most direct tool for DRY in Python: **functions**.

The connection is simple: whenever you find yourself duplicating a block of logic, that block belongs in a function. A function is the language mechanism that turns a repeated pattern into a named, reusable unit.

```python
# Pattern repeated 3 times — DRY violation (Lesson 03 warned us about this)
name1 = "Alice"; grade1 = 72
if grade1 >= 60: print(f"{name1} passed!")
else: print(f"{name1} failed.")

name2 = "Bruno"; grade2 = 45
if grade2 >= 60: print(f"{name2} passed!")
else: print(f"{name2} failed.")
```

```python
# The function is the fix — logic lives in one place
def check_pass(name, grade):
    if grade >= 60:
        print(f"{name} passed!")
    else:
        print(f"{name} failed.")

check_pass("Alice", 72)
check_pass("Bruno", 45)
check_pass("Carla", 88)
```

The passing threshold (`60`) appears **once**. Changing it means editing a single line. This is DRY expressed through a function.

> 📎 **Lesson 03 connection:** The data-driven discount example from L03 and this function approach are two sides of the same coin. When the repetition is in *data*, extract it to a structure. When the repetition is in *logic*, extract it to a function.

---

## Part 4 — Default Arguments (20 min)

You can give parameters a **default value** that is used when no argument is provided.

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Hello, Alice!
greet("Bruno", "Olá")      # Olá, Bruno!
greet("Carla", "Hi")       # Hi, Carla!
```

### Rules for Default Arguments

- Parameters with defaults must come **after** parameters without defaults.

```python
# Correct
def power(base, exponent=2):
    return base ** exponent

# Wrong — will cause a SyntaxError
# def power(base=2, exponent):
```

---

### Keyword Arguments

When calling a function, you can name the arguments (in any order):

```python
def describe_pet(name, animal_type, age):
    print(f"{name} is a {animal_type}, {age} years old.")

# Positional (order matters)
describe_pet("Rex", "dog", 3)

# Keyword (order doesn't matter)
describe_pet(age=5, name="Whiskers", animal_type="cat")
```

---

## Part 5 — Built-in Functions Reference (20 min)

Python comes with dozens of useful built-in functions. Here are the most important ones:

### 5.1 Math Functions

```python
print(abs(-7))          # 7     — absolute value
print(round(3.7))       # 4     — round to nearest integer
print(round(3.14159, 2))# 3.14  — round to 2 decimal places
print(max(3, 8, 2, 9))  # 9
print(min(3, 8, 2, 9))  # 2
print(sum([1, 2, 3, 4]))# 10
print(pow(2, 10))       # 1024  — same as 2 ** 10
```

### 5.2 Type Functions

```python
print(type("hello"))    # <class 'str'>
print(isinstance(5, int))   # True
print(isinstance(5, str))   # False
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(str(100))         # "100"
print(bool(0))          # False
```

### 5.3 String and Sequence Functions

```python
print(len("Python"))        # 6
print(len([1, 2, 3, 4]))    # 4
print(sorted([3, 1, 4, 1])) # [1, 1, 3, 4]
print(list(range(5)))       # [0, 1, 2, 3, 4]
```

### 5.4 Input / Output

```python
name = input("Enter your name: ")
print("Hello", name, sep=", ", end="!\n")
```

### 5.5 Useful Math Module Functions

For advanced math, import the `math` module:

```python
import math

print(math.sqrt(16))      # 4.0
print(math.floor(3.9))    # 3
print(math.ceil(3.1))     # 4
print(math.pi)            # 3.141592653589793
```

---

## Part 6 — Writing Clean Functions (10 min)

Lesson 03 established the general principles: Single Responsibility, naming as documentation, commenting the *why*. Here we apply those principles specifically to Python function signatures and documentation tooling.

### 6.1 Function Naming Conventions

Python functions follow the same `snake_case` convention as variables, but good function names carry an **action** — they tell you what the function *does*, not just what it's about.

```python
# Good — starts with a verb, describes the action precisely
def calculate_area(width, height):   ...
def get_user_name():                 ...
def is_valid_email(email):           ...   # bool-returning functions use "is_" or "has_"
def send_confirmation(email):        ...

# Bad — noun-only names, cryptic abbreviations, camelCase
def area(w, h):        ...   # what kind of area?
def proc(x):           ...   # process what? return what?
def calculateArea():   ...   # camelCase belongs in JavaScript
```

**Prefix conventions in Python:**
- `get_` / `fetch_` → retrieves and returns data
- `calculate_` / `compute_` → performs math or transformation
- `is_` / `has_` / `can_` → returns a boolean
- `print_` / `display_` / `show_` → produces output, returns nothing
- `save_` / `write_` / `send_` → performs a side effect

### 6.2 Docstrings — Python's Built-in Documentation

A **docstring** is a string literal placed at the very start of a function body. Python stores it as metadata — accessible via `help()` and all documentation generators.

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(100))   # 212.0
help(celsius_to_fahrenheit)         # ← Python prints the docstring
```

Write a docstring for every function that isn't obvious in one glance. Describe: what it does, what parameters it expects, and what it returns.

### 6.3 Functions and Testability

The SRP from Lesson 03 has a practical payoff: a function that does one thing can be tested in isolation. A function that does three things can only be tested as a whole — and when it breaks, you don't know which part failed.

```python
# One function — three concerns — untestable in isolation
def process_student(name, score):
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
    print(f"Name: {name}, Score: {score}, Grade: {grade}")
    with open("grades.txt", "a") as f:
        f.write(f"{name},{score},{grade}\n")

# Three functions — one concern each — each testable on its own
def calculate_grade(score):
    """Return a letter grade for a 0–100 score."""
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    return "F"

def format_result(name, score, grade):
    """Return a formatted result string for display."""
    return f"Name: {name}, Score: {score}, Grade: {grade}"

def save_result(name, score, grade, filepath="grades.txt"):
    """Append a student result to the grades file."""
    with open(filepath, "a") as f:
        f.write(f"{name},{score},{grade}\n")
```

You can now test `calculate_grade(85)` without worrying about file access or print output.

---

## Part 7 — Complete Example: Calculator Module (10 min)

```python
# calculator.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return a divided by b. Returns None if b is zero."""
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None
    return a / b

def display_menu():
    print("\n=== CALCULATOR ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

# ---- Main Program ----

while True:
    display_menu()
    choice = input("Select operation (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)

    if result is not None:
        print(f"Result: {result}")
```

---

## ✅ Exercises

**Exercise 1 — Temperature toolkit**
Write three functions:
- `celsius_to_fahrenheit(c)` → returns `(c * 9/5) + 32`
- `fahrenheit_to_celsius(f)` → returns `(f - 32) * 5/9`
- `celsius_to_kelvin(c)` → returns `c + 273.15`

Call each function and print the results.

**Exercise 2 — String utilities**
Write a function `is_palindrome(text)` that returns `True` if the text reads the same backwards (ignore case and spaces).
- `"racecar"` → `True`
- `"A man a plan a canal Panama"` → `True`
- `"hello"` → `False`

**Exercise 3 — Grade statistics**
Write a function `analyse_grades(grades)` that takes a list of numbers and prints:
- The average
- The highest grade
- The lowest grade
- How many students passed (score ≥ 60)

**Exercise 4 — Refactor challenge**
Take this code and refactor it into clean functions with proper names and docstrings:

```python
# Ugly code to refactor
n = int(input("Number: "))
r = 1
for i in range(1, n + 1):
    r = r * i
print(r)
```

---

## 🔑 Key Takeaways

- `def name(params):` defines a function; calling `name(args)` executes it.
- `return` sends a value back; without it, the function returns `None`.
- Functions enforce DRY — logic lives in one place and is reused many times.
- Default arguments make parameters optional; keyword arguments improve readability.
- Python's built-in functions (`len`, `max`, `min`, `round`, `sorted`, etc.) are powerful tools.
- Good functions have clear names, do one thing, and are documented with docstrings.

---

## 📚 Further Reading

- [Python Docs — Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Built-in Functions Reference](https://docs.python.org/3/library/functions.html)
- [Real Python — Functions in Python](https://realpython.com/defining-your-own-python-function/)

---

*Next lesson → **Lesson 10: Practice Lab — Python Basics**  
Previous lesson → **Lesson 08: Loops — `for` & `while`***
