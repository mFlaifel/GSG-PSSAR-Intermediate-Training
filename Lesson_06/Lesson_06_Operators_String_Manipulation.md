# Lesson 06 — Operators & String Manipulation

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Learning Objectives

By the end of this lesson you will be able to:

- Apply arithmetic, comparison, and logical operators
- Use Python's augmented assignment shortcuts
- Manipulate strings with built-in methods like `.upper()`, `.strip()`, `.split()`
- Build readable strings using f-strings
- Convert between data types with `int()`, `str()`, and `float()`

---

## Part 1 — Arithmetic Operators (25 min)

Python supports all the standard math operations you'd expect, plus a few extras.

### 1.1 The Seven Arithmetic Operators

| Operator | Name               | Example   | Result |
| -------- | ------------------ | --------- | ------ |
| `+`      | Addition           | `5 + 3`   | `8`    |
| `-`      | Subtraction        | `10 - 4`  | `6`    |
| `*`      | Multiplication     | `6 * 7`   | `42`   |
| `/`      | Division           | `7 / 2`   | `3.5`  |
| `//`     | Floor Division     | `7 // 2`  | `3`    |
| `%`      | Modulo (remainder) | `7 % 2`   | `1`    |
| `**`     | Exponentiation     | `2 ** 10` | `1024` |

```python
a = 17
b = 5

print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4   ← always returns float
print(a // b)   # 3     ← whole part only
print(a % b)    # 2     ← remainder
print(a ** b)   # 1419857
```

> 💡 **Modulo tip:** `x % 2 == 0` is a classic test for even numbers. If the remainder when divided by 2 is 0, the number is even.

```python
number = 14
print(number % 2 == 0)   # True  → even
number = 9
print(number % 2 == 0)   # False → odd
```

---

### [1.2 Operator Precedence (PEMDAS / BODMAS)](https://www.w3schools.com/python/python_operators_precedence.asp)

Python follows standard mathematical order of operations:

1. `**` (exponentiation)
2. `*`, `/`, `//`, `%`
3. `+`, `-`

```python
print(2 + 3 * 4)      # 14  (not 20!)
print((2 + 3) * 4)    # 20  ← parentheses override the order
print(2 ** 3 + 1)     # 9   (2³ = 8, then 8 + 1)
print(10 - 4 / 2)     # 8.0 (4/2=2, then 10-2)
```

---

### 1.3 Augmented Assignment Operators

These are shortcut operators for updating a variable's value.

| Shortcut  | Equivalent   |
| --------- | ------------ |
| `x += 5`  | `x = x + 5`  |
| `x -= 3`  | `x = x - 3`  |
| `x *= 2`  | `x = x * 2`  |
| `x /= 4`  | `x = x / 4`  |
| `x //= 2` | `x = x // 2` |
| `x %= 3`  | `x = x % 3`  |
| `x **= 2` | `x = x ** 2` |

```python
score = 100
score += 50    # score is now 150
score -= 20    # score is now 130
score *= 2     # score is now 260
print(score)   # 260
```

---

## Part 2 — Comparison Operators (20 min)

Comparison operators **compare two values** and always return a `bool` (`True` or `False`).

### 2.1 The Six Comparison Operators

| Operator | Meaning                  | Example  | Result  |
| -------- | ------------------------ | -------- | ------- |
| `==`     | Equal to                 | `5 == 5` | `True`  |
| `!=`     | Not equal to             | `5 != 3` | `True`  |
| `>`      | Greater than             | `7 > 3`  | `True`  |
| `<`      | Less than                | `2 < 1`  | `False` |
| `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
| `<=`     | Less than or equal to    | `4 <= 3` | `False` |

```python
age = 18

print(age == 18)    # True
print(age != 21)    # True
print(age > 17)     # True
print(age < 18)     # False
print(age >= 18)    # True
print(age <= 17)    # False
print(5 < age < 20) # True
print("apple" < "banana") 
```

> ⚠️ **Common mistake:** Using `=` (assignment) when you mean `==` (comparison). `x = 5` stores 5; `x == 5` checks if x is 5.

---

## Part 3 — Logical Operators (15 min)

Logical operators **combine multiple boolean expressions**.

| Operator | Meaning                              | Example          | Result  |
| -------- | ------------------------------------ | ---------------- | ------- |
| `and`    | True only if **both** sides are True | `True and False` | `False` |
| `or`     | True if **at least one** is True     | `True or False`  | `True`  |
| `not`    | Flips the boolean                    | `not True`       | `False` |

```python
age     = 20
has_id  = True

