from flask import render_template

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/waitlisted", methods=["GET"])
def waitlisted():
    proposals = Proposals.has_been_waitlisted()
    return render_template(bp.tmpl("waitlisted.html"), proposals=proposals)
