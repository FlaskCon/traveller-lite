from flask import render_template

from app.models.talks import Talks
from . import bp, decorator_group


@decorator_group("/rejected", methods=["GET"])
def rejected():
    talks = Talks.select_all()
    return render_template(bp.tmpl("index.html"))
