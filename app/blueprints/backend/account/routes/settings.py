from flask import render_template, request, url_for, redirect, session, flash
from flask_imp.security import login_check, include_csrf

from app.models.accounts import Accounts
from .. import bp


@bp.route("/settings", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
@include_csrf()
def settings():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm_new_password = request.form.get("confirm_new_password")
        delete_account = True if request.form.get("delete_account") == "true" else False

        if delete_account:
            delete_password = request.form.get("delete_password")
            account = Accounts.select_using_account_id(session.get("account_id"))

            if account.password_check(delete_password):
                account.delete_account(session.get("account_id"))
            else:
                flash("Incorrect password. Please try again.")
                return redirect(url_for("account.settings"))

            session.clear()
            flash("Account deleted successfully. We are sorry to see you go.")
            return redirect(url_for("auth.login"))

        if not old_password or not new_password or not confirm_new_password:
            flash("Old password, new password and confirm new password fields cannot be empty.")
            return redirect(url_for("account.settings"))

        account = Accounts.select_using_account_id(session.get("account_id"))

        if account.password_check(old_password):
            if new_password == confirm_new_password:
                account.set_new_password(new_password)

                flash("Password changed successfully.")
                return redirect(url_for("account.settings"))

            flash("New password and confirm new password do not match.")
            return redirect(url_for("account.settings"))

    return render_template(bp.tmpl("settings.html"), csrf=session.get("csrf"))
