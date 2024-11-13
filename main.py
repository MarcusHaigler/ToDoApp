from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

tasks = ["task1", "task2", "task3"]
finished_tasks = []

@app.route("/")
def home():
    return render_template('index.html', tasks=tasks, finished_tasks=finished_tasks)

@app.route("/add-task", methods=["POST"])
def add_task():
    pass

if __name__ == '__main__':
    app.run(debug=True)