from collections import OrderedDict
from datetime import datetime

from sqlalchemy import func

from . import *


class Proposals(db.Model, MetaMixins):
    proposal_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    fk_proposal_status_id = db.Column(db.Integer, db.ForeignKey("proposal_statuses.proposal_status_id"))

    year = db.Column(db.Integer, nullable=False)  # This is taken on the date of submission
    title = db.Column(db.String, nullable=False)

    # An in-depth explanation of your proposal, read only by reviewers.
    # What you'll be talking about.
    # What they'll learn from your proposal.
    # What background experience they should have to get the most out of your proposal.
    # DO NOT place any identifying information in this field.
    detail = db.Column(db.String, nullable=True)
    detail_markdown = db.Column(db.String, nullable=True)

    # A short description of your proposal.
    # If your proposal is accepted, the abstract will be published on the conference website.
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
    submit_reminder_sent = db.Column(db.Boolean, nullable=False, default=False)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    # Relationships
    rel_proposal_status = relationship(
        "ProposalStatuses",
        primaryjoin="Proposals.fk_proposal_status_id == ProposalStatuses.proposal_status_id",
        viewonly=True,
        uselist=False,
    )

    rel_proposal_votes = relationship(
        "ProposalVotes",
        primaryjoin="Proposals.proposal_id == ProposalVotes.fk_proposal_id",
        viewonly=True,
        uselist=True,
    )

    rel_account = relationship(
        "Accounts",
        primaryjoin="Proposals.fk_account_id == Accounts.account_id",
        viewonly=True,
        uselist=False,
    )

    @staticmethod
    def save():
        db.session.commit()

    @property
    def proposal_status(self):
        return self.rel_proposal_status.name

    @property
    def votes(self) -> dict:
        votes_default = {"for": 0, "against": 0}
        votes_calc = {
            (vote.vote and "for" or "against"): votes_default["for" if vote.vote else "against"] + 1 for
            vote in self.rel_proposal_votes or []
        }

        if not votes_calc.get("for"):
            votes_calc["for"] = 0
        if not votes_calc.get("against"):
            votes_calc["against"] = 0

        return votes_calc

    def get_voting_position_using_account_id(self, account_id: int) -> t.Optional[bool]:
        for vote in self.rel_proposal_votes or []:
            if vote.fk_account_id == account_id:
                return vote.vote
        return None

    def set_submit_reminder_sent(self):
        self.submit_reminder_sent = True
        db.session.commit()

    @classmethod
    def select_proposals_in_status_prep(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch([101])
        return db.session.execute(
            select(
                cls
            ).where(
                cls.fk_proposal_status_id.in_(proposal_ids)
            )
        ).scalars().all()

    @classmethod
    def select_proposals_in_status_prep_no_reminder(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch([101])
        return db.session.execute(
            select(
                cls
            ).where(
                cls.fk_proposal_status_id.in_(proposal_ids),
                cls.submit_reminder_sent == False
            )
        ).scalars().all()

    @classmethod
    def count_total_proposals_in_status_prep_not_sent_a_reminder_to_submit(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch([101])
        return db.session.execute(
            select(
                func.count(cls.proposal_id)
            ).where(
                cls.fk_proposal_status_id.in_(proposal_ids),
                cls.submit_reminder_sent == False
            )
        ).scalar_one_or_none()

    @classmethod
    def count_total_proposals_in_status_prep(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch([101])
        return db.session.execute(
            select(
                func.count(cls.proposal_id)
            ).where(
                cls.fk_proposal_status_id.in_(proposal_ids)
            )
        ).scalar_one_or_none()

    @classmethod
    def count_total_proposals_at_reviewer_seen_statuses(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch(
            [102, 103, 104, 105])
        return db.session.execute(
            select(
                func.count(cls.proposal_id)
            ).where(
                cls.fk_proposal_status_id.in_(proposal_ids)
            )
        ).scalar_one_or_none()

    @classmethod
    def select_using_account_id(cls, account_id: int):
        return db.session.execute(
            select(cls).where(cls.fk_account_id == account_id).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def select_using_proposal_id(cls, proposal_id: int):
        return db.session.execute(
            select(cls).where(cls.proposal_id == proposal_id).order_by(cls.created.asc())
        ).scalar_one_or_none()

    @classmethod
    def for_review(cls):
        from .proposal_statuses import ProposalStatuses
        proposal_ids = ProposalStatuses.select_proposal_status_id_using_unique_proposal_status_id_batch(
            [102, 103, 104, 105])
        return db.session.execute(
            select(cls).where(cls.fk_proposal_status_id.in_(proposal_ids)).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def has_been_accepted(cls):
        from .proposal_statuses import ProposalStatuses
        accepted_status_id: int = ProposalStatuses.select_using_unique_proposal_status_id(
            107).proposal_status_id

        return db.session.execute(
            select(cls).where(
                cls.fk_proposal_status_id == accepted_status_id
            ).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def has_been_rejected(cls):
        from .proposal_statuses import ProposalStatuses
        accepted_status_id: int = ProposalStatuses.select_using_unique_proposal_status_id(
            108).proposal_status_id

        return db.session.execute(
            select(cls).where(
                cls.fk_proposal_status_id == accepted_status_id
            ).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def has_been_waitlisted(cls):
        from .proposal_statuses import ProposalStatuses
        accepted_status_id: int = ProposalStatuses.select_using_unique_proposal_status_id(
            106).proposal_status_id

        return db.session.execute(
            select(cls).where(
                cls.fk_proposal_status_id == accepted_status_id
            ).order_by(cls.created.asc())
        ).scalars().all()

    @classmethod
    def leaderboard(cls):
        proposals = cls.for_review()

        leaderboard = OrderedDict()

        for proposal in proposals:
            votes_for = [vote for vote in proposal.rel_proposal_votes if vote.vote]
            votes_against = [vote for vote in proposal.rel_proposal_votes if not vote.vote]
            leaderboard[proposal.proposal_id] = {
                "row": proposal,
                "votes_for": len(votes_for),
                "votes_against": len(votes_against),
            }

        return sorted(leaderboard.items(), key=lambda x: x[1]["votes_for"], reverse=True)

    @classmethod
    def save_new_proposal(
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
        from .proposal_statuses import ProposalStatuses

        result = db.session.execute(
            insert(cls).values(
                fk_account_id=fk_account_id,
                fk_proposal_status_id=ProposalStatuses.select_using_unique_proposal_status_id(101).proposal_status_id,
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

    def save_proposal(
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
        from .proposal_statuses import ProposalStatuses

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

        if submit_proposal:
            self.fk_proposal_status_id = ProposalStatuses.select_using_unique_proposal_status_id(102).proposal_status_id

        db.session.commit()
