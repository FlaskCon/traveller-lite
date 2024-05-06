from flask import redirect, url_for, render_template
from flask_imp import Blueprint

from app.models.conferences import Conferences

bp = Blueprint(__name__)

bp.import_nested_blueprints("conferences")


@bp.get("/")
def index():
    conference = Conferences.select_latest()

    if conference is None:
        return render_template("global/errors/no-conference.html")

    return redirect(url_for('frontend.2024.index'))
