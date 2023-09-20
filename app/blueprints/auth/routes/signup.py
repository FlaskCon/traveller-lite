from flask import (
    render_template,
    request,
    url_for,
    redirect,
    flash,
    session
)
from flask_imp.security import login_check

from .. import bp
from app.models.accounts import Accounts
from app.extensions import email_settings, EmailService
from flask_imp.auth import Auth


@bp.route("/signup", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
def signup():
    if request.method == "POST":
        csrf = request.form.get("csrf")
        if not csrf or csrf != session["csrf"]:
            flash("Invalid CSRF token")
            return redirect(url_for("auth.signup"))

        email_address = request.form.get("email_address")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if email_address and password and confirm_password:
            if password != confirm_password:
                flash("Passwords do not match")
                return render_template(bp.tmpl("signup.html"), email_address=email_address)

            if Accounts.exists(request.form["email_address"]):
                flash("An account with that email address already exists")
                return redirect(url_for("auth.signup"))

            new_account = Accounts.create(email_address, password)
            if new_account:
                EmailService(
                    email_settings).recipients(
                    [email_address]).subject(
                    "Confirm your account").body(
                    render_template(
                        "global/email/confirm-email.html",
                        account_id=new_account.account_id,
                        private_key=new_account.private_key,
                    )
                ).send()
                flash("Account created. Please check your email to confirm your account")
                return redirect(url_for("auth.login"))
            else:
                flash("There was an error creating your account")
                return redirect(url_for("auth.signup"))

    session["csrf"] = Auth.generate_form_token()
    return render_template(bp.tmpl("signup.html"), csrf=session["csrf"])
