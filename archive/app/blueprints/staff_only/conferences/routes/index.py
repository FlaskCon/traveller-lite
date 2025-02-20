from flask import render_template

from app.models.conferences import Conferences
from .. import bp, conferences_group


@conferences_group("/", methods=["GET"])
def index():
    conferences = Conferences.select_all()
    return render_template(bp.tmpl("index.html"), conferences=conferences)
