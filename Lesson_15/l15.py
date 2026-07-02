import pandas as pd

students = pd.read_csv("Lesson_14/examples/students.csv")
print(students.head())
print(students["score"].mean())
