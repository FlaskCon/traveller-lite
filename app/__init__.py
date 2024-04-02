from dotenv import load_dotenv
from flask import Flask

from app.extensions import imp, db, vite
from app.models import Resources
from app.models.display_pictures import DisplayPictures

load_dotenv()


def create_app():
    app = Flask(__name__)
    imp.init_app(app)
    vite.init_app(app)
    db.init_app(app)
    imp.import_models("models")

    imp.import_app_resources(
        factories=["dev_cli"] if app.config["ENV"] == "development" else [],
        folders_to_import=["*"],
        files_to_import=["*"],
    )

    imp.import_blueprint("blueprints/account")
    imp.import_blueprint("blueprints/auth")
    imp.import_blueprint("blueprints/staff_only")
    imp.import_blueprint("blueprints/frontend")

    return app
