from flask import url_for, redirect

from . import decorator_group


@decorator_group("/", methods=["GET"])
def index():
    return redirect(url_for("staff_only.proposals.dashboard"))
