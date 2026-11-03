"""
Basic Flask API for INFO U762 Interoperability.

This application includes a GET endpoint that returns a greeting
and a POST endpoint that accepts a list of numbers and returns their sum.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)


# GET endpoint that returns a greeting
@app.route("/hello", methods=["GET"])
def hello():
    name = request.args.get("name")

    if name:
        return jsonify({"message": f"Hello, {name}!"})
    else:
        return jsonify({"message": "Hello, World!"})


# POST endpoint that calculates the sum of a list of numbers
@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json(silent=True)

    # Check for missing or invalid JSON data
    if not data or "numbers" not in data:
        return jsonify({"error": "Please provide a list of numbers."}), 400

    numbers = data["numbers"]

    # Make sure numbers is a list
    if not isinstance(numbers, list):
        return jsonify({"error": "Numbers must be provided as a list."}), 400

    # Make sure every item in the list is a number
    if not all(isinstance(number, (int, float)) for number in numbers):
        return jsonify({"error": "The list must contain only numbers."}), 400

    return jsonify({"sum": sum(numbers)})


if __name__ == "__main__":
    app.run(port=5000)