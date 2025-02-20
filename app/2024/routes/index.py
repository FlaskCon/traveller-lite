from flask import render_template, url_for, redirect

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return render_template(bp.tmpl("index.html"))


@bp.route("/coming-soon", methods=["GET"])
def coming_soon():
    return redirect(url_for("2024.index"))
