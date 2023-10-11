from flask import render_template, session
from flask_imp.security import login_check

from app.models.proposals import Proposals
from .. import bp


@bp.route("/proposals", methods=["GET"])
@login_check("logged_in", True, "auth.login")
def proposals():
    proposals_ = Proposals.select_using_account_id(session.get("account_id"))
    return render_template(bp.tmpl("proposals.html"), proposals=proposals_)
