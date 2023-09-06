from flask import Flask
from app.extensions import bigapp


def create_app():
    app = Flask(__name__)
    bigapp.init_app(app)

    bigapp.import_app_resources()

    bigapp.import_blueprints("blueprints")

    return app
