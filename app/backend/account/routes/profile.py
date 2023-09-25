from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/profile", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def profile():
    # account pulled from global/extends/backend.html using __account__
    return render_template(bp.tmpl("profile.html"))
