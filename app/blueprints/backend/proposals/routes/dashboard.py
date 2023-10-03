from flask import render_template

from app.models.proposal_votes import ProposalVotes
from app.models.proposals import Proposals
from . import decorator_group, bp


@decorator_group("/dashboard", methods=["GET"])
def dashboard():
    total_proposals = Proposals.count_total_proposals_at_reviewer_seen_statuses()
    total_votes = ProposalVotes.count_total_votes()
    total_for_votes = ProposalVotes.count_total_for_votes()
    total_against_votes = ProposalVotes.count_total_against_votes()

    total_for_review = len(Proposals.for_review())
    total_accepted = len(Proposals.has_been_accepted())
    total_rejected = len(Proposals.has_been_rejected())
    total_waitlisted = len(Proposals.has_been_waitlisted())

    return render_template(
        bp.tmpl("dashboard.html"),
        total_proposals=total_proposals,
        total_votes=total_votes,
        total_for_votes=total_for_votes,
        total_against_votes=total_against_votes,
        total_for_review=total_for_review,
        total_accepted=total_accepted,
        total_rejected=total_rejected,
        total_waitlisted=total_waitlisted
    )
