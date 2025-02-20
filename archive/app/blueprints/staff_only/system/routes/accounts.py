from flask import render_template

from app.models.accounts import Accounts
from .. import system_group, bp


@system_group("/accounts", methods=["GET"])
def accounts():
    accounts_ = Accounts.select_all()

    return render_template(
        bp.tmpl("accounts.html"),
        accounts=accounts_,
    )
