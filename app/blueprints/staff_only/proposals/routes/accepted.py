from flask import render_template

from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/accepted", methods=["GET"])
def accepted():
    proposals = Proposals.has_been_accepted()
    return render_template(bp.tmpl("accepted.html"), proposals=proposals)
