# Lesson 10 — Practice Lab: Python Basics

**Phase 2 — Python Core | Duration: 2 Hours**

---

## 🎯 Lesson Overview

This is a **hands-on coding lab**. There are no new concepts today — instead, you will apply everything from Lessons 05–09 by building complete projects from scratch. 

The goal is to:

- Consolidate your understanding of variables, types, operators, conditions, loops, and functions
- Practice reading and writing real Python code
- Experience AI-assisted debugging using Claude or GitHub Copilot
- Build confidence through working software

---

## How This Lab Works

| Time        | Activity                                   |
|-------------|--------------------------------------------|
| 0:00–0:10   | Warm-up challenges                         |
| 0:10–0:55   | Project A — Quiz Game                      |
| 0:55–1:40   | Project B — Number Guessing Game           |
| 1:40–2:00   | Debugging practice & AI-assisted workflow  |

Choose **one main project** to build in full, or do both if you finish early. Read the full spec before writing any code.

---

## Warm-Up Challenges (10 min)

Solve these quickly in a scratch file. They cover key concepts from each lesson.

**W1 — Types and conversion (Lesson 05)**
What does this code print? Answer before running it.
```python
x = "3"
y = 2
print(x * y)
print(int(x) * y)
print(type(int(x) + y))
```

**W2 — Operators (Lesson 06)**
Without running the code, what is the value of `result`?
```python
result = 5 + 3 * 2 ** 2 - 10 // 3 % 2
```

**W3 — Conditions (Lesson 07)**
What does this print for `score = 75`?
```python
score = 75
label = "Pass" if score >= 60 else "Fail"
print(f"{'High ' if score >= 80 else ''}{label}")
```

**W4 — Loops (Lesson 08)**
What is the final value of `total`?
```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        continue
    total += i
```

**W5 — Functions (Lesson 09)**
What does this return? What does it print?
```python
def mystery(n):
    if n <= 1:
        return 1
    return n * mystery(n - 1)

print(mystery(5))
```

---

## Project A — Quiz Game

### Spec

Build a **multiple-choice quiz game** that:

1. Shows 5 questions one at a time, each with 4 options (A, B, C, D)
2. Accepts the player's answer (case-insensitive)
3. Tells the player immediately if they were right or wrong
4. Keeps a running score
5. Shows a final result with score, percentage, and a message based on performance
6. Allows the player to quit early by typing `"quit"`

---

### Starter Structure

Plan your functions **before** writing code:

```
show_welcome()         → print banner and rules
ask_question()         → display one question and return True/False
calculate_grade()      → return a letter grade from a percentage
show_results()         → display the final scoreboard
run_quiz()             → main game loop (calls the above)
```

---

### Question Data

