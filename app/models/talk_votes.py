from sqlalchemy import and_

from . import *


class TalkVotes(db.Model, MetaMixins):
    talk_vote_id = db.Column(db.Integer, primary_key=True)
    fk_talk_id = db.Column(db.Integer, db.ForeignKey("talks.talk_id"))
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"))
    vote = db.Column(db.Boolean, nullable=False, default=True)

    @classmethod
    def vote_for(cls, talk_id, account_id):
        vote = db.session.execute(
            select(cls).filter(
                and_(
                    cls.fk_talk_id == talk_id,
                    cls.fk_account_id == account_id,
                )
            ).limit(1)
        ).scalar_one_or_none()
        if vote:
            vote.vote = True
        else:
            db.session.execute(
                insert(cls).values(
                    fk_talk_id=talk_id,
                    fk_account_id=account_id,
                    vote=True
                )
            )

        db.session.commit()

    @classmethod
    def vote_against(cls, talk_id, account_id):
        vote = db.session.execute(
            select(cls).filter(
                and_(
                    cls.fk_talk_id == talk_id,
                    cls.fk_account_id == account_id,
                )
            ).limit(1)
        ).scalar_one_or_none()
        if vote:
            vote.vote = True
        else:
            db.session.execute(
                insert(cls).values(
                    fk_talk_id=talk_id,
                    fk_account_id=account_id,
                    vote=True
                )
            )

        db.session.commit()

    @classmethod
    def abstain(cls, talk_id, account_id):
        db.session.execute(
            delete(cls).filter(
                and_(
                    cls.fk_talk_id == talk_id,
                    cls.fk_account_id == account_id,
                )
            )
        )
        db.session.commit()
