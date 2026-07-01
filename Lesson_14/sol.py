# def show_tasks():
#     tasks = []

#     try:
#         with open("tasks.txt", "r") as file:
#             tasks = file.readlines()
#     except FileNotFoundError:
#         tasks = []

#     for task in tasks:
#         print(task.strip())


# show_tasks()

import csv

total_score = 0
valid_students = 0

with open("./Lesson_14/students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    # print(str(reader))
    for row in reader:
        try:
            score = int(row["score"])

            print(f"{row['name']} ({row['track']}): {score}")

            total_score += score
            valid_students += 1

        except ValueError:
            print(
                f"Skipping row for {row['name']}: "
                f"invalid score '{row['score']}'"
            )

if valid_students > 0:
    average = total_score / valid_students
    print(f"\nAverage score: {average:.2f}")
else:
    print("\nNo valid scores found.")