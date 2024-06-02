#!/usr/bin/python3
""" Using Web Flak to display "n" is a number """

from flask import Flask
from flask import abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_msg():
    """Displaying "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_txt(text):
    """Displays 'C' followed by tag of HTML <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_msg(text="is cool"):
    """Displays 'Python' followed by tag of HTML <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
