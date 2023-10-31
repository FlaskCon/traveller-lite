from flask import render_template, request, abort, url_for, redirect, flash, session

from app.models.proposal_statuses import ProposalStatuses
from app.models.proposal_votes import ProposalVotes
from app.models.proposals import Proposals
from app.models.update_feed import UpdateFeed
from . import bp, decorator_group


@decorator_group("/review/<int:proposal_id>", methods=["GET", "POST"])
def review_proposal(proposal_id):
    proposal = Proposals.select_using_proposal_id(proposal_id)
    if not proposal:
        return abort(404)

    if proposal.rel_proposal_status.unique_proposal_status_id == 102:
        UpdateFeed.create(
            fk_account_id=proposal.fk_account_id,
            title="Your proposal is under review!",
            message=f"Your proposal: {proposal.title}, is now under review by the committee.",
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

        if change_requested:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                104).proposal_status_id
        elif waitlisted:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                106).proposal_status_id
            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Your proposal has been waitlisted.",
                message=f"Your proposal: {proposal.title}, has been waitlisted. "
                        f"The committee accepted your proposal, but there was no space to accommodate for it. "
                        f"We may contact you in the future if a spot opens up.",
                image=None,
            )
        elif accepted:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                107).proposal_status_id
            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Your proposal has been accepted!",
                message=f"Your proposal: {proposal.title}, is now under review by the committee.",
                image=None,
            )
        elif rejected:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                108).proposal_status_id
            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Unfortunately your proposal has been rejected...",
                message=f"Your proposal: {proposal.title}, has been rejected. "
                        f"You can view the reason why by viewing the proposal.",
                image=None,
            )
        else:
            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                103).proposal_status_id

        if request.form.get("redirect_to"):
            flash("Proposal has been updated.")
            return redirect(url_for(request.form.get("redirect_to"), proposal_id=proposal_id))

        vote_for = True if request.form.get("vote_for") == "true" else False
        vote_against = True if request.form.get("vote_against") == "true" else False

        if vote_for:
            ProposalVotes.vote_for(proposal.proposal_id, session.get("account_id", 0))
        elif vote_against:
            ProposalVotes.vote_against(proposal.proposal_id, session.get("account_id", 0))
        else:
            ProposalVotes.abstain(proposal.proposal_id, session.get("account_id", 0))

        flash("Proposal has been updated.")
        return redirect(url_for("staff_only.proposals.review_proposal", proposal_id=proposal_id))

    breadcrumbs = [
        ("Proposals Dashboard", url_for('staff_only.proposals.dashboard')),
        ("Proposals to Review", url_for('staff_only.proposals.review')),
        (proposal.title, None)
    ]

    return render_template(
        bp.tmpl("review-proposal.html"),
        proposal=proposal,
        breadcrumbs=breadcrumbs,
        show_voting=True,
        vote_position=ProposalVotes.get_vote_position(proposal.proposal_id, session.get("account_id", 0)),
    )
