#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask
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
    return f'c {text.replace("_", " ")}'


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text):
    """ This function returns a string"""
    return f'python {text.replace("_", " ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def show_number(n):
    """ This function returns a string"""
    return f"{n} is a number"


if __name__ == '__main__':
    hello(host='0.0.0.0', port=5000)
    hbnb(host='0.0.0.0', port=5000)
    show_c(host='0.0.0.0', port=5000)
    show_python(host='0.0.0.0', port=5000)
    show_number(host='0.0.0.0', port=5000)
