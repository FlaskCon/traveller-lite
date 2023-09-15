from . import *


class Proposals(db.Model, MetaMixins):
    proposal_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)  # This is taken on the date of submission
    title = db.Column(db.String, nullable=False)

