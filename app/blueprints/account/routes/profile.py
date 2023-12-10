import pycountry
from flask import render_template, session, request, url_for, redirect, flash
from flask_imp.security import login_check, include_csrf

from app.models.display_pictures import DisplayPictures
from app.models.profiles import Profiles
from .. import bp


@bp.route("/profile", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
@include_csrf()
def profile():
    # account pulled from global/extends/backend.html using __account__
    profile_ = Profiles.select_using_account_id(session.get("account_id"))

    if request.method == "POST":
        fk_display_picture_id = request.form.get("fk_display_picture_id")
        company_name = request.form.get("company_name")
        name_or_alias = request.form.get("name_or_alias")
        pronouns = request.form.get("pronouns")
        bio = request.form.get("bio")
        country = request.form.get("country")
        website = request.form.get("website")

        profile_.fk_display_picture_id = fk_display_picture_id
        profile_.company_name = company_name
        profile_.name_or_alias = name_or_alias
        profile_.pronouns = pronouns
        profile_.bio = bio
        profile_.country = country
        profile_.website = website

        profile_.save()

        session[
            "unique_display_picture_id"
        ] = DisplayPictures.select_using_display_picture_id(
            fk_display_picture_id
        ).unique_display_picture_id

        flash("Your profile has been updated.")
        return redirect(url_for("account.profile"))

    display_pictures = DisplayPictures.select_all()
    raw_earned_display_pictures = profile_.earned_display_pictures.get("earned", [])
    standard_display_pictures = [dp for dp in display_pictures if not dp.limited]
    earned_display_pictures = (
        [
            dp
            for dp in display_pictures
            if dp.unique_display_picture_id in raw_earned_display_pictures
        ]
        if raw_earned_display_pictures
        else []
    )

    sorted_countries = sorted([country.name for country in pycountry.countries])

    return render_template(
        bp.tmpl("profile.html"),
        profile=profile_,
        standard_display_pictures=standard_display_pictures,
        earned_display_pictures=earned_display_pictures,
        csrf=session["csrf"],
        all_countries=sorted_countries,
    )
