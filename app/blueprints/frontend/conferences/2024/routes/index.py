from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"))


@bp.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template(bp.tmpl("coming-soon.html"))
