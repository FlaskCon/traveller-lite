from flask import render_template

from app.models.talks import Talks
from . import bp, decorator_group


@decorator_group("/review", methods=["GET"])
def review():
    talks = Talks.for_review()
    return render_template(bp.tmpl("review.html"), talks=talks)
