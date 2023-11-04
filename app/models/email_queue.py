from datetime import datetime

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
    def add_emails_to_send(cls, list_of_emails: list):
        result = db.session.execute(insert(cls), list_of_emails)
        db.session.commit()
        return result
