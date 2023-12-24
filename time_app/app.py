import os, random
from flask import Flask
from routes import home
app = Flask(__name__)

@app.route('/')
def index():
    return home()

if __name__ == '__main__':
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 81))
    app.run(host=host, port=port, debug=True)