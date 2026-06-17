# quiz_game.py
# Phase 2 Practice Lab — Quiz Game

questions = [
    {
        "question": "What keyword is used to define a function in Python?",
        "options": {"A": "func", "B": "def", "C": "define", "D": "function"},
        "answer": "B",
    },
    {
        "question": "What is the output of: print(10 // 3)?",
        "options": {"A": "3.33", "B": "3.0", "C": "3", "D": "4"},
        "answer": "C",
    },
    {
        "question": "Which of these is a falsy value in Python?",
        "options": {"A": '"False"', "B": "1", "C": "0", "D": "-1"},
        "answer": "C",
    },
    {
        "question": "What does the 'break' statement do in a loop?",
        "options": {
            "A": "Skips to the next iteration",
            "B": "Restarts the loop from the beginning",
            "C": "Exits the loop immediately",
            "D": "Pauses the loop for 1 second",
        },
        "answer": "C",
    },
    {
        "question": "What is the correct way to call a function named 'greet' with argument 'Alice'?",
        "options": {
            "A": "greet['Alice']",
            "B": "call greet('Alice')",
            "C": "greet.Alice",
            "D": "greet('Alice')",
        },
        "answer": "D",
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


def run_quiz():
    """Run the full quiz game."""
    print("write logic her")
