from . import *


class SecureEndpointsMembership(db.Model):
    secure_endpoint_membership_id = db.Column(db.Integer, primary_key=True)
    fk_secure_endpoint_id = db.Column(db.Integer, db.ForeignKey("secure_endpoints.secure_endpoint_id"), nullable=False)
    fk_role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)
