from flask import (
    render_template,
    request,
    url_for,
    redirect,
    session,
    flash
)
from flask_imp.security import login_check, include_csrf

from app.models.accounts import Accounts
from app.models.email_queue import EmailQueue
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

                EmailQueue.add_emails_to_send([
                    {
                        "email_to": email_address,
                        "email_subject": "Confirm your account",
                        "email_message": render_template(
                            "global/email/password-reset-link.html",
                            account_id=account.account_id,
                            private_key=private_key,
                        )
                    }
                ])

                EmailQueue.process_queue()

                flash("Password reset link sent to your email address.")
                return redirect(url_for("auth.login"))

        flash("That account does not exist.")
        return redirect(url_for("auth.login"))

    return render_template(bp.tmpl("forgot-password.html"), csrf=session["csrf"])
