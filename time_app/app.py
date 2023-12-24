import os, random
from flask import Flask,render_template, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calender')
def calender():
    return render_template('calender.html')

@app.route('/newtask')
def new_task():
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
