from flask import render_template, request, redirect, url_for, flash

from app.models.conferences import Conferences
from .. import bp


@bp.route("/add", methods=["GET", "POST"])
def add():
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
            flash("Please fill out all fields.")
            return redirect(url_for("staff_only.conferences.add"))

        Conferences.create(
            year=int(year),
            index_endpoint=index_endpoint,
            latest=True if latest == "true" else False,
            call_for_proposals_start_date=call_for_proposals_start_date,
            call_for_proposals_end_date=call_for_proposals_end_date,
            conference_start_date=conference_start_date,
            conference_end_date=conference_end_date
        )

        flash(f"Conference {year} added.")
        return redirect(url_for("staff_only.conferences.index"))

    return render_template(bp.tmpl("add.html"))
