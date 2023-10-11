from flask import render_template, flash, redirect, url_for, request

from app.models import Resources
from app.models.sponsors import Sponsors
from .. import bp


@bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        year = request.form.get("year")
        name = request.form.get("name")
        level = request.form.get("level")
        description = request.form.get("description")
        url = request.form.get("url")
        logo = request.form.get("logo")
        contact_information = request.form.get("contact_information")
        possible = request.form.get("possible")
        requested = request.form.get("requested")
        confirmed = request.form.get("confirmed")
        rejected = request.form.get("rejected")

        required_fields = [
            year,
            name,
        ]

        if not all(required_fields):
            flash("Year and name fields are required.")
            return redirect(url_for("staff_only.sponsors.add"))

        Sponsors.create(
            year=int(year),
            name=name,
            level=level,
            description=description,
            url=url,
            logo=logo,
            contact_information=contact_information,
            possible=True if possible == "true" else False,
            requested=True if requested == "true" else False,
            confirmed=True if confirmed == "true" else False,
            rejected=True if rejected == "true" else False,
        )

        flash("Sponsor added.")
        return redirect(url_for("staff_only.sponsors.index"))

    return render_template(
        bp.tmpl("add.html"),
        sponsor_levels=Resources.sponsor_levels,
    )
