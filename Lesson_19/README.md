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

## Big Idea

In Lessons 16–18, students mostly acted as the browser/client. In this lesson, they build the other side of the conversation: **a Python server that receives requests and sends responses.**

### Today's Build

Students will create:

- A tiny Flask app
- One route that returns plain text
- One route that returns JSON
- One Python script that calls someone else's API using `requests`

---

## Timed Breakdown

| Time      | Segment                                   | Format                       |
| --------- | ----------------------------------------- | ---------------------------- |
| 0:00–0:10 | Recap Lessons 16–18, frame Phase 5        | Discussion                   |
| 0:10–0:25 | What does a server do? (revisit + deepen) | Lecture + diagram            |
| 0:25–0:40 | REST APIs, JSON, HTTP verbs               | Lecture + live examples      |
| 0:40–1:00 | Flask hello-world application             | Live coding, students follow |
| 1:00–1:10 | **Break**                                 | —                            |
| 1:10–1:30 | Building a JSON API route in Flask        | Live coding                  |
| 1:30–1:45 | Reading API data with Python `requests`   | Live coding                  |
| 1:45–1:55 | Database overview (conceptual)            | Lecture + diagram            |
| 1:55–2:00 | Wrap-up, homework                         | Discussion                   |

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

That's the core idea: a server is a Python program with an extra job, which is staying alive and listening for requests.

Plain-English summary: a route is a URL path connected to a Python function.

---

## 2. REST APIs, JSON, and HTTP Verbs (15 min)

### What Is an API?

An **API (Application Programming Interface)** is a defined way for two programs to talk to each other. A **REST API** is a common style of API built on top of HTTP — the same protocol from Lesson 16.

Simple way to say it: an API is a menu of actions or data that another program is allowed to request.

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

| Python Dict               | JSON                             |
| ------------------------- | -------------------------------- |
| `True` / `False` / `None` | `true` / `false` / `null`        |
| Single or double quotes   | Double quotes only               |
| A Python object in memory | Plain text sent over the network |

### HTTP Verbs — Now With Real Meaning

Students saw this table in Lesson 16 as a preview. Now it becomes something they build.

| Verb   | Meaning              | Typical Use             |
| ------ | -------------------- | ----------------------- |
| GET    | Retrieve data        | Load a list of products |
| POST   | Create new data      | Submit a signup form    |
| PUT    | Update existing data | Edit a user's profile   |
| DELETE | Remove data          | Delete a comment        |

---

## 3. Flask Hello-World Application (20 min)

### Setup

```bash
pip install flask
```

If `pip` does not work on a student's machine, try:

```bash
python -m pip install flask
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

`127.0.0.1` means "this computer." Students are visiting a server running on their own machine.

### Explaining the Code

| Line                     | What it does                                        |
| ------------------------ | --------------------------------------------------- |
| `app = Flask(__name__)`  | Creates the server application                      |
| `@app.route("/")`        | A **decorator** — maps a URL path to a function     |
| `def home():`            | The function that runs when that path is requested  |
| `return "Hello, World!"` | Whatever is returned becomes the HTTP response body |
| `app.run(debug=True)`    | Starts the server listening for requests            |

> `debug=True` auto-reloads the server on code changes and shows detailed error pages — useful for learning, should be turned off in production (worth one sentence, not a detour).

### Quick Check

Ask: "What happens if we change the route from `/` to `/hello`?"

Expected answer: the app will respond at `http://127.0.0.1:5000/hello`; the old homepage route `/` will no longer match unless we keep both routes.

---

## 4. Building a JSON API Route (20 min)

Extend the app with a route that returns JSON instead of plain text:
pre setup

```cmd
python -m venv project_name_env
#mac
source myenv/bin/activate
#windows
myenv\Scripts\activate

pip install requests
pip freeze > requirements.txt
```

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

Plain-English summary: `jsonify()` turns Python data into an HTTP response that other programs can easily read.

### Route Parameters (brief extension)

```python
@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})
```

Visiting `/api/greet/Sara` returns `{"message": "Hello, Sara!"}` — show how the URL itself can carry data into the function.

### JSON Route Checklist

