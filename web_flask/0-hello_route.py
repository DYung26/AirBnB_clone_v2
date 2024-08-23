#!/usr/bin/python3
"""
Starts a simple Flask web application,

The application listens on `0.0.0.0`, port `5000`, and displays a simple
message when accessed.

Routes:
    /: Displays "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Handles the root route (`/`).

    Returns:
        str: A message "Hello HBNB!" displayed on the web page.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
