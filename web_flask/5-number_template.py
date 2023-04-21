#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ This function returns a string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function returns a string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """ This function returns a string"""
    return 'C {}'.format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text="is_cool"):
    """ This function returns a string"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """ This function returns a string"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def show_number_html(n):
    """ This function returns a html page"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
