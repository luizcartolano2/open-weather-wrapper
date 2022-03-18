""" Docstring for the app.py module.

The app module implements the basic
routes off application.
"""
from flask import Flask
from flask_caching import Cache
from src import CACHE_TTL


config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": CACHE_TTL * 60
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


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


@app.route('/temperature/<string:city_name>', methods=['GET'])
@cache.cached(timeout=CACHE_TTL * 60, query_string=True)
def get_temperature(city_name: str):
    """
    Method to return the temperature for a given city.

    :return:
    """
    print(city_name)