# Can enter the club?
can_enter = age >= 18 and has_id
print(can_enter)   # True

# Weekend or holiday?
is_weekend = False
is_holiday = True
day_off = is_weekend or is_holiday
print(day_off)     # True

# Is the door locked?
is_open = False
print(not is_open) # True  (door is locked = not open)
```

### Truth Tables

**`and`**
| A | B | A and B |
|-------|-------|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**`or`**
| A | B | A or B |
|-------|-------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Part 4 — String Manipulation (35 min)

Strings come with many built-in **methods** — functions that belong to a string object. You call them using dot notation: `string.method()`.

### 4.1 Case Methods

```python
name = "ana luísa"

print(name.upper())       # ANA LUÍSA
print(name.lower())       # ana luísa
print(name.capitalize())  # Ana luísa  (only first letter)
print(name.title())       # Ana Luísa  (first letter of each word)
```

---

### 4.2 Whitespace Methods

```python
raw = "   hello, world!   "

print(raw.strip())     # "hello, world!"   (removes both ends)
print(raw.lstrip())    # "hello, world!   " (left only)
print(raw.rstrip())    # "   hello, world!" (right only)
```

> 💡 Always `.strip()` user input before processing — users often accidentally add leading/trailing spaces.

---

### 4.3 Search Methods

```python
sentence = "The quick brown fox"

print(sentence.startswith("The"))    # True
print(sentence.endswith("fox"))      # True
print(sentence.find("quick"))        # 4  (index where it starts)
print(sentence.find("cat"))          # -1 (not found)
print("quick" in sentence)           # True  ← very common pattern
print("cat" in sentence)             # False
print(sentence.count("o"))           # 2
```

---

### 4.4 Replace and Split

```python
text = "I love cats and cats love me"

# Replace all occurrences
new_text = text.replace("cats", "dogs")
print(new_text)   # I love dogs and dogs love me

# Split into a list of words
words = text.split()           # splits on whitespace by default
print(words)                   # ['I', 'love', 'cats', 'and', 'cats', 'love', 'me']

# Split on a specific character
csv_line = "Alice,30,Brasília"
parts = csv_line.split(",")
print(parts)                   # ['Alice', '30', 'Brasília']
print(parts[0])                # Alice
print(parts[1])                # 30
```

**Joining a list back into a string:**

```python
words = ["Python", "is", "fun"]
sentence = " ".join(words)     # separator.join(list)
print(sentence)                # Python is fun
```

---

### 4.5 String Slicing

You can extract a piece of a string using `[start:stop:step]` notation.

```python
text = "Hello, Python!"
#       0123456789...

print(text[0:5])    # Hello    (indices 0,1,2,3,4 — stop is excluded)
print(text[7:])     # Python!  (from index 7 to end)
print(text[:5])     # Hello    (from start to index 4)
print(text[-7:])    # Python!  (last 7 characters)
print(text[::2])    # Hlo yhn  (every 2nd character)
print(text[::-1])   # !nohtyP ,olleH  (reversed!)
```

---

### 4.6 F-Strings — The Modern Way to Format Strings

F-strings (formatted string literals) let you embed variables directly inside a string. Prefix the string with `f` and wrap variables in `{}`.

```python
name  = "Gabriel"
age   = 19
grade = 8.75

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your grade is {grade}.")

# Expressions inside {}
print(f"In 5 years you will be {age + 5}.")
print(f"Grade rounded: {round(grade, 1)}")
```

**Formatting numbers:**

```python
price = 1999.5
print(f"Price: R${price:.2f}")       # Price: R$1999.50  (2 decimal places)
print(f"Price: R${price:,.2f}")      # Price: R$1,999.50 (thousands separator)

ratio = 0.756
print(f"Completion: {ratio:.1%}")    # Completion: 75.6%

pi = 3.14159
print(f"Pi ≈ {pi:.3f}")             # Pi ≈ 3.142
```

> 💡 F-strings are the preferred way to format strings in modern Python (3.6+). You may also see `.format()` and `%` formatting in older code.

---

## Part 5 — Type Conversion (15 min)

Sometimes you need to convert a value from one type to another. This is called **casting** or **type conversion**.

### 5.1 Built-in Conversion Functions

| Function  | Converts to | Example         | Result  |
| --------- | ----------- | --------------- | ------- |
| `int()`   | Integer     | `int("42")`     | `42`    |
| `float()` | Float       | `float("3.14")` | `3.14`  |
| `str()`   | String      | `str(100)`      | `"100"` |
| `bool()`  | Boolean     | `bool(0)`       | `False` |

```python
# String to number
user_input = "25"
age = int(user_input)
print(age + 5)         # 30

