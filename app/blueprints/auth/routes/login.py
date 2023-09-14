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
    if request.method == "POST":
        # Login logic
        session["logged_in"] = True
        session["account_id"] = 1
        return redirect(url_for("account.index"))
    return render_template(bp.tmpl("login.html"))
