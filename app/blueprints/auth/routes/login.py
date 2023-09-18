from flask import (
    render_template,
    request,
    url_for,
    redirect, session
)
from flask_imp.security import login_check

from .. import bp


@bp.route("/login", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
def login():
    return render_template(bp.tmpl("login.html"))
