from flask import current_app as app

from app.extensions import db
from app.extensions.emailer_client import start_emailer
from app.models.email_queue import EmailQueue


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")


@app.cli.command("emails-add-send")
def cli_add_emails_and_send():
    EmailQueue.add_emails_to_send(
        [
            {
                "to": "carmichaelits@gmail.com",
                "subject": "Test3",
                "message": "Test3",
            },
        ]
    )

    print(start_emailer(app.config["SQLALCHEMY_DATABASE_URI"]))
