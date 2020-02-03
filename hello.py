from flask import Flask
from flask import Request
from flask import jsonify

app = Flask(__name__)
members = [
        'name':'Adam',
        'birthday':'02.03.2000'
]
    

@app.route('/')
def index_page():
    return 'Index page'

@app.route('/members')
def get_members():
    return jsonify(name=members.name,birthday=members.birthday)

@app.route('/hello/<username>')
@app.route('/hello')
def hello_world(username=''):
    if username == '':
        username="world"
    return 'Hello, %s!' % username

