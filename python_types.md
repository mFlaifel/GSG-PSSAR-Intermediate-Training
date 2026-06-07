# Python Types: Simple Guide With Examples

In Python, every value has a type. A type tells Python what kind of data a value is and what operations are allowed.

For example:

```python
name = "Ali"       # str: text
age = 20           # int: whole number
price = 9.99       # float: decimal number
is_student = True  # bool: true or false
```

Python is dynamically typed. That means you do not need to write the type when you create a variable. Python figures it out from the value.

```python
x = 10       # x is an int
x = "hello"  # now x is a str
```

You can check a value's type with `type()`:

```python
print(type("hello")) # <class 'str'>
print(type(10))      # <class 'int'>
```

## Quick Reference

| Type | Simple meaning | Example | Changeable? |
| --- | --- | --- | --- |
| `str` | Text | `"hello"` | No |
| `int` | Whole number | `42` | No |
| `float` | Decimal number | `3.14` | No |
| `complex` | Real + imaginary number | `3 + 4j` | No |
| `bool` | True or false | `True` | No |
| `list` | Ordered items | `[1, 2, 3]` | Yes |
| `tuple` | Ordered fixed items | `(1, 2, 3)` | No |
| `range` | Sequence of numbers | `range(5)` | No |
| `dict` | Key-value data | `{"name": "Ali"}` | Yes |
| `set` | Unique unordered items | `{1, 2, 3}` | Yes |
| `frozenset` | Fixed set | `frozenset({1, 2})` | No |
| `bytes` | Raw binary data | `b"abc"` | No |
| `bytearray` | Changeable binary data | `bytearray(b"abc")` | Yes |
| `memoryview` | View of binary data | `memoryview(b"abc")` | Depends on source |
| `NoneType` | No value | `None` | No |

## 1. Text Type: `str`

Use `str` for text.

```python
message = "Hello, Python"

print(message.upper()) # HELLO, PYTHON
print(message.lower()) # hello, python
print(len(message))    # 13
```

Strings are ordered, so you can access characters by position:

```python
word = "Python"

print(word[0])   # P
print(word[-1])  # n
print(word[0:3]) # Pyt
```

Useful string methods:

```python
text = "  hello world  "

print(text.strip())              # hello world
print(text.replace("world", "Ali")) #   hello Ali
print("a,b,c".split(","))        # ['a', 'b', 'c']
print("-".join(["a", "b", "c"])) # a-b-c
```

Use f-strings to put values inside text:

```python
name = "Sara"
age = 25

print(f"{name} is {age} years old")
```

## 2. Numeric Types

Python has three main number types: `int`, `float`, and `complex`.

### `int`

Use `int` for whole numbers.

```python
count = 10
year = 2026
negative = -5
big_number = 1_000_000 # underscores make large numbers easier to read
```

Python integers can be very large. They do not have a fixed size limit like many other languages.

```python
very_big = 999999999999999999999999999999
print(type(very_big)) # <class 'int'>
```

### `float`

Use `float` for decimal numbers.

```python
price = 19.99
temperature = 36.6
scientific = 1.5e3 # 1500.0
```

Be careful with float precision:

```python
print(0.1 + 0.2) # 0.30000000000000004
```

This happens because computers store many decimal numbers as approximations. For money, consider using `decimal.Decimal` instead of `float`.

### `complex`

Use `complex` for numbers with a real part and an imaginary part. This is common in math, science, and engineering.

```python
z = 3 + 4j

print(z.real) # 3.0
print(z.imag) # 4.0
print(abs(z)) # 5.0
```

### Common Math Operators

```python
a = 10
b = 3

print(a + b)  # 13, addition
print(a - b)  # 7, subtraction
print(a * b)  # 30, multiplication
print(a / b)  # 3.333..., normal division
print(a // b) # 3, floor division
print(a % b)  # 1, remainder
print(a ** b) # 1000, exponent
```

## 3. Boolean Type: `bool`

`bool` has only two values: `True` and `False`.

```python
is_active = True
is_done = False
```

Booleans are used in conditions:

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Some values behave like `False` in conditions. These are called falsy values:

```python
False
None
0
0.0
""
[]
{}
set()
```

Most other values are truthy:

```python
if "hello":
    print("This runs")

if [1, 2, 3]:
    print("This also runs")
```

A useful detail: `bool` is a subclass of `int`.

```python
print(True + True) # 2
```

You usually should not rely on that behavior, but it explains why the example works.

## 4. Lists: `list`

A list stores multiple values in order. Lists are changeable.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # apple
print(fruits[-1]) # cherry
```

Common list operations:

```python
fruits.append("date")      # add to the end
fruits.insert(1, "orange") # add at index 1
fruits.remove("banana")    # remove by value
last = fruits.pop()         # remove and return last item

