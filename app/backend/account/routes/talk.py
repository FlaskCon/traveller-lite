import mistune
from flask import render_template, request, redirect, url_for
from flask_imp.security import login_check

from app.models.talks import Talks
from app.utilities.render_engines import HighlightRenderer
from .. import bp


@bp.route("/talks/talk/<int:talk_id>", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def talk(talk_id):
    talk_ = Talks.select_using_talk_id(talk_id)

    if not talk_:
        return redirect(url_for("account.talks"))

    if request.method == "POST":
        title = request.form.get("title")
        detail = request.form.get("detail")
        abstract = request.form.get("abstract")
        short_biography = request.form.get("short_biography")
        notes_or_requests = request.form.get("notes_or_requests")
        tags = request.form.get("tags")

        # hidden vals
        submit_proposal = request.form.get("submit_proposal")

        html_engine = mistune.create_markdown(renderer=HighlightRenderer())

        if detail:
            detail_markdown = html_engine(detail)
        else:
            detail_markdown = None

        if abstract:
            abstract_markdown = html_engine(abstract)
        else:
            abstract_markdown = None

        if short_biography:
            short_biography_markdown = html_engine(short_biography)
        else:
            short_biography_markdown = None

        if notes_or_requests:
            notes_or_requests_markdown = html_engine(notes_or_requests)
        else:
            notes_or_requests_markdown = None

        talk_.save_talk(
            title=title,
            detail=detail,
            detail_markdown=detail_markdown,
            abstract=abstract,
            abstract_markdown=abstract_markdown,
            short_biography=short_biography,
            short_biography_markdown=short_biography_markdown,
            notes_or_requests=notes_or_requests,
            notes_or_requests_markdown=notes_or_requests_markdown,
            tags=tags.replace(" ", "") if tags else None,
            submit_proposal=submit_proposal,
        )

        if submit_proposal:
            return redirect(url_for("account.talks"))

        return redirect(url_for("account.talk", talk_id=talk_id))

    return render_template(bp.tmpl("talk.html"), talk=talk_)
