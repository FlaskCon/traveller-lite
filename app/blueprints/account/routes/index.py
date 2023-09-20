from flask import render_template, session
from flask_imp.security import login_check

from .. import bp
from app.models.accounts import Accounts


@bp.route("/", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def index():
    account_id = session.get("account_id")
    account = Accounts.select_using_account_id(account_id)
    profile = account.rel_profile
    return render_template(
        bp.tmpl("index.html"),
        account=account,
        profile=profile[0] if profile else None
    )
