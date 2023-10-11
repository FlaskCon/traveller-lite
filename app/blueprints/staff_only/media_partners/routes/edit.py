from flask import render_template

from .. import bp


@bp.route("/edit/<int:media_partner_id>", methods=["GET"])
def edit(media_partner_id):
    return render_template(bp.tmpl("edit.html"))
