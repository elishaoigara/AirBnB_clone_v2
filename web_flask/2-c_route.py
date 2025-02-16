#!/usr/bin/python3
"""A simple Flask web application with multiple routes"""

from flask import Flask

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

