from flask import render_template

from .. import bp


@bp.route("/edit/<int:sponsor_id>", methods=["GET"])
def edit(sponsor_id):
    return render_template(bp.tmpl("edit.html"))
