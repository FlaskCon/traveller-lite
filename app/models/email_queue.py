from datetime import datetime

from app.extensions.emailer_client import start_emailer
from . import *


class EmailQueue(db.Model, MetaMixins):
    email_id = db.Column(db.Integer, primary_key=True)
    email_to = db.Column(db.String, nullable=True)
    email_subject = db.Column(db.String, nullable=True)
    email_message = db.Column(db.String, nullable=True)
    staged = db.Column(db.Boolean, nullable=False, default=False)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @classmethod
    def add_emails_to_send(cls, email_group: list[dict[str, str]]):
        """
        :param email_group: A list of tuples containing the email address, subject, and message.
        """
        result = db.session.execute(insert(cls).values(email_group))
        db.session.commit()
        return result

    @staticmethod
    def process_queue() -> str:
        """
        Process the email queue, sending emails that have not yet been sent.
        """
        return start_emailer(db.engine.url, processor="PROCESS")

    @staticmethod
    def reprocess_queue() -> str:
        """
        Reprocess the email queue, sending all emails.
        """
        return start_emailer(db.engine.url, processor="REPROCESS")
