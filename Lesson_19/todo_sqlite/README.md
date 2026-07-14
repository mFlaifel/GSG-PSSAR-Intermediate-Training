# Todo List With Flask and SQLite

This is the assembled project for Lesson 19. It is a small todo list app where tasks are saved in a SQLite database.

## What You Will Practice

- Flask routes
- HTML forms
- Reading form data with `request.form`
- Connecting Python to SQLite
- Running `SELECT`, `INSERT`, `UPDATE`, and `DELETE`
- Rendering database rows in an HTML template

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

SQLite is built into Python, so no extra database server is needed. The app creates the `tasks.db` file and `tasks` table automatically when it starts.

## Run

```bash
python3 app.py
```

If your computer uses `python` instead of `python3`, use `python` in those commands.

Open:

```text
http://127.0.0.1:5000
```

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Flask routes and todo actions |
| `db.py` | SQLite connection and table setup |
| `templates/index.html` | HTML page shown in the browser |
| `static/style.css` | Page styling |

## Try This

After the app works, add a new feature:

- Show how many tasks are incomplete
- Add a priority field
- Add a due date
- Add a button that deletes completed tasks
