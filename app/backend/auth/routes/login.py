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

from app.models.accounts import Accounts
from app.models.display_pictures import DisplayPictures
from .. import bp


@bp.route("/login", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
@include_csrf()
def login():
    if request.method == "POST":
        email_address = request.form.get("email_address")
        password = request.form.get("password")

        if email_address and password:
            account = Accounts.login(email_address, password)

            if account:

                if not account.confirmed:
                    flash(
                        "Please confirm your account via the link sent to your email address, "
                        "if you don't have this link, reset your password."
                    )
                    return redirect(url_for("auth.login"))

                if account.private_key:
                    account.remove_private_key()

                if not account.rel_profile:
                    account.create_profile()

                display_picture = account.rel_profile[0].fk_display_picture_id or 1

                session["logged_in"] = True
                session["account_id"] = account.account_id
                session["unique_display_picture_id"] = DisplayPictures.select_using_display_picture_id(
                    display_picture
                ).unique_display_picture_id
                return redirect(url_for("account.index"))
            else:
                flash("Incorrect email address or password")
                return redirect(url_for("auth.login"))

        else:
            flash("Please enter an email address and password")
            return redirect(url_for("auth.login"))

    return render_template(bp.tmpl("login.html"), csrf=session["csrf"])
