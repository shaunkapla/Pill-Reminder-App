from flask import Flask
from .api import api_bp  # Import the Blueprint for API routes

def create_app():
    app = Flask(__name__)  # Create a Flask app instance

    # Register the API Blueprint under the '/api' URL prefix
    app.register_blueprint(api_bp, url_prefix='/api')

    return app  # Return the initialized Flask app