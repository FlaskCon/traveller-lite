from flask import render_template, session

from app.models.conferences import Conferences
from app.models.proposal_votes import ProposalVotes
from app.models.proposals import Proposals
from .. import bp, proposals_group


@proposals_group("/dashboard", methods=["GET"])
def dashboard():
    year = session.get("year", 0)
    available_years = Conferences.get_all_available_years()

    if year == 0:
        year = available_years[0]
        session["year"] = year

    leaderboard = Proposals.leaderboard(year=year)
    prep_not_sent_reminder = (
        Proposals.count_total_proposals_in_status_prep_not_sent_a_reminder_to_submit(
            year=year
        )
    )
    total_in_prep = Proposals.count_total_proposals_in_status_prep(year=year)
    total_proposals, total_proposal_ids = (
        Proposals.count_total_proposals_at_reviewer_seen_statuses(year=year)
    )

    total_votes = ProposalVotes.count_total_votes(total_proposal_ids)
    total_for_votes = ProposalVotes.count_total_for_votes(total_proposal_ids)
    total_against_votes = ProposalVotes.count_total_against_votes(total_proposal_ids)

    total_for_review = len(Proposals.for_review(year=year))
    total_accepted = len(Proposals.has_been_accepted(year=year))
    total_rejected = len(Proposals.has_been_rejected(year=year))
    total_waitlisted = len(Proposals.has_been_waitlisted(year=year))

    return render_template(
        bp.tmpl("dashboard.html"),
        available_years=available_years,
        total_proposals=total_proposals,
        total_in_prep=total_in_prep,
        prep_not_sent_reminder=prep_not_sent_reminder,
        total_votes=total_votes,
        total_for_votes=total_for_votes,
        total_against_votes=total_against_votes,
        total_for_review=total_for_review,
        total_accepted=total_accepted,
        total_rejected=total_rejected,
        total_waitlisted=total_waitlisted,
        leaderboard=leaderboard,
    )
