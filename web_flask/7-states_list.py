#!/usr/bin/python3
"""starts a Flask web application
- The application must listens on 0.0.0.0, port 5000.
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present
                in DBStorage sorted by name
        LI tag: description of one State: <state.id>:
               <B><state.name></B>
- strict_slashes=False is mandatory in route definition
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """display a HTML the States"""
    all_states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """function that call close method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
