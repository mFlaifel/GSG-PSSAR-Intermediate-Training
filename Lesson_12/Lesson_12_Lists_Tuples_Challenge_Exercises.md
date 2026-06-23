# Lesson 12 - Lists & Tuples Challenge Exercises

These exercises reinforce the learning outcomes from Lesson 12:

- Index, slice, and update lists
- Use list methods such as `.append()`, `.insert()`, `.remove()`, `.pop()`, and `.sort()`
- Loop through lists with values, indexes, and `enumerate()`
- Copy lists safely and explain when the original list changes
- Use list comprehensions for simple filters and transformations
- Use tuples and tuple unpacking for fixed records

Suggested time: **25-30 minutes total**. Try each challenge before opening the solution.

---

## Challenge 1 - Slice Detective

Before running the code, predict every line of output.

```python
topics = ["variables", "loops", "functions", "lists", "tuples", "dictionaries"]

print(topics[0])
print(topics[-2])
print(topics[1:4])
print(topics[:3])
print(topics[3:])
print(topics[::-1])

topics[3] = "lists and tuples"
print(topics)
```

Questions:

1. What does each `print()` output?
2. Why does `topics[1:4]` stop before `"tuples"`?
3. Which line changes the original list?

<details>
<summary>Show solution</summary>

Output:

```text
variables
tuples
['loops', 'functions', 'lists']
['variables', 'loops', 'functions']
['lists', 'tuples', 'dictionaries']
['dictionaries', 'tuples', 'lists', 'functions', 'loops', 'variables']
['variables', 'loops', 'functions', 'lists and tuples', 'tuples', 'dictionaries']
```

`topics[1:4]` starts at index `1` and stops before index `4`, so it includes indexes `1`, `2`, and `3`.

The line `topics[3] = "lists and tuples"` changes the original list because lists are mutable.

</details>

---

## Challenge 2 - Workshop Queue

Complete the queue program.

Starter code:

```python
queue = ["Amina", "Omar", "Lina"]

# 1. Add "Yousef" to the end.

# 2. Insert "Sara" at index 1.

# 3. If "Omar" is in the queue, remove him.

# 4. Serve the first student and store the name in served_student.

# 5. Print the served student.

# 6. Print the remaining queue as a numbered list starting from 1.
```

Expected output:

```text
Served: Amina
1. Sara
2. Lina
3. Yousef
```

Rules:

- Use `.append()` for step 1.
- Use `.insert()` for step 2.
- Use `in` before `.remove()` for step 3.
- Use `.pop()` for step 4.
- Use `enumerate()` for step 6.

<details>
<summary>Show solution</summary>

```python
queue = ["Amina", "Omar", "Lina"]

queue.append("Yousef")
queue.insert(1, "Sara")

if "Omar" in queue:
    queue.remove("Omar")

served_student = queue.pop(0)

print(f"Served: {served_student}")

for number, student in enumerate(queue, start=1):
    print(f"{number}. {student}")
```

After the edits, the queue becomes `["Amina", "Sara", "Lina", "Yousef"]`.

`queue.pop(0)` removes and returns the first item, so `"Amina"` is stored in `served_student`.

</details>

---

## Challenge 3 - Keep the Original Scores Safe

The code below has a copying bug. It accidentally changes the original list.

```python
scores = [72, 90, 61, 88, 95, 70]

original_scores = scores
top_scores = scores
top_scores.sort(reverse=True)

print("Original:", original_scores)
print("Top three:", top_scores[:3])
```

Fix the program so that:

1. `scores` stays in its original order.
2. `top_scores` is a new list sorted from highest to lowest.
3. `passing_scores` contains only scores greater than or equal to `70`.
4. `score_range` is a tuple containing the lowest and highest score.

Expected output:

```text
Original: [72, 90, 61, 88, 95, 70]
Top three: [95, 90, 88]
Passing: [72, 90, 88, 95, 70]
Range: (61, 95)
```

<details>
<summary>Show solution</summary>

```python
scores = [72, 90, 61, 88, 95, 70]

top_scores = sorted(scores, reverse=True)
passing_scores = [score for score in scores if score >= 70]
score_range = (min(scores), max(scores))

print("Original:", scores)
print("Top three:", top_scores[:3])
print("Passing:", passing_scores)
print("Range:", score_range)
```

`original_scores = scores` and `top_scores = scores` do not create new lists. They create extra names for the same list.

`sorted(scores, reverse=True)` returns a new sorted list, so `scores` keeps its original order.

The tuple `(min(scores), max(scores))` is a good fit because the lowest and highest values belong together as one fixed pair.

</details>

---

## Challenge 4 - Tuple Records and Nested Lists

Each student record is a tuple: `(name, scores)`.

```python
records = [
    ("Amina", [90, 88, 95]),
    ("Omar", [58, 61, 70]),
    ("Lina", [100, 98, 94]),
]
```

Write code that:

1. Uses tuple unpacking in the loop.
2. Prints each student's average with one decimal place.
3. Builds a list called `passing_students` with names whose average is at least `70`.
4. Prints the passing students list.

Expected output:

```text
Amina: 91.0
Omar: 63.0
Lina: 97.3
Passing students: ['Amina', 'Lina']
```

<details>
<summary>Show solution</summary>

```python
records = [
    ("Amina", [90, 88, 95]),
    ("Omar", [58, 61, 70]),
    ("Lina", [100, 98, 94]),
]

passing_students = []

for name, scores in records:
    average = sum(scores) / len(scores)
    print(f"{name}: {average:.1f}")

    if average >= 70:
        passing_students.append(name)

print("Passing students:", passing_students)
```

The loop uses tuple unpacking here:

```python
for name, scores in records:
```

Each record has two parts, so Python places the first value in `name` and the second value in `scores`.

The `scores` value is a list inside the tuple, so this challenge also practices nested data.

</details>

