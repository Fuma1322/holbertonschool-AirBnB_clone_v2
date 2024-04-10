#!/usr/bin/python3
""" Starting A Flask Web Application"""
from flask import Flask

app = Flask(_name_)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)