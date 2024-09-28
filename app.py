from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory to-do list storage
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/rearrange', methods=['POST'])
def rearrange_tasks():
    reordered_tasks = request.form.getlist('task')
    global tasks
    tasks = reordered_tasks
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

