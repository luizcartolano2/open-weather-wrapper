""" Docstring for the constants.py module.

"""
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = getenv('API_KEY')
