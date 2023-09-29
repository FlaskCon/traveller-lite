from flask import render_template, request, abort, url_for, redirect, flash

from app.models.talk_votes import TalkVotes
from app.models.talks import Talks
from . import bp, decorator_group


@decorator_group("/review/<int:talk_id>", methods=["GET", "POST"])
def review_talk(talk_id):
    talk = Talks.select_using_talk_id(talk_id)
    if not talk:
        return abort(404)

    if request.method == "POST":
        vote_for = True if request.form.get("vote_for") == "true" else False
        vote_against = True if request.form.get("vote_against") == "true" else False

        if vote_for:
            TalkVotes.vote_for(talk.talk_id, 1)
        elif vote_against:
            TalkVotes.vote_against(talk.talk_id, 1)
        else:
            TalkVotes.abstain(talk.talk_id, 1)

        flash("Your vote has been recorded.")
        return redirect(url_for("proposals.review_talk", talk_id=talk_id))

    return render_template(bp.tmpl("review_talk.html"), talk=talk)
