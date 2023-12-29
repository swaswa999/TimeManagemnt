import os, random
from datetime import date
from flask import Flask,render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    overdue = 1
    taskdue = 1
    return render_template('index.html', overdue=overdue, taskdue=taskdue)

@app.route('/calender')
def calender():
    return render_template('calender.html')

@app.route('/newtask', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        current_date = date.today()

        task = request.form.get('task_name')
        date_added = current_date.strftime('%Y/%d/%m') #sets current date in yyyy/dd/mm
        date_due = request.form.get('due_date')
        subject = request.form.get('subject')
        priority = request.form.get('priority') #scale of 1-3
        location_added = 'manual' #when redoing scraper, indicates to not change this task
        description = request.form.get('task_description')
        subtasks = request.form.getlist('subtasks[]')  # Get a list of subtasks
        subtask_times = request.form.getlist('subtask_times[]')  # Get a list of subtask times
        status = 'not_complete' #shows that its a fresh task

        with open('time_app/data/swayam.txt', 'a') as file:
            file.write(f"{task} {date_added} {date_due} {subject} {priority} {location_added} {description} {subtasks} {subtask_times} {status} /n")


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
