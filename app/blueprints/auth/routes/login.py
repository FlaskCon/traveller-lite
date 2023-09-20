from flask import (
    render_template,
    request,
    url_for,
    redirect,
    session,
    flash
)
from flask_imp import Auth
from flask_imp.security import login_check

from app.models.accounts import Accounts
from app.models.display_pictures import DisplayPictures
from .. import bp


@bp.route("/login", methods=["GET", "POST"])
@login_check("logged_in", True, pass_endpoint="account.index")
def login():
    if request.method == "POST":
        csrf = request.form.get("csrf")
        if not csrf or csrf != session["csrf"]:
            flash("Invalid CSRF token")
            return redirect(url_for("auth.login"))

        email_address = request.form.get("email_address")
        password = request.form.get("password")

        if email_address and password:
            account = Accounts.login(email_address, password)
            if account:
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

    session["csrf"] = Auth.generate_form_token()
    return render_template(bp.tmpl("login.html"), csrf=session["csrf"])
