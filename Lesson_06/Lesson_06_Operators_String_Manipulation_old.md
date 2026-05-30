# Lesson 06 — Operators & String Manipulation

**Phase 2 — Python Core | Duration: 2 Hours**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Use arithmetic, comparison, and logical operators in Python
- Apply common string methods: `.upper()`, `.lower()`, `.split()`, `.join()`, `.strip()`
- Format strings using f-strings
- Convert between data types using `int()`, `str()`, and `float()`
- Combine operators and string methods to solve real-world problems

---

## Part 1 — Arithmetic Operators (25 min)

### 1.1 Basic Math

Python supports all standard arithmetic operations:

```python
# Addition
print(5 + 3)    # 8

# Subtraction
print(10 - 4)   # 6

# Multiplication
print(3 * 7)    # 21

# Division (always returns a float)
print(10 / 3)   # 3.333...

# Integer division (floor)
print(10 // 3)  # 3

# Modulo (remainder)
print(10 % 3)   # 1

# Exponentiation
print(2 ** 4)   # 16
```

### 1.2 Operator Precedence

Use parentheses to control the order of operations:

```python
result = (5 + 3) * 2   # 16
result = 5 + 3 * 2     # 11 (multiplication first)
```

---

## Part 2 — Comparison & Logical Operators (20 min)

### 2.1 Comparison Operators

These return `True` or `False`:

| Operator | Meaning         |
|----------|-----------------|
| `==`     | Equal to        |
| `!=`     | Not equal to    |
| `<`      | Less than       |
| `>`      | Greater than    |
| `<=`     | Less or equal   |
| `>=`     | Greater or equal|

```python
print(5 == 5)   # True
print(5 != 3)   # True
print(7 < 4)    # False
```

### 2.2 Logical Operators

Combine multiple conditions:

```python
age = 20
has_id = True

print(age >= 18 and has_id)   # True
print(age < 18 or has_id)     # True
print(not has_id)             # False
```

---

## Part 3 — String Methods (30 min)

### 3.1 Common Methods

```python
text = "  Hello, World!  "

print(text.upper())          # "  HELLO, WORLD!  "
print(text.lower())          # "  hello, world!  "
print(text.strip())          # "Hello, World!"
print(text.replace("World", "Python"))  # "  Hello, Python!  "
```

### 3.2 Splitting & Joining

```python
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")      # ["apple", "banana", "cherry"]

joined = " | ".join(fruits)       # "apple | banana | cherry"
```

### 3.3 Checking Content

```python
email = "user@example.com"
print(email.startswith("user"))   # True
print(email.endswith(".com"))     # True
print("@" in email)               # True
print(email.count("@"))           # 1
```

---

## Part 4 — Type Conversion (15 min)

```python
# String to integer
age_str = "25"
age_int = int(age_str)

# Float to integer (truncates)
pi = 3.14159
approx = int(pi)          # 3

# Number to string
score = 95
message = f"Score: " + str(score)

# String to float
price = float("19.99")
```

---

## Part 5 — f-Strings (15 min)

f-strings make string formatting clean and readable:

```python
name = "Sara"
age = 22
score = 87.5

print(f"Student: {name}, Age: {age}, Score: {score}%")

# Expressions inside f-strings
print(f"{name} will be {age + 5} in 5 years")

# Formatting numbers
print(f"Score: {score:.1f}")   # "Score: 87.5"
```

---

## Part 6 — Practice Exercises (15 min)

1. Ask the user for a temperature in Celsius and convert it to Fahrenheit using `(c * 9/5) + 32`.
2. Ask for a full name, then print the initials in uppercase (e.g., "mohamed ali" → "M.A.").
3. Take a sentence, count the number of words, and print the result using an f-string.
4. Ask for a number, check if it is even or odd using the modulo operator, and print the result.

---

## Summary

- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `and`, `or`, `not`
- **String methods**: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.count()`
- **Type conversion**: `int()`, `str()`, `float()`
- **f-strings**: embed variables and expressions inside `f"..."` strings
