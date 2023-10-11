from flask import render_template

from .. import bp


@bp.route("/edit/<int:conference_id>", methods=["GET"])
def edit(conference_id):
    return render_template(bp.tmpl("edit.html"))
