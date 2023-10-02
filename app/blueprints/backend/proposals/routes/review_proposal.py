from flask import render_template, request, abort, url_for, redirect, flash

from app.models.update_feed import UpdateFeed
from app.models.proposal_votes import ProposalVotes
from app.models.proposal_statuses import ProposalStatuses
from app.models.proposals import Proposals
from . import bp, decorator_group


@decorator_group("/review/<int:proposal_id>", methods=["GET", "POST"])
def review_proposal(proposal_id):
    proposal = Proposals.select_using_proposal_id(proposal_id)
    if not proposal:
        return abort(404)

    if proposal.rel_proposal_status.unique_proposal_status_id == 102:
        UpdateFeed.create(
            fk_account_id=proposal.fk_account_id,
            title="Your Proposal is Under Review",
            message=f"Your proposal, {proposal.title}, is now under review by the committee.",
            image=None,
        )
        proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
            103).proposal_status_id
        proposal.save()

    if request.method == "POST":
        change_requested = True if request.form.get("change_requested") == "true" else False
        waitlisted = True if request.form.get("waitlisted") == "true" else False
        accepted = True if request.form.get("accepted") == "true" else False
        rejected = True if request.form.get("rejected") == "true" else False
        vote_for = True if request.form.get("vote_for") == "true" else False
        vote_against = True if request.form.get("vote_against") == "true" else False

        if change_requested:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                104).proposal_status_id
        elif waitlisted:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                106).proposal_status_id
        elif accepted:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                107).proposal_status_id
        elif rejected:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                108).proposal_status_id
        else:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                103).proposal_status_id

        if vote_for:
            ProposalVotes.vote_for(proposal.proposal_id, 1)
        elif vote_against:
            ProposalVotes.vote_against(proposal.proposal_id, 1)
        else:
            ProposalVotes.abstain(proposal.proposal_id, 1)

        flash("Proposal has been updated.")
        return redirect(url_for("proposals.review_proposal", proposal_id=proposal_id))

    return render_template(bp.tmpl("review-proposal.html"), proposal=proposal)
