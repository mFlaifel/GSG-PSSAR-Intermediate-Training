# Lesson 08 — Loops: `for` & `while`

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Learning Objectives

By the end of this lesson you will be able to:

- Use `for` loops to iterate over sequences and ranges
- Use `while` loops to repeat code while a condition is true
- Control loop execution with `break`, `continue`, and `else`
- Apply common loop patterns: counting, summing, searching, and building strings
- Choose the right loop type for a given problem

---

## Part 1 — Why Loops? (10 min)

Imagine printing numbers from 1 to 10,000 without a loop:

```python
print(1)
print(2)
print(3)
# ... 9,997 more lines 😱
```

With a loop, one construct handles any size:

```python
for i in range(1, 10001):
    print(i)
```

Loops are the tool for **repetition** — doing the same thing (or something slightly different) many times.

---

## Part 2 — The `for` Loop (40 min)

A `for` loop **iterates over a sequence** — running its body once for each item.

### 2.1 Iterating Over a String

```python
for letter in "Python":
    print(letter)
```

**Output:**
```
P
y
t
h
o
n
```

Each character in the string becomes the loop variable (`letter`) in turn.

---

### 2.2 The `range()` Function

`range()` generates a sequence of integers. It's the most common companion to `for`.

| Call               | Generates                   |
|--------------------|-----------------------------|
| `range(5)`         | 0, 1, 2, 3, 4               |
| `range(1, 6)`      | 1, 2, 3, 4, 5               |
| `range(0, 10, 2)`  | 0, 2, 4, 6, 8               |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 |

**Syntax:** `range(start, stop, step)`
- `stop` is **excluded** (like slicing)
- Default `start` is 0, default `step` is 1

```python
# Count 1 to 5
for i in range(1, 6):
    print(i)

# Count by 5s
for i in range(0, 51, 5):
    print(i, end=" ")   # 0 5 10 15 20 25 30 35 40 45 50

# Countdown
for i in range(10, 0, -1):
    print(i, end=" ")   # 10 9 8 7 6 5 4 3 2 1
```

---

### 2.3 Iterating Over a List (Preview)

You'll learn lists in depth in Lesson 12, but you can already loop over them:

```python
fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(f"I like {fruit}")
```

---

### 2.4 `enumerate()` — Getting Index and Value

When you need both the position and the value:

```python
students = ["Alice", "Bruno", "Carla", "Daniel"]

for index, name in enumerate(students):
    print(f"{index + 1}. {name}")
```

**Output:**
```
1. Alice
2. Bruno
3. Carla
4. Daniel
```

---

### 2.5 Nested `for` Loops

A loop inside a loop. The inner loop runs **completely** for each iteration of the outer loop.

```python
# Multiplication table (1–5)
for row in range(1, 6):
    for col in range(1, 6):
        print(f"{row * col:3}", end="")
    print()   # newline after each row
```

**Output:**
```
  1  2  3  4  5
  2  4  6  8 10
  3  6  9 12 15
  4  8 12 16 20
  5 10 15 20 25
```

> ⚠️ Nested loops multiply execution time. A 3-level deep nested loop over 100 items runs 100³ = 1,000,000 iterations. Use with care.

---

## Part 3 — The `while` Loop (30 min)

A `while` loop **repeats as long as a condition is `True`**. It's used when you don't know in advance how many times to loop.

```
while <condition>:
    <body>
```

### 3.1 Basic `while` Loop

```python
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1     # IMPORTANT: update the variable or loop runs forever!

print("Done!")
```

**Output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
Done!
```

---

### 3.2 ⚠️ Infinite Loops

If the condition never becomes `False`, the loop runs forever — this is a bug!

```python
# DANGEROUS — don't run this
x = 1
while x > 0:
    print(x)
    # x is never changed → x > 0 is always True → infinite loop
```

Always make sure the loop variable is updated in a way that will eventually make the condition `False`.

If you accidentally run an infinite loop, press `Ctrl + C` to stop it.

---

### 3.3 Input Validation with `while`

A great use case for `while` — keep asking until the user gives valid input:

```python
while True:
    age = int(input("Enter your age (1–120): "))
    if 1 <= age <= 120:
        break   # valid input: exit the loop
    print("Invalid age. Try again.")

print(f"Your age is {age}.")
```

---

### 3.4 Countdown Timer Pattern

```python
import time   # standard library (Lesson 15 covers this in detail)

seconds = int(input("Start countdown from: "))

while seconds > 0:
    print(f"⏱  {seconds}...")
    time.sleep(1)   # pause for 1 second
    seconds -= 1

print("🚀 Lift off!")
```

---

### 3.5 `for` vs `while` — When to Use Which

| Use `for` when...                       | Use `while` when...                        |
|-----------------------------------------|--------------------------------------------|
| You know how many iterations you need   | You don't know how many iterations         |
| Iterating over a sequence               | Waiting for an event (user input, sensor)  |
| Working with `range()`                  | Retrying until success                     |

---

## Part 4 — `break`, `continue`, and Loop `else` (30 min)

### 4.1 `break` — Exit the Loop Immediately

```python
# Find the first even number
for n in range(1, 20):
    if n % 2 == 0:
        print(f"First even number: {n}")
        break   # stop the loop; no point checking further
