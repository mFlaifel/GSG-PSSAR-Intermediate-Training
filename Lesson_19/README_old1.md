# Lesson 19 - Flask + MySQL Todo List Project

**Phase 5 - Backend & Final Project** | **Duration: 2 Hours** | **Session 19 of 20**

---

## Lesson Profile

This lesson is a guided teaching material for helping students move from "Flask can return a response" to "Flask can save real data in a database."

Students will build and study a small todo list application. The app looks simple on purpose:

- A page shows tasks
- A form adds a new task
- A button marks a task as done or not done
- A button deletes a task
- MySQL stores the tasks permanently

The important idea is persistence: data should still exist after refreshing the page or restarting the Flask server.

---

## Learning Objectives

By the end of this session, students will be able to:

- Explain why a web app needs a database
- Describe the role of Flask, HTML forms, and MySQL in one project
- Create a MySQL database table for todo items
- Read rows from MySQL and display them on a web page
- Insert, update, and delete rows using Flask routes
- Run a small assembled full-stack project locally

---

## Big Idea

In earlier lessons, students learned that Python variables only live while the program is running. A database gives an application memory.

```text
Browser form -> Flask route -> MySQL table
       ^              |
       |              v
       +------ HTML response with saved tasks
```

The todo list is not the real goal. The real goal is understanding how information moves through a backend application.

---

## Today's Build

Students will use the assembled project in:

```text
Lesson_19/todo_mysql_project/
```

Project structure:

```text
todo_mysql_project/
+-- app.py
+-- db.py
+-- requirements.txt
+-- schema.sql
+-- README.md
+-- templates/
|   +-- index.html
+-- static/
    +-- style.css
```

---

## Timed Breakdown

| Time      | Segment                           | Format                       |
| --------- | --------------------------------- | ---------------------------- |
| 0:00-0:10 | Recap Flask routes and HTML forms | Discussion                   |
| 0:10-0:25 | Why databases exist               | Lecture + diagram            |
| 0:25-0:40 | MySQL table design for tasks      | Guided explanation           |
| 0:40-1:05 | Run the assembled todo project    | Live coding, students follow |
| 1:05-1:15 | Break                             | -                            |
| 1:15-1:35 | Read and explain the Flask routes | Code walkthrough             |
| 1:35-1:50 | Student modification challenge    | Pair/solo work               |
| 1:50-2:00 | Wrap-up and exit ticket           | Discussion                   |

---

## 1. Why Do We Need MySQL?

Ask students:

> What happens to a Python list when the program stops?

Example:

```python
tasks = ["Study Flask", "Practice MySQL"]
```

This list exists only while Python is running. If the program stops, the list disappears.

A database solves that problem. MySQL stores data on disk in tables, so the app can read it again later.

Simple comparison:

| Python list              | MySQL table                        |
| ------------------------ | ---------------------------------- |
| Temporary                | Permanent                          |
| Good for small examples  | Good for real applications         |
| Lost when program stops  | Still available after restart      |
| Lives inside one program | Can be shared by multiple programs |

---

## 2. The Todo Table

The app uses one table named `tasks`.

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    is_done BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Explain each column:

| Column       | Purpose                      |
| ------------ | ---------------------------- |
| `id`         | Unique number for each task  |
| `title`      | The text the user typed      |
| `is_done`    | Whether the task is complete |
| `created_at` | When the task was created    |

The `id` is important because many tasks can have similar titles. Flask uses the `id` to update or delete the exact row.

---

## 3. Run the Assembled Project

From the repository root:

```bash
cd Lesson_19/todo_mysql_project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows:

```bash
cd Lesson_19\todo_mysql_project
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Make sure MySQL is running. The app uses these default settings:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=lesson19_todo
```

On macOS with Homebrew, install and start MySQL with:

```bash
brew install mysql
brew services start mysql
```

Check that MySQL opens:

```bash
mysql -u root
```

If your MySQL password is different, set it before running Flask.

macOS/Linux:

```bash
export MYSQL_PASSWORD=your_password
```

Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="your_password"
```

Run the app:

```bash
python3 app.py
```

If your computer uses `python` instead of `python3`, use `python` in those commands.

Open:

```text
http://127.0.0.1:5000
```

The app creates the database and table automatically when it starts. `schema.sql` is also included so students can see the SQL directly.

---

## 4. How the App Works

### Display Tasks

The home route reads rows from MySQL and sends them to the HTML template.

```python
@app.route("/")
def index():
    tasks = fetch_tasks()
    return render_template("index.html", tasks=tasks)
```

Plain English:

1. Flask receives a request for `/`
2. Python asks MySQL for all tasks
3. Flask gives the tasks to `index.html`
4. The browser shows the list

### Add a Task

The form sends a `POST` request to `/tasks`.

```python
@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()
```

Plain English:

1. The student types a task
2. The browser submits the form
3. Flask reads the form value
4. Flask inserts a new row into MySQL
5. Flask redirects back to the home page

### Toggle a Task

The complete button changes `is_done` from false to true, or true to false.

```sql
UPDATE tasks
SET is_done = 1 - is_done
WHERE id = %s
```

### Delete a Task

The delete button removes one row.

```sql
DELETE FROM tasks
WHERE id = %s
```

---

## 5. Student Modification Challenge

Choose one small improvement:

1. Add a "priority" column to the database
2. Add a "Clear completed tasks" button
3. Change the page style
4. Show the total number of remaining tasks
5. Add a date field for when the task is due

Keep the challenge small. The goal is to practice the same flow:

```text
HTML form -> Flask route -> SQL query -> MySQL table -> HTML page
```

---

## Common Beginner Mistakes

- MySQL is not running
- The MySQL password in the terminal does not match the real password
- The virtual environment is not activated before installing packages
- Forgetting to restart Flask after changing Python code
- Typing the wrong database or table name
- Forgetting that `POST` routes are usually triggered by forms, not by typing the URL in the browser

---

## Success Checklist

Students are successful when they can:

- Start the Flask server
- Open the todo page in the browser
- Add a task and see it appear
- Refresh the page and see that the task is still there
- Mark a task complete
- Delete a task
- Explain which file connects to MySQL
- Explain which route inserts a new task

---

## Exit Ticket

Answer in 2-3 sentences:

> Why does this todo list still remember tasks after the Flask server restarts?

Expected idea: the tasks are saved in MySQL, not only inside Python variables.
