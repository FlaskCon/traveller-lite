from flask import url_for, redirect

from .. import proposals_group


@proposals_group("/", methods=["GET"])
def index():
    return redirect(url_for("staff_only.proposals.dashboard"))
