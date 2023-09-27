from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/dashboard", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def dashboard():
    return render_template(bp.tmpl("dashboard.html"))
