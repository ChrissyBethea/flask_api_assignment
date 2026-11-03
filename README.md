# Flask API Assignment

This project is a basic Flask application created for INFO U762 Interoperability. The application demonstrates how Flask can be used to create REST API endpoints that accept requests and return JSON responses.

## Features

The application includes two endpoints:

- `/hello` - Returns a JSON greeting. A name can be provided as an optional query parameter.
- `/sum` - Accepts a JSON list of numbers through a POST request and returns the sum.

The application also includes error handling for invalid or missing input.

## Setup

Create a virtual environment:

    python -m venv venv

Install Flask and pytest:

    pip install Flask pytest

## Run the Application

Run the Flask server with:

    python app.py

The application runs locally on port 5000.

Example:

    http://127.0.0.1:5000/hello

A name can also be included:

    http://127.0.0.1:5000/hello?name=Christaljah

## Testing

Run the automated tests with:

    pytest test_app.py

The tests check the `/hello` and `/sum` endpoints, including valid requests and error handling.

## Test Results

The application was tested successfully using pytest.

Result:

    5 passed

The `/hello` endpoint was also manually tested with and without a name parameter, and the Flask server returned a successful HTTP 200 response.
