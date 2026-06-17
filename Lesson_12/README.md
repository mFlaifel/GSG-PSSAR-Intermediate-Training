# Lesson 12 - Lists & Tuples

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Create, index, slice, and update lists
- Use list methods such as `.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()`, and `.sort()`
- Loop through lists using values, indexes, and `enumerate()`
- Copy lists safely and explain why assignment is not a copy
- Build simple transformations with list comprehensions
- Use tuples for fixed records and unpack tuple values

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Why collections matter |
| 0:10-0:35 | Indexing, slicing, and updating lists |
| 0:35-0:55 | List methods and membership checks |
| 0:55-1:15 | Sorting, copying, and nested lists |
| 1:15-1:35 | List comprehensions |
| 1:35-1:50 | Tuples and unpacking |
| 1:50-2:00 | Mini-project setup and exercises |

---

## Part 1 - Why Collections Matter (10 min)

So far, most variables stored one value at a time.

```python
student_1 = "Amina"
student_2 = "Omar"
student_3 = "Lina"
```

A list lets one variable store many values.

```python
students = ["Amina", "Omar", "Lina"]
scores = [90, 75, 88]
mixed = ["Python", 3, True]
```

Lists are:

- Ordered
- Mutable, meaning they can change
- Able to contain any type of value
- Commonly used for collections that grow, shrink, or get updated

---

## Part 2 - Indexing, Slicing, and Updating Lists (25 min)

### 2.1 Indexing

Indexes start at `0`.

```python
students = ["Amina", "Omar", "Lina", "Yousef"]

print(students[0])   # Amina
print(students[1])   # Omar
print(students[-1])  # Yousef
```

Negative indexes count from the end.

| Index | Value |
|-------|-------|
| `0` | `"Amina"` |
| `1` | `"Omar"` |
| `2` | `"Lina"` |
| `3` | `"Yousef"` |
| `-1` | `"Yousef"` |

### 2.2 Slicing

Slicing creates a new list from part of another list.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[3:])    # [40, 50, 60]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10]
```

The stop index is excluded.

### 2.3 Updating Values

```python
students = ["Amina", "Omar", "Lina"]
students[1] = "Sara"

print(students)  # ['Amina', 'Sara', 'Lina']
```

Lists are mutable, so their contents can change after creation.

---

## Part 3 - List Methods and Membership (20 min)

### 3.1 Adding Items

```python
tasks = []

tasks.append("Review lesson")
tasks.append("Solve exercise")
print(tasks)
```

Use `.insert()` when position matters.

```python
tasks.insert(0, "Open VS Code")
print(tasks)
```

Use `.extend()` to add many items.

```python
tasks.extend(["Submit homework", "Read feedback"])
print(tasks)
```

### 3.2 Removing Items

```python
tasks = ["Open VS Code", "Review lesson", "Solve exercise"]

tasks.remove("Review lesson")  # removes by value
print(tasks)

last_task = tasks.pop()        # removes and returns the last item
print(last_task)
print(tasks)
```

Use `del` to remove by index.

```python
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)  # [10, 30, 40]
```

### 3.3 Checking Membership

```python
students = ["Amina", "Omar", "Lina"]

if "Omar" in students:
    print("Omar is enrolled")

if "Sara" not in students:
    print("Sara is not enrolled yet")
```

Use `.index()` only when you know the item exists, or check with `in` first.

```python
if "Lina" in students:
    print(students.index("Lina"))  # 2
```

---

## Part 4 - Sorting, Copying, and Nested Lists (20 min)

### 4.1 Sorting

`.sort()` changes the original list.

```python
names = ["Lina", "Amina", "Yousef", "Omar"]
names.sort()
print(names)
```

`sorted()` returns a new sorted list.

```python
names = ["Lina", "Amina", "Yousef", "Omar"]
sorted_names = sorted(names)

print(names)         # original unchanged
print(sorted_names)  # sorted copy
```

Sort in reverse:

```python
scores = [90, 75, 88, 61]
scores.sort(reverse=True)
print(scores)
```

Sort by a custom rule:

```python
students = ["Lina", "Amina", "Yousef", "Omar"]
students.sort(key=len)
print(students)
```

### 4.2 Copying Lists

Assignment does not copy a list. It creates another name for the same list.

```python
original = [1, 2, 3]
alias = original

alias.append(4)
print(original)  # [1, 2, 3, 4]
```

Use `.copy()` or slicing for a shallow copy.

```python
original = [1, 2, 3]
copy_one = original.copy()
copy_two = original[:]

copy_one.append(4)
print(original)  # [1, 2, 3]
```

### 4.3 Nested Lists

A nested list is a list inside another list.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6
```

Nested lists are useful for grids, tables, schedules, and game boards.

```python
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

---

## Part 5 - List Comprehensions (20 min)

A list comprehension builds a new list from an existing iterable.

```python
numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

The same transformation as a comprehension:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)
```

Add a condition:

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)  # [2, 4, 6]
```

Keep comprehensions simple. If the logic becomes hard to read, use a normal `for` loop.

---

## Part 6 - Tuples and Unpacking (15 min)

A tuple is an ordered collection like a list, but immutable.

```python
point = (10, 20)
rgb_color = (255, 120, 0)
```

You can index and slice tuples:

```python
print(point[0])  # 10
```

But you cannot change them:

```python
# point[0] = 99  # TypeError
```

### 6.1 Tuple Unpacking

```python
point = (10, 20)
x, y = point

print(x)
print(y)
```

This is useful when functions return multiple values.

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 8, 1, 9])
print(low, high)
```

### 6.2 Lists vs Tuples

| Use a list when... | Use a tuple when... |
|--------------------|---------------------|
| The collection will change | The collection should stay fixed |
| You need to add or remove items | The values belong together as one record |
| You are building data step by step | You want to protect the structure |

```python
shopping_list = ["bread", "milk", "eggs"]
coordinates = (31.5, 34.4)
```

---

## Mini-Project - Task Manager (10 min setup + homework)

Build a simple task manager using a list.

### Requirements

1. Store tasks in a list
2. Show a menu repeatedly
3. Add a task
4. Show numbered tasks using `enumerate()`
5. Remove a task by number
6. Exit with `break`

### Starter Version

```python
tasks = []

while True:
    print("\nTASK MANAGER")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
    elif choice == "2":
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    elif choice == "3":
        number = int(input("Task number to remove: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
```

Challenge: store each task as a dictionary with `title` and `done`. This previews Lesson 13.

---

## Exercises

**Exercise 1 - First and last**

Write a function that receives a list and returns a tuple containing the first and last item.

**Exercise 2 - Filter passing grades**

Given a list of grades, create a new list with only grades greater than or equal to 60.

**Exercise 3 - Reverse words**

Ask the user for a sentence, split it into words, reverse the list, and join it back.

**Exercise 4 - Top three scores**

Given a list of scores, print the top three in descending order.

**Exercise 5 - Matrix total**

Given a nested list of numbers, calculate the total of all values.

---

## Key Takeaways

- Lists are ordered and mutable.
- Indexing starts at `0`; negative indexes count from the end.
- Slicing creates a new list.
- `.sort()` changes the list; `sorted()` returns a new sorted list.
- Assignment does not copy a list.
- List comprehensions are useful for simple transformations and filters.
- Tuples are ordered and immutable.

---

*Next lesson -> **Lesson 13: Dictionaries & Sets**  
Previous lesson -> **Lesson 11: Functions II - Scope & Advanced Design***
