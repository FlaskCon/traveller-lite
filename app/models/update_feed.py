from datetime import datetime

from . import *


class UpdateFeed(db.Model, MetaMixins):
    update_feed_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    title = db.Column(db.String(128), nullable=False)
    message = db.Column(db.String(512), nullable=False)
    image = db.Column(db.String(128), nullable=True)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    @classmethod
    def create(cls, fk_account_id, title, message, image):
        db.session.execute(
            insert(cls).values(
                fk_account_id=fk_account_id,
                title=title,
                message=message,
                image=image,
            )
        )
        db.session.commit()

    @classmethod
    def delete_using_account_id(cls, account_id: int):
        db.session.execute(delete(cls).where(cls.fk_account_id == account_id))
        db.session.commit()
