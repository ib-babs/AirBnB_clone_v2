#!/usr/bin/python3
""" A script that starts a Flask web application:
    - Listening on 0.0.0.0, port 5000
    Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display “HBNB!”
        - /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
        - /python/<text>: display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
            - The default value of text is “is cool”
        - /number_template/<n>: display a HTML page only if n is an integer:
            - H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Return C + <text>"""
    replace_underscore = text.replace('_', ' ')
    return 'C {}'.format(replace_underscore)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Return Python + <text>"""
    replace_underscore = text.replace('_', ' ')
    return 'Python {}'.format(replace_underscore)


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_integer(n):
    """Return if <n> is an int"""
    return '{} is a number'.format(n)


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_integer(n):
    """Return if <n> is an int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template_is_integer(n):
    """Rendr template if <n> is an int"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
