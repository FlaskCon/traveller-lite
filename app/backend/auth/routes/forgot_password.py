from flask import (
    render_template,
    request,
    url_for,
    redirect,
    session,
    flash
)
from flask_imp import Auth
from flask_imp.security import login_check, include_csrf

from app.extensions import EmailService, email_settings
from app.models.accounts import Accounts
from app.models.display_pictures import DisplayPictures
from .. import bp


@bp.route("/forgot-password", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
@include_csrf()
def forgot_password():
    if request.method == "POST":
        email_address = request.form.get("email_address")

        if email_address:
            if Accounts.exists(email_address):
                account = Accounts.select_using_email_address(email_address)
                private_key = account.new_private_key()

                EmailService(
                    email_settings).recipients(
                    [email_address]).subject(
                    "Password reset link").body(
                    render_template(
                        "global/email/password-reset-link.html",
                        account_id=account.account_id,
                        private_key=private_key,
                    )
                ).send()

                flash("Password reset link sent to your email address")
                return redirect(url_for("auth.login"))

        flash("That account does not exist")
        return redirect(url_for("auth.login"))

    return render_template(bp.tmpl("forgot-password.html"), csrf=session["csrf"])