```

```python
# Security: 3 login attempts
MAX_ATTEMPTS = 3
password = "secret123"

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = input(f"Attempt {attempt}/{MAX_ATTEMPTS} — Enter password: ")
    if guess == password:
        print("✅ Access granted!")
        break
    else:
        print("❌ Wrong password.")
else:
    # This runs only if the loop completed WITHOUT hitting break
    print("🔒 Account locked.")
```

---

### 4.2 `continue` — Skip This Iteration, Move to the Next

```python
# Print only odd numbers from 1 to 10
for n in range(1, 11):
    if n % 2 == 0:
        continue    # skip even numbers
    print(n, end=" ")
# Output: 1 3 5 7 9
```

```python
# Process only valid scores
raw_scores = [85, -5, 92, 101, 78, 60]

for score in raw_scores:
    if score < 0 or score > 100:
        print(f"Skipping invalid score: {score}")
        continue
    print(f"Processing score: {score}")
```

---

### 4.3 Loop `else` Clause

The `else` block on a loop runs **only if the loop completed normally** (no `break`).

```python
# Search for a target value
numbers = [4, 7, 2, 9, 1, 13]
target  = 5

for n in numbers:
    if n == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was not found in the list.")
# Output: 5 was not found in the list.
```

---

## Part 5 — Common Loop Patterns (15 min)

These patterns appear constantly in real-world code.

### 5.1 Accumulator — Summing Values

```python
total = 0

for i in range(1, 101):   # sum 1 to 100
    total += i

print(f"Sum: {total}")    # Sum: 5050
```

### 5.2 Counter — Counting Occurrences

```python
text  = "Programming is fun and programming is powerful"
word  = "programming"
count = 0

for w in text.lower().split():
    if w == word:
        count += 1

print(f"'{word}' appears {count} time(s).")   # 2 times
```

### 5.3 Maximum and Minimum

```python
numbers  = [14, 8, 37, 3, 91, 22, 56]
max_val  = numbers[0]
min_val  = numbers[0]

for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print(f"Max: {max_val}")   # 91
print(f"Min: {min_val}")   # 3
```

### 5.4 Building a String

```python
# Create a row of stars
width = 20
row   = ""

for _ in range(width):   # _ is a convention for "I don't use this variable"
    row += "*"

print(row)   # ********************
```

---

## Part 6 — Mini-Projects (15 min)

### Project 1: Number Guessing Game (sneak peek at Lesson 10!)

```python
import random

secret  = random.randint(1, 100)
guesses = 0
MAX     = 7

print("=== NUMBER GUESSING GAME ===")
print(f"I'm thinking of a number between 1 and 100.")
print(f"You have {MAX} attempts.\n")

while guesses < MAX:
    guess   = int(input(f"Attempt {guesses + 1}/{MAX} — Your guess: "))
    guesses += 1

    if guess < secret:
        print("📈 Too low!\n")
    elif guess > secret:
        print("📉 Too high!\n")
    else:
        print(f"🎉 Correct! You got it in {guesses} attempt(s)!")
        break
else:
    print(f"😞 Game over! The number was {secret}.")
```

### Project 2: Times Table Generator

```python
n = int(input("Generate times table for: "))

print(f"\n  TIMES TABLE FOR {n}")
print("-" * 25)

for i in range(1, 13):
    print(f"  {n:2} × {i:2} = {n * i:4}")
```

---

## ✅ Exercises

**Exercise 1 — FizzBuzz**
Print numbers from 1 to 50. But:
- For multiples of 3, print `"Fizz"` instead
- For multiples of 5, print `"Buzz"` instead
- For multiples of both 3 and 5, print `"FizzBuzz"`

**Exercise 2 — Sum of digits**
Ask the user for a number (e.g. `1234`).
Convert it to a string, loop over each character, convert back to `int`, and sum all digits.
Expected: `1+2+3+4 = 10`

**Exercise 3 — Password generator preview**
Print all even numbers between 1 and 100 whose square root is also a whole number.
*(Hint: `n ** 0.5 % 1 == 0` checks for perfect squares)*

**Exercise 4 — ATM Simulation**
Start with a balance of R$1000.  
In a `while True` loop, show a menu:
```
1. Check balance
2. Deposit
3. Withdraw
4. Exit
```
Use `break` to exit on option 4. Prevent withdrawals greater than the current balance.

---

## 🔑 Key Takeaways

- `for` iterates over a sequence (string, list, range). Use it when you know the count.
- `while` repeats while a condition is `True`. Use it when you don't know the count.
- `range(start, stop, step)` generates integer sequences; `stop` is excluded.
- `break` exits a loop immediately; `continue` skips to the next iteration.
- The `else` block on a loop runs only when no `break` was hit.
- Classic patterns: accumulator (`total += n`), counter, max/min finder, string builder.

---

## 📚 Further Reading

- [Python Docs — `for` Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Docs — `range()`](https://docs.python.org/3/library/stdtypes.html#ranges)
- [Real Python — Python `while` Loops](https://realpython.com/python-while-loop/)

---

*Next lesson → **Lesson 09: Functions I — Basics**  
Previous lesson → **Lesson 07: Conditional Logic***
