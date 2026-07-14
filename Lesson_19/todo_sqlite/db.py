import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "tasks.db")


def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with _get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                is_done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL
            )
            """
        )


def fetch_tasks():
    with _get_conn() as conn:
        rows = conn.execute(
            "SELECT id, title, is_done, created_at FROM tasks ORDER BY is_done, created_at"
        ).fetchall()
    return [
        {"id": r["id"], "title": r["title"], "is_done": bool(r["is_done"]), "created_at": r["created_at"]}
        for r in rows
    ]


def add_task(title):
    with _get_conn() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, is_done, created_at) VALUES (?, 0, ?)",
            (title, datetime.now().isoformat()),
        )
        return {"id": cursor.lastrowid, "title": title, "is_done": False, "created_at": datetime.now().isoformat()}


def toggle_task(task_id):
    with _get_conn() as conn:
        conn.execute("UPDATE tasks SET is_done = NOT is_done WHERE id = ?", (task_id,))


def delete_task(task_id):
    with _get_conn() as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
