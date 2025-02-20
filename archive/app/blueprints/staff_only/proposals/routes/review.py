from flask import render_template, session

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/review", methods=["GET"])
def review():
    proposals = Proposals.for_review(session.get("year", 0))
    return render_template(bp.tmpl("review.html"), proposals=proposals)
