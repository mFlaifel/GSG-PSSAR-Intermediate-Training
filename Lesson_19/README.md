# Lesson 19 — Backend & APIs — Introduction

**Phase 5 — Backend & Final Project** | **Duration: 2 Hours** | **Session 19 of 20**

---

## Session Objectives

By the end of this session, students will be able to:

- Explain what a server does and how it differs from a client
- Define REST API, JSON, and describe the four main HTTP verbs
- Build and run a "Hello World" Flask application
- Create a simple Flask route that returns JSON
- Use Python's `requests` library to call a public API
- Describe, at a high level, what a database is and why apps need one

---

## Timed Breakdown

| Time      | Segment                                    | Format               |
| --------- | --------------------------------------------- | ----------------------- |
| 0:00–0:10 | Recap Lessons 16–18, frame Phase 5             | Discussion              |
| 0:10–0:25 | What does a server do? (revisit + deepen)      | Lecture + diagram       |
| 0:25–0:40 | REST APIs, JSON, HTTP verbs                    | Lecture + live examples |
| 0:40–1:00 | Flask hello-world application                  | Live coding, students follow |
| 1:00–1:10 | **Break**                                     | —                        |
| 1:10–1:30 | Building a JSON API route in Flask              | Live coding              |
| 1:30–1:45 | Reading API data with Python `requests`         | Live coding              |
| 1:45–1:55 | Database overview (conceptual)                  | Lecture + diagram         |
| 1:55–2:00 | Wrap-up, homework                               | Discussion                |

---

## 1. What Does a Server Do? (15 min)

Revisit the client-server diagram from Lesson 16, but now flip the perspective: **today, students become the server.**

```
        REQUEST
   ┌──────────────────────────────►
┌─────────┐                    ┌─────────┐
│ CLIENT  │                    │ SERVER  │  ← you are building this today
│(browser)│                    │ (Flask) │
└─────────┘                    └─────────┘
   ◄──────────────────────────────┘
        RESPONSE
```

A server is just a program that:
1. Stays running and **listens** on a network port
2. **Receives** incoming requests
3. **Decides** what to do based on the request (which URL, which verb)
4. **Sends back** a response

That's it — a server is not magic, it's a Python program with an extra job: staying alive and listening.

---

## 2. REST APIs, JSON, and HTTP Verbs (15 min)

### What Is an API?

An **API (Application Programming Interface)** is a defined way for two programs to talk to each other. A **REST API** is a common style of API built on top of HTTP — the same protocol from Lesson 16.

### JSON — The Common Language

JSON (JavaScript Object Notation) is the standard format APIs use to send structured data. It should look immediately familiar:

```json
{
    "name": "Sara",
    "age": 25,
    "skills": ["Python", "HTML", "CSS"]
}
```

Point out explicitly: **this is nearly identical to a Python dictionary** (Lesson 13). The main practical differences:

| Python Dict            | JSON                      |
| ------------------------ | --------------------------- |
| `True` / `False` / `None` | `true` / `false` / `null`   |
| Single or double quotes   | Double quotes only            |
| A Python object in memory | Plain text sent over the network |

### HTTP Verbs — Now With Real Meaning

Students saw this table in Lesson 16 as a preview. Now it becomes something they build.

| Verb   | Meaning              | Typical Use                       |
| ------ | ---------------------- | ------------------------------------ |
| GET    | Retrieve data          | Load a list of products               |
| POST   | Create new data        | Submit a signup form                  |
| PUT    | Update existing data    | Edit a user's profile                 |
| DELETE | Remove data            | Delete a comment                      |

---

## 3. Flask Hello-World Application (20 min)

### Setup

```bash
pip install flask
```

### Minimal App

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

Run it:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in the browser — **this is the moment to connect everything back to Lesson 16.** The browser (client) sends a GET request to `127.0.0.1:5000/`, Flask (server) matches the `/` route, runs `home()`, and sends the returned string back as the response body.

### Explaining the Code

