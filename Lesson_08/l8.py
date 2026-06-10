# for i in range(11, 1, -1):  # [1,...... 10000]
#     print(i)

# for letter in "Python":
#     print(letter)


# fruits = ["apple", "banana", "cherry", "mango"]

# for fruit in fruits:
#     print(f"I like {fruit}")


# students = ["Alice", "Bruno", "Carla", "Daniel"]

# for index, name in enumerate(students):
#     print(f"{index}. {name}")


# student_scores = {"Alice": 92, "Bruno": 78, "Carla": 85}

# for student, score in student_scores.items():
#     # print(f"student name: {student}, score: {score}")
#     print(f"key: {student}, value: {score}")


# student_scores = {"Alice": 92, "Bruno": 50, "Carla": 85}

# student_new_scores = {}
# print("students scores dictionary before", student_scores)
# # for student in student_scores.keys():
# #     # print(f"student name: {student}, score: {score}")
# #     print(f"key: {student}")


# for student, score in student_scores.items():
#     if score >= 60:
#         student_new_scores[student] = "pass"
#     else:
#         student_new_scores[student] = "fail"

# print("students scores dictionary after", student_scores)


# for row in range(1, 6):
#     for col in range(1, 6):
#         print(f"{row * col:3}", end="")
#     print()  # newline after each row


# while

# count = 1

# while count <= 5:  # True => false
#     print(f"Count: {count}")
#     count += 1  # IMPORTANT: update the variable or loop runs forever!

# print("Done!")

# x = 1
# while x > 0:  # true
#     print(x)

# while True:
#     age = int(input("Enter your age (1–120): "))
#     if 1 <= age <= 120:
#         break  # valid input: exit the loop
#     print("Invalid age. Try again.")

# print(f"Your age is {age}.")

# import time  # standard library (Lesson 15 covers this in detail)

# seconds = int(input("Start countdown from: "))  # =>10

# while seconds > 0:
#     print(f"⏱  {seconds}...")
#     time.sleep(1)  # pause for 1 second
#     seconds -= 1

# print("🚀 Lift off!")


# for second in range(seconds, 0, -1):
#     print(f"⏱  {second}...")
#     time.sleep(1)  # pause for 1 second


# for n in range(1, 20):
#     if n % 2 == 0:
#         print(f"First even number: {n}")
#         break  # stop the loop; no point checking further


# MAX_ATTEMPTS = 3
# password = "secret123"

# for attempt in range(1, MAX_ATTEMPTS + 1):
#     guess = input(f"Attempt {attempt}/{MAX_ATTEMPTS} — Enter password: ")
#     if guess == password:
#         print("✅ Access granted!")
#         break
#     else:
#         print("❌ Wrong password.")
# else:
#     # This runs only if the loop completed WITHOUT hitting break
#     print("🔒 Account locked.")


# Print only odd numbers from 1 to 10
# for n in range(1, 11):
#     if n % 2 == 0:
#         continue  # skip even numbers
#     print(n, end=" ")
# # Output: 1 3 5 7 9


# Search for a target value
# numbers = [4, 7, 5, 9, 1, 13]
# target = 5

# for n in numbers:
#     if n == target:
#         print(f"Found {target}!")
#         break
# else:
#     print(f"{target} was not found in the list.")
# Output: 5 was not found in the list.


# text = "Programming is fun and programming is powerful"
# word = "programming"
# count = 0

# print("text.lower().split()", text.lower().split())

# for w in text.lower().split():
#     if w == word:
#         count += 1

# print(f"'{word}' appears {count} time(s).")  # 2 times


# Create a row of stars
# width = 20
# row = ""

# for _ in range(width):  # _ is a convention for "I don't use this variable"
#     row += "*"

# print(row)  # ********************

# names = ["Alice", "Bruno", "Carla"]
# name_lengths = {}

# for name in names:
#     name_lengths[name] = len(name)

# print(name_lengths)  # {'Alice': 5, 'Bruno': 5, 'Carla': 5}


# import random

# secret = 44
# guesses = 0
# MAX = 7

# print("=== NUMBER GUESSING GAME ===")
# print("I'm thinking of a number between 1 and 100.")
# print(f"You have {MAX} attempts.\n")

# for _ in range(1, MAX + 1):
#     guess = int(input(f"Attempt {guesses + 1}/{MAX} — Your guess: "))
#     guesses += 1

#     if guess < secret:
#         print("📈 Too low!\n")
#     elif guess > secret:
#         print("📉 Too high!\n")
#     else:
#         print(f"🎉 Correct! You got it in {guesses} attempt(s)!")
#         break
# else:
#     print(f"😞 Game over! The number was {secret}.")


# n = int(input("Generate times table for: "))

# print(f"\n  TIMES TABLE FOR {n}")
# print("-" * 25)

# for i in range(1, 13):
#     print(f"  {n:2} × {i:2} = {n * i:4}")


# colour = "red"


# text = "hello"

# text[0] = "H"
