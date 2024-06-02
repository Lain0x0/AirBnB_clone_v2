#!/usr/bin/python3
""" Routing with Flask """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying a message"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_msg():
    """Displays "HBNB" """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
