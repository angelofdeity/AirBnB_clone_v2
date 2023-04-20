#!/usr/bin/python3
"""This script"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    return f'c {text.replace("_", " ")}'


if __name__ == '__main__':
    hello(host='0.0.0.0', port=5000)
    hbnb(host='0.0.0.0', port=5000)
    show_c(host='0.0.0.0', port=5000)
