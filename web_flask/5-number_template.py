#!/usr/bin/python3
"""A Flask web application with multiple routes"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns a greeting message"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    """Displays 'C ' followed by the text variable with underscores replaced by spaces"""
    return "C " + text.replace("_", " ")

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_fun(text="is cool"):
    """Displays 'Python ' followed by the text variable with underscores replaced by spaces"""
    return "Python " + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if n is an integer"""
    return f"{n} is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

