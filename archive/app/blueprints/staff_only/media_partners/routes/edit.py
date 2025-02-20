from flask import render_template, request, flash, redirect, url_for

from app.models.media_partners import MediaPartners

from .. import bp, media_partners_group


@media_partners_group("/edit/<int:media_partner_id>", methods=["GET", "POST"])
def edit(media_partner_id):
    media_partner = MediaPartners.select_by_media_partner_id(media_partner_id)
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
            return redirect(
                url_for(
                    "staff_only.media_partners.edit", media_partner_id=media_partner_id
                )
            )

        MediaPartners.update_by_media_partner_id(
            media_partner_id=media_partner_id,
            year=int(year),
            name=name,
            description=description,
            url=url,
            logo=logo,
        )

        flash("Media partner updated successfully.")
        return redirect(url_for("staff_only.media_partners.index"))

    return render_template(
        bp.tmpl("edit.html"),
        media_partner=media_partner,
    )
