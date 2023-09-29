from flask import (
    render_template,
    url_for,
    redirect,
    request,
    flash,
    abort,
    session
)
from flask_imp.security import login_check, include_csrf
from app.models.accounts import Accounts

from .. import bp


@bp.route("/password-reset/<int:account_id>/<private_key>", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
@include_csrf()
def password_reset(account_id, private_key):
    account = Accounts.select_using_account_id(account_id)
    if not account:
        abort(404)
    if account.private_key is None or account.private_key != private_key:
        abort(404)

    if not account.confirmed:
        account.confirm_account()

    if request.method == "POST":
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                flash("Passwords do not match.")
                return redirect(url_for("auth.password_reset", account_id=account_id, private_key=private_key))

            account.reset_password(password)
            flash("Your password has been reset, you can now login.")
            return redirect(url_for("auth.login"))

    return render_template(bp.tmpl("set-new-password.html"), csrf=session["csrf"])
