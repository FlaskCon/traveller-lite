from flask import render_template, session

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/waitlisted", methods=["GET"])
def waitlisted():
    proposals = Proposals.has_been_waitlisted(session.get("year", 0))
    return render_template(bp.tmpl("waitlisted.html"), proposals=proposals)
