from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
completed_tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, completed_tasks=completed_tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')


@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    if task_id < len(tasks):
        completed_task = tasks.pop(task_id)
        completed_tasks.append(completed_task)
    return redirect('/')


@app.route('/delete_completed_task/<int:task_id>')
def delete_completed_task(task_id):
    if task_id < len(completed_tasks):
        task_to_move = completed_tasks.pop(task_id)
        tasks.append(task_to_move)
    return redirect('/')


@app.route('/refresh')
def refresh():
    global tasks
    global completed_tasks
    tasks = []
    completed_tasks = []
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
