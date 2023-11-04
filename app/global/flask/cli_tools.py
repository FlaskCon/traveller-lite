import faker
from flask import current_app as app

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

    for r in range(10):
        emails.append(
            {
                "email_to": faker.Faker().email(),
                "email_subject": faker.Faker().sentence(),
                "email_message": faker.Faker().paragraph(),
            }
        )

    EmailQueue.add_emails_to_send(emails)

    result = start_emailer(app.config["SQLALCHEMY_DATABASE_URI"], processor="PROCESS")

    print(result)


@app.cli.command("emailr")
def cli_add_emails_and_reprocess():
    result = start_emailer(app.config["SQLALCHEMY_DATABASE_URI"], processor="REPROCESS")

    print(result)
