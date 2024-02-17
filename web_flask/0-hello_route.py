from flask import Flask
""" A script that starts a Flask web application:
    - Listening on 0.0.0.0, port 5000
    Routes:
        - /: display “Hello HBNB!”
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
