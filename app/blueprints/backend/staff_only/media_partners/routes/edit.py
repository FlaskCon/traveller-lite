from flask import render_template

from .. import bp


@bp.route("/edit", methods=["GET"])
def edit():
    return render_template(bp.tmpl("edit.html"))
