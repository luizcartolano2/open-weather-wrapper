""" Docstring for the response_validation.py.

"""
from pydantic import BaseModel


class City(BaseModel):
    """
    Class to model a City object.

    Attributes
    ----------
    name : str
        The name of the city.
    country : str
        The country of the city.
    """
    name: str
    country: str


class OpenWeatherResponse(BaseModel):
    """
    Class to model the Open Weather response object.

    Attributes
    ----------
    min : float
        The minimum temperature.
    max : float
        The maximum temperature.
    avg : float
        The average temperature.
    feels_like : float
        The feels like temperature.
    city : City
        The city whose information is being retrieved.
    """
    min: float
    max: float
    avg: float
    feels_like: float
    city: City
