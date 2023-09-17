from flask import render_template

from .. import bp


@bp.route("/<year>/<slug>", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"))
