from flask import Flask, escape, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
