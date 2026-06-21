# Lesson 11 - Functions Challenge Exercises

These exercises reinforce the learning outcomes from:

- Lesson 09: function basics, parameters, return values, defaults, built-ins, DRY, clean names
- Lesson 11: scope, LEGB, pure functions, `*args`, `**kwargs`, mutable defaults, docstrings, type hints

Try each challenge before opening the solution. The goal is not only to get the answer, but to explain why the answer happens.

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

<details>
<summary>Show solution</summary>

Output:

```text
5
x: None
y: 5
10
```

`add_and_print(2, 3)` prints `5`, but it does not return anything. In Python, a function with no `return` statement returns `None`, so `x` becomes `None`.

`add_and_return(2, 3)` returns `5`, so `y` becomes `5`. Returned values can be stored, printed, or used in another expression.

</details>

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

<details>
<summary>Show solution</summary>

One possible improvement:

```python
def calculate_rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def count_items(items: list) -> int:
    """Return the number of items in a list."""
    return len(items)


def is_valid_email(email: str) -> bool:
    """Return True if the email has a basic valid shape."""
    return "@" in email and "." in email
```

Why this is better:

- `calculate_rectangle_area` says what is being calculated.
- `count_items` says what is being counted.
- `is_valid_email` follows the common boolean naming style.
- Returning the area is more flexible than printing it.

</details>

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

<details>
<summary>Show solution</summary>

```python
def calculate_ticket_total(ticket_count: int, ticket_price: float = 12) -> float:
    """Return the final ticket total after any group discount."""
    total = ticket_count * ticket_price

    if ticket_count >= 5:
        total = total * 0.8

    return total


def format_ticket_order(name: str, ticket_count: int) -> str:
    """Return a formatted ticket order summary."""
    total = calculate_ticket_total(ticket_count)
    return f"{name} pays ${total:.2f}"


print(format_ticket_order("Lina", 2))
print(format_ticket_order("Omar", 5))
print(format_ticket_order("Nour", 8))
```

Output:

```text
Lina pays $24.00
Omar pays $48.00
Nour pays $76.80
```

The discount rule now lives in one place: `calculate_ticket_total`.

</details>

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

<details>
<summary>Show solution</summary>

Output:

```text
inner: local
outer: enclosing
global: global
```

Inside `inner()`, Python finds the closest `status`, which is the local variable inside `inner`.

Inside `outer()`, Python uses the `status` local to `outer`.

The global `status` is never changed. The local variables only shadow it.

</details>

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

<details>
<summary>Show solution</summary>

```python
def spend_energy(current_energy: int, amount: int) -> int:
    """Return the energy left after spending the given amount."""
    return current_energy - amount


energy = 10

energy = spend_energy(energy, 3)
print(f"Energy left: {energy}")

energy = spend_energy(energy, 4)
print(f"Energy left: {energy}")
```

Output:

```text
Energy left: 7
Energy left: 3
```

This version is easier to test:

```python
print(spend_energy(100, 25))  # 75
```

The function only depends on its inputs and returns a result.

</details>

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

<details>
<summary>Show solution</summary>

```python
def summarize_scores(player_name: str, *scores: int) -> str:
    """Return a summary for any number of player scores."""
    if len(scores) == 0:
        return f"No scores for {player_name} yet."

    best_score = max(scores)
    average_score = sum(scores) / len(scores)
    attempts = len(scores)

    return f"{player_name}: best={best_score}, average={average_score:.1f}, attempts={attempts}"


print(summarize_scores("Mona", 90, 80, 100))
print(summarize_scores("Kareem"))
```

`*scores` collects the extra positional arguments into a tuple.

</details>

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

<details>
<summary>Show solution</summary>

```python
def build_badge(name: str, **details) -> dict:
    """Return a badge dictionary with a name and optional details."""
    badge = {"name": name}

    for key, value in details.items():
        badge[key] = value

    return badge


badge = build_badge(
    "Rana",
    track="Python",
    city="Gaza",
    laptop=True,
    level="intermediate"
)

print(badge)
```

`**details` collects extra keyword arguments into a dictionary.

</details>

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

<details>
<summary>Show solution</summary>

Output:

```text
['read']
['read', 'practice']
['submit']
['read', 'practice', 'review']
```

The default list is created once when the function is defined, not each time the function is called. The calls without a custom list share the same default list.

Correct version:

```python
def add_task(task: str, tasks: list | None = None) -> list:
    """Return a task list with the new task added."""
    if tasks is None:
        tasks = []

    tasks.append(task)
    return tasks


print(add_task("read"))
print(add_task("practice"))
print(add_task("submit", []))
print(add_task("review"))
```

Correct output:

```text
['read']
['practice']
['submit']
['review']
```

</details>

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

<details>
<summary>Show solution</summary>

One possible solution:

```python
def analyze_numbers(numbers: list[float]) -> dict:
    """Return count, average, highest, and lowest values for a list of numbers."""
    if len(numbers) == 0:
        return {
            "count": 0,
            "average": None,
            "highest": None,
            "lowest": None,
        }

    return {
        "count": len(numbers),
        "average": sum(numbers) / len(numbers),
        "highest": max(numbers),
        "lowest": min(numbers),
    }


result = analyze_numbers([80, 95, 70, 100])
print(result)
```

Output:

```text
{'count': 4, 'average': 86.25, 'highest': 100, 'lowest': 70}
```

The calculation function returns data. Another function could format and print it later.

</details>

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

<details>
<summary>Show solution</summary>

```python
def item_subtotal(item: dict) -> float:
    """Return the subtotal for one cart item."""
    return item["price"] * item["quantity"]


def cart_total(cart: list) -> float:
    """Return the total price before discount or tax."""
    total = 0

    for item in cart:
        total = total + item_subtotal(item)

    return total


def apply_discount(total: float, percent: float = 0) -> float:
    """Return total after applying a percentage discount."""
    return total - (total * percent / 100)


def add_tax(total: float, tax_percent: float = 0) -> float:
    """Return total after adding percentage tax."""
    return total + (total * tax_percent / 100)


def format_receipt(
    cart: list,
    discount_percent: float = 0,
    tax_percent: float = 0,
    **store_info
) -> str:
    """Return a formatted receipt for the cart."""
    lines = []

    store_name = store_info.get("store_name", "Training Shop")
    cashier = store_info.get("cashier", "Unknown")

    lines.append(store_name)
    lines.append(f"Cashier: {cashier}")
    lines.append("-" * 30)

    for item in cart:
        subtotal = item_subtotal(item)
        lines.append(f"{item['name']} x{item['quantity']}: ${subtotal:.2f}")

    subtotal = cart_total(cart)
    discounted_total = apply_discount(subtotal, discount_percent)
    final_total = add_tax(discounted_total, tax_percent)

    lines.append("-" * 30)
    lines.append(f"Subtotal: ${subtotal:.2f}")
    lines.append(f"Discount: {discount_percent}%")
    lines.append(f"Tax: {tax_percent}%")
    lines.append(f"Total: ${final_total:.2f}")

    return "\n".join(lines)


cart = [
    {"name": "Notebook", "price": 4.50, "quantity": 3},
    {"name": "Pen", "price": 1.25, "quantity": 5},
    {"name": "Backpack", "price": 35.00, "quantity": 1},
]

receipt = format_receipt(
    cart,
    discount_percent=10,
    tax_percent=5,
    store_name="GSG Campus Store",
    cashier="Alaa"
)

print(receipt)
```

Sample output:

```text
GSG Campus Store
Cashier: Alaa
------------------------------
Notebook x3: $13.50
Pen x5: $6.25
Backpack x1: $35.00
------------------------------
Subtotal: $54.75
Discount: 10%
Tax: 5%
Total: $51.74
```

</details>

---

## Bonus - Explain Your Design

Pick one function from your solution and answer:

1. What data enters through parameters?
2. What data leaves through `return`?
3. Does the function print or change outside state?
4. Is it easy to test with one line of code?

<details>
<summary>Show example answer</summary>

Example for `apply_discount`:

- Data enters through `total` and `percent`.
- Data leaves through the returned discounted total.
- It does not print or change outside state.
- It is easy to test:

```python
print(apply_discount(100, 20))  # 80.0
```

</details>