print(fruits)
print(last)
```

Lists can contain different types, but it is often clearer when one list stores one kind of thing:

```python
scores = [90, 85, 100]
mixed = [1, "hello", True]
```

Use a list when:

- Order matters.
- You need to add, remove, or update items.
- Duplicate values are allowed.

## 5. Tuples: `tuple`

A tuple is an ordered collection that cannot be changed after it is created.

```python
point = (10, 20)

print(point[0]) # 10
print(point[1]) # 20
```

A one-item tuple needs a comma:

```python
single = (42,)
```

Tuples are useful for fixed groups of values:

```python
rgb = (255, 0, 0)
latitude_longitude = (30.0444, 31.2357)
```

You can unpack a tuple into variables:

```python
x, y = point
print(x) # 10
print(y) # 20
```

Use a tuple when:

- The values belong together.
- The values should not change.
- You want a lightweight fixed structure.

## 6. Ranges: `range`

A `range` represents a sequence of numbers. It is commonly used in loops.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Range examples:

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 6)     # 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

A `range` does not store every number in memory. It creates numbers when needed, so it is memory-efficient.

## 7. Dictionaries: `dict`

A dictionary stores key-value pairs. Use it when each value has a label.

```python
person = {
    "name": "Ali",
    "age": 20,
    "city": "Cairo"
}

print(person["name"]) # Ali
```

Access values safely with `.get()`:

```python
print(person.get("email"))        # None
print(person.get("email", "N/A")) # N/A
```

Add or update values:

```python
person["age"] = 21
person["email"] = "ali@example.com"
```

Loop through a dictionary:

```python
for key, value in person.items():
    print(key, value)
```

Dictionary keys must be hashable. Common key types are `str`, `int`, and `tuple`.

```python
scores = {
    "math": 90,
    "english": 85
}
```

Use a dictionary when:

- You want to look up values by name or key.
- Your data has labels.
- You are representing an object-like structure.

## 8. Sets: `set` and `frozenset`

A set stores unique values. It removes duplicates automatically.

```python
numbers = {1, 2, 2, 3}
print(numbers) # {1, 2, 3}
```

Sets are unordered, so you should not depend on item position.

Common set operations:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # union: values in a or b
print(a & b) # intersection: values in both
print(a - b) # difference: values in a but not b
print(a ^ b) # symmetric difference: values in one set only
```

Use a set when:

- You need unique values.
- You want fast membership checks with `in`.
- You want set operations like union and intersection.

```python
allowed_users = {"Ali", "Sara", "Mona"}

if "Sara" in allowed_users:
    print("Allowed")
```

A `frozenset` is an immutable set.

```python
fixed = frozenset([1, 2, 2, 3])
print(fixed) # frozenset({1, 2, 3})
```

Use `frozenset` when you need a set that cannot change, or when you need to use a set-like value as a dictionary key.

## 9. Binary Types

Binary types store raw bytes. You usually use them when working with files, images, network data, encryption, or encoded text.

### `bytes`

`bytes` is immutable binary data.

```python
data = b"hello"

print(data[0])       # 104
print(data.decode()) # hello
```

Text can be converted to bytes with `.encode()`:

```python
text = "hello"
encoded = text.encode("utf-8")

print(encoded) # b'hello'
```

### `bytearray`

`bytearray` is like `bytes`, but changeable.

```python
data = bytearray(b"hello")
data[0] = 72

data.append(33)
print(data) # bytearray(b'Hello!')
```

### `memoryview`

`memoryview` lets you look at binary data without copying it.

```python
data = bytearray(b"hello world")
view = memoryview(data)

print(bytes(view[6:])) # b'world'
```

This is mostly useful for performance-sensitive code.

## 10. No Value: `None`

`None` means no value.

```python
result = None
```

Use `is None` to check for it:

```python
if result is None:
    print("No result yet")
```

Do not use `== None` in normal Python code.

A common use is an optional function argument:

```python
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"
```

## 11. Mutable and Immutable Types

A mutable value can be changed after it is created.

Mutable types include:

- `list`
- `dict`
- `set`
- `bytearray`

Example:

```python
items = [1, 2, 3]
items.append(4)

print(items) # [1, 2, 3, 4]
```

An immutable value cannot be changed after it is created.

Immutable types include:

- `str`
- `int`
- `float`
- `complex`
- `bool`
- `tuple`
- `range`
- `frozenset`
- `bytes`
- `NoneType`

Example:

```python
text = "hello"
upper_text = text.upper()

print(text)       # hello
print(upper_text) # HELLO
```

The original string did not change. Python created a new string.

Important list example:

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a) # [1, 2, 3, 4]
```

`a` and `b` point to the same list. If you want a copy, use `.copy()`:

```python
b = a.copy()
```

## 12. Changing Types

You can convert values from one type to another.

```python
age_text = "20"
age_number = int(age_text)

print(age_number + 5) # 25
```

Common conversions:

```python
int("10")        # 10
float("3.14")    # 3.14
str(100)         # "100"
list("abc")      # ['a', 'b', 'c']
tuple([1, 2, 3]) # (1, 2, 3)
set([1, 1, 2])   # {1, 2}
bool(1)          # True
bool(0)          # False
```

Not every conversion works:

```python
int("hello") # ValueError
```

When converting user input, validate it first or handle errors:

```python
text = "42"

