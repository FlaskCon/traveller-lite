from . import *


class DisplayPictures(db.Model, MetaMixins):
    display_picture_id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.Integer, nullable=False)
    attribution = db.Column(db.String, nullable=False)
    attribution_url = db.Column(db.String, nullable=False)
