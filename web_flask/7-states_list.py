#!/usr/bin/python3
"""A script that starts a Flask web application:
    - Listening on 0.0.0.0, port 5000
    - `storage` for fetching data from the storage engine (`FileStorage`
    or `DBStorage`) => from models import storage and storage.all(...)
    - Routes:
        - /states_list: display a HTML page: (inside the tag BODY)
            - H1 tag: “States”
            - UL tag: with the list of all State objects present in
                DBStorage sorted by name (A->Z) tip
            - LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """List State"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(error=None):
    """Remove current SQL session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
