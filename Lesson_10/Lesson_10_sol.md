# Lesson 10 — Solutions

## Project A — Quiz Game

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
