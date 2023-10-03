from flask import render_template

from app.models.accounts import Accounts
from . import decorator_group, bp


@decorator_group("/dashboard", methods=["GET"])
def dashboard():
    total_accounts = Accounts.count_total_accounts()
    return render_template(bp.tmpl("dashboard.html"), total_accounts=total_accounts)
