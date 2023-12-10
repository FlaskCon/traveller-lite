from flask import render_template, url_for, redirect, flash
from flask_imp.security import login_check
from app.models.accounts import Accounts

from .. import bp


@bp.get("/confirm/<int:account_id>/<private_key>")
@login_check("logged_in", True, pass_endpoint="account.index")
def confirm(account_id, private_key):
    account = Accounts.select_using_account_id(account_id)
    if account:
        if account.confirmed:
            flash("Your account is already confirmed.")
            return redirect(url_for("auth.login"))

        if Accounts.confirm_account_successful(account_id, private_key):
            flash("Your account has been confirmed, you can now login.")
            return redirect(url_for("auth.login"))
        else:
            render_template(bp.tmpl("confirm-error.html"))

    return redirect(url_for("auth.login"))
