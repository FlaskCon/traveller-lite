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
