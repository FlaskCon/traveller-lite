import os

from flask import render_template, request, abort, url_for, redirect, flash, session

from app.models.email_queue import EmailQueue
from app.models.proposal_statuses import ProposalStatuses
from app.models.proposal_votes import ProposalVotes
from app.models.proposals import Proposals
from app.models.update_feed import UpdateFeed
from . import bp, decorator_group

FLASKCON_EMAIL_ADDRESS = os.environ.get("FLASKCON_EMAIL_ADDRESS")


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
        canceled = True if request.form.get("canceled") == "true" else False

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
                        f"The committee accepted your proposal, but there was no space to accommodate for it.",
                image=None,
            )

            EmailQueue.add_emails_to_send([
                {
                    "email_to": proposal.rel_account.email_address,
                    "email_subject": "Your Proposal Has Been Waitlisted",
                    "email_message": render_template(
                        "global/email/proposal-waitlisted.html",
                        proposal=proposal,
                        to_account=True,
                        flaskcon_email=FLASKCON_EMAIL_ADDRESS,
                    )
                },
                {
                    "email_to": FLASKCON_EMAIL_ADDRESS,
                    "email_subject": "Notification: Proposal Waitlisted",
                    "email_message": render_template(
                        "global/email/proposal-waitlisted.html",
                        proposal=proposal,
                        to_account=False,
                        account_email_address=proposal.rel_account.email_address,
                    )
                }
            ])

            EmailQueue.process_queue()

        elif accepted:

            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                107).proposal_status_id

            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Your proposal has been accepted!",
                message=f"Your proposal: {proposal.title}, is now under review by the committee.",
                image=None,
            )

            EmailQueue.add_emails_to_send([
                {
                    "email_to": proposal.rel_account.email_address,
                    "email_subject": "Your Proposal Has Been Accepted!",
                    "email_message": render_template(
                        "global/email/proposal-accepted.html",
                        proposal=proposal,
                        to_account=True,
                        flaskcon_email=FLASKCON_EMAIL_ADDRESS,
                    )
                },
                {
                    "email_to": FLASKCON_EMAIL_ADDRESS,
                    "email_subject": "Notification: Proposal Accepted",
                    "email_message": render_template(
                        "global/email/proposal-accepted.html",
                        proposal=proposal,
                        to_account=False,
                        account_email_address=proposal.rel_account.email_address,
                    )
                }
            ])

            EmailQueue.process_queue()

        elif rejected:

            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                108).proposal_status_id

            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Unfortunately your proposal has been rejected...",
                message=f"Your proposal: {proposal.title}, has been rejected. ",
                image=None,
            )

            EmailQueue.add_emails_to_send([
                {
                    "email_to": proposal.rel_account.email_address,
                    "email_subject": "We Have Some Bad News...",
                    "email_message": render_template(
                        "global/email/proposal-rejected.html",
                        proposal=proposal,
                        to_account=True,
                        flaskcon_email=FLASKCON_EMAIL_ADDRESS,
                    )
                },
                {
                    "email_to": FLASKCON_EMAIL_ADDRESS,
                    "email_subject": "Notification: Proposal Accepted",
                    "email_message": render_template(
                        "global/email/proposal-rejected.html",
                        proposal=proposal,
                        to_account=False,
                        account_email_address=proposal.rel_account.email_address,
                    )
                }
            ])

            EmailQueue.process_queue()

        elif canceled:

            proposal.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(
                109).proposal_status_id

            UpdateFeed.create(
                fk_account_id=proposal.fk_account_id,
                title="Your proposal has been canceled.",
                message=f"Your proposal: {proposal.title}, has been canceled. ",
                image=None,
            )

            EmailQueue.add_emails_to_send([
                {
                    "email_to": proposal.rel_account.email_address,
                    "email_subject": "Your Proposal Has Been Canceled",
                    "email_message": render_template(
                        "global/email/proposal-canceled.html",
                        proposal=proposal,
                        to_account=True,
                        flaskcon_email=FLASKCON_EMAIL_ADDRESS,
                    )
                },
                {
                    "email_to": FLASKCON_EMAIL_ADDRESS,
                    "email_subject": "Notification: Proposal Canceled",
                    "email_message": render_template(
                        "global/email/proposal-canceled.html",
                        proposal=proposal,
                        to_account=False,
                        account_email_address=proposal.rel_account.email_address,
                    )
                }
            ])

            EmailQueue.process_queue()

            flash("Proposal has been canceled.")
            return redirect(url_for("staff_only.proposals.dashboard"))

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
