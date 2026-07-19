# Lesson 20 — Capstone Project & Next Steps

**Phase 5 — Backend & Final Project** | **Duration: 2 Hours** | **Session 20 of 20 (Final Session)**

---

## Session Objectives

By the end of this session, students will be able to:

- Combine Python, Flask, HTML, CSS, and JavaScript into one working mini-application
- Connect a frontend page to a backend Flask route
- Present and explain a small project they built
- Identify at least one career path in tech that interests them
- Name concrete next steps and resources to keep learning after the course ends

---

## Big Idea

This final session turns the course into one complete loop:

**Python logic → Flask route → JSON response → JavaScript fetch → DOM update**

Students do not need to build a large app. The goal is to build a small app where every layer connects.

### Today's Build

Each student or pair will create a mini full-stack project with:

- A Flask backend
- At least one JSON API route
- A frontend page
- JavaScript that calls the backend using `fetch()`
- A short presentation of what they built

---

## Timed Breakdown

| Time           | Segment                                     | Format                       |
| -------------- | ------------------------------------------- | ---------------------------- |
| 0:00–0:10      | Recap the full course arc, frame the finale | Discussion                   |
| 0:10–0:25      | Capstone project brief & requirements       | Lecture + live demo          |
| 0:25–0:45      | Guided build: connecting frontend to Flask  | Live coding, students follow |
| 0:45–1:15      | Structured work time                        | Independent/paired work      |
| 1:15–1:25      | **Break**                                   | —                            |
| 1:25–1:45      | Continued work time + roaming support       | Independent/paired work      |
| 1:45–2:00      | Mini-presentations / share-outs             | Student-led                  |
| If time allows | Career paths & next steps                   | Discussion                   |

> **Facilitator note**: this session runs tight. If class size is large, consider extending presentations into a follow-up session, or capping each share-out to 60–90 seconds so everyone gets a turn.

---

## 1. Recap the Full Course Arc (10 min)

Before building, zoom out. Put the phase table on screen and walk through it as a story, not a list:

```
Phase 1 → How to THINK like a programmer
Phase 2 → Python fundamentals — the LOGIC
Phase 3 → Data structures, files, libraries — the TOOLS
Phase 4 → HTML, CSS, JS — the FRONTEND (what users see)
Phase 5 → Flask, APIs — the BACKEND (what powers it)
```

Today's project uses a piece from every phase. Say this clearly so students can recognize how much they have built up across the course.

---

## 2. Capstone Project Brief (15 min)

### The Project: A Mini Full-Stack App

Students build a small application with:

1. **Backend**: a Flask app with at least one route that returns JSON data (reusing patterns from Lesson 19)
2. **Frontend**: an HTML/CSS page (Lesson 17) that uses JavaScript's `fetch()` (new — introduced today) to call that route and display the result (Lesson 18's DOM skills)
3. **Logic**: at least one piece of real Python logic behind the data (a function, a loop, a calculation — reusing Phases 2–3 skills)

**Suggested project options** (offer choice — ownership drives engagement on a capstone):

| Project Idea         | Backend Logic                               | Frontend Display                        |
| -------------------- | ------------------------------------------- | --------------------------------------- |
| Quote/fact generator | Random pick from a Python list              | Button that fetches a new quote         |
| Simple to-do list    | Store/return a list of tasks                | Add/display tasks on the page           |
| Grade calculator     | Take inputs, calculate average/letter grade | Form that submits and shows result      |
| Mini quiz app        | Store questions, check answers              | Show question, check click, show result |

Keep scope deliberately small — the goal is _connecting the full pipeline end-to-end_, not building something elaborate.

### Minimum Project Requirements

Every project should include:

- `app.py`
- A `static/index.html` file
- At least one Flask route that returns JSON
- At least one `fetch()` call in JavaScript
- At least one DOM update based on the response

Recommended folder structure:

```text
project/
├── app.py
└── static/
    └── index.html
```

### Good Scope vs. Too Much Scope

| Good for today                        | Too much for today        |
| ------------------------------------- | ------------------------- |
| One button, one API route, one result | Login system              |
| A small list stored in Python         | Full database setup       |
| Simple styling                        | Complex responsive design |
| One calculation                       | Many pages and features   |

---

## 3. Guided Build: Connecting Frontend to Backend (20 min)

This is the one genuinely new technique of the session: calling a Flask API from JavaScript using `fetch()`. Live-code this full example before releasing students to their own projects.

### Backend (`app.py`)

```python
from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Code is read more often than it is written.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency."
]

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/api/quote")
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    app.run(debug=True)
```

### Frontend (`static/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Quote Generator</title>
  </head>
  <body>
    <h1>Random Quote Generator</h1>
    <p id="quoteText">Click the button for a quote.</p>
    <button id="quoteBtn">New Quote</button>

    <script>
      const button = document.querySelector("#quoteBtn");
      const quoteText = document.querySelector("#quoteText");

      button.addEventListener("click", function () {
        fetch("/api/quote")
          .then((response) => response.json())
          .then((data) => {
            quoteText.textContent = data.quote;
          });
      });
    </script>
  </body>
