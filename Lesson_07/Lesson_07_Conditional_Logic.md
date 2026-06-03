# Lesson 07 — Conditional Logic (`if / elif / else`)

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Learning Objectives

By the end of this lesson you will be able to:

- Use `if`, `elif`, and `else` to control the flow of a program
- Write and read nested conditions
- Understand truthiness and how Python evaluates any value as a boolean
- Build real-world programs: a grade calculator and a login system
- Apply best practices to keep conditions clean and readable

---

## Part 1 — Making Decisions in Code (20 min)

Every meaningful program needs to make decisions. In plain English you might say:

> *"If the temperature is above 30°C, wear light clothes; otherwise, bring a jacket."*

Python expresses this logic with the `if` statement.

### 1.1 The Basic `if` Statement

```
if <condition>:
    <code to run when condition is True>
```

- The condition must evaluate to `True` or `False`.
- The body is **indented** by 4 spaces (or 1 tab). **Indentation is mandatory in Python** — it's how Python knows which lines belong inside the `if`.

```python
temperature = 35

if temperature > 30:
    print("It's hot today!")
    print("Don't forget sunscreen.")

print("Have a great day!")   # This always runs
```

**Output:**
```
It's hot today!
Don't forget sunscreen.
Have a great day!
```

Now change `temperature = 20` — only the last line prints.

> ⚠️ **The most common beginner error:** forgetting the colon `:` at the end of the `if` line.

---

### 1.2 Adding an `else` Clause

`else` handles the case when the condition is `False`.

```python
age = 16

if age >= 18:
    print("You may enter.")
else:
    print("Sorry, you must be 18 or older.")
```

**Structure:**
```
if <condition>:
    <runs when True>
else:
    <runs when False>
```

Only one of the two blocks will ever execute per run.

---

### 1.3 Multiple Branches with `elif`

`elif` (short for "else if") lets you test several conditions in sequence.  
Python checks them **from top to bottom** and runs the **first** one that is `True`.  
The `else` block catches anything that didn't match.

```python
score = 72

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")   # Your grade is: C
```

**The flow:**
1. Is `72 >= 90`? No → move on
2. Is `72 >= 80`? No → move on
3. Is `72 >= 70`? **Yes** → set grade to "C" and stop

---

### 1.4 You Can Have as Many `elif` Blocks as You Need

```python
day_number = int(input("Enter a day number (1–7): "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid number. Please enter 1–7.")
```

---

## Part 2 — Nested Conditions (25 min)

You can place an `if` statement **inside** another `if` statement. This is called **nesting**.

### 2.1 Basic Nesting

```python
age     = 20
has_id  = True

if age >= 18:
    if has_id:
        print("Welcome! You may enter.")
    else:
        print("You are old enough, but we need to see your ID.")
else:
    print("Sorry, you must be 18 or older.")
```

### 2.2 Combining Conditions vs. Nesting

Many nested conditions can be **flattened** using `and`, `or`, making the code easier to read.

```python
# Nested version — harder to read
if age >= 18:
    if has_id:
        print("Welcome!")

# Flat version — cleaner
if age >= 18 and has_id:
    print("Welcome!")
```

