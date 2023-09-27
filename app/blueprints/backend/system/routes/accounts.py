from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def accounts():
    return render_template(bp.tmpl("accounts.html"))
