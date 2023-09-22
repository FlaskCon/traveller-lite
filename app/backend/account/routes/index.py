from flask import render_template, session
from flask_imp.security import login_check

from .. import bp
from app.models.accounts import Accounts


@bp.route("/", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def index():
    account = Accounts.select_using_account_id(session.get("account_id"))

    return render_template(
        bp.tmpl("index.html"),
        profile=account.rel_profile[0] if account.rel_profile else None,
    )
