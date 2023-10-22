#!/usr/bin/python3
"""Script that starts a flask web application."""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displaying hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displaying hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """replace underscore with spaces in the text variables"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_is_cool(text):
    """replace underscore with spaces in the text variables"""
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n', strict_slashes=False)
def number(n):
    """displaying HTML page if only n is a integer"""
    if isinstance(n, int):
        return f"{n} is a number"
    else:
        return "Not a valid integer"

@app.route('number_template.html', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number_template.htm, n=n')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)