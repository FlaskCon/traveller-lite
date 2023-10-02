from flask import render_template

from app.models.proposals import Proposals
from . import bp, decorator_group


@decorator_group("/review", methods=["GET"])
def review():
    proposals = Proposals.for_review()
    return render_template(bp.tmpl("review.html"), proposals=proposals)
