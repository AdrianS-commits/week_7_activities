from flask import Flask


def create_app():
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "2007539874039847"

    # Register the api blueprint for the routes in api_routes.py
    from .api_routes import bp

    app.register_blueprint(bp)

    # Register the routes in paralypic_routes.py
    with app.app_context():
        from . import paralympic_routes

    return app
