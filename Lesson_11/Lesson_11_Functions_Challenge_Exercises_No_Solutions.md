# Lesson 11 - Functions Challenge Exercises

These exercises reinforce the learning outcomes from:

- Lesson 09: function basics, parameters, return values, defaults, built-ins, DRY, clean names
- Lesson 11: scope, LEGB, pure functions, `*args`, `**kwargs`, mutable defaults, docstrings, type hints

Try each challenge before running the code or checking with your instructor. The goal is not only to get the answer, but to explain why the answer happens.

---

## Challenge 1 - Return Value Detective

Before running the code, predict the full output.

```python
def add_and_print(a, b):
    result = a + b
    print(result)


def add_and_return(a, b):
    return a + b


x = add_and_print(2, 3)
y = add_and_return(2, 3)

print("x:", x)
print("y:", y)
print(add_and_return(4, 1) * 2)
```

Questions:

1. What does the program print?
2. Which function gives back a value that can be reused?
3. Why is `x` not equal to `5`?


---

## Challenge 2 - Function Name Clinic

The code works, but the function design is weak.

```python
def calc(x, y):
    print(x * y)


def Data(a):
    return len(a)


def valid(email):
    return "@" in email
```

Improve the code by:

- Using clear `snake_case` function names
- Choosing names that describe actions
- Returning values instead of printing when the result may be reused
- Adding short docstrings
- Adding type hints


---

## Challenge 3 - DRY Repair: Ticket Booth

This code repeats the same logic three times.

```python
ticket_price = 12

name1 = "Lina"
tickets1 = 2
total1 = tickets1 * ticket_price
if tickets1 >= 5:
    total1 = total1 * 0.8
print(f"{name1} pays ${total1}")

name2 = "Omar"
tickets2 = 5
total2 = tickets2 * ticket_price
if tickets2 >= 5:
    total2 = total2 * 0.8
print(f"{name2} pays ${total2}")

name3 = "Nour"
tickets3 = 8
total3 = tickets3 * ticket_price
if tickets3 >= 5:
    total3 = total3 * 0.8
print(f"{name3} pays ${total3}")
```

Refactor it into functions.

Requirements:

- `calculate_ticket_total(ticket_count, ticket_price=12)` returns the final total.
- Groups buying 5 or more tickets get a 20% discount.
- `format_ticket_order(name, ticket_count)` returns a friendly string.
- Avoid repeating the calculation logic.


---

## Challenge 4 - Scope Detective: LEGB

Predict the output before running the code.

```python
status = "global"


def outer():
    status = "enclosing"

    def inner():
        status = "local"
        print("inner:", status)

    inner()
    print("outer:", status)


outer()
print("global:", status)
```

Questions:

1. What gets printed?
2. Which scope is used inside `inner()`?
3. Does the global `status` ever change?


---

## Challenge 5 - Clean Up the Global State

This code works, but it depends on global state.

```python
energy = 10


def spend_energy(amount):
    global energy
    energy = energy - amount
    print(f"Energy left: {energy}")


spend_energy(3)
spend_energy(4)
```

Refactor it so that:

- The function does not use `global`.
- The function returns the new energy value.
- Printing happens outside the calculation function.
- The same function can be tested with any starting energy.


---

## Challenge 6 - Flexible Scores with `*args`

Write a function called `summarize_scores(player_name, *scores)`.

The function should:

- Accept any number of scores
- Return `"No scores for NAME yet."` when no scores are given
- Return a string with the player's best score, average score, and number of attempts
- Use built-in functions where helpful
- Return a string instead of printing

Example calls:

```python
print(summarize_scores("Mona", 90, 80, 100))
print(summarize_scores("Kareem"))
```

Expected output:

```text
Mona: best=100, average=90.0, attempts=3
No scores for Kareem yet.
```


---

## Challenge 7 - Flexible Profiles with `**kwargs`

Write a function called `build_badge(name, **details)`.

The function should:

- Return a dictionary
- Always include the person's `name`
- Include any extra named details passed to the function
- Not depend on global variables

Example:

```python
badge = build_badge(
    "Rana",
    track="Python",
    city="Gaza",
    laptop=True,
    level="intermediate"
)

print(badge)
```

Expected output:

```python
{'name': 'Rana', 'track': 'Python', 'city': 'Gaza', 'laptop': True, 'level': 'intermediate'}
```


---

## Challenge 8 - Mutable Default Trap

Predict the output before running the code.

```python
def add_task(task, tasks=[]):
    tasks.append(task)
    return tasks


print(add_task("read"))
print(add_task("practice"))
print(add_task("submit", []))
print(add_task("review"))
```

Questions:

1. What does this print?
2. Why is the result surprising?
3. Rewrite the function correctly.


---

## Challenge 9 - Built-in Function Upgrade

This function manually does work that Python built-ins can already do.

```python
def analyze_numbers(numbers):
    total = 0
    highest = numbers[0]
    lowest = numbers[0]

    for number in numbers:
        total = total + number

        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

    average = total / len(numbers)

    print(f"Average: {average}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
```

Improve it so that:

- It uses built-in functions.
- It returns data instead of printing.
- It handles an empty list safely.
- It has a docstring and type hints.


---

## Challenge 10 - Mini Project: Checkout Function Lab

Build a small checkout system using clean functions.

Starter data:

```python
cart = [
    {"name": "Notebook", "price": 4.50, "quantity": 3},
    {"name": "Pen", "price": 1.25, "quantity": 5},
    {"name": "Backpack", "price": 35.00, "quantity": 1},
]
```

Create these functions:

1. `item_subtotal(item)` returns one item's subtotal.
2. `cart_total(cart)` returns the full cart total.
3. `apply_discount(total, percent=0)` returns the discounted total.
4. `add_tax(total, tax_percent=0)` returns the total after tax.
5. `format_receipt(cart, discount_percent=0, tax_percent=0, **store_info)` returns a receipt string.

Requirements:

- Calculation functions should be pure.
- Use parameters instead of hidden global state.
- Use at least one default argument.
- Use `**kwargs` for optional store information.
- Add docstrings and type hints.


---

## Bonus - Explain Your Design

Pick one function from your solution and answer:

1. What data enters through parameters?
2. What data leaves through `return`?
3. Does the function print or change outside state?
4. Is it easy to test with one line of code?
