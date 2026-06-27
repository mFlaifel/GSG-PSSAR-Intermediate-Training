# Lesson 14 - File Handling & Error Handling

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Read text files with `with open(...)`
- Write and append text files safely
- Read and write simple CSV files with the `csv` module
- Use `try`, `except`, `else`, and `finally` to handle expected errors
- Handle common errors such as `FileNotFoundError`, `ValueError`, and `KeyError`
- Combine files, dictionaries, and functions to persist program data

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Why programs need persistent data |
| 0:10-0:35 | Reading text files |
| 0:35-0:55 | Writing and appending text files |
| 0:55-1:15 | CSV files with dictionaries |
| 1:15-1:40 | Error handling with `try`/`except` |
| 1:40-2:00 | Mini-project and exercises |

---

## Part 1 - Why Files Matter (10 min)

Variables disappear when a program ends.

```python
tasks = ["Study Python", "Submit homework"]
```

If the program closes, that list is gone. Files let programs save data and load it again later.

Common uses:

- Save task lists
- Store scores
- Read configuration
- Process CSV data
- Keep logs

This lesson connects Lesson 11 functions, Lesson 12 lists, and Lesson 13 dictionaries to real saved data.

---

## Part 2 - Reading Text Files (25 min)

### 2.1 Basic File Reading

[Use `with open(...)` so Python closes the file automatically.](./why_use_with_to_open_file.md)

```python
with open("notes.txt", "r") as file:
    content = file.read()

print(content)
```

The `"r"` mode means read.

### 2.2 Reading Lines

```python
with open("tasks.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Each line usually includes the newline character `\n`. Clean it with `.strip()`.

```python
with open("tasks.txt", "r") as file:
    for line in file:
        task = line.strip()
        print(task)
```

### 2.3 File Paths

If you write:

```python
open("notes.txt")
```

Python looks in the current working directory: the folder where the program is running.

For beginner projects, keep the data file in the same folder as the script.

---

## Part 3 - Writing and Appending Text Files (20 min)

### 3.1 Writing Files

The `"w"` mode creates a file or replaces an existing file.

```python
tasks = ["Study Python", "Submit homework", "Review feedback"]

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")
```

Be careful: `"w"` overwrites the file.

### 3.2 Appending Files

The `"a"` mode adds to the end of a file.

```python
with open("tasks.txt", "a") as file:
    file.write("Practice dictionaries\n")
```

### 3.3 Read-Modify-Write Pattern

Many programs follow this pattern:

1. Read existing data from a file
2. Convert it into Python data
3. Modify the data
4. Write the updated data back to the file

```python
def load_tasks(filepath):
    tasks = []

    with open(filepath, "r") as file:
        for line in file:
            tasks.append(line.strip())

    return tasks


def save_tasks(filepath, tasks):
    with open(filepath, "w") as file:
        for task in tasks:
            file.write(task + "\n")
```

---

## Part 4 - CSV Files with Dictionaries (20 min)

CSV means comma-separated values. It is common for spreadsheets and simple datasets.

```text
name,score,track
Amina,90,Python
Omar,75,Python
Lina,88,Frontend
```

Use Python's built-in `csv` module instead of splitting lines by comma manually.

### 4.1 Reading CSV as Dictionaries

```python
import csv

students = []

with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["score"] = int(row["score"])
        students.append(row)

print(students)
```

### 4.2 Writing CSV from Dictionaries

```python
import csv

students = [
    {"name": "Amina", "score": 90, "track": "Python"},
    {"name": "Omar", "score": 75, "track": "Python"},
]

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "score", "track"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)
```

CSV values are read as strings, so convert numbers with `int()` or `float()` when needed.

---

## Part 5 - Error Handling (25 min)

Programs should not crash for expected problems like missing files or invalid input.

### 5.1 Basic `try`/`except`

```python
try:
    age = int(input("Age: "))
    print(f"Next year you will be {age + 1}")
except ValueError:
    print("Please enter a valid number.")
```

### 5.2 Handling Missing Files

```python
try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
except FileNotFoundError:
    tasks = []

print(tasks)
```

This is useful when a program should start with empty data the first time it runs.

### 5.3 Multiple Exceptions

```python
student = {"name": "Amina", "score": "90"}

try:
    bonus_score = int(student["bonus"])
except KeyError:
    print("Missing bonus key.")
except ValueError:
    print("Bonus score must be a number.")
```

### 5.4 `else` and `finally`

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid number.")
else:
    print(f"Double: {number * 2}")
finally:
    print("Input attempt finished.")
```

- `else` runs only if no exception happens
- `finally` runs whether an exception happens or not

Use `finally` for cleanup. With files, `with open(...)` already handles cleanup for you.

### 5.5 Avoid Bare `except`

Avoid catching everything without naming the error.

```python
# Avoid
try:
    score = int(input("Score: "))
except:
    print("Something went wrong.")
```

Better:

```python
try:
    score = int(input("Score: "))
except ValueError:
    print("Score must be a number.")
```

Specific errors make debugging easier.

---

## Mini-Project - Persistent Task Manager (20 min)

Upgrade the Lesson 12 task manager so tasks are saved to a file.

### Requirements

1. Load tasks from `tasks.txt` when the program starts
2. If `tasks.txt` does not exist, start with an empty list
3. Let the user add, show, and remove tasks
4. Save tasks back to `tasks.txt` after every change
5. Use functions for loading, saving, and menu actions
6. Handle invalid task numbers with `try`/`except`

### Starter Functions

```python
def load_tasks(filepath):
    try:
        with open(filepath, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def save_tasks(filepath, tasks):
    with open(filepath, "w") as file:
        for task in tasks:
            file.write(task + "\n")
```

Challenge: save each task as CSV with `title` and `done` columns.

---

## Exercises

**Exercise 1 - Read notes**

Create `notes.txt`, write three lines into it, then read and print each line without extra newline characters.

**Exercise 2 - Append log**

Ask the user for an action and append it to `activity_log.txt`.

**Exercise 3 - Safe number input**

Write a function `get_number(prompt)` that keeps asking until the user enters a valid number.

**Exercise 4 - CSV average**

Read `students.csv` and calculate the average score.

**Exercise 5 - Error map**

For each error, write one example that could cause it: `FileNotFoundError`, `ValueError`, `KeyError`.

---

## Key Takeaways

- Use `with open(...)` for safe file handling.
- `"r"` reads, `"w"` writes and overwrites, `"a"` appends.
- Use the `csv` module for CSV files.
- Convert CSV numbers from strings before doing math.
- Catch specific exceptions instead of using bare `except`.
- File handling becomes more useful when combined with functions and collections.

---

*Next lesson -> **Lesson 15: Libraries & Modules**  
Previous lesson -> **Lesson 13: Dictionaries & Sets***
