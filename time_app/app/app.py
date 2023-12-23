import os, random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def mainmenu():
    return render_template('mainmenu.html')

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 81))
    app.run(host=host, port=port, debug=True)  # Enable debug mode
