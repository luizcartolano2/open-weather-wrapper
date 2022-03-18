""" Docstring for the open_weather_class_tests.py module.

"""
import unittest
from .open_weather_class import OpenWeather


class TestOpenWeatherClass(unittest.TestCase):
    """
    Class to test if OpenWeather class is working as expected.

    Attributes
    ----------
    open_weather : OpenWeather
        An open weather object.
    location : str
        A city to perform tests.

    Methods
    -------
    test_fetch(self) -> None
        Method to check if fetch method is working.
    test_response_format(self) -> None
        Method to check if all data is being returned.
    """
    def setUp(self) -> None:
        """
        Setup method for tests.
        """
        self.open_weather = OpenWeather()
        self.location = 'London,uk'

    def test_fetch(self) -> None:
        """
        Method to check if fetch method is working.
        """
        response, _ = self.open_weather.fetch_weather(location=self.location)

        self.assertIsNotNone(response)

    def test_response_format(self) -> None:
        """
        Method to check if all data is being returned.
        """
        response, _ = self.open_weather.fetch_weather(location=self.location)

        self.assertIsNotNone(response['min'])
        self.assertIsNotNone(response['max'])
        self.assertIsNotNone(response['avg'])
        self.assertIsNotNone(response['feels_like'])
        self.assertIsNotNone(response['city.name'])
        self.assertIsNotNone(response['city.country'])


if __name__ == '__main__':
    unittest.main()
