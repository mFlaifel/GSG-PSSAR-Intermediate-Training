# Why Use `with` When Opening a File?

```python
with open("tasks.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## Benefits

- Automatically opens and closes the file.
- Prevents resource leaks.
- Ensures the file is closed even if an error occurs.

## Without `with`

```python
file = open("tasks.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

You must remember to call `file.close()` yourself.

## What `with` Does Internally

```python
file = open("tasks.txt", "r")

try:
    # use file
    pass
finally:
    file.close()
```

## Summary

Use `with` because it automatically handles file cleanup and makes your code safer and cleaner.