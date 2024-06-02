#!/usr/bin/python3
""" Web Flask {odd or even ?} """

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displaying "Hello HBNB" """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_msg():
    """Displays "HBNB" """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_msg(text):
    """Displays 'C' followed by tag of HTML <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_txt(text="is cool"):
    """Displays 'Python' followed by tag of HTML <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Displays 'n is a number' only if <n> is an int"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """Displays an HTML page only if <n> is an int"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    """Displays an HTML page only if <n> is an int"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
