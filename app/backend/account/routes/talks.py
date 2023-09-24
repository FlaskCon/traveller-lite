from flask import render_template
from flask_imp.security import login_check

from .. import bp


@bp.route("/talks", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def talks():
    return render_template(bp.tmpl("talks.html"))


@bp.route("/talks/propose-a-new-talk", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def propose_a_new_talk():
    return render_template(bp.tmpl("propose-a-new-talk.html"))
