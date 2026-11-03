"""
Tests for the Flask API application.

These tests verify the /hello and /sum endpoints,
including successful requests and invalid input.
"""

from app import app


def test_hello():
    client = app.test_client()

    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_hello_with_name():
    client = app.test_client()

    response = client.get("/hello?name=Christaljah")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, Christaljah!"}


def test_sum():
    client = app.test_client()

    response = client.post("/sum", json={"numbers": [1, 2, 3]})

    assert response.status_code == 200
    assert response.get_json() == {"sum": 6}


def test_sum_missing_numbers():
    client = app.test_client()

    response = client.post("/sum", json={})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "Please provide a list of numbers."
    }


def test_sum_invalid_data():
    client = app.test_client()

    response = client.post("/sum", json={"numbers": [1, "two", 3]})

    assert response.status_code == 400
    assert response.get_json() == {
        "error": "The list must contain only numbers."
    }