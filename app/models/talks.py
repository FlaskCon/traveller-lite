from . import *


class Talks(db.Model, MetaMixins):
    talk_id = db.Column(db.Integer, primary_key=True)
    fk_talk_status_id = db.Column(db.Integer, db.ForeignKey("talk_statuses.talk_status_id"))

    year = db.Column(db.Integer, nullable=False)  # This is taken on the date of submission
    title = db.Column(db.String, nullable=False)

    # A short description of your talk.
    # If your talk is accepted, the abstract will be published on the conference website.
    # DO NOT place any identifying information in this field.
    abstract = db.Column(db.String, nullable=False)

    # An in-depth explanation of your talk, read only by reviewers.
    # What you'll be talking about.
    # What they'll learn from your talk.
    # What background experience they should have to get the most out of your talk.
    # DO NOT place any identifying information in this field.
    detail = db.Column(db.String, nullable=False)

    # A short biography of yourself.
    # This will not be published on the conference website.
    short_biography = db.Column(db.String, nullable=False)

    # Any additional notes or needs you have from us.
    notes_or_needs = db.Column(db.String, nullable=False)

    # Tags are used to help reviewers find proposals that interest them.
    tags = db.Column(db.String, nullable=False)

    # Fields used by the committee
    committee_comments = db.Column(db.String, nullable=True)
    reason_for_rejection = db.Column(db.String, nullable=True)
    scheduled_date = db.Column(db.DateTime, nullable=True)
    scheduled_confirmed = db.Column(db.Boolean, nullable=False, default=False)
