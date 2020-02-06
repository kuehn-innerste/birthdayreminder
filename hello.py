from flask import Flask
from flask import Request
from flask import escape
from flask import jsonify

app = Flask(__name__)
members = [
	('Adam','03.03.2000'),
    ('Berthold', '03.06.1943'),
    ('Dietrich', '23.07.1968'),
    ('Carlotta', '12.01.1953')
]
    

@app.route('/')
def index_page():
    return 'Index page'

@app.route('/members')
def get_members():
    return jsonify(members)

@app.route('/hello/<username>')
@app.route('/hello')
def hello_world(username=''):
    if username == '':
        username="world"
    return 'Hello, %s!' % username

