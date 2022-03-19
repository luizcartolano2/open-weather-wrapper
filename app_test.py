""" Docstring for the app_test.py module.

"""
import pytest
from app import app


@pytest.fixture
def client():
    """
    Method to yield a test client from app.
    """
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_ping(client):
    """
    Function to test debug route.

    :param client: A testing client object.
    """
    rep = client.get("/ping")
    assert 200 == rep.status_code


def test_weather(client):
    """
    Function to test weather route.

    :param client: A testing client object.
    """
    rep = client.get('temperature/London,uk')
    assert 200 == rep.status_code


def test_all_temperature(client):
    """
    Function to test weather cached route.

    :param client: A testing client object.
    """
    rep = client.get('temperature?max=4')
    assert 200 == rep.status_code
