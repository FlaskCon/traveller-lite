from flask import render_template, session
from flask_imp.security import login_check

from app.models.talks import Talks
from .. import bp


@bp.route("/talks", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def talks():
    talks_ = Talks.select_using_account_id(session.get("account_id"))
    return render_template(bp.tmpl("talks.html"), talks=talks_)
