from datetime import datetime, date

import mistune
from flask import render_template, request, session, redirect, url_for, flash
from flask_imp.security import login_check

from app.extensions import email_settings
from app.huey import tasks
from app.models.accounts import Accounts
from app.models.conferences import Conferences
from app.models.proposals import Proposals
from app.utilities import DatetimeDeltaMC
from app.utilities.render_engines import HighlightRenderer
from .new_proposal import FLASKCON_EMAIL_ADDRESS
from .. import bp


@bp.route("/proposals/proposal/<int:proposal_id>/edit", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def edit_proposal(proposal_id):
    proposal_ = Proposals.select_using_proposal_id(proposal_id)

    if not proposal_:
        return redirect(url_for("account.proposals"))

    if request.method == "POST":
        account = Accounts.select_using_account_id(session.get("account_id"))

        title = request.form.get("title")
        detail = request.form.get("detail")
        abstract = request.form.get("abstract")
        speaker_name = request.form.get("speaker_name")
        short_biography = request.form.get("short_biography")
        notes_or_requests = request.form.get("notes_or_requests")
        tags = request.form.get("tags")

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

        if request.form.get("submit_proposal"):
            proposal_.submit_proposal(
                fk_account_id=session.get("account_id"),
                title=title,
                detail=detail,
                detail_markdown=detail_markdown,
                abstract=abstract,
                abstract_markdown=abstract_markdown,
                speaker_name=speaker_name,
                short_biography=short_biography,
                short_biography_markdown=short_biography_markdown,
                notes_or_requests=notes_or_requests,
                notes_or_requests_markdown=notes_or_requests_markdown,
                tags=tags.replace(" ", ""),
            )

            tasks.send_email(
                email_settings,
                [account.email_address],
                "Proposal Submission Confirmation",
                render_template(
                    "global/email/proposal-submitted.html",
                    title=title,
                    flaskcon_email=FLASKCON_EMAIL_ADDRESS,
                ),
            )

            flash("Your proposal has been submitted! We will be in touch soon.")
            return redirect(url_for("account.view_proposal", proposal_id=proposal_id))

        else:
            proposal_.save_proposal(
                title=title,
                detail=detail,
                detail_markdown=detail_markdown,
                abstract=abstract,
                abstract_markdown=abstract_markdown,
                speaker_name=speaker_name,
                short_biography=short_biography,
                short_biography_markdown=short_biography_markdown,
                notes_or_requests=notes_or_requests,
                notes_or_requests_markdown=notes_or_requests_markdown,
                tags=tags.replace(" ", ""),
            )

            flash("Your proposal has been saved as a draft.")
            return redirect(url_for("account.proposals"))

    conference_ = Conferences.select_latest()

    able_to_propose = False
    now = DatetimeDeltaMC()

    if conference_:
        if isinstance(conference_.call_for_proposals_end_date, date):
            able_to_propose = (
                True
                if (conference_.call_for_proposals_end_date - now.date).days > -1
                else False
            )

        if isinstance(conference_.call_for_proposals_end_date, datetime):
            able_to_propose = (
                True
                if (conference_.call_for_proposals_end_date.date() - now.date).days > -1
                else False
            )

    return render_template(
        bp.tmpl("edit-proposal.html"),
        proposal=proposal_,
        able_to_propose=able_to_propose,
        conference=conference_,
    )