| Line                        | What it does                                        |
| ----------------------------- | ------------------------------------------------------ |
| `app = Flask(__name__)`       | Creates the server application                          |
| `@app.route("/")`             | A **decorator** — maps a URL path to a function         |
| `def home():`                 | The function that runs when that path is requested       |
| `return "Hello, World!"`      | Whatever is returned becomes the HTTP response body       |
| `app.run(debug=True)`         | Starts the server listening for requests                  |

> `debug=True` auto-reloads the server on code changes and shows detailed error pages — useful for learning, should be turned off in production (worth one sentence, not a detour).

---

## 4. Building a JSON API Route (20 min)

Extend the app with a route that returns JSON instead of plain text:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/api/student")
def get_student():
    student = {
        "name": "Sara",
        "age": 25,
        "skills": ["Python", "HTML", "CSS"]
    }
    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)
```

Visit `http://127.0.0.1:5000/api/student` — the browser displays raw JSON. This is precisely what a real-world API endpoint looks like (weather APIs, social media APIs, etc. — connect to whatever API is used in the next section).

### Route Parameters (brief extension)

```python
@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})
```

Visiting `/api/greet/Sara` returns `{"message": "Hello, Sara!"}` — show how the URL itself can carry data into the function.

---

## 5. Reading API Data with `requests` (15 min)

Flip perspective one more time: now Python acts as the *client*, requesting data from someone else's server.

```bash
pip install requests
```

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()

print(data["name"])
print(data["public_repos"])
```

| Line                         | What it does                              |
| ------------------------------ | -------------------------------------------- |
| `requests.get(url)`            | Sends a GET request, just like a browser does |
| `response.json()`              | Converts the JSON response into a Python dict |
| `data["name"]`                 | Access it exactly like any dict (Lesson 13)   |

Use any free, no-auth public API for the live demo (a public REST test API, or GitHub's user endpoint as above) so nothing blocks on setting up API keys mid-lecture.

---

## 6. Database Overview — Conceptual Only (10 min)

Keep this section high-level; a full database module is out of scope for this course, but students should leave with orientation, not implementation depth.

```
   YOUR APP                      DATABASE
┌─────────────┐               ┌──────────────┐
│   Flask      │  reads/writes │   Stores data │
│   Server     │◄─────────────►│   permanently │
└─────────────┘               └──────────────┘
```

Without a database, data typed into an app disappears the moment the server restarts — the same limitation as a Python script that only holds values in variables during a single run (tie back to Lesson 14's file handling: files were the students' first taste of *persistence*).

| Type       | Example         | Structure                        |
| ----------- | ----------------- | ----------------------------------- |
| SQL         | PostgreSQL, MySQL | Tables with rows and columns, like a spreadsheet |
| NoSQL       | MongoDB           | Flexible documents, closer to nested JSON |

> One-line takeaway: "A database is just a more powerful, permanent, multi-user version of the `.txt` and `.csv` files you already know how to read and write."

---

## Hands-On Activity (woven into the live coding above)

By the end of the session, each student should have, running locally:
1. A Flask app with at least two routes
2. One route returning plain text, one returning JSON via `jsonify`
3. A separate small script using `requests` to call a public API and print one field from the response

---

## Common Beginner Mistakes

- Forgetting `pip install flask` / `pip install requests` before running
- Route path typos (`/api/student` vs `/api/students`) — reinforce careful reading, same muscle as reading Python tracebacks (Lesson 03)
- Trying to return a raw Python dict instead of using `jsonify()` — Flask needs the conversion step
- Confusing the Flask server's `requests` (incoming, handled by routes) with the `requests` *library* (outgoing, used to call other APIs) — same word, opposite direction. Worth explicitly disambiguating.

---

## Homework

1. Add a third route to your Flask app that accepts a name via the URL (like the `/api/greet/<name>` example) and returns a personalized JSON message
2. Find one free public API online, use `requests` to call it, and print two different fields from the response
3. In 2–3 sentences: explain the difference between your Flask app acting as a *server* and your `requests` script acting as a *client*

---

## Looking Ahead

Lesson 20 is the capstone: students combine everything from Phases 2–5 — Python logic, Flask backend, HTML/CSS/JS frontend — into one small full-stack project, and the course closes with career paths and next steps.
