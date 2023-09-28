from flask import render_template

from app.models.talks import Talks
from .. import bp


@bp.route("/review", methods=["GET"])
def review():
    talks = Talks.for_review()
    return render_template(bp.tmpl("review.html"), talks=talks)


@bp.route("/review/<int:talk_id>", methods=["GET"])
def review_talk(talk_id):
    talk = Talks.select_using_talk_id(talk_id)
    return render_template(bp.tmpl("review_talk.html"), talk=talk)
