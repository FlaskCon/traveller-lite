from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def index():
    return render_template(bp.tmpl("index.html"))
