#!/usr/bin/python3
""" A script that starts a Flask web application:
    - Listening on 0.0.0.0, port 5000
    Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display "HBNB!”
"""
from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Hello to HBNB"""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """HBNB"""
    return 'HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
