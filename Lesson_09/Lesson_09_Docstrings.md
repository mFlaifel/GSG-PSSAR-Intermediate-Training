# Lesson 09 - Python Docstrings

## Introduction to Docstrings

A **docstring** is a short description written inside Python code to explain what a function, class, module, or method does.

In Python, a docstring is written using triple quotes:

```python
"""This is a docstring."""
```

Docstrings are usually placed as the first statement inside a function.

Example:

```python
def greet_user(name):
    """Print a greeting message for the user."""
    print(f"Hello, {name}!")
```

The docstring explains the purpose of the function before the function code starts.

---

## Why Use Docstrings?

Docstrings help make code easier to understand, especially when other people read your code later.

Use docstrings because they:

- Explain what a function does
- Make your code more readable
- Help other developers understand your work
- Remind you what your own code does when you return to it later
- Can be shown by Python tools such as `help()`

Example:

```python
def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


help(add_numbers)
```

The `help()` function can read and display the docstring.

---

## How to Use Docstrings in Functions

To write a docstring in a function, place it directly under the function definition.

Basic structure:

```python
def function_name(parameters):
    """Explain what the function does."""
    # function code
```

Example:

```python
def calculate_area(width, height):
    """Return the area of a rectangle."""
    return width * height
```

For simple functions, one short sentence is enough.

For functions with parameters and return values, you can write a longer docstring.

Example:

```python
def calculate_total(price, quantity):
    """
    Return the total cost for an item order.

    Parameters:
        price: The price of one item.
        quantity: The number of items.

    Returns:
        The total cost.
    """
    return price * quantity
```

### Good Docstring Tips

- Start with a capital letter
- Use clear and simple language
- Describe what the function does, not every line of code
- Keep short docstrings on one line
- Use longer docstrings when the function has important parameters or return values

Good example:

```python
def is_even(number):
    """Return True if the number is even."""
    return number % 2 == 0
```

Not very helpful:

```python
def is_even(number):
    """This function uses modulo and compares the result with zero."""
    return number % 2 == 0
```

The first docstring is better because it explains the purpose of the function.
