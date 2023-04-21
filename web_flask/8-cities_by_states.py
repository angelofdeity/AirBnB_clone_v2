#!/usr/bin/python3
"""This script starts a Flask web application"""


from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ This function closes the session"""
    storage.close()


@app.route('/cities_by_states')
def show_states():
    """ This function renders the template 8-cities_by_states.html"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
