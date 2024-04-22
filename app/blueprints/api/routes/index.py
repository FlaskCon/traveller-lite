from datetime import datetime

from flask import session

from app.models.conferences import Conferences
from app.utilities.datetime_delta import DatetimeDelta
from .. import bp


@bp.get("/logged-in")
def is_logged_in():
    return {"logged_in": session.get("logged_in", False)}


@bp.get("/conference/<int:year>")
def index(year):
    conference = Conferences.select_by_year(year)

    def style_date(date):

        day = date.strftime("%-d")
        month = date.strftime("%B")

        if int(day) % 10 == 1:
            day += "st"
        elif int(day) % 10 == 2:
            day += "nd"
        elif int(day) % 10 == 3:
            day += "rd"
        else:
            day += "th"

        return f"{month} the {day}"



    cfp_end_date = style_date(conference.call_for_proposals_end_date)
    cfp_start_date = style_date(conference.call_for_proposals_start_date)
    cfp_days_left = DatetimeDelta().days_between(conference.call_for_proposals_end_date)

    conference_end_date = style_date(conference.conference_end_date)
    conference_start_date = style_date(conference.conference_start_date)

    return {
        "year": conference.year,
        "latest": conference.latest,
        "call_for_proposals_start_date": cfp_start_date,
        "call_for_proposals_end_date": cfp_end_date,
        "call_for_proposals_days_left": cfp_days_left,
        "conference_start_date": conference_start_date,
        "conference_end_date": conference_end_date,
    }
