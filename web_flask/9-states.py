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


@app.route('/states')
@app.route('/states/<id>')
def show_states(id=None):
    """ This function renders the template 9-states.html"""
    states = storage.all(State).values()
    state_name_ids = {state.id: state.name for state in states}
    cities = storage.all(City).values()
    return render_template('9-states.html', states=states,
                           cities=cities, id=id, state_name_ids=state_name_ids)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
