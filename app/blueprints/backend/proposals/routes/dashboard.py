from flask import render_template

from app.models.talk_votes import TalkVotes
from app.models.talks import Talks
from . import decorator_group, bp


@decorator_group("/dashboard", methods=["GET"])
def dashboard():
    total_talks = Talks.count_total_talks_at_reviewer_seen_statuses()
    total_votes = TalkVotes.count_total_votes()
    total_for_votes = TalkVotes.count_total_for_votes()
    total_against_votes = TalkVotes.count_total_against_votes()

    return render_template(
        bp.tmpl("dashboard.html"),
        total_talks=total_talks,
        total_votes=total_votes,
        total_for_votes=total_for_votes,
        total_against_votes=total_against_votes,
    )
