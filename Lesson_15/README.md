# Lesson 15 - Libraries & Modules

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Explain what a module, package, and library are
- Import Python standard library modules
- Use selected tools from `math`, `random`, `datetime`, `os`, and `pathlib`
- Create your own module and import functions from it
- Install and import a third-party package with `pip`
- Understand how libraries connect Python to real-world APIs and data work

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Why libraries matter |
| 0:10-0:30 | Import syntax and standard library overview |
| 0:30-0:55 | Useful standard modules |
| 0:55-1:15 | Creating your own modules |
| 1:15-1:35 | Third-party packages and `pip` |
| 1:35-2:00 | Mini-project, Phase 3 recap, and next steps |

---

## Part 1 - Why Libraries Matter (10 min)

You do not have to write everything from scratch.

A **module** is a Python file that contains reusable code.

A **package** is a folder of modules.

A **library** is a broader collection of reusable code, often made of many packages and modules.

Examples:

- `math` helps with mathematical operations
- `random` generates random choices and numbers
- `datetime` works with dates and times
- `csv` reads and writes CSV files
- `requests` can fetch data from the web
- `pandas` helps analyze table-like data

Lesson 14 introduced `csv`. Today you learn the general pattern for using modules and libraries.

---

## Part 2 - Import Syntax (20 min)

### 2.1 Import the Whole Module

```python
import math

print(math.sqrt(16))
print(math.pi)
```

This style makes it clear where each tool comes from.

### 2.2 Import Specific Names

```python
from math import sqrt, pi

print(sqrt(16))
print(pi)
```

This is shorter, but readers may need to know where `sqrt` came from.

### 2.3 Import with an Alias

```python
import random as rnd

print(rnd.randint(1, 10))
```

Aliases are common for popular libraries:

```python
import pandas as pd
```

Use aliases only when they are standard or make the code clearer.

---

## Part 3 - Useful Standard Library Modules (25 min)

The standard library comes with Python. You do not install it separately.

### 3.1 `math`

```python
import math

print(math.sqrt(25))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)
```

### 3.2 `random`

```python
import random

print(random.randint(1, 6))
print(random.choice(["A", "B", "C"]))

items = ["question 1", "question 2", "question 3"]
random.shuffle(items)
print(items)
```

### 3.3 `datetime`

```python
from datetime import datetime, timedelta

now = datetime.now()
tomorrow = now + timedelta(days=1)

print(now.strftime("%Y-%m-%d %H:%M"))
print(tomorrow.strftime("%Y-%m-%d"))
```

### 3.4 `os` and `pathlib`

`os` and `pathlib` help with files, folders, and paths.

```python
import os

print(os.getcwd())
print(os.listdir("."))

data_path = os.path.join("data", "tasks.txt")
print(data_path)
```

`pathlib` gives a modern object-based way to work with paths.

```python
from pathlib import Path

data_path = Path("data") / "tasks.txt"
print(data_path)
print(data_path.exists())
```

Prefer `pathlib` for new code when building file paths.

---

## Part 4 - Creating Your Own Modules (20 min)

Any `.py` file can be a module.

Create `grade_utils.py`:

```python
def calculate_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def passed(score):
    return score >= 60
```

Create `main.py` in the same folder:

```python
from grade_utils import calculate_grade, passed

score = 85

print(calculate_grade(score))
print(passed(score))
```

This keeps reusable logic separate from the program that uses it.

### 4.1 Avoid Running Code on Import

If a module contains test code, protect it with:

```python
if __name__ == "__main__":
    print(calculate_grade(85))
```

That code runs when the file is executed directly, but not when the file is imported.

---

## Part 5 - Third-Party Packages and `pip` (20 min)

[Don't forget to create virtual environment](./venv.md)

Third-party packages are created outside the Python standard library.

Install packages with `pip`:

```bash
python -m pip install requests
```

Then import and use the package:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json().keys())
```

### 5.1 Requirements Files

Projects often list dependencies in `requirements.txt`.

```text
requests
pandas
```

Install them with:

```bash
python -m pip install -r requirements.txt
```

### 5.2 Quick Look at `pandas`

`pandas` is widely used for data analysis.

```python
import pandas as pd

students = pd.read_csv("students.csv")
print(students.head())
print(students["score"].mean())
```

You do not need to master `pandas` today. The goal is to understand that Python libraries can give you powerful tools for specific domains.

---

## Part 6 - Choosing and Verifying Libraries (10 min)

Before adding a package, ask:

- Does the standard library already solve this?
- Is the package actively maintained?
- Does it have clear documentation?
- Is it popular enough that issues are easy to search?
- Does the project really need the dependency?

AI tools can suggest libraries, but you should still verify the package name and documentation before installing.

---

## Mini-Project - Quiz Tools Module (25 min)

Refactor the Lesson 10 quiz idea into reusable modules.

### Requirements

1. Create `quiz_utils.py`
2. Add a function that shuffles questions using `random.shuffle`
3. Add a function that calculates percentage score
4. Add a function that returns a result message
5. Create `main.py` that imports and uses those functions
6. Add `if __name__ == "__main__":` where appropriate

### Starter `quiz_utils.py`

```python
import random


def shuffle_questions(questions):
    questions_copy = questions.copy()
    random.shuffle(questions_copy)
    return questions_copy


def calculate_percentage(correct, total):
    if total == 0:
        return 0
    return (correct / total) * 100


def result_message(percentage):
    if percentage >= 90:
        return "Excellent work"
    if percentage >= 70:
        return "Good job"
    if percentage >= 50:
        return "Keep practicing"
    return "Review and try again"
```

Challenge: read questions from a CSV file using Lesson 14 skills.

---

## Phase 3 Recap

| Lesson | Skill |
|--------|-------|
| 11 | Advanced function design, scope, `*args`, `**kwargs` |
| 12 | Lists, tuples, slicing, comprehensions |
| 13 | Dictionaries, sets, records |
| 14 | Files, CSV, error handling |
| 15 | Modules, standard library, third-party packages |

You now have the core tools needed to build larger Python programs:

- Functions organize behavior
- Collections organize data
- Files preserve data
- Errors make programs safer
- Libraries expand what Python can do

---

## Exercises

**Exercise 1 - Random picker**

Write a program that stores names in a list and uses `random.choice()` to select one.

**Exercise 2 - Date formatter**

Print today's date in three different formats using `datetime`.

**Exercise 3 - Path checker**

Ask the user for a filename and use `pathlib.Path` to check whether it exists.

**Exercise 4 - Grade module**

Move grade-related functions into `grade_utils.py` and import them into `main.py`.

**Exercise 5 - Explore a package**

Pick one package from `requests`, `pandas`, or another instructor-approved package. Find one example from its documentation and explain what the code does.

---

## Key Takeaways

- A module is a `.py` file containing reusable code.
- The standard library comes with Python.
- `import module` is explicit and beginner-friendly.
- `pip` installs third-party packages.
- `requirements.txt` records project dependencies.
- Use `if __name__ == "__main__":` to keep importable modules clean.
- Libraries are powerful, but each dependency should have a reason.

---

*Next phase -> **Phase 4 - Frontend (Lessons 16-18)**  
Previous lesson -> **Lesson 14: File Handling & Error Handling***
