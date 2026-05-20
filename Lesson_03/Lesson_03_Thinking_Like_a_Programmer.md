# Lesson 03 — Thinking Like a Programmer

> **Phase 1 — Foundations | Duration: 2 hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Apply decomposition and abstraction to break real-world problems into solvable software components
- Recognize common beginner traps and structural anti-patterns in code design
- Read and interpret stack traces and error messages with precision
- Approach debugging as a disciplined, reproducible process
- Critically evaluate your own code for correctness and maintainability

---

## 1. The Mental Models That Define Good Developers

There is a persistent myth that great programmers write perfect code fast. In reality, experienced developers spend a significant portion of their time **thinking, designing, and debugging** — not typing.

The mental shifts that define intermediate-to-advanced programmers:

| Beginner Mindset                    | Intermediate Mindset                                     |
| ----------------------------------- | -------------------------------------------------------- |
| "Does it run?"                      | "Does it run correctly under all conditions?"            |
| "I'll fix the structure later"      | "Poor structure now creates exponential technical debt"  |
| "The error message doesn't help"    | "The error message tells me almost exactly what's wrong" |
| "I'll add features until it works"  | "I'll remove complexity until I find the bug"            |
| "I copied this from Stack Overflow" | "I understand this code and can defend every line"       |

The goal of this lesson is to accelerate that mental shift.

---

## 2. Decomposition — Turning Complexity into Manageability

### The Single Responsibility Principle (SRP)

Every function, module, and class should do **one thing**. This isn't just a stylistic preference — it's a practical tool for managing complexity.

**Violation of SRP:**

```python
# This function does too many things
def process_user_registration(username, email, password):
    # Validation
    if len(username) < 3:
        print("Username too short")
        return False
    if "@" not in email:
        print("Invalid email")
        return False
    if len(password) < 8:
        print("Password too short")
        return False

    # Hashing
    import hashlib
    hashed = hashlib.sha256(password.encode()).hexdigest()

    # Database insertion
    db.execute("INSERT INTO users VALUES (?, ?, ?)", username, email, hashed)

    # Send confirmation email
    send_email(email, "Welcome!", "Thanks for signing up.")

    print("Registration successful")
    return True
```

This function is impossible to test in isolation, hard to reuse, and fragile — a change in email sending logic forces you to touch registration logic.

**Decomposed version:**

```python
def validate_username(username: str) -> tuple[bool, str]:
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    if not username.isalnum():
        return False, "Username must contain only letters and numbers"
    return True, ""

def validate_email(email: str) -> tuple[bool, str]:
    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "Invalid email format"
    return True, ""

def hash_password(password: str) -> str:
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username: str, email: str, hashed_password: str) -> bool:
    return db.execute("INSERT INTO users VALUES (?, ?, ?)", username, email, hashed_password)

def register_user(username: str, email: str, password: str) -> dict:
    valid, error = validate_username(username)
    if not valid:
        return {"success": False, "error": error}

    valid, error = validate_email(email)
    if not valid:
        return {"success": False, "error": error}

    hashed = hash_password(password)
    saved = save_user(username, email, hashed)

    if saved:
        send_confirmation_email(email)
        return {"success": True}

    return {"success": False, "error": "Database error"}
```

Now each function can be tested, replaced, and reasoned about independently.

### Abstraction Layers

Good software has clearly defined layers where each layer only communicates with adjacent layers:

```
User Interface Layer         ← User sees this
      ↓ ↑
Application Logic Layer      ← Business rules live here
      ↓ ↑
Data Access Layer            ← Queries, reads, writes
      ↓ ↑
Database / Storage           ← Raw data lives here
```

Violating this — e.g., writing SQL directly in a UI event handler — creates code that's nearly impossible to maintain or test.

---

## 3. Pattern Recognition — Seeing the Shape of Problems

### Common Patterns and Their Solutions

Recognizing that a problem fits a known pattern is the fastest path to a solution:

| Problem Shape                         | Pattern                 | Approach                                |
| ------------------------------------- | ----------------------- | --------------------------------------- |
| "Find all X that meet condition Y"    | Filter                  | Loop + condition, or list comprehension |
| "Transform each item"                 | Map                     | Apply function to each element          |
| "Combine all items into one value"    | Reduce                  | Accumulate (sum, join, merge)           |
| "Do something after a delay or event" | Callback / event-driven | Functions as arguments                  |
| "Avoid duplicate work"                | Caching / Memoization   | Store computed results                  |
| "Process items as they arrive"        | Stream / Iterator       | Generator functions                     |
| "Coordinate multiple operations"      | Pipeline                | Chained functions                       |

### The DRY Principle in Practice

