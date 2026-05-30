# Lesson 05 — Python Setup & First Steps

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Learning Objectives

By the end of this lesson you will be able to:

- Install Python and Visual Studio Code on your machine
- Run your first Python script from the terminal and from VS Code
- Declare variables and understand the four basic data types: `int`, `float`, `str`, and `bool`
- Use `print()` to display output and `input()` to read user input
- Write single-line and multi-line comments

---

## Part 1 — Installing Your Tools (30 min)

### 1.1 Installing Python

1. Go to [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest stable version (3.12+).
3. **Windows**: Run the installer and **check "Add Python to PATH"** before clicking Install.
4. **macOS / Linux**: Python may already be present. Confirm with:

```bash
python3 --version
```

You should see something like `Python 3.12.x`.

---

### 1.2 Installing Visual Studio Code

1. Go to [https://code.visualstudio.com/](https://code.visualstudio.com/) and download VS Code for your OS.
2. Install and open it.
3. Install the **Python extension** by Microsoft:
   - Click the Extensions icon (left sidebar) or press `Ctrl+Shift+X`
   - Search for **"Python"** → Install

---

### 1.3 Your First Python File

1. Create a folder on your desktop called `python_course`.
2. Open VS Code → **File → Open Folder** → select `python_course`.
3. Create a new file: `hello.py`
4. Type the following:

```python
print("Hello, world!")
```

5. Open the integrated terminal: **Terminal → New Terminal** (or `` Ctrl+` ``).
6. Run the script:

```bash
python hello.py
# or on macOS/Linux:
python3 hello.py
```

**Expected output:**
```
Hello, world!
```

> 🎉 You just ran your first Python program!

---

## Part 2 — Variables and Data Types (45 min)

### 2.1 What Is a Variable?

A **variable** is a named container that stores a value in memory.  
Think of it as a labelled box: you put something inside and refer to it by its label.

```python
name = "Alice"
age  = 25
```

Python uses **dynamic typing** — you don't declare the type explicitly; Python figures it out.

---

### 2.2 The Four Basic Data Types

| Type    | Keyword  | Example             | Description                        |
|---------|----------|---------------------|------------------------------------|
| Integer | `int`    | `42`, `-7`, `0`     | Whole numbers, no decimal point    |
| Float   | `float`  | `3.14`, `-0.5`      | Numbers with a decimal point       |
| String  | `str`    | `"hello"`, `'hi'`  | Text, always inside quotes         |
| Boolean | `bool`   | `True`, `False`     | Represents yes/no, on/off values   |

---

### 2.3 Integers — `int`

```python
score     = 100
year      = 2024
negative  = -15

print(score)    # 100
print(type(score))  # <class 'int'>
```

Use integers for **counting**, **indexing**, and any whole-number value.

---

### 2.4 Floats — `float`

```python
temperature = 36.6
price       = 9.99
pi          = 3.14159

print(temperature)      # 36.6
print(type(price))      # <class 'float'>
```

> ⚠️ **Floating-point precision:** Computers store floats in binary, which can cause tiny rounding errors.

```python
print(0.1 + 0.2)   # 0.30000000000000004  ← not a bug, it's how floats work
```

---

### 2.5 Strings — `str`

A string is any sequence of characters wrapped in single `'...'` or double `"..."` quotes.

```python
first_name = "Maria"
city       = 'Brasília'
greeting   = "Hello, World!"

print(first_name)
print(len(greeting))   # 13  (counts every character including the comma and space)
```

**Multi-line strings** use triple quotes:

```python
paragraph = """This is the first line.
This is the second line.
This is the third line."""

print(paragraph)
```

**Accessing individual characters (indexing):**

```python
word = "Python"
print(word[0])   # P  (indexing starts at 0!)
print(word[5])   # n
print(word[-1])  # n  (negative index = count from the end)
```

---

### 2.6 Booleans — `bool`

Booleans can only be `True` or `False` (capitalised in Python).

```python
is_logged_in  = True
has_paid      = False

print(is_logged_in)          # True
print(type(has_paid))        # <class 'bool'>
```

Under the hood, `True == 1` and `False == 0` in Python.

---

### 2.7 Checking the Type of Any Variable

Use the built-in `type()` function:

```python
x = 42
y = 3.14
z = "hello"
w = True

print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>
print(type(z))   # <class 'str'>
print(type(w))   # <class 'bool'>
```

---

### 2.8 Variable Naming Rules

| Rule | Example |
|------|---------|
| Use only letters, digits, and underscores | `user_name`, `score1` ✅ |
| Must not start with a digit | `1score` ❌ |
| Case-sensitive | `Name` ≠ `name` |
| Use `snake_case` by convention | `first_name` ✅ (not `firstName`) |
| Avoid reserved keywords | `if`, `for`, `while`, `True` are reserved ❌ |

```python
# Good variable names
user_age    = 20
total_score = 95.5
is_active   = True

# Bad variable names (will cause errors)
# 2fast = True       ← starts with a digit
# my-name = "Ana"    ← hyphens not allowed
```

---

## Part 3 — `print()` and `input()` (25 min)

### 3.1 The `print()` Function

`print()` sends output to the terminal. It accepts multiple values separated by commas.

```python
name = "Carlos"
age  = 30

print("Name:", name)
print("Age:", age)
print("Name:", name, "| Age:", age)
```

**Controlling separator and end character:**

```python
print("A", "B", "C")                  # A B C  (default sep=" ")
print("A", "B", "C", sep="-")         # A-B-C
print("Loading", end="")
print("...")                           # Loading...  (no newline between them)
```

---

### 3.2 The `input()` Function

`input()` pauses the program and waits for the user to type something. It **always returns a string**.

```python
name = input("What is your name? ")
print("Hello,", name)
```

**Getting a number from the user:**

Because `input()` returns a `str`, you must convert it:

```python
age_str = input("How old are you? ")
age     = int(age_str)           # convert string to integer
print("In 10 years you will be", age + 10)
```

Or more concisely:

```python
age = int(input("How old are you? "))
print("In 10 years you will be", age + 10)
```

> ⚠️ If the user types something that isn't a number, `int()` will raise an error. You will learn to handle that in Lesson 14.

---

## Part 4 — Comments (10 min)

Comments are notes for humans — Python ignores them completely.

### Single-line comment

```python
# This line will not be executed
name = "Ana"   # inline comment explaining the variable
```

### Multi-line comment (using triple quotes)

Technically these are string literals that aren't assigned to anything, but they're commonly used as block comments or documentation strings.

```python
"""
This script collects the user's name and age
and displays a personalised greeting.
Author: Maria
Date: 2024-01-15
"""

name = input("Enter your name: ")
age  = int(input("Enter your age: "))
print(f"Hi {name}, you are {age} years old.")
```

> 💡 In Lesson 03 you studied the principle of commenting the *why*, not the *what*. Now you can apply it directly in Python syntax. The rule is the same: the code already says *what* happens; your comment should say *why* it was written that way.

```python
# BAD — restates the obvious
age = age + 1   # add 1 to age

# GOOD — explains the intent, which the code alone cannot convey
age = age + 1   # birthday has passed; keep in sync with user's profile record
```

---

## Part 5 — Putting It All Together (10 min)

### Mini-Project: Personal Info Card

Build a script that asks the user for their name, age, and city, then prints a formatted card.

```python
# personal_card.py

# Collect information from the user
name = input("Enter your full name: ")
age  = int(input("Enter your age: "))
city = input("Enter your city: ")

# Display a formatted card
print()
print("=" * 30)
print("    PERSONAL INFO CARD")
print("=" * 30)
print("Name:", name)
print("Age: ", age)
print("City:", city)
print("=" * 30)
```

**Sample run:**
```
Enter your full name: Lucas Ferreira
Enter your age: 22
Enter your city: São Paulo

==============================
    PERSONAL INFO CARD
==============================
Name: Lucas Ferreira
Age:  22
City: São Paulo
==============================
```

---

## ✅ Exercises

Try to solve these before looking at the answers.

**Exercise 1 — Data types**
Create one variable of each type (`int`, `float`, `str`, `bool`) and print both the value and its type.

**Exercise 2 — User rectangle**
Ask the user for the width and height of a rectangle (as integers).  
Calculate and print the **area** and the **perimeter**.

```
Area      = width × height
Perimeter = 2 × (width + height)
```

**Exercise 3 — Temperature converter**
Ask the user for a temperature in Celsius.  
Convert it to Fahrenheit and print the result.

```
Fahrenheit = (Celsius × 9/5) + 32
```

**Exercise 4 — Descriptive script**
Write a script with at least 5 meaningful comments that explains what each section does.

---

## 🔑 Key Takeaways

- Python must be installed and added to `PATH`; VS Code is the recommended editor.
- Variables are named containers; Python assigns their type automatically.
- The four fundamental types are `int`, `float`, `str`, and `bool`.
- `print()` displays output; `input()` reads a string from the user.
- Always convert `input()` to the right type with `int()` or `float()` when you need a number.
- Comments use `#`; write them to explain *why*, not *what*.

---

## 📚 Further Reading

- [Python Official Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

---

*Next lesson → **Lesson 06: Operators & String Manipulation***
