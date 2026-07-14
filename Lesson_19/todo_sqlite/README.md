# Todo List With Flask and MySQL

This is the assembled project for Lesson 19. It is a small todo list app where tasks are saved in a MySQL database.

## What You Will Practice

- Flask routes
- HTML forms
- Reading form data with `request.form`
- Connecting Python to MySQL
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

## MySQL Settings

This project needs a real MySQL server running before Flask starts.

On macOS with Homebrew:

```bash
brew install mysql
brew services start mysql
mysql -u root
```

The app reads these environment variables:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=lesson19_todo
```

If your MySQL root user has a password, set it before running the app.

macOS/Linux:

```bash
export MYSQL_PASSWORD=your_password
```

Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="your_password"
```

The app creates the database and `tasks` table automatically when it starts.

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
| `db.py` | MySQL connection and table setup |
| `schema.sql` | SQL version of the database setup |
| `templates/index.html` | HTML page shown in the browser |
| `static/style.css` | Page styling |

## Try This

After the app works, add a new feature:

- Show how many tasks are incomplete
- Add a priority field
- Add a due date
- Add a button that deletes completed tasks