**Don't Repeat Yourself** is more than avoiding copy-paste. If you find yourself writing similar logic in two places, ask: what is the generalized version of this?

**Before DRY:**

```python
# Calculating discount for different user types
if user_type == "student":
    price = base_price * 0.80
    print(f"Student discount applied: {price}")

if user_type == "senior":
    price = base_price * 0.85
    print(f"Senior discount applied: {price}")

if user_type == "employee":
    price = base_price * 0.70
    print(f"Employee discount applied: {price}")
```

**After DRY — data-driven design:**

```python
DISCOUNT_RATES = {
    "student":  0.80,
    "senior":   0.85,
    "employee": 0.70,
    "standard": 1.00,
}

def apply_discount(base_price: float, user_type: str) -> float:
    rate = DISCOUNT_RATES.get(user_type, 1.00)  # default: no discount
    price = base_price * rate
    print(f"{user_type.capitalize()} discount applied: {price:.2f}")
    return price
```

Now adding a new user type requires changing **one line** (in the dictionary), not writing new conditional logic.

---

## 4. Common Beginner Mistakes — Intermediate-Level Analysis

These aren't just syntax mistakes — they're structural and conceptual errors that persist into intermediate code.

### Mistake 1: Mutating Data You Don't Own

```python
# PROBLEM: modifying a list passed in as an argument
def remove_negatives(numbers):
    for i, n in enumerate(numbers):
        if n < 0:
            numbers.pop(i)   # Mutating while iterating — skips elements
    return numbers

data = [1, -2, -3, 4, -5]
result = remove_negatives(data)
print(data)    # data is also changed! Caller didn't expect this.
```

**Fix:** Return new data; don't mutate inputs unless explicitly documented.

```python
def remove_negatives(numbers):
    return [n for n in numbers if n >= 0]
```

### Mistake 2: Handling Only the Happy Path

```python
# Only works if the file exists and is valid JSON
import json

def load_config(filepath):
    with open(filepath) as f:
        return json.load(f)

config = load_config("settings.json")  # crashes if file missing or malformed
```

**Fix:** Think through failure modes explicitly.

```python
def load_config(filepath: str) -> dict:
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found. Using defaults.")
        return {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {e}")
```

### Mistake 3: Magic Numbers and Strings

```python
# What does 86400 mean? Why 3?
if elapsed_time > 86400:
    retry_count += 1
    if retry_count > 3:
        status = "FAILED"
```

**Fix:** Name your constants.

```python
SECONDS_IN_A_DAY = 86_400
MAX_RETRY_ATTEMPTS = 3
STATUS_FAILED = "FAILED"

if elapsed_time > SECONDS_IN_A_DAY:
    retry_count += 1
    if retry_count > MAX_RETRY_ATTEMPTS:
        status = STATUS_FAILED
```

### Mistake 4: Premature Optimization

Writing complex, clever code to optimize performance before establishing that:

1. The code is correct
2. Performance is actually a problem
3. This specific part is the bottleneck

> "Premature optimization is the root of all evil." — Donald Knuth

Write clear, correct code first. Measure. Then optimize the bottleneck.

```python
def whatIdo(numbers):
    result = []
    append = result.append

    for i in range(len(numbers)):
        if not (numbers[i] & 1):
            append(numbers[i])

    return result
```

<details>
<summary>Simple Ver</summary>

```python
def whatIdoV2(numbers):
    return [n for n in numbers if n % 2 == 0]
```

</details>

### Mistake 5: Global Mutable State

```python
# PROBLEMATIC: global state makes behavior unpredictable
current_user = None
auth_token = None

def login(username, password):
    global current_user, auth_token
    # ... validation ...
    current_user = username
    auth_token = generate_token()

def get_profile():
    # depends on invisible global state — hard to test
    return db.get_user(current_user)
```

Pass state explicitly. Prefer return values and parameters over global variables.

---

## 5. Reading Error Messages — A Systematic Approach

Most developers lose significant time because they don't read error messages carefully. An error message contains:

1. **Exception type** — what category of error occurred
2. **Message** — human-readable description
3. **Stack trace** — the call chain leading to the error

### Anatomy of a Python Stack Trace

```
Traceback (most recent call last):             ← Read bottom-up
  File "app.py", line 42, in process_order     ← Outer function call
    result = calculate_total(items)
  File "app.py", line 17, in calculate_total   ← Inner function call
    return sum(item["price"] for item in items)
  File "app.py", line 17, in <genexpr>         ← Exact failing line
    return sum(item["price"] for item in items)
KeyError: 'price'                               ← Exception type + message
```

**Reading process:**

