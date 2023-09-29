from flask import render_template

from app.models.accounts import Accounts
from . import decorator_group, bp


@decorator_group("/accounts", methods=["GET"])
def accounts():
    accounts_ = Accounts.select_all()

    return render_template(
        bp.tmpl("accounts.html"),
        accounts=accounts_,
    )
