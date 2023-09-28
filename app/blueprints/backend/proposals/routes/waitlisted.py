from flask import render_template
from app.models.talks import Talks
from app.models.roles_membership import RolesMembership

from .. import bp


@bp.route("/waitlisted", methods=["GET"])
def waitlisted():
    talks = Talks.select_all()
    return render_template(bp.tmpl("index.html"))
