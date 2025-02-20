from datetime import datetime

from flask import render_template, request, url_for, redirect, session, flash
from flask_imp.security import login_check, include_csrf

from app.models.accounts import Accounts
from app.models.display_pictures import DisplayPictures
from app.models.profiles import Profiles
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
                # if account exists

                if account.disabled:
                    # if account is disabled
                    flash(
                        "Your account has been disabled, please contact the administrator."
                    )
                    return redirect(url_for("auth.login"))

                if not account.confirmed:
                    # if account is not confirmed
                    flash(
                        "Please confirm your account via the link sent to your email address, "
                        "if you don't have this link, reset your password."
                    )
                    return redirect(url_for("auth.login"))

                if account.private_key:
                    # if account has a private key, remove it
                    account.remove_private_key()

                if not account.rel_profile:
                    # if account has no profile, create one
                    account.create_profile()

                # get current display picture id
                display_picture_id = account.rel_profile.fk_display_picture_id or 1

                session["logged_in"] = True
                session["account_id"] = account.account_id
                # get unique display picture id, and add it to the session
                session["unique_display_picture_id"] = (
                    DisplayPictures.select_using_display_picture_id(
                        display_picture_id
                    ).unique_display_picture_id
                )

                if DisplayPictures.select_using_unique_display_picture_id(
                    datetime.now().year
                ):
                    # get the current year's display picture
                    Profiles.add_earned_display_picture(
                        account.account_id, datetime.now().year
                    )

                return redirect(url_for("account.index"))
            else:
                flash("Incorrect email address or password.")
                return redirect(url_for("auth.login"))

        else:
            flash("Please enter an email address and password.")
            return redirect(url_for("auth.login"))

    return render_template(bp.tmpl("login.html"), csrf=session["csrf"])
