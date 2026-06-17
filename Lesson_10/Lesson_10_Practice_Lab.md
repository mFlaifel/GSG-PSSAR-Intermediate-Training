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
