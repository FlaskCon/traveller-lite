from flask import render_template

from .. import bp


@bp.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template(bp.tmpl("dashboard.html"))