Before moving on, students should confirm:

- The Flask server is running
- `/` returns plain text
- `/api/student` returns JSON
- The browser URL matches the route exactly

---

## 5. Reading API Data with `requests` (15 min)

Flip perspective one more time: now Python acts as the _client_, requesting data from someone else's server.

```bash
pip install requests
```

If needed:

```bash
python -m pip install requests
```

```python
import requests

response = requests.get("https://api.github.com/users/octocat")
data = response.json()

print(data["name"])
print(data["public_repos"])
```

| Line                | What it does                                  |
| ------------------- | --------------------------------------------- |
| `requests.get(url)` | Sends a GET request, just like a browser does |
| `response.json()`   | Converts the JSON response into a Python dict |
| `data["name"]`      | Access it exactly like any dict (Lesson 13)   |

Use any free, no-auth public API for the live demo (a public REST test API, or GitHub's user endpoint as above) so nothing blocks on setting up API keys mid-lecture.

### Direction Check

This lesson uses the word "request" in two directions:

| Situation                  | Your Code's Role | What Happens                      |
| -------------------------- | ---------------- | --------------------------------- |
| Flask route                | Server           | Receives a request from a browser |
| `requests.get(...)` script | Client           | Sends a request to another server |

This distinction is worth repeating because the names are similar.

---

## 6. Database Overview — Conceptual Only (10 min)

Keep this section high-level. A full database module is out of scope for this course, but students should leave knowing what a database is for.

```
   YOUR APP                      DATABASE
┌─────────────┐               ┌──────────────┐
│   Flask      │  reads/writes │   Stores data │
│   Server     │◄─────────────►│   permanently │
└─────────────┘               └──────────────┘
```

Without a database, data typed into an app disappears the moment the server restarts — the same limitation as a Python script that only holds values in variables during a single run (tie back to Lesson 14's file handling: files were the students' first taste of _persistence_).

| Type  | Example           | Structure                                        |
| ----- | ----------------- | ------------------------------------------------ |
| SQL   | PostgreSQL, MySQL | Tables with rows and columns, like a spreadsheet |
| NoSQL | MongoDB           | Flexible documents, closer to nested JSON        |

> One-line takeaway: "A database is just a more powerful, permanent, multi-user version of the `.txt` and `.csv` files you already know how to read and write."

---

## Hands-On Activity (woven into the live coding above)

By the end of the session, each student should have, running locally:

1. A Flask app with at least two routes
2. One route returning plain text, one returning JSON via `jsonify`
3. A separate small script using `requests` to call a public API and print one field from the response

### Success Checklist

Students are ready for Lesson 20 if they can:

- Start the Flask server
- Visit a route in the browser
- Explain what a route does
- Return JSON from Flask
- Use `requests.get()` and read one value from the returned JSON

---

## Common Beginner Mistakes

- Forgetting `pip install flask` / `pip install requests` before running
- Route path typos (`/api/student` vs `/api/students`) — reinforce careful reading, same muscle as reading Python tracebacks (Lesson 03)
- Returning data inconsistently — for this course, use `jsonify()` for JSON responses so the intent is clear
- Confusing the Flask server's `requests` (incoming, handled by routes) with the `requests` _library_ (outgoing, used to call other APIs) — same word, opposite direction. Worth explicitly disambiguating.
- Forgetting that the Flask terminal must stay running while testing the app in the browser

---

## Homework

1. Add a third route to your Flask app that accepts a name via the URL (like the `/api/greet/<name>` example) and returns a personalized JSON message
2. Find one free public API online, use `requests` to call it, and print two different fields from the response
3. In 2–3 sentences: explain the difference between your Flask app acting as a _server_ and your `requests` script acting as a _client_

### Exit Ticket

Before leaving, students answer:

> What is the difference between visiting `/api/student` in the browser and calling an outside API with `requests.get()`?

---

## Looking Ahead

Lesson 20 is the capstone: students combine everything from Phases 2–5 — Python logic, Flask backend, HTML/CSS/JS frontend — into one small full-stack project, and the course closes with career paths and next steps.

## extra links

[free api](https://public-api-lists.github.io/public-api-lists/)
