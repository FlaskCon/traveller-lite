import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, redirect, url_for

from app.extensions import imp, db

load_dotenv()

DEV_MODE = True if os.environ.get("DEV_MODE") else False


def create_app():
    app = Flask(__name__)
    imp.init_app(app)
    db.init_app(app)
    imp.import_models("models")

    with app.app_context():
        db.create_all()

    imp.import_app_resources(
        app_factories=["dev_cli"] if DEV_MODE else [],
    )

    imp.import_blueprints("blueprints/backend")
    imp.import_blueprints("blueprints/frontend")

    if DEV_MODE:
        print("DEV_MODE is enabled. Remember to turn this off in production (unset DEV_MODE)")

    @app.get("/")
    def index():
        year = datetime.now().year
        if f"{year}.index" in [rule.endpoint for rule in app.url_map.iter_rules()]:
            return redirect(url_for(f"{year}.index"))
        return "No index page found."

    return app
