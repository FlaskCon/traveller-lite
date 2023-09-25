from . import *


class TalkNotes(db.Model, MetaMixins):
    talk_note_id = db.Column(db.Integer, primary_key=True)
    fk_talk_id = db.Column(db.Integer, db.ForeignKey("talks.talk_id"))
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    committee_note = db.Column(db.Boolean, nullable=False, default=True)
    note = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
