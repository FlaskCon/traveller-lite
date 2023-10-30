from datetime import datetime, date

from flask import render_template, session
from flask_imp.security import login_check

from app.models.conferences import Conferences
from app.models.proposals import Proposals
from app.utilities import DatetimeDeltaMC
from .. import bp


@bp.route("/proposals", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def proposals():
    proposals_ = Proposals.select_using_account_id(session.get("account_id"))
    conference_ = Conferences.select_by_year(datetime.now().year)

    able_to_propose = False
    now = DatetimeDeltaMC()

    if conference_:
        if isinstance(conference_.call_for_proposals_end_date, date):
            able_to_propose = True if (conference_.call_for_proposals_end_date - now.date).days > -1 else False

        if isinstance(conference_.call_for_proposals_end_date, datetime):
            able_to_propose = True if (conference_.call_for_proposals_end_date.date() - now.date).days > -1 else False

    return render_template(bp.tmpl("proposals.html"), proposals=proposals_, able_to_propose=able_to_propose)
