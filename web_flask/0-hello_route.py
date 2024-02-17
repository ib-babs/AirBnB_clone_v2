from flask import Flask, request
from markupsafe import escape
""" A script that starts a Flask web application:
    - Listening on 0.0.0.0, port 5000
    Routes:
        - /: display “Hello HBNB!”
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello to HBNB"""
    name = request.args.get("name", "HBNB")
    return f'Hello {escape(name)}!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