# Number to string
score = 95
label = "Your score: " + str(score)
print(label)           # Your score: 95

# Float to int (truncates, does NOT round!)
x = 7.9
print(int(x))          # 7  (not 8!)
```

---

### 5.2 Truthiness — What Counts as True or False?

Any Python value can be evaluated as a boolean. This is used frequently in conditions.

```python
# "Falsy" values — evaluate to False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(""))        # False  ← empty string
print(bool(None))      # False

# "Truthy" values — evaluate to True
print(bool(1))         # True
print(bool(-5))        # True  (any non-zero number)
print(bool("hello"))   # True  (any non-empty string)
print(bool("False"))   # True  ← the string "False" is truthy!
```

---

## Part 6 — Putting It All Together (10 min)

### Mini-Project: Simple Invoice Generator

```python
# invoice.py

print("=== INVOICE GENERATOR ===\n")

# Collect item details
item1_name  = input("Item 1 name: ")
item1_price = float(input(f"Price of {item1_name}: R$ "))

item2_name  = input("Item 2 name: ")
item2_price = float(input(f"Price of {item2_name}: R$ "))

# Calculations
subtotal    = item1_price + item2_price
tax_rate    = 0.08
tax_amount  = subtotal * tax_rate
total       = subtotal + tax_amount

# Output
print()
print("=" * 35)
print(f"  {item1_name:<20} R${item1_price:>6.2f}")
print(f"  {item2_name:<20} R${item2_price:>6.2f}")
print("-" * 35)
print(f"  {'Subtotal':<20} R${subtotal:>6.2f}")
print(f"  {'Tax (8%)':<20} R${tax_amount:>6.2f}")
print("=" * 35)
print(f"  {'TOTAL':<20} R${total:>6.2f}")
print("=" * 35)
```

**Sample output:**

```
=== INVOICE GENERATOR ===

Item 1 name: Coffee
Price of Coffee: R$ 12.50
Item 2 name: Sandwich
Price of Sandwich: R$ 18.00

===================================
  Coffee               R$ 12.50
  Sandwich             R$ 18.00
-----------------------------------
  Subtotal             R$ 30.50
  Tax (8%)             R$  2.44
===================================
  TOTAL                R$ 32.94
===================================
```

---

## ✅ Exercises

**Exercise 1 — Calculator**
Ask the user for two numbers and print the result of all seven arithmetic operators on them (add, subtract, multiply, divide, floor divide, modulo, power).

**Exercise 2 — String analyser**
Ask the user for a sentence and print:

- The sentence in UPPERCASE
- The number of characters (including spaces)
- The number of words
- Whether the sentence contains the word `"Python"` (True/False)
- The sentence reversed

**Exercise 3 — Type conversion chain**
Start with the string `"3.7"`. Convert it to float, multiply by 4, convert to int, then convert back to string. Print the result and its type at every step.

**Exercise 4 — Password strength checker**
Ask for a password. Print `True` or `False` for each of these checks:

- Is it longer than 8 characters?
- Does it contain an uppercase letter? (hint: `password != password.lower()`)
- Does it start with a letter? (hint: `password[0].isalpha()`)

---

## 🔑 Key Takeaways

- Python has 7 arithmetic operators; `/` always returns float, `//` returns int.
- Comparison operators return `True` or `False` and are essential for conditions.
- `and`, `or`, `not` combine boolean expressions.
- Strings are packed with methods: `.upper()`, `.strip()`, `.split()`, `.replace()`, etc.
- F-strings (`f"Hello {name}"`) are the cleanest way to embed variables in text.
- `int()`, `float()`, and `str()` convert between types; `input()` always returns a string.

---

## 📚 Further Reading

- [Python String Methods — Official Docs](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python F-String Guide (Real Python)](https://realpython.com/python-f-strings/)

---

\*Next lesson → **Lesson 07: Conditional Logic (`if / elif / else`)**  
Previous lesson → **Lesson 05: Python Setup & First Steps\***
