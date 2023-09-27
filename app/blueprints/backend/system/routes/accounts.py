from flask import render_template
from flask_imp.security import login_check

from app.models.accounts import Accounts
from .. import bp


@bp.route("/accounts", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def accounts():
    accounts_ = Accounts.select_all()

    return render_template(
        bp.tmpl("accounts.html"),
        accounts=accounts_,
    )
