from flask import request, session, url_for, redirect

from .. import proposals_group


@proposals_group("/set/year", methods=["POST"])
def set_year():
    year = request.form.get("year", default=0, type=int)
    session["year"] = year
    return redirect(url_for("staff_only.proposals.dashboard"))
