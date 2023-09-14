from flask import redirect, url_for, current_app
from datetime import datetime

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    year = datetime.now().year
    if f"www.{year}.index" in [rule.endpoint for rule in current_app.url_map.iter_rules()]:
        return redirect(url_for(f"www.{year}.index"))
    return "No index page found."
