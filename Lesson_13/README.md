# Lesson 13 - Dictionaries & Sets

**Phase 3 - Python Advanced | Duration: 2 Hours | Level: Intermediate**

---

## Learning Objectives

By the end of this lesson you will be able to:

- Create dictionaries to store key-value data
- Read, add, update, and delete dictionary entries
- Use `.get()`, `.keys()`, `.values()`, and `.items()`
- Loop through dictionaries safely and clearly
- Build nested dictionaries for records and grouped data
- Use sets to store unique values and compare groups
- Choose between lists, tuples, dictionaries, and sets for a given problem

---

## Lesson Flow - 2 Hours

| Time | Topic |
|------|-------|
| 0:00-0:10 | Review: lists store positions, dictionaries store labels |
| 0:10-0:35 | Dictionary basics: create, read, update, delete |
| 0:35-0:55 | Dictionary methods and looping patterns |
| 0:55-1:15 | Nested dictionaries and records |
| 1:15-1:35 | Sets and uniqueness |
| 1:35-2:00 | Mini-project and exercises |

---

## Part 1 - From Lists to Dictionaries (10 min)

In Lesson 12, lists stored values by position.

```python
student = ["Amina", 90, "Python"]

print(student[0])  # Amina
print(student[1])  # 90
```

This works, but the indexes do not explain themselves. A dictionary stores values by meaningful labels called keys.

```python
student = {
    "name": "Amina",
    "score": 90,
    "track": "Python"
}

print(student["name"])   # Amina
print(student["score"])  # 90
```

Use a dictionary when each value has a name.

---

## Part 2 - Dictionary Basics (25 min)

### 2.1 Creating Dictionaries

```python
profile = {
    "username": "sara",
    "email": "sara@example.com",
    "is_admin": False
}
```

Dictionary keys are usually strings. Values can be any type.

```python
course = {
    "title": "Python Advanced",
    "hours": 10,
    "active": True,
    "topics": ["functions", "lists", "dictionaries"]
}
```

### 2.2 Reading Values

```python
print(profile["username"])
print(profile["email"])
```

If the key does not exist, bracket access raises `KeyError`.

```python
# print(profile["phone"])  # KeyError
```

Use `.get()` when a missing key is possible.

```python
phone = profile.get("phone", "No phone number")
print(phone)
```

### 2.3 Adding and Updating Values

```python
profile["city"] = "Gaza"                 # add
profile["email"] = "new@example.com"     # update

print(profile)
```

### 2.4 Deleting Values

```python
removed_email = profile.pop("email")
print(removed_email)

del profile["is_admin"]
print(profile)
```

Use `.pop()` when you need the removed value. Use `del` when you only want to delete it.

---

## Part 3 - Dictionary Methods and Loops (20 min)

### 3.1 Keys, Values, and Items

```python
student = {
    "name": "Omar",
    "score": 82,
    "track": "Python"
}

print(student.keys())
print(student.values())
print(student.items())
```

### 3.2 Looping Through Keys

```python
for key in student:
    print(key)
```

This loops through keys by default.

### 3.3 Looping Through Values

```python
for value in student.values():
    print(value)
```

### 3.4 Looping Through Key-Value Pairs

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

This is the most common dictionary loop.

---

## Part 4 - Nested Dictionaries and Records (20 min)

A nested dictionary stores dictionaries inside another dictionary.

```python
students = {
    "s001": {
        "name": "Amina",
        "score": 90,
        "track": "Python"
    },
    "s002": {
        "name": "Omar",
        "score": 75,
        "track": "Python"
    }
}

print(students["s001"]["name"])   # Amina
print(students["s002"]["score"])  # 75
```

Loop through records:

```python
for student_id, data in students.items():
    print(f"{student_id}: {data['name']} scored {data['score']}")
```

### List of Dictionaries

For ordered records, a list of dictionaries is often simpler.

```python
students = [
    {"name": "Amina", "score": 90},
    {"name": "Omar", "score": 75},
    {"name": "Lina", "score": 88},
]

for student in students:
    print(f"{student['name']}: {student['score']}")
```

This shape appears often in APIs and data files.

---

## Part 5 - Sets and Uniqueness (20 min)

A set stores unique values.

```python
names = {"Amina", "Omar", "Lina", "Amina"}
print(names)  # duplicate Amina appears once
```

Sets are:

- Unordered
- Mutable
- Unique
- Fast for membership checks

### 5.1 Creating Sets

```python
tags = {"python", "beginner", "functions"}
empty_set = set()
```

Use `set()` for an empty set. `{}` creates an empty dictionary.

### 5.2 Adding and Removing Items

```python
tags.add("data")
tags.remove("beginner")
print(tags)
```

Use `.discard()` if the value may not exist.

```python
tags.discard("missing-tag")  # no error
```

### 5.3 Removing Duplicates

```python
emails = ["a@example.com", "b@example.com", "a@example.com"]
unique_emails = set(emails)

print(unique_emails)
```

### 5.4 Comparing Groups

```python
python_students = {"Amina", "Omar", "Lina"}
web_students = {"Lina", "Yousef", "Sara"}

print(python_students | web_students)  # union
print(python_students & web_students)  # intersection
print(python_students - web_students)  # difference
```

---

## Part 6 - Choosing the Right Collection (10 min)

| Collection | Best for |
|------------|----------|
| List | Ordered items that can change |
| Tuple | Fixed group of values |
| Dictionary | Labeled data and records |
| Set | Unique values and group comparisons |

Examples:

```python
tasks = ["Study", "Practice", "Submit"]         # list
location = (31.5, 34.4)                         # tuple
student = {"name": "Amina", "score": 90}        # dictionary
unique_tags = {"python", "data", "web"}         # set
```

---

## Mini-Project - Student Records (25 min)

Build a student records program using a list of dictionaries and a set.

### Requirements

1. Store each student as a dictionary with `name`, `score`, and `track`
2. Store all students in a list
3. Print all students in a readable format
4. Calculate the class average
5. Print the names of students who passed
6. Use a set to show the unique tracks represented in the class

### Starter Data

```python
students = [
    {"name": "Amina", "score": 90, "track": "Python"},
    {"name": "Omar", "score": 75, "track": "Python"},
    {"name": "Lina", "score": 88, "track": "Frontend"},
    {"name": "Yousef", "score": 52, "track": "Python"},
]
```

### Starter Functions

```python
def class_average(students):
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


def get_unique_tracks(students):
    tracks = set()
    for student in students:
        tracks.add(student["track"])
    return tracks
```

Challenge: add a menu that lets the user add a new student.

---

## Exercises

**Exercise 1 - Safe lookup**

Create a dictionary for a product with `name`, `price`, and `quantity`. Use `.get()` to read a missing `discount` key with default value `0`.

**Exercise 2 - Word frequency**

Ask the user for a sentence and count how many times each word appears.

**Exercise 3 - Unique visitors**

Given a list of visitor emails with duplicates, print the number of unique visitors.

**Exercise 4 - Passed students**

Given a list of student dictionaries, create a list containing only students with score `>= 60`.

**Exercise 5 - Common interests**

Given two sets of interests, print the interests they have in common.

---

## Key Takeaways

- Dictionaries store key-value pairs.
- Use `.get()` when a key may be missing.
- `.items()` is the common way to loop through key-value pairs.
- Nested dictionaries and lists of dictionaries are useful for records.
- Sets store unique values and make membership checks fast.
- Choose the collection that matches the shape of the data.

---

*Next lesson -> **Lesson 14: File Handling & Error Handling**  
Previous lesson -> **Lesson 12: Lists & Tuples***
