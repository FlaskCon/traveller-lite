from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/update-feed", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def update_feed():
    return render_template(bp.tmpl("update-feed.html"))
