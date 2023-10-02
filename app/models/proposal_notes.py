from . import *


class ProposalNotes(db.Model, MetaMixins):
    proposal_note_id = db.Column(db.Integer, primary_key=True)
    fk_proposal_id = db.Column(db.Integer, db.ForeignKey("proposals.proposal_id"))
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    committee_note = db.Column(db.Boolean, nullable=False, default=True)
    note = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
