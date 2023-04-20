#!/usr/bin/python3
"""This script"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    hello(host='0.0.0.0', port=5000)
