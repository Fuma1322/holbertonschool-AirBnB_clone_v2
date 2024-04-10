#!/usr/bin/python3
""" Starts a Flash Web Application HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message when /hbnb is called """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """ Prints a Message when /c/<text> is called """
    return 'C {}'.format(escape(text).replace('_',''))    


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