</html>
```

### Walking Through `fetch()`

| Line                                 | What it does                                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `fetch("/api/quote")`                | Sends a GET request to the Flask route — this is JavaScript's version of Lesson 19's `requests.get()` |
| `.then(response => response.json())` | Converts the raw response into usable JSON                                                            |
| `.then(data => { ... })`             | Runs once the data is ready — updates the DOM                                                         |

> Name the symmetry explicitly: **Python's `requests` library (Lesson 19) and JavaScript's `fetch()` do the same job on two different sides of the client-server line from Lesson 16.** This is the full circle moment of the course.

Note on file structure: Flask looks for frontend files in a `static/` folder by default — mention this briefly so students don't lose time to a file-path error mid-build.

### Full Pipeline Trace

When the button is clicked:

1. JavaScript runs the click handler
2. `fetch("/api/quote")` sends a GET request
3. Flask receives the request at `/api/quote`
4. Python chooses a random quote
5. Flask returns JSON
6. JavaScript reads the JSON
7. The DOM updates on the page

This is the whole course working together.

---

## 4. Structured Work Time (45 min total, with break)

Let students choose to work solo or in pairs. Circulate constantly — this session lives or dies on hands-on support, not lecture.

**Suggested checkpoints to announce partway through:**

- 15 min in: "You should have your Flask route returning JSON in the browser directly."
- 30 min in: "You should have your HTML page loading and your button wired up, even if it's not fetching data yet."
- 40 min in: "Aim to have _something_ fetching and displaying, even if it's not fully polished — a working simple version beats an unfinished ambitious one."

This staged pacing mirrors the debugging methodology from Lesson 03 — build the smallest working piece first, then extend.

### Debugging Order

When something breaks, check in this order:

1. Is the Flask server running?
2. Does the API route work directly in the browser?
3. Is `index.html` loading from the `static/` folder?
4. Does the button click handler run? Use `console.log("clicked")`.
5. Does `fetch()` return data? Log the `data` object.
6. Is the DOM selector correct?

This gives students a calm path through the most common capstone bugs.

---

## 5. Mini-Presentations (15 min)

Each student or pair gets ~60–90 seconds to:

1. Show their project running
2. Name one thing that was tricky and how they solved it (or didn't yet — that's fine)

Keep the tone celebratory, not evaluative. The goal is to help students notice what they can now build.

### Presentation Prompts

Students can use this simple script:

- "My project is..."
- "The Flask route does..."
- "The JavaScript fetches..."
- "One problem I solved was..."
- "One thing I would add next is..."

---

## 6. Career Paths & Next Steps (Discussion)

### Career Paths in Tech

Briefly map the paths that build on what was just covered, without diving deep into any one:

| Path                      | What it builds on from this course                     |
| ------------------------- | ------------------------------------------------------ |
| **Web Development**       | Phases 4–5 — HTML/CSS/JS, Flask, APIs                  |
| **Data / Data Analysis**  | Phase 3 — files, `pandas`, structured data             |
| **AI / Machine Learning** | Lesson 04's AI tools + Python foundations (Phases 2–3) |
| **Systems / DevOps**      | Lesson 16's client-server model, servers, networks     |

### Resources for Continued Learning

- [CS50x: Introduction to Computer Science](https://cs50.harvard.edu/x/) — a strong next step for students who want a deeper computer science foundation
- [roadmap.sh](https://roadmap.sh/) — visual learning paths for frontend, backend, full-stack, Python, Git/GitHub, data, AI, and more
- [GitHub Student Developer Pack](https://education.github.com/pack) — free and discounted developer tools for verified students
- [GitHub Skills](https://skills.github.com/) — short hands-on practice courses for Git, GitHub, publishing projects, and collaboration
- [GitHub Docs: Setting up your profile](https://docs.github.com/en/get-started/start-your-journey/setting-up-your-profile) — guidance for making a student GitHub profile presentable
- University computer science program pathways, for students considering formal study
- Open-source contribution as a way to keep building real skills
- Building small personal projects — the single best predictor of continued growth after any bootcamp-style course
- Continuing to use AI tools deliberately (Lesson 04) as a learning accelerator, not a shortcut around understanding

### Suggested Next Projects

- Improve the capstone with better styling
- Add a second API route
- Save data to a file
- Rebuild a small page from a website they like
- Create a GitHub profile and publish one project

### Closing Framing

Bring the course back to its opening line from Lesson 01 (or Mohammed's preferred framing): the course started with _how to think_, not _what to type_. That mindset — decomposition, debugging, reading errors, breaking problems down — is the actual transferable skill; every specific tool covered (Flask, this version of JavaScript, this specific syntax) will change over a career, but the thinking underneath it won't.

---

## Common Beginner Mistakes

- File path issues serving the HTML from Flask's `static/` folder
- Forgetting `.then()` chaining syntax in `fetch()` — easy to drop a `.then()` or misplace a bracket
- Scope creep — pairs trying to build something too large for the time available; redirect toward the smallest working version early
- Forgetting that `fetch("/api/quote")` only works when the HTML is served by Flask, not opened directly as a local file
- Updating the wrong DOM element because the selector does not match the HTML

---

## Facilitator Notes for Course Wrap-Up

- Collect final projects (screenshots, GitHub links, or in-class demo is enough — no need for formal grading infrastructure)
- Consider a short anonymous feedback form on the course itself
- If a certificate or completion note is part of the program, this is the natural session to distribute it

---

## Course Complete

This closes all 20 sessions across the 5 phases — from computational thinking with no prior background, through Python fundamentals and advanced topics, into a working full-stack mini-project. Students should leave with a technical foundation and the confidence to keep learning independently.
