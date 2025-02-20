from flask import render_template, request, url_for, redirect, flash, session
from flask_imp.auth import Auth
from flask_imp.security import login_check
from pyisemail import is_email

from app.extensions import email_settings
from app.huey import tasks
from app.models.accounts import Accounts
from .. import bp


@bp.route("/signup", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
def signup():
    if request.method == "POST":
        csrf = request.form.get("csrf")
        if not csrf or csrf != session["csrf"]:
            flash("Invalid CSRF token.")
            return redirect(url_for("auth.signup"))

        email_address = request.form.get("email_address")
        name_or_alias = request.form.get("name_or_alias")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not is_email(email_address):
            flash("Invalid email address.")
            return redirect(url_for("auth.signup"))

        if email_address and password and confirm_password:
            if password != confirm_password:
                flash("Passwords do not match.")
                return render_template(
                    bp.tmpl("signup.html"), email_address=email_address
                )

            if Accounts.exists(request.form["email_address"]):
                flash("An account with that email address already exists.")
                return redirect(url_for("auth.signup"))

            new_account = Accounts.signup(email_address, password, name_or_alias, False)
            if new_account:
                tasks.send_email(
                    email_settings,
                    [email_address],
                    "Confirm Your Account",
                    render_template(
                        "global/email/confirm-email.html",
                        account_id=new_account.account_id,
                        private_key=new_account.private_key,
                    ),
                )

                flash(
                    "Account created. Please check your email to confirm your account."
                )
                return redirect(url_for("auth.signup_confirm", account_id=new_account.account_id))

            else:
                flash("There was an error creating your account.")
                return redirect(url_for("auth.signup"))

    session["csrf"] = Auth.generate_form_token()
    return render_template(bp.tmpl("signup.html"), csrf=session["csrf"])
