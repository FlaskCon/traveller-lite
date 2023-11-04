from flask import current_app as app
import faker

from app.extensions import db
from app.extensions.emailer_client import start_emailer
from app.models.email_queue import EmailQueue


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")


@app.cli.command("email")
def cli_add_emails_and_send():
    emails = []

    for r in range(100):
        emails.append(
            {
                "to": faker.Faker().email(),
                "subject": faker.Faker().sentence(),
                "message": faker.Faker().paragraph(),
            }
        )

    EmailQueue.add_emails_to_send(emails)
    start_emailer(app.config["SQLALCHEMY_DATABASE_URI"])
