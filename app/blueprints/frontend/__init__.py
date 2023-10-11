from datetime import datetime

from flask import redirect, url_for, current_app as app
from flask_imp import Blueprint

bp = Blueprint(__name__)

bp.import_nested_blueprint("2023")


@bp.get("/")
def index():
    year = datetime.now().year
    if f"frontend.{year}.index" in [rule.endpoint for rule in app.url_map.iter_rules()]:
        return redirect(url_for(f"frontend.{year}.index"))
    return "No index page found."
