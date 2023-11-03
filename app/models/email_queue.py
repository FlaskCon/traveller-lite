from datetime import datetime

from . import *


class EmailQueue(db.Model, MetaMixins):
    __bind_key__ = "email_queue"
    email_id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(256), nullable=True)
    to = db.Column(db.String, nullable=True)
    subject = db.Column(db.String, nullable=True)
    message = db.Column(db.String, nullable=True)
    sent = db.Column(db.Boolean, nullable=True, default=False)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @classmethod
    def update_uid(cls, email_id: int, uid: str) -> None:
        db.session.execute(update(cls).where(cls.email_id == email_id).values(uid=uid))
        db.session.commit()

    @classmethod
    def add_emails_to_send(cls, list_of_emails: list):
        result = db.session.scalars(insert(cls).returning(cls), list_of_emails).all()
        db.session.commit()
        return result
