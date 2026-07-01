

## Review Exercises - 30 Minutes

These two exercises are designed for the start of the next lecture. Students should work in pairs or small groups, then briefly explain their solution to the class.

### Review Exercise 1 - Debug the Broken File Reader (15 min)

**Goal:** Review `with open(...)`, file modes, `.strip()`, and specific `except` blocks.

**Setup:** Give students this broken program:

```python
def show_tasks():
    file = open("tasks.txt", "w")
    tasks = file.readlines()

    for task in tasks:
        print(task)


show_tasks()
```

**Interactive task:**

1. find at least three problems in the code.
2. Rewrite the function so it:
   - Reads from `tasks.txt`
   - Uses `with open(...)`
   - Prints each task without extra newline characters
   - Starts with an empty list if the file does not exist
   
<details>
<summary>
**Expected review points:**
</summary>

- `"w"` overwrites the file; use `"r"` for reading.
- `with open(...)` closes the file automatically.
- `.strip()` removes `\n`.
- `FileNotFoundError` should be handled directly.
</details>

### Review Exercise 2 - CSV Score Board Challenge (15 min)

**Goal:** Review `csv.DictReader`, converting strings to numbers, dictionaries, and `try`/`except`.

**Setup:** Students create `students.csv`:

```text
name,score,track
Amina,90,Python
Omar,not-ready,Python
Lina,88,Frontend
```

**Interactive task:**

Write a program that:

1. Reads the CSV file with `csv.DictReader`
2. Converts valid `score` values to integers
3. Skips invalid scores using `try`/`except ValueError`
4. Prints:
   - Each valid student and score
   - The average score
   - A short message for skipped rows

**Class check:**

Ask each group:

- Which values did Python read as strings?
- Where did you use `try`/`except`?
- Why is `csv.DictReader` better than manually splitting by commas?