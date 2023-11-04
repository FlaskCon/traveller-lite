from datetime import datetime

from . import *


class EmailQueue(db.Model, MetaMixins):
    email_id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String, nullable=True)
    subject = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @classmethod
    def add_emails_to_send(cls, list_of_emails: list):
        result = db.session.scalars(insert(cls).returning(cls), list_of_emails).all()
        db.session.commit()
        return result
