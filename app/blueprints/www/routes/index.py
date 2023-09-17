from flask import redirect, url_for, current_app, render_template
from datetime import datetime

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    year = datetime.now().year
    if f"{year}.index" in [rule.endpoint for rule in current_app.url_map.iter_rules()]:
        return redirect(url_for(f"{year}.index"))
    return "No index page found."


@bp.route("/style", methods=["GET"])
def style():
    return render_template(bp.tmpl("index.html"))
