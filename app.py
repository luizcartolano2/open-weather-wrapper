""" Docstring for the app.py module.

The app module implements the basic
routes off application.
"""
from flask import Flask, request, jsonify
from flask_caching import Cache
from src import CACHE_TTL, DEFAULT_MAX_NUMBER
from src.open_weather import OpenWeather


config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": CACHE_TTL * 60
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
list_of_cities = []


@app.route('/ping', methods=['GET'])
def debug():
    """
    Method to debug server.
    """
    return {'message': 'pong'}, 200


def manage_cached_dict(last_cities: list) -> dict:
    """
    Verify if each searched city is in cache, them
    storage it in a dict.

    :param last_cities: A list of cities to retrieve cached information.
    :return: A dict with requested information.
    """
    cached_cities = {}

    for city in last_cities:
        if cache.get(city):
            cached_cities[city] = cache.get(city)
        else:
            last_cities.remove(city)
            if city in cached_cities.keys():
                cached_cities.pop(city)

    return cached_cities


@app.route('/temperature/<string:city_name>', methods=['GET'])
def get_temperature(city_name: str):
    """
    Method to return the temperature for a given city.

    :return: The dict with response and the status code.
    """
    if cache.get(city_name):
        return cache.get(city_name)

    open_weather = OpenWeather()
    res, _ = open_weather.fetch_weather(location=city_name)

    if res:
        cache.set(city_name, res)
        list_of_cities.append(city_name)
        status = 200
    else:
        status = 500

    return res, status


@app.route('/temperature', methods=['GET'])
def get_cached_temperature():
    """
    Function to retrieve cached information.

    :return: The dict with response and the status code.
    """
    max_number = int(request.args.get('max', default=DEFAULT_MAX_NUMBER))
    cities_to_search = list_of_cities[:max_number]

    return jsonify(manage_cached_dict(cities_to_search)), 200