Copy this data structure (you'll learn dictionaries deeply in Lesson 13):

```python
questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "define", "D": "function"},
        "answer": "B"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3.0", "C": "3", "D": "4"},
        "answer": "C"
    },
    {
        "question": "Which of these is a falsy value in Python?",
        "options": {"A": '"False"', "B": "1", "C": "0", "D": "-1"},
        "answer": "C"
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": {
            "A": "Skips to the next iteration",
            "B": "Restarts the loop from the beginning",
            "C": "Exits the loop immediately",
            "D": "Pauses the loop for 1 second"
        },
        "answer": "C"
    },
    {
        "question": "What is the correct way to call a function named 'greet' with argument 'Alice'?",
        "options": {"A": "greet['Alice']", "B": "call greet('Alice')", "C": "greet.Alice", "D": "greet('Alice')"},
        "answer": "D"
    },
]
```

---

### Full Solution

Build your own version first. Use this as reference only after attempting it yourself.

```python
# quiz_game.py
# Phase 2 Practice Lab — Quiz Game

questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "define", "D": "function"},
        "answer": "B"
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3.0", "C": "3", "D": "4"},
        "answer": "C"
    },
    {
        "question": "Which of these is a falsy value in Python?",
        "options": {"A": '"False"', "B": "1", "C": "0", "D": "-1"},
        "answer": "C"
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": {
            "A": "Skips to the next iteration",
            "B": "Restarts the loop from the beginning",
            "C": "Exits the loop immediately",
            "D": "Pauses the loop for 1 second"
        },
        "answer": "C"
    },
    {
        "question": "What is the correct way to call a function named 'greet' with argument 'Alice'?",
        "options": {"A": "greet['Alice']", "B": "call greet('Alice')", "C": "greet.Alice", "D": "greet('Alice')"},
        "answer": "D"
    },
]


# ── Helper functions ──────────────────────────────────────────────

def show_welcome():
    """Print the welcome banner and rules."""
    print("=" * 45)
    print("       🐍 PYTHON KNOWLEDGE QUIZ 🐍")
    print("=" * 45)
    print(f"  Questions : {len(questions)}")
    print("  Options   : A, B, C, or D")
    print("  Type 'quit' at any time to exit")
    print("=" * 45)
    print()


def display_question(number, total, question_data):
    """Display a single question with its options."""
    print(f"Question {number}/{total}")
    print("-" * 40)
    print(f"  {question_data['question']}")
    print()
    for key, value in question_data["options"].items():
        print(f"  {key}) {value}")
    print()


def get_answer():
    """Prompt the user and return a valid answer or 'quit'."""
    valid_choices = ["a", "b", "c", "d", "quit"]
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer in valid_choices:
            return answer
        print("  ⚠️  Please enter A, B, C, D, or 'quit'.")


def check_answer(user_answer, correct_answer):
    """Return True if the user's answer matches the correct answer."""
    return user_answer.upper() == correct_answer.upper()


def calculate_grade(percentage):
    """Return a letter grade and message based on percentage."""
    if percentage >= 90:
        return "A", "🏆 Outstanding! You really know your Python!"
    elif percentage >= 75:
        return "B", "🎉 Great job! Solid Python knowledge."
    elif percentage >= 60:
        return "C", "✅ Good effort. Keep practising!"
    elif percentage >= 40:
        return "D", "📖 Keep studying — you're getting there."
    else:
        return "F", "💪 Review the lessons and try again!"


def show_results(score, total, quit_early):
    """Display the final scoreboard."""
    percentage = (score / total) * 100
    grade, message = calculate_grade(percentage)

    print()
    print("=" * 45)
    if quit_early:
        print("  You quit the quiz early.")
    print("       📊 YOUR RESULTS")
    print("=" * 45)
    print(f"  Score      : {score} / {total}")
    print(f"  Percentage : {percentage:.1f}%")
    print(f"  Grade      : {grade}")
    print("-" * 45)
    print(f"  {message}")
    print("=" * 45)


# ── Main Game Loop ────────────────────────────────────────────────

def run_quiz():
    """Run the full quiz game."""
    show_welcome()

    score      = 0
    quit_early = False

    for i, question_data in enumerate(questions, start=1):
        display_question(i, len(questions), question_data)
        user_answer = get_answer()

        if user_answer == "quit":
            quit_early = True
            answered   = i - 1
            break

        if check_answer(user_answer, question_data["answer"]):
            print("  ✅ Correct!\n")
            score += 1
        else:
            correct_key   = question_data["answer"]
            correct_value = question_data["options"][correct_key]
            print(f"  ❌ Wrong. The correct answer was {correct_key}) {correct_value}\n")

        answered = i

    show_results(score, answered if quit_early else len(questions), quit_early)


# ── Entry Point ───────────────────────────────────────────────────

run_quiz()
```

---

## Project B — Number Guessing Game

### Spec

Build a **number guessing game** that:

1. Generates a random secret number between 1 and 100
2. Gives the player a configurable number of attempts (default: 7)
3. Provides directional hints: "Too low", "Too high", "Getting warmer"
4. Displays a hint about how far away the guess is (cold/warm/hot)
5. Tracks the player's best score across multiple rounds
6. Asks if the player wants to play again after each round

---

### Starter Structure

```
get_hint()          → returns "cold", "warm", or "hot" based on distance
play_round()        → runs one game round, returns number of guesses taken
show_leaderboard()  → prints all round scores
main()              → outer loop for multiple rounds
```

---

### Full Solution

```python
# guessing_game.py
# Phase 2 Practice Lab — Number Guessing Game

import random


# ── Constants ─────────────────────────────────────────────────────

MIN_NUMBER  = 1
MAX_NUMBER  = 100
MAX_GUESSES = 7


# ── Helper functions ──────────────────────────────────────────────

def show_welcome():
    """Print the game banner."""
    print()
    print("╔══════════════════════════════════╗")
    print("║   🎯 NUMBER GUESSING GAME 🎯     ║")
    print("╠══════════════════════════════════╣")
    print(f"║  Range    : {MIN_NUMBER} – {MAX_NUMBER}                  ║")
    print(f"║  Attempts : {MAX_GUESSES}                          ║")
    print("╚══════════════════════════════════╝")
    print()


def get_temperature_hint(guess, secret):
    """
    Return a temperature emoji hint based on how far the guess is.

    Parameters:
        guess  (int): The player's guess.
        secret (int): The secret number.

    Returns:
        str: '🥶 Ice cold', '😐 Warm', or '🔥 Hot!'
    """
    distance = abs(guess - secret)
    if distance > 30:
        return "🥶 Ice cold"
    elif distance > 10:
        return "😐 Warm"
    else:
        return "🔥 Hot!"


def get_direction_hint(guess, secret):
    """Return 'Too low' or 'Too high' based on the comparison."""
    if guess < secret:
        return "📈 Too low!"
    return "📉 Too high!"


def play_round():
    """
    Run one round of the guessing game.

    Returns:
        int: Number of guesses used (MAX_GUESSES + 1 if player lost).
    """
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f"I'm thinking of a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_GUESSES} attempts. Good luck!\n")

    for attempt in range(1, MAX_GUESSES + 1):
        # Get a valid guess from the player
        while True:
            try:
                guess = int(input(f"Attempt {attempt}/{MAX_GUESSES} — Your guess: "))
                if MIN_NUMBER <= guess <= MAX_NUMBER:
                    break
                print(f"  ⚠️  Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
            except ValueError:
                print("  ⚠️  Please enter a valid integer.")

        # Correct!
        if guess == secret:
            if attempt == 1:
                print(f"\n🎉 Unbelievable! You got it on the first try!")
            else:
                print(f"\n🎉 Correct! You found {secret} in {attempt} attempt(s)!")
            return attempt

        # Wrong — give hints
        direction = get_direction_hint(guess, secret)
        temp      = get_temperature_hint(guess, secret)
        remaining = MAX_GUESSES - attempt

        print(f"  {direction}  |  {temp}  |  {remaining} attempt(s) left.\n")

    # Out of attempts
    print(f"\n😞 Out of attempts! The number was {secret}.")
    return MAX_GUESSES + 1   # signal: player lost


def show_leaderboard(scores):
    """Print all round scores in a formatted table."""
    print()
    print("═" * 35)
    print("        📊 LEADERBOARD")
    print("═" * 35)

    for i, score in enumerate(scores, start=1):
        if score <= MAX_GUESSES:
            bar    = "★" * score + "☆" * (MAX_GUESSES - score)
            result = f"{score} guess(es)"
        else:
            bar    = "✗" * MAX_GUESSES
            result = "Lost"
        print(f"  Round {i}: {result:14}  {bar}")

    # Best round (lowest guesses, losses excluded)
    wins = [s for s in scores if s <= MAX_GUESSES]
    if wins:
        print("-" * 35)
        print(f"  🏆 Best round: {min(wins)} guess(es)")

    rounds_won  = len(wins)
    rounds_lost = len(scores) - rounds_won
    print(f"  Won: {rounds_won}   Lost: {rounds_lost}")
    print("═" * 35)


# ── Main Program ──────────────────────────────────────────────────

def main():
    """Outer loop — lets the player play multiple rounds."""
    show_welcome()

    scores = []

    while True:
        result = play_round()
        scores.append(result)

        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            break
        print()

    show_leaderboard(scores)
    print("\nThanks for playing! 🐍")


main()
```

---

## Part 3 — Debugging and AI: Applying Lessons 03 & 04 to Python (20 min)

You covered the 6-step debugging methodology in Lesson 03 and the full AI prompting workflow in Lesson 04. This section is not a repeat — it's a **Python-specific application** of those tools.

### Python Error Taxonomy

Lesson 03 gave you the full exception table. Here is how that maps to the Python code you are now writing, with the errors most likely to appear at your current level:

| Error               | Lesson 03 covered? | Where it typically appears in L05–L09 code              |
|---------------------|--------------------|---------------------------------------------------------|
| `SyntaxError`       | ✅                  | Missing `:` after `if`/`for`/`def`, unmatched brackets  |
| `IndentationError`  | ✅ (as SyntaxError) | Mixed tabs and spaces, wrong body indentation           |
| `NameError`         | ✅                  | Using a variable before assigning it                    |
| `TypeError`         | ✅                  | `"Score: " + 85` instead of `"Score: " + str(85)`      |
| `ValueError`        | ✅                  | `int(input(...))` when user types letters               |
| `ZeroDivisionError` | (new for L05–L09)  | `average = total / len(scores)` when `scores` is empty  |
| `IndexError`        | ✅                  | `text[99]` when the string is shorter than 99 chars     |

> 📎 **Reminder:** Read the stack trace bottom-up. The last line is the error; the lines above tell you *how you got there*. This was demonstrated in Lesson 03 with the `KeyError: 'price'` example.

---

### Exercise: Buggy Code — Apply the Full Workflow

The code below contains **5 deliberate bugs**. Apply the Lesson 03 process:
1. Read the error message — what type is it? What line?
2. Isolate: which of the 5 bug categories (syntax, type, logic, indentation, missing conversion)?
3. Form a hypothesis before changing anything.
4. Fix one bug at a time and re-run.

```python
# buggy_score_tracker.py — contains 5 bugs

def calculate_average(scores)       # Bug 1
    total = 0
    for score in scores:
        total = total + score
    average = total / len(scores)
    return average

def classify(average):
    if average >= 90               # Bug 2
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50             # Bug 3
        return "Average"
    else:
        return "Needs Improvement"

student_name = input("Student name: ")
raw_scores   = input("Enter 5 scores separated by commas: ")
scores_list  = raw_scores.split(",")

# Bug 4: scores_list contains strings — calculate_average will fail on addition
average = calculate_average(scores_list)
rating  = classify(average)

print(f"\nStudent : {student_name}")
print(f"Average : {round(average, 1))}")   # Bug 5: extra closing bracket
print(f"Rating  : {rating}")
```

---

### Applying the Lesson 04 AI Debugging Workflow to Python

Lesson 04 gave you the full template for a debugging prompt. Here is that template filled in with a **real Python error** you might produce from this phase:

```
Language: Python 3.12

Error:
  TypeError: unsupported operand type(s) for +: 'int' and 'str'
  File "score_tracker.py", line 6, in calculate_average
    total = total + score

Expected behaviour:
  calculate_average(["85", "90", "72"]) should return 82.33

Actual behaviour:
  Crashes with TypeError on the first iteration

Relevant code:
  def calculate_average(scores):
      total = 0
      for score in scores:
          total = total + score   # line 6
      return total / len(scores)

I think the issue is that scores contains strings, not numbers.
Is that correct, and what is the safest fix?
```

Notice the structure: language + exact error + expected behaviour + actual behaviour + code + your hypothesis. This is the Lesson 04 prompt anatomy applied to a real Python problem. The hypothesis at the end is important — it forces you to think before the AI answers, so you are learning, not just copying.

> ⚠️ **One rule that hasn't changed from Lesson 04:** Never paste the AI's fix without understanding it. If the fix uses syntax or a built-in you haven't seen, ask: *"Can you explain why this works?"*

---

## ✅ Bonus Challenges

If you finish both projects, try these extensions:

**Quiz Game — Extensions**
- Add a timer: give the player 15 seconds per question
- Randomise question order using `random.shuffle(questions)`
- Add a "50/50" lifeline that removes 2 wrong answers

**Guessing Game — Extensions**
- Let the player choose difficulty: Easy (1–50, 10 guesses), Medium (1–100, 7 guesses), Hard (1–200, 5 guesses)
- Add a hint system: for 1 point penalty, reveal if the secret number is even or odd
- Save the high score to a file (preview of Lesson 14!)

---

## 🔑 Key Takeaways

- Writing complete programs from scratch is where all prior lessons click together.
- Plan your function decomposition (Lesson 09 + SRP from Lesson 03) before writing any code.
- Apply the Lesson 03 stack-trace process: identify error type, isolate the line, form a hypothesis, fix, verify.
- Apply the Lesson 04 prompt anatomy when asking AI: language + error + expected vs actual + code + your hypothesis.
- The most important rule from both L03 and L04 still holds: understand every line before you ship it.

---

## 📚 Phase 2 Recap — What You Now Know

| Lesson | Skill                       |
|--------|------------------------------|
| 05     | Variables, data types, I/O   |
| 06     | Operators, strings, f-strings, type conversion |
| 07     | Conditions and branching     |
| 08     | Loops — `for`, `while`, `break`, `continue` |
| 09     | Functions, DRY, built-ins    |
| 10     | Full programs + debugging    |

---

*Next phase → **Phase 3 — Python Advanced (Lessons 11–15)**  
Previous lesson → **Lesson 09: Functions I — Basics***
