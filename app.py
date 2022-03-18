""" Docstring for the app.py module.

The app module implements the basic
routes off application.
"""
from flask import Flask, request


app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def debug():
    """
    Simple debug route to check
    if server is working as expected.
    """
    test = {
        "message": "pong!",
    }

    return test, 200
