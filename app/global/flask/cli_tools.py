from flask import current_app as app

from app.extensions import db
from app.extensions.emailer_client import send_enqueued_email
from app.models.email_queue import EmailQueue


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")


@app.cli.command("emails-add-send")
def cli_add_emails_and_send():
    results = EmailQueue.add_emails_to_send(
        [
            {
                "to": "bob@bob.com",
                "subject": "Test",
                "message": "Test",
            },
            {
                "to": "jane@jane.com",
                "subject": "Test",
                "message": "Test",
            },
        ]
    )

    for result in results:
        send_enqueued_email(result.email_id, result.to)
