from flask import render_template

from app.extensions import email_settings
from app.models.accounts import Accounts
from app.models.proposals import Proposals
from app.utilities import EmailService
from . import decorator_group


@decorator_group("/api/send-submit-reminder", methods=["GET"])
def api_send_submit_reminder():
    total_in_prep = Proposals.select_proposals_in_status_prep_no_reminder()

    already_sent_account_ids = []

    email_service = EmailService(email_settings)

    for proposal in total_in_prep:
        if proposal.fk_account_id not in already_sent_account_ids:

            account = Accounts.select_using_account_id(proposal.fk_account_id)

            if account:

                already_sent_account_ids.append(proposal.fk_account_id)

                if account.email_address != "ACCOUNT DELETED":
                    email_service.recipients(
                        [f"{account.email_address}"]
                    ).subject(
                        "Reminder: Submit your proposal(s)!"
                    ).body(
                        render_template("global/email/submit-reminder.html")
                    ).send()

        proposal.submit_reminder_sent = True

    Proposals.save()

    total_in_pnsr_recount = Proposals.count_total_proposals_in_status_prep_not_sent_a_reminder_to_submit()

    return {
        "status": "success",
        "total_in_pnsr_recount": total_in_pnsr_recount
    }
