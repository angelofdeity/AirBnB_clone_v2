#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ This function closes the session"""
    storage.close()


@app.route('/states_list')
def show_states():
    """ This function renders the template 7-states_list.html"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
