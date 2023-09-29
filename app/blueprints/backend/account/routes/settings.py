from flask import render_template, request, url_for, redirect, session, flash
from flask_imp.security import login_check

from app.models.accounts import Accounts
from .. import bp


@bp.route("/settings", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def settings():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        delete_account = True if request.form.get("delete_account") == "true" else False

        if delete_account:
            return redirect(url_for("account.delete"))

        account = Accounts.select_using_account_id(session.get("account_id"))

        if account.password_check(old_password):
            if new_password == confirm_password:
                account.set_new_password(new_password)

                flash("Password changed successfully.")
                return redirect(url_for("account.settings"))

            flash("Password and confirm password do not match.")
            return redirect(url_for("account.settings"))

    return render_template(bp.tmpl("settings.html"))
