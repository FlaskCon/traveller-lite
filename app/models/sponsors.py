from . import *


class Sponsors(db.Model, MetaMixins):
    sponsor_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    requested = db.Column(db.Boolean, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False)
    rejected = db.Column(db.Boolean, nullable=False)
