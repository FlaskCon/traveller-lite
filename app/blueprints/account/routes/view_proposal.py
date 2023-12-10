from flask import render_template, redirect, url_for
from flask_imp.security import login_check

from app.models.proposals import Proposals
from .. import bp


@bp.route("/proposals/proposal/<int:proposal_id>/view", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def view_proposal(proposal_id):
    proposal_ = Proposals.select_using_proposal_id(proposal_id)

    if not proposal_:
        return redirect(url_for("account.proposals"))

    return render_template(bp.tmpl("view-proposal.html"), proposal=proposal_)
