from flask import render_template

from app.models.proposals import Proposals
from . import bp, decorator_group


@decorator_group("/waitlisted", methods=["GET"])
def waitlisted():
    proposals = Proposals.has_been_waitlisted()
    return render_template(bp.tmpl("waitlisted.html"), proposals=proposals)
