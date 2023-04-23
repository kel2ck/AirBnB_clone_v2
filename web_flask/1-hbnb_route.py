#!/usr/bin/python3
"""starts a Flask web application
- The application must listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”.
    /hbnb: display "HBNB".
- strict_slashes=False is mandatory in route definition.
"""
from flask import Flask

app = Flask(__name__)

"""display 'Hello HBNB!' and 'HBNB'"""

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def redirect():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
