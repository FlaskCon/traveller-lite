import os

from dotenv import load_dotenv
from flask import Flask

from app.extensions import imp, db

load_dotenv()

DEV_MODE = True if os.environ.get("DEV_MODE") else False


def create_app():
    app = Flask(__name__)
    imp.init_app(app)
    db.init_app(app)
    imp.import_models("models")

    imp.import_app_resources(
        app_factories=["dev_cli"] if DEV_MODE else [],
    )

    imp.import_blueprint("blueprints/account")
    imp.import_blueprint("blueprints/auth")
    imp.import_blueprint("blueprints/staff_only")
    imp.import_blueprint("blueprints/frontend")

    if DEV_MODE:
        print("DEV_MODE is enabled. Remember to turn this off in production (unset DEV_MODE)")

    return app
