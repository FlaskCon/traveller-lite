from flask import render_template, session

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/accepted", methods=["GET"])
def accepted():
    proposals = Proposals.has_been_accepted(session.get("year", 0))
    return render_template(bp.tmpl("accepted.html"), proposals=proposals)
