# Lesson 13 - Dictionaries & Sets Challenge Exercises

These exercises reinforce the learning outcomes from Lesson 13:

- Create dictionaries to store key-value data
- Read, add, update, and delete dictionary entries
- Use `.get()`, `.keys()`, `.values()`, and `.items()`
- Loop through dictionaries clearly
- Work with nested dictionaries and lists of dictionaries
- Use sets to remove duplicates and compare groups
- Choose the right collection for a given problem

Suggested time: **20-25 minutes total**. Try each challenge before opening the solution.

---

## Challenge 1 - Product Profile

Complete the product profile program.

Starter code:

```python
product = {
    "name": "Keyboard",
    "price": 45,
    "quantity": 8
}

# 1. Print the product name.

# 2. Use .get() to read a missing "discount" key with a default value of 0.

# 3. Add a new key called "category" with the value "Accessories".

# 4. Update the price to 40.

# 5. Remove the quantity using .pop() and store it in removed_quantity.

# 6. Loop through the dictionary and print each key-value pair.
```

Expected output:

```text
Product: Keyboard
Discount: 0
Removed quantity: 8
name: Keyboard
price: 40
category: Accessories
```

Rules:

- Use bracket access for the existing `name` key.
- Use `.get()` for the missing `discount` key.
- Use `.pop()` to remove `quantity`.
- Use `.items()` when looping through the dictionary.

<details>
<summary>Show solution</summary>

```python
product = {
    "name": "Keyboard",
    "price": 45,
    "quantity": 8
}

print(f"Product: {product['name']}")

discount = product.get("discount", 0)
print(f"Discount: {discount}")

product["category"] = "Accessories"
product["price"] = 40

removed_quantity = product.pop("quantity")
print(f"Removed quantity: {removed_quantity}")

for key, value in product.items():
    print(f"{key}: {value}")
```

`.get("discount", 0)` returns `0` because the `discount` key does not exist.

`.pop("quantity")` removes the key and returns its value, so `8` is stored in `removed_quantity`.

</details>

---

## Challenge 2 - Student Records Report

Write a report for this list of student dictionaries.

```python
students = [
    {"name": "Amina", "score": 90, "track": "Python"},
    {"name": "Omar", "score": 75, "track": "Python"},
    {"name": "Lina", "score": 88, "track": "Frontend"},
    {"name": "Yousef", "score": 52, "track": "Python"},
]
```

Write code that:

1. Prints each student in the format `Name - Track - Score`.
2. Calculates and prints the class average with one decimal place.
3. Builds a list called `passing_students` containing names with scores greater than or equal to `60`.
4. Builds a set called `unique_tracks` containing all tracks.
5. Prints the passing students list and unique tracks set.

Expected output:

```text
Amina - Python - 90
Omar - Python - 75
Lina - Frontend - 88
Yousef - Python - 52
Average: 76.2
Passing students: ['Amina', 'Omar', 'Lina']
Unique tracks: {'Python', 'Frontend'}
```

The order of values inside `unique_tracks` may be different because sets are unordered.

<details>
<summary>Show solution</summary>

```python
students = [
    {"name": "Amina", "score": 90, "track": "Python"},
    {"name": "Omar", "score": 75, "track": "Python"},
    {"name": "Lina", "score": 88, "track": "Frontend"},
    {"name": "Yousef", "score": 52, "track": "Python"},
]

total = 0
passing_students = []
unique_tracks = set()

for student in students:
    print(f"{student['name']} - {student['track']} - {student['score']}")

    total += student["score"]
    unique_tracks.add(student["track"])

    if student["score"] >= 60:
        passing_students.append(student["name"])

average = total / len(students)

print(f"Average: {average:.1f}")
print("Passing students:", passing_students)
print("Unique tracks:", unique_tracks)
```

Each student is a dictionary, and all student dictionaries are stored inside one list.

The set removes duplicate tracks automatically, so `"Python"` appears only once.

</details>

---

## Challenge 3 - Club Overlap

Two clubs recorded their registered students.

```python
python_club = {"Amina", "Omar", "Lina", "Sara"}
web_club = {"Lina", "Yousef", "Sara", "Khaled"}
```

Write code that:

1. Prints all students who joined at least one club.
2. Prints students who joined both clubs.
3. Prints students who joined only the Python club.
4. Adds `"Mona"` to the Python club.
5. Safely removes `"Khaled"` from the web club without causing an error if the name is missing.
6. Prints both updated sets.

Expected output:

```text
All students: {'Amina', 'Omar', 'Lina', 'Sara', 'Yousef', 'Khaled'}
Both clubs: {'Lina', 'Sara'}
Python only: {'Amina', 'Omar'}
Updated Python club: {'Amina', 'Omar', 'Lina', 'Sara', 'Mona'}
Updated Web club: {'Lina', 'Yousef', 'Sara'}
```

The order of values inside each set may be different because sets are unordered.

Rules:

- Use `|` to find all students.
- Use `&` to find students in both clubs.
- Use `-` to find students only in the Python club.
- Use `.add()` to add `"Mona"`.
- Use `.discard()` to safely remove `"Khaled"`.

<details>
<summary>Show solution</summary>

```python
python_club = {"Amina", "Omar", "Lina", "Sara"}
web_club = {"Lina", "Yousef", "Sara", "Khaled"}

all_students = python_club | web_club
both_clubs = python_club & web_club
python_only = python_club - web_club

print("All students:", all_students)
print("Both clubs:", both_clubs)
print("Python only:", python_only)

python_club.add("Mona")
web_club.discard("Khaled")

print("Updated Python club:", python_club)
print("Updated Web club:", web_club)
```

The union `|` combines both sets.

The intersection `&` keeps only names found in both sets.

The difference `-` keeps names from the first set that are not in the second set.

`.discard()` is safer than `.remove()` when the value might not exist.

</details>