> 💡 **Rule of thumb:** Try to avoid nesting deeper than 2 levels. If your indentation goes very deep, consider restructuring with combined conditions or functions (which you'll learn in Lesson 09).

---

### 2.3 Real-World Example: Ticket Pricing System

```python
# ticket_price.py

age         = int(input("Enter your age: "))
is_student  = input("Are you a student? (yes/no): ").lower() == "yes"
is_weekend  = input("Is it a weekend? (yes/no): ").lower() == "yes"

base_price = 50.0

if age < 5:
    price = 0
    category = "Infant (free)"
elif age < 12:
    price = base_price * 0.50
    category = "Child (50% off)"
elif age >= 65:
    price = base_price * 0.40
    category = "Senior (60% off)"
elif is_student:
    price = base_price * 0.70
    category = "Student (30% off)"
else:
    price = base_price
    category = "Adult (full price)"

if is_weekend:
    price += 10
    print(f"\nWeekend surcharge applied: +R$10.00")

print(f"\nCategory : {category}")
print(f"Price    : R${price:.2f}")
```

---

## Part 3 — Truthiness Deep Dive (20 min)

As introduced in Lesson 06, Python evaluates many types of values as booleans. Understanding this lets you write much cleaner conditions.

### 3.1 Falsy vs. Truthy Values

**Falsy (evaluate to `False`):**

| Value       | Type    |
|-------------|---------|
| `0`         | `int`   |
| `0.0`       | `float` |
| `""`        | `str`   |
| `None`      | NoneType|
| `[]`        | list    |
| `{}`        | dict    |

**Truthy:** Everything else.

```python
# You can use these directly in an if condition
name = ""

if name:
    print(f"Hello, {name}!")
else:
    print("No name was entered.")   # ← This runs because "" is falsy
```

```python
username = "admin"

if username:   # equivalent to: if username != ""
    print("Username is set:", username)
```

---

### 3.2 `is` vs `==`

- `==` checks if two values are **equal**
- `is` checks if two variables point to the **exact same object in memory**

```python
x = None

if x is None:       # preferred way to check for None
    print("x has no value")

if x == None:       # works but not recommended
    print("x has no value")
```

> 💡 Always use `is None` (not `== None`) when checking for `None`.

---

### 3.3 `in` Operator

Checks if a value exists inside a collection (string, list, etc.).

```python
valid_roles = ["admin", "editor", "viewer"]
user_role   = "admin"

if user_role in valid_roles:
    print("Access granted")
else:
    print("Unknown role")

# Works with strings too
email = "user@example.com"
if "@" in email and "." in email:
    print("Looks like a valid email")
```

---

## Part 4 — Real-World Projects (30 min)

### Project 1: Grade Calculator

```python
# grade_calculator.py

print("=== GRADE CALCULATOR ===\n")

name     = input("Student name: ")
subject  = input("Subject: ")
score    = float(input(f"Score for {subject} (0–100): "))

# Determine grade and feedback
if score < 0 or score > 100:
    print("Error: score must be between 0 and 100.")
elif score >= 90:
    grade    = "A"
    feedback = "Excellent! Outstanding work."
    passed   = True
elif score >= 80:
    grade    = "B"
    feedback = "Great job! Above average."
    passed   = True
elif score >= 70:
    grade    = "C"
    feedback = "Good. Room for improvement."
    passed   = True
elif score >= 60:
    grade    = "D"
    feedback = "Passed, but needs significant improvement."
    passed   = True
else:
    grade    = "F"
    feedback = "Failed. Please seek extra help."
    passed   = False

# Display result
status = "PASSED ✓" if passed else "FAILED ✗"

print(
    f"""
===================================
  Student : {name}
  Subject : {subject}
  Score   : {score:.1f} / 100
  Grade   : {grade}
  Status  : {status}
-----------------------------------
  {feedback}
===================================
"""
)
```

---

### Project 2: Shipping Cost Calculator

A real e-commerce decision tree — multiple branching conditions that mirror exactly what a conditional logic system is built for.

```python
# shipping_calculator.py

print("=== SHIPPING COST CALCULATOR ===\n")

weight_kg    = float(input("Package weight (kg): "))
distance_km  = int(input("Delivery distance (km): "))
is_fragile   = input("Fragile item? (yes/no): ").lower() == "yes"
is_express   = input("Express delivery? (yes/no): ").lower() == "yes"

# --- Base rate by weight ---
if weight_kg <= 1:
    base_rate = 10.0
    weight_category = "Light (up to 1 kg)"
elif weight_kg <= 5:
    base_rate = 20.0
    weight_category = "Medium (1–5 kg)"
elif weight_kg <= 20:
    base_rate = 40.0
    weight_category = "Heavy (5–20 kg)"
else:
    base_rate = 80.0
    weight_category = "Oversized (20+ kg)"

# --- Distance multiplier ---
if distance_km <= 50:
    multiplier = 1.0
    zone = "Local"
elif distance_km <= 300:
    multiplier = 1.5
    zone = "Regional"
else:
    multiplier = 2.5
    zone = "National"

# --- Add-ons ---
fragile_fee = 15.0 if is_fragile else 0.0
express_fee = base_rate * 0.8 if is_express else 0.0

# --- Total ---
total = (base_rate * multiplier) + fragile_fee + express_fee

# --- Display receipt ---
print()
print("=" * 40)
print("        SHIPPING QUOTE")
print("=" * 40)
print(f"  Package  : {weight_category}")
print(f"  Zone     : {zone} ({distance_km} km)")
print(f"  Base     : R${base_rate * multiplier:.2f}")
if is_fragile:
    print(f"  Fragile  : R${fragile_fee:.2f}")
if is_express:
    print(f"  Express  : R${express_fee:.2f}")
print("-" * 40)
print(f"  TOTAL    : R${total:.2f}")
print("=" * 40)

if total > 150:
    print("\n  ⚠️  High shipping cost — consider splitting the order.")
```

> 📝 **Note:** Notice each decision (weight, zone, add-ons) is a separate `if/elif/else` block. This separation of concerns is the **Single Responsibility Principle** you studied in Lesson 03 — applied directly to conditional logic.

---

## Part 5 — Ternary / Inline Conditionals (10 min)

Python has a compact one-liner form for simple if/else conditions.

**Syntax:**
```python
value_if_true if condition else value_if_false
```

```python
age    = 20
status = "adult" if age >= 18 else "minor"
print(status)    # adult

score  = 85
label  = "Pass" if score >= 60 else "Fail"
print(label)     # Pass
```

This is great for simple assignments. For complex logic, always use the full `if/elif/else` form.

---

## ✅ Exercises

**Exercise 1 — Season Detector**
Ask the user for a month number (1–12) and print the season:
- Dec, Jan, Feb → Summer (Southern Hemisphere)
- Mar, Apr, May → Autumn
- Jun, Jul, Aug → Winter
- Sep, Oct, Nov → Spring
- Other → Invalid

**Exercise 2 — BMI Calculator**
Ask for weight (kg) and height (m). Calculate BMI = weight / height².  
Print the BMI and the category:
- Below 18.5 → Underweight
- 18.5 – 24.9 → Normal
- 25.0 – 29.9 → Overweight
- 30.0 or above → Obese

**Exercise 3 — Electricity Bill**
Ask for kWh consumed. Apply the tiered rate:
- First 100 kWh: R$0.40/kWh
- Next 200 kWh (101–300): R$0.65/kWh
- Above 300 kWh: R$0.95/kWh
Print the bill total.

**Exercise 4 — Rock, Paper, Scissors (vs. Computer)**
Ask the player for their choice.  
Hard-code the computer's choice as `"rock"`.  
Print who wins. (Hint: use `and` / `or` in your conditions.)

---

## 🔑 Key Takeaways

- `if`, `elif`, and `else` control which code runs based on conditions.
- Python evaluates conditions **top to bottom** and stops at the first `True` branch.
- Indentation is not optional — it defines which code belongs to which block.
- Nested conditions work but should be kept shallow; `and`/`or` often flattens them.
- Truthiness means any value can act as a boolean; empty strings and `0` are falsy.
- The ternary operator (`x if cond else y`) is useful for simple one-liner assignments.

---

## 📚 Further Reading

- [Python Docs — More Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)

---

*Next lesson → **Lesson 08: Loops — `for` & `while`**  
Previous lesson → **Lesson 06: Operators & String Manipulation***
