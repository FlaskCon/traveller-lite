from flask import render_template, request, flash, redirect, url_for

from app.models.media_partners import MediaPartners
from .. import bp


@bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        year = request.form.get("year")
        name = request.form.get("name")
        description = request.form.get("description")
        url = request.form.get("url")
        logo = request.form.get("logo")

        required_fields = [
            year,
            name,
        ]

        if not all(required_fields):
            flash("Year and name fields are required.")
            return redirect(url_for("staff_only.media_partners.add"))

        MediaPartners.create(
            year=int(year),
            name=name,
            description=description,
            url=url,
            logo=logo,
        )

        flash("Media partner added.")
        return redirect(url_for("staff_only.media_partners.index"))
    return render_template(bp.tmpl("add.html"))
