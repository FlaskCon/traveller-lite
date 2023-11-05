import os

import click
import faker
from flask import current_app as app

from app.extensions import db


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")


@app.cli.command("email-test")
def email_test_command():
    from app.models.email_queue import EmailQueue

    emails: list[dict[str, str]] = []

    for r in range(10):
        fake = faker.Faker()
        emails.append({
            "email_to": fake.email(),
            "email_subject": fake.sentence(),
            "email_message": fake.text(),
        })

    EmailQueue.add_emails_to_send(emails)
    print(EmailQueue.process_queue())


@app.cli.command("email-live-test")
def email_live_test_command():
    from app.models.email_queue import EmailQueue

    emails: list[dict[str, str]] = []

    fake = faker.Faker()

    emails.append({
        "email_to": os.getenv("LIVE_TEST_EMAIL_ONE", os.getenv("FLASKCON_EMAIL_ADDRESS")),
        "email_subject": fake.sentence(),
        "email_message": fake.text(),
    })

    emails.append({
        "email_to": os.getenv("LIVE_TEST_EMAIL_TWO", os.getenv("FLASKCON_EMAIL_ADDRESS")),
        "email_subject": fake.sentence(),
        "email_message": fake.text(),
    })

    EmailQueue.add_emails_to_send(emails)
    print(EmailQueue.process_queue())


@app.cli.command("email-reprocess")
def email_test_command():
    from app.models.email_queue import EmailQueue

    print(EmailQueue.reprocess_queue())


@app.cli.command("email-kill")
@click.argument("pid")
def email_test_command(pid: str):
    from app.extensions.emailer_client import kill_process

    print(kill_process(pid))
