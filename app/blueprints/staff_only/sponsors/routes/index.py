from flask import render_template

from app.models.sponsors import Sponsors
from .. import bp


@bp.route("/", methods=["GET"])
def index():
    sponsors = Sponsors.select_all()
    return render_template(
        bp.tmpl("index.html"),
        sponsors=sponsors,
    )
