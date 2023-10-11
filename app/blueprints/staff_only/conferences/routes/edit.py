from flask import render_template, request, flash, redirect, url_for

from app.models.conferences import Conferences
from .. import bp


@bp.route("/edit/<int:conference_id>", methods=["GET", "POST"])
def edit(conference_id):
    conference = Conferences.select_by_conference_id(conference_id)
    if request.method == "POST":
        year = request.form.get("year")
        index_endpoint = request.form.get("index_endpoint")
        latest = request.form.get("latest")
        call_for_proposals_start_date = request.form.get("call_for_proposals_start_date")
        call_for_proposals_end_date = request.form.get("call_for_proposals_end_date")
        conference_start_date = request.form.get("conference_start_date")
        conference_end_date = request.form.get("conference_end_date")

        required_fields = [
            year,
            index_endpoint,
            latest,
            call_for_proposals_start_date,
            call_for_proposals_end_date,
            conference_start_date,
            conference_end_date,
        ]

        if not all(required_fields):
            flash("All fields are required.")
            return redirect(url_for("staff_only.conferences.edit", conference_id=conference_id))

        Conferences.update_by_conference_id(
            conference_id=conference_id,
            year=int(year),
            index_endpoint=index_endpoint,
            latest=True if latest == "True" else False,
            call_for_proposals_start_date=call_for_proposals_start_date,
            call_for_proposals_end_date=call_for_proposals_end_date,
            conference_start_date=conference_start_date,
            conference_end_date=conference_end_date
        )

        flash("Conference updated successfully.")
        return redirect(url_for("staff_only.conferences.index"))

    return render_template(bp.tmpl("edit.html"), conference=conference)