try:
    number = int(text)
    print(number)
except ValueError:
    print("Please enter a valid number")
```

## 13. Checking Types

Use `isinstance()` to check a type.

```python
value = "hello"

if isinstance(value, str):
    print("This is text")
```

Check multiple possible types:

```python
number = 10

if isinstance(number, (int, float)):
    print("This is numeric")
```

You can use `type()` when you only want to inspect the exact type:

```python
x = True

print(type(x))          # <class 'bool'>
print(type(x).__name__) # bool
```

Best practice: use `isinstance()` for most type checks because it works better with inheritance.

```python
print(isinstance(True, int)) # True
print(type(True) is int)     # False
```

## 14. Callable Types

A callable is something you can call with parentheses, like `name()`.

### Functions

Functions created with `def` are callable.

```python
def add(a, b):
    return a + b

print(add(2, 3))     # 5
print(callable(add)) # True
```

A `lambda` is a small anonymous function:

```python
double = lambda x: x * 2
print(double(5)) # 10
```

For most real code, a normal `def` function is easier to read than a `lambda`.

### Methods

A method is a function that belongs to an object.

```python
text = "hello"
print(text.upper()) # upper is a string method
```

Classes can also define methods:

```python
class Dog:
    def bark(self):
        return "Woof!"

rex = Dog()
print(rex.bark())
```

### Classes

Classes are callable too. Calling a class creates an object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(type(p)) # <class '__main__.Point'>
```

## 15. Iterators and Generators

An iterable is something you can loop over.

```python
for letter in "abc":
    print(letter)
```

Common iterables include:

- strings
- lists
- tuples
- dictionaries
- sets
- ranges

An iterator gives values one at a time.

```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
```

A generator is a simple way to create an iterator. It uses `yield`.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)
```

Output:

```text
3
2
1
```

Generators are useful because they create values lazily. That means they do not need to store everything in memory at once.

Generator expression example:

```python
squares = (x * x for x in range(5))
print(list(squares)) # [0, 1, 4, 9, 16]
```

## 16. Type Hints and Annotations

Type hints describe the type you expect. They do not force Python to check types at runtime, but they help editors, linters, and other developers.

```python
name: str = "Alice"
age: int = 30
price: float = 19.99
```

Function annotations:

```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()
```

Collection annotations:

```python
scores: list[int] = [90, 85, 100]
profile: dict[str, str] = {"name": "Ali", "city": "Cairo"}
point: tuple[int, int] = (10, 20)
```

Optional values:

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Ali"
    return None
```

Union types:

```python
def stringify(value: int | float | str) -> str:
    return str(value)
```

Type aliases give a name to a type:

```python
Vector = list[float]

def length(vector: Vector) -> float:
    return sum(x * x for x in vector) ** 0.5
```

Python 3.12 also supports the `type` statement for aliases:

```python
type UserId = int
```

## 17. Useful Types From `typing`

Modern Python can often use built-in forms like `list[str]` and `int | None`. The `typing` module is still useful for advanced cases.

| Type | Meaning | Example |
| --- | --- | --- |
| `Any` | Any type is allowed | `x: Any = "anything"` |
| `Callable` | A function-like value | `Callable[[int], str]` |
| `Iterable` | Something you can loop over | `Iterable[int]` |
| `Generator` | A generator type | `Generator[int, None, None]` |
| `TypeVar` | A generic type variable | `T = TypeVar("T")` |
| `Generic` | Builds generic classes | `class Box(Generic[T])` |
| `Literal` | Only specific values allowed | `Literal["r", "w"]` |

Example generic stack:

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
print(stack.pop()) # 2
```

## 18. Common Mistakes

### Mixing strings and numbers

```python
age = "20"

# print(age + 5) # TypeError
print(int(age) + 5) # 25
```

### Changing a list while another variable points to it

```python
a = [1, 2]
b = a
b.append(3)

print(a) # [1, 2, 3]
```

Use a copy when you need a separate list:

```python
b = a.copy()
```

### Using a mutable default argument

Avoid this:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Use `None` instead:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

### Comparing with `None` incorrectly

Use this:

```python
if value is None:
    print("No value")
```

Avoid this:

```python
if value == None:
    print("No value")
```

## Final Summary

- `str` is for text.
- `int`, `float`, and `complex` are for numbers.
- `bool` is for `True` and `False`.
- `list` is for ordered items that can change.
- `tuple` is for ordered items that should stay fixed.
- `range` is for number sequences, often in loops.
- `dict` is for key-value data.
- `set` is for unique values.
- `bytes`, `bytearray`, and `memoryview` are for binary data.
- `None` means no value.
- `isinstance()` is usually the best way to check a type.
- Type hints help explain your code, but they do not change how Python runs it.
