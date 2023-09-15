from . import *


class Conferences(db.Model, MetaMixins):
    conference_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)

    latest = db.Column(db.Boolean, nullable=False, default=False)

    call_for_proposals_start_date = db.Column(db.Date, nullable=True)
    call_for_proposals_end_date = db.Column(db.Date, nullable=True)

    conference_start_date = db.Column(db.Date, nullable=False)
    conference_end_date = db.Column(db.Date, nullable=False)
