from flask import render_template

from app.models.talks import Talks
from . import decorator_group, bp


@decorator_group("/accepted", methods=["GET"])
def accepted():
    talks = Talks.select_all()
    return render_template(bp.tmpl("index.html"))
