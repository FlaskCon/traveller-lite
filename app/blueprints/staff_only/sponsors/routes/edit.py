from flask import render_template, flash, redirect, url_for, request

from app.models import Resources
from app.models.sponsors import Sponsors
from .. import bp, sponsor_group


@sponsor_group("/edit/<int:sponsor_id>", methods=["GET", "POST"])
def edit(sponsor_id):
    sponsor = Sponsors.select_by_sponsor_id(sponsor_id)
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
            return redirect(url_for("staff_only.sponsors.edit", sponsor_id=sponsor_id))

        Sponsors.update_by_sponsor_id(
            sponsor_id=sponsor_id,
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

        flash("Sponsor updated successfully.")
        return redirect(url_for("staff_only.sponsors.index"))

    sponsor_status = (
        "possible"
        if sponsor.possible
        else "requested"
        if sponsor.requested
        else "confirmed"
        if sponsor.confirmed
        else "rejected"
    )

    return render_template(
        bp.tmpl("edit.html"),
        sponsor=sponsor,
        sponsor_status=sponsor_status,
        sponsor_levels=Resources.sponsor_levels,
    )
