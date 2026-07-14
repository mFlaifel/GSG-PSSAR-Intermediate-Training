from flask import Flask, flash, redirect, render_template, request, url_for

from db import add_task, delete_task, fetch_tasks, toggle_task


app = Flask(__name__)
app.secret_key = "lesson-19-dev-secret"


@app.route("/")
def index():
    tasks = fetch_tasks()
    remaining_count = sum(1 for task in tasks if not task["is_done"])
    return render_template("index.html", tasks=tasks, remaining_count=remaining_count)


@app.post("/tasks")
def add_task_route():
    title = request.form.get("title", "").strip()

    if not title:
        flash("Please type a task before adding it.")
        return redirect(url_for("index"))

    add_task(title)
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/toggle")
def toggle_task_route(task_id):
    toggle_task(task_id)
    return redirect(url_for("index"))


@app.post("/tasks/<int:task_id>/delete")
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
