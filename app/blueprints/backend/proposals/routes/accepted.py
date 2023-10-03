from flask import render_template

from app.models.proposals import Proposals
from . import bp, decorator_group


@decorator_group("/accepted", methods=["GET"])
def accepted():
    proposals = Proposals.has_been_accepted()
    return render_template(bp.tmpl("accepted.html"), proposals=proposals)