1. Jump to the **bottom** — that's the actual error
2. `KeyError: 'price'` → a dictionary doesn't have the key `"price"`
3. The failing line: `item["price"]` — one of your items lacks a `"price"` key
4. Look up the stack to understand **how you got there**

**Common Python Exceptions and What They Mean:**

| Exception        | Meaning                                   | Common Cause                                         |
| ---------------- | ----------------------------------------- | ---------------------------------------------------- |
| `KeyError`       | Dictionary key doesn't exist              | Assuming a key is always present                     |
| `AttributeError` | Object doesn't have that attribute/method | Wrong type, or `None` instead of an object           |
| `TypeError`      | Wrong type for the operation              | Mixing strings and numbers, wrong function arguments |
| `IndexError`     | List index out of range                   | Off-by-one errors, empty list access                 |
| `ValueError`     | Right type, wrong value                   | `int("abc")`, invalid enum value                     |
| `ImportError`    | Module not found                          | Missing installation, wrong name                     |
| `RecursionError` | Stack overflow from infinite recursion    | Missing base case in recursive function              |

---

## 6. The Debugging Methodology

Debugging is empirical. Follow the scientific method:

### The Six-Step Process

**Step 1 — Reproduce reliably**
A bug you can't reproduce consistently is the hardest kind. Before anything else, create a minimal, reproducible test case. Can you trigger it with specific inputs?

**Step 2 — Understand what "correct" looks like**
What _should_ happen? If you can't state the expected behavior precisely, you can't know when it's fixed.

**Step 3 — Isolate the location**
Use binary search on your codebase:

- Does the bug occur in the first half of the code or the second half?
- Add a checkpoint in the middle. Narrow down further.

**Step 4 — Examine state**
At the bug location, what is the actual value of every relevant variable? Use print statements, a debugger, or logging.

```python
# Temporary diagnostic output
print(f"DEBUG: items={items}, type={type(items)}")
print(f"DEBUG: current user={current_user!r}")
```

**Step 5 — Form and test a hypothesis**
State your theory explicitly: _"I think the bug is that `items` is sometimes `None` because the API call fails silently."_ Then test it. Don't fix code until you've confirmed the cause.

**Step 6 — Fix, verify, and clean up**
Apply the minimal fix that addresses the root cause. Verify the bug is gone. Remove all diagnostic output. Consider adding a test to prevent regression.

### Using a Debugger

Python's built-in debugger (`pdb`) lets you pause execution and inspect state interactively:

```python
import pdb

def calculate_total(items):
    pdb.set_trace()    # Execution pauses here
    return sum(item["price"] for item in items)
```

At the `(Pdb)` prompt:

- `n` — next line
- `s` — step into function call
- `p variable` — print variable value
- `l` — show surrounding code
- `q` — quit debugger

Modern IDEs (VS Code, PyCharm) provide visual debuggers with breakpoints — learn to use them early.

---

## 7. Code Readability — Writing for Humans

Code is read far more often than it is written. Optimize for the reader.

### Naming as Documentation

```python
# Cryptic:
def calc(x, y, z):
    return x * (1 - y) * (1 + z)

# Self-documenting:
def calculate_final_price(base_price: float, discount_rate: float, tax_rate: float) -> float:
    return base_price * (1 - discount_rate) * (1 + tax_rate)
```

### Comment the Why, Not the What

```python
# BAD: states the obvious
x = x + 1  # increment x by 1

# GOOD: explains non-obvious reasoning
retry_count += 1  # include initial attempt in count to match SLA reporting format
```

### Function Length

If a function doesn't fit on one screen, it's a signal to decompose further. A function that does one thing is naturally short.

---

## Summary

- The intermediate mindset prioritizes correctness, structure, and maintainability over just making code run
- Decomposition via SRP prevents the accumulation of "God functions" that do everything
- Pattern recognition (filter, map, reduce, pipeline) speeds up problem solving
- Common mistakes — mutation of inputs, ignoring failure paths, magic numbers — are structural problems, not syntax errors
- Stack traces tell you exactly what failed; read them bottom-up
- Debugging is a scientific process: reproduce → isolate → hypothesize → test → fix → verify
- Write code for the human reader first; machines don't care about clarity, but your teammates and future self do

---

## Further Exploration

- [**"Clean Code" by Robert C. Martin** — canonical text on readable, maintainable code](https://github.com/zedr/clean-code-python)
- **"The Pragmatic Programmer" by Hunt & Thomas** — mindset and methodology for software development
- Python's `pdb` documentation: `python -m pdb your_script.py`
- Try: Take a piece of code you wrote previously and refactor it applying SRP — count how many individual functions you end up with

---

_Next: Lesson 04 — Using AI as a Developer_
