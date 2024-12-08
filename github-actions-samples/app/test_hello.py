import pytest
from hello import app, get_message
from unittest.mock import patch


def test_get_message_anastasiia():
    with patch("hello.configparser.RawConfigParser.getboolean", return_value=True):
        assert get_message() == "Hello, Anastasiia!"


def test_get_message_world():
    with patch("hello.configparser.RawConfigParser.getboolean", return_value=False):
        assert get_message() == "Hello, World!"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_hello_endpoint_anastasiia(client):
    with patch("hello.configparser.RawConfigParser.getboolean", return_value=True):
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode() == "Hello, Anastasiia!"


def test_hello_endpoint_world(client):
    with patch("hello.configparser.RawConfigParser.getboolean", return_value=False):
        response = client.get("/")
        assert response.status_code == 200
        assert response.data.decode() == "Hello, World!"
