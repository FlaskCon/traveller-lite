from flask import render_template, request, url_for, redirect, flash, session
from flask_imp.auth import Auth
from flask_imp.security import login_check

from app.models.accounts import Accounts
from .. import bp


@bp.route("/signup/confirm/<int:account_id>", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
def signup_confirm(account_id):
    account = Accounts.select_using_account_id(account_id)
    if account:
        if account.confirmed:
            return redirect(url_for("account.index"))
    if not account:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        csrf = request.form.get("csrf")
        if not csrf or csrf != session["csrf"]:
            flash("Invalid CSRF token.")
            return redirect(url_for("auth.signup_confirm", account_id=account_id))

        conf_code = request.form.get("conf_code")

        if conf_code == account.private_key:
            account.confirmed = True
            account.save()

            flash("Account is confirmed, you can now login.")
            return redirect(url_for("auth.login"))

        else:
            flash("Confirmation code is incorrect.")
            return redirect(url_for("auth.signup_confirm", account_id=account_id))

    session["csrf"] = Auth.generate_form_token()
    return render_template(bp.tmpl("signup-confirm.html"), csrf=session["csrf"])
