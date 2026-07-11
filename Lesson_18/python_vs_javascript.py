# Python version: same ideas as the JavaScript file, different syntax.

# Print output
print("Hi from Python")

# Variable
age = 25

# Constant-style variable
# Python does not have a true const keyword. By convention, uppercase means
# "do not change this value".
MAX_AGE = 120

# Function
def greet(name):
    return "Hello, " + name + "!"


# If statement
if age > 18:
    print("Adult")

# List
skills = ["HTML", "CSS"]

# Dictionary
student = {
    "name": "Sara",
    "age": age,
    "skills": skills
}

# Use the function and print the data
print(greet(student["name"]))
print(student)
print("Maximum age:", MAX_AGE)
