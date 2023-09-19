from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/your-account", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def your_account():
    return render_template(bp.tmpl("your-account.html"))
