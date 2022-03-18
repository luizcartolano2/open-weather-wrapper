""" Docstring for the open_weather_class.py module.

"""
from typing import Tuple

import requests
from .constants import API_KEY


class OpenWeather:
    """
    Class that implements an Open Weather API wrapper.

    Attributes
    ----------
    api_key : str
        The api key for open weather api.
    base_url : str
        The base url for open weather api.

    Methods
    -------
    fetch_weather(self, location: str) -> Tuple[dict, str]
        Method to fetch the weather for a given location.
    """
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?q='

    def fetch_weather(self, location: str) -> Tuple[dict, str]:
        """
        Method to fetch the weather for a given location.

        :param location: The location as a string.
        :return: Method returns the json with information and a message.
        """
        url = f'{self.base_url}{location}&units=metric&appid={self.api_key}'
        response = requests.get(url).json()

        # error like unknown city name, invalid api key
        if response.get('cod') != 200:
            message = response.get('message', '')
            return {}, f'Error getting temperature for {location}. Error message = {message}'

        try:
            data_return = {
                'min': response.get('main').get('temp_min'),
                'max': response.get('main').get('temp_max'),
                'avg': response.get('main').get('temp'),
                'feels_like': response.get('main').get('feels_like'),
                'city.name': response.get('name'),
                'city.country': response.get('sys').get('country')
            }
            message = f'Temperature retrieved for {location}.'
        except KeyError:
            data_return = {}
            message = f'Error getting temperature for {location}.'

        return data_return, message
