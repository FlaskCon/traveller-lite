import mistune
from flask import render_template, request, redirect, url_for, session, flash
from flask_imp.security import login_check, include_csrf

from app.models.proposals import Proposals
from app.utilities.render_engines import HighlightRenderer
from .. import bp


@bp.route("/proposals/proposal/<int:proposal_id>", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
@include_csrf()
def proposal(proposal_id):
    proposal_ = Proposals.select_using_proposal_id(proposal_id)

    if not proposal_:
        return redirect(url_for("account.proposals"))

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

        proposal_.save_proposal(
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
            submit_proposal=True if submit_proposal == "true" else False,
        )

        if submit_proposal == "true":
            flash("Your proposal has been submitted! We will be in touch soon.")
            return redirect(url_for("account.proposals"))

        flash("Your proposal has been saved.")
        return redirect(url_for("account.proposals"))

    return render_template(bp.tmpl("proposal.html"), proposal=proposal_, csrf=session.get("csrf"))
