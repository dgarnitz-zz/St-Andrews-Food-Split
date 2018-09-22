from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>My Flask App</h1>'

@app.route('/info')
def info():
    return '<p>This page provides info about my application</p>'
