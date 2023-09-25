from datetime import datetime

from . import *


class Talks(db.Model, MetaMixins):
    talk_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    fk_talk_status_id = db.Column(db.Integer, db.ForeignKey("talk_statuses.talk_status_id"))

    year = db.Column(db.Integer, nullable=False)  # This is taken on the date of submission
    title = db.Column(db.String, nullable=False)

    # An in-depth explanation of your talk, read only by reviewers.
    # What you'll be talking about.
    # What they'll learn from your talk.
    # What background experience they should have to get the most out of your talk.
    # DO NOT place any identifying information in this field.
    detail = db.Column(db.String, nullable=True)
    detail_markdown = db.Column(db.String, nullable=True)

    # A short description of your talk.
    # If your talk is accepted, the abstract will be published on the conference website.
    # DO NOT place any identifying information in this field.
    abstract = db.Column(db.String, nullable=True)
    abstract_markdown = db.Column(db.String, nullable=True)

    # A short biography of yourself.
    # This will not be published on the conference website.
    short_biography = db.Column(db.String, nullable=True)
    short_biography_markdown = db.Column(db.String, nullable=True)

    # Any additional notes or needs you have from us.
    notes_or_requests = db.Column(db.String, nullable=True)
    notes_or_requests_markdown = db.Column(db.String, nullable=True)

    # Tags are used to help reviewers find proposals that interest them.
    tags = db.Column(db.String, nullable=True)

    # Fields used by the committee
    committee_comments = db.Column(db.String, nullable=True)
    reason_for_rejection = db.Column(db.String, nullable=True)
    scheduled_date = db.Column(db.DateTime, nullable=True)
    scheduled_confirmed = db.Column(db.Boolean, nullable=False, default=False)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    # Relationships
    rel_talk_status = relationship(
        "TalkStatuses",
        primaryjoin="Talks.fk_talk_status_id == TalkStatuses.talk_status_id",
        viewonly=True,
        uselist=False,
    )

    @property
    def talk_status(self):
        return self.rel_talk_status.name

    @classmethod
    def select_using_account_id(cls, account_id: int):
        return db.session.execute(
            select(cls).where(cls.fk_account_id == account_id).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def select_using_talk_id(cls, talk_id: int):
        return db.session.execute(
            select(cls).where(cls.talk_id == talk_id).order_by(cls.created.asc())
        ).scalar_one_or_none()

    @classmethod
    def save_new_talk(
            cls,
            fk_account_id,
            title,
            detail,
            detail_markdown,
            abstract,
            abstract_markdown,
            short_biography,
            short_biography_markdown,
            notes_or_requests,
            notes_or_requests_markdown,
            tags,
    ):
        from .talk_statuses import TalkStatuses

        result = db.session.execute(
            insert(cls).values(
                fk_account_id=fk_account_id,
                fk_talk_status_id=TalkStatuses.select_using_unique_talk_status_id(101).talk_status_id,
                year=datetime.now().year,
                title=title,
                detail=detail,
                detail_markdown=detail_markdown,
                abstract=abstract,
                abstract_markdown=abstract_markdown,
                short_biography=short_biography,
                short_biography_markdown=short_biography_markdown,
                notes_or_requests=notes_or_requests,
                notes_or_requests_markdown=notes_or_requests_markdown,
                tags=tags,
            )
        )
        db.session.commit()
        return result.lastrowid

    def save_talk(
            self,
            title,
            detail,
            detail_markdown,
            abstract,
            abstract_markdown,
            short_biography,
            short_biography_markdown,
            notes_or_requests,
            notes_or_requests_markdown,
            tags,
            submit_proposal,
    ):
        from .talk_statuses import TalkStatuses

        self.title = title
        self.detail = detail
        self.detail_markdown = detail_markdown
        self.abstract = abstract
        self.abstract_markdown = abstract_markdown
        self.short_biography = short_biography
        self.short_biography_markdown = short_biography_markdown
        self.notes_or_requests = notes_or_requests
        self.notes_or_requests_markdown = notes_or_requests_markdown
        if tags:
            self.tags = tags

        if submit_proposal != "false":
            self.fk_talk_status_id = TalkStatuses.select_using_unique_talk_status_id(102).talk_status_id

        db.session.commit()
