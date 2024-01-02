import os, random
from datetime import date
from flask import Flask,render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    today = date.today().strftime('%Y-%d-%m')
    today_task = []
    overdue_task = []

    with open('time_app/data/swayam.txt', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        current_line = lines[i].strip().split('_')
        if current_line[2] == today:
            today_task.append(current_line[6])
        if current_line[2] < today:
            overdue_task.append(f"{current_line[6]} [{current_line[2]}]")
        


    overdue = len(overdue_task)
    taskdue = len(today_task)
    return render_template('index.html', overdue=overdue, taskdue=taskdue, today_task=today_task, overdue_task=overdue_task)

@app.route('/calender')
def calender():
    return render_template('calender.html')

@app.route('/newtask', methods=['GET', 'POST'])
def new_task():

    if request.method == 'POST':
        current_date = date.today()

        task = request.form.get('task_name')
        date_added = current_date.strftime('%Y-%d-%m') #sets current date in yyyy/dd/mm
        date_due = request.form.get('due_date')
        subject = request.form.get('subject')
        priority = request.form.get('priority') #scale of 1-3
        location_added = 'manual' #when redoing scraper, indicates to not change this task
        description = request.form.get('task_description')
        subtasks = request.form.getlist('subtasks[]')  # Get a list of subtasks
        subtask_times = request.form.getlist('subtask_times[]')  # Get a list of subtask times
        status = 'not_complete' #shows that its a fresh task 
        repeating = request.form.get('')

        with open('time_app/data/swayam.txt', 'a') as file:
            file.write(f"{task}_{date_added}_{date_due}_{subject}_{priority}_{location_added}_{description}_{subtasks}_{subtask_times}_{status}_{repeating} \n")

        return redirect('/')  

    return render_template('new_task.html')
@app.route('/setting')
def settings():
    return render_template('settings.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 81))
    app.run(host=host, port=port, debug=True)
