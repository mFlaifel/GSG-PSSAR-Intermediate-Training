# Lesson 08 — Loops: `for` & `while`

**Phase 2 — Python Core | Duration: 2 Hours**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Write `for` loops to iterate over sequences and ranges
- Write `while` loops for conditional repetition
- Use `range()` to generate sequences of numbers
- Control loop flow with `break` and `continue`
- Apply common loop patterns: counting, summing, searching

---

## Part 1 — The `for` Loop (30 min)

### 1.1 Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 1.2 Using `range()`

```python
# Numbers 0 through 4
for i in range(5):
    print(i)

# Numbers 2 through 6
for i in range(2, 7):
    print(i)

# Steps (2, 4, 6, 8)
for i in range(2, 10, 2):
    print(i)
```

### 1.3 Iterating Over a String

```python
for char in "Python":
    print(char)
```

---

## Part 2 — The `while` Loop (25 min)

### 2.1 Basic While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 2.2 Input Validation Loop

```python
password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted!")
```

---

## Part 3 — Loop Control (20 min)

### 3.1 `break` — Exit the Loop

```python
for i in range(10):
    if i == 5:
        break
    print(i)          # Prints 0, 1, 2, 3, 4
```

### 3.2 `continue` — Skip to Next Iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)          # Prints 1, 3, 5, 7, 9
```

---

## Part 4 — Common Loop Patterns (25 min)

### 4.1 Counting

```python
count = 0
for char in "hello world":
    if char == "l":
        count += 1
print(f"Letter 'l' appears {count} times")
```

### 4.2 Summing

```python
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")
```

### 4.3 Searching

```python
names = ["Ali", "Sara", "Mohamed", "Nora"]
search = "Sara"
found = False
for name in names:
    if name == search:
        found = True
        break
print(f"Found {search}: {found}")
```

---

## Part 5 — Nested Loops (10 min)

```python
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()
```

---

## Part 6 — Practice Exercises (10 min)

1. Print all even numbers from 1 to 20 using a `for` loop.
2. Ask the user for numbers until they type `-1`, then print the sum.
3. Print a multiplication table (1 to 5) using nested loops.
4. Count how many vowels are in a user-provided sentence.

---

## Summary

- `for` loops iterate over sequences and `range()`
- `while` loops run while a condition is `True`
- `break` exits the loop immediately
- `continue` skips to the next iteration
- `range(start, stop, step)` generates number sequences
- Nested loops place one loop inside another
