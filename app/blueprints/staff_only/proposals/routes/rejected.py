from flask import render_template

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/rejected", methods=["GET"])
def rejected():
    proposals = Proposals.has_been_rejected()
    return render_template(bp.tmpl("rejected.html"), proposals=proposals)
