import mistune
from flask import render_template, request, redirect, url_for
from flask_imp.security import login_check

from app.models.talks import Talks
from app.utilities.render_engines import HighlightRenderer
from .. import bp


@bp.route("/talks/talk/<int:talk_id>/view", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def view_talk(talk_id):
    talk_ = Talks.select_using_talk_id(talk_id)

    if not talk_:
        return redirect(url_for("account.talks"))

    return render_template(bp.tmpl("view-talk.html"), talk=talk_)
