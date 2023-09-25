from . import *


class SecureEndpoints(db.Model):
    secure_endpoint_id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String, nullable=False)
