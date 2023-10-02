from . import *


class ProposalStatuses(db.Model, MetaMixins):
    proposal_status_id = db.Column(db.Integer, primary_key=True)
    unique_proposal_status_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.proposal_status_id)
        ).scalars().all()

    @classmethod
    def select_all_proposal_status_id(cls):
        return db.session.execute(
            select(cls.proposal_status_id).order_by(cls.proposal_status_id)
        ).scalars().all()

    @classmethod
    def select_using_proposal_status_id(cls, proposal_status_id):
        return db.session.execute(
            select(cls).filter_by(proposal_status_id=proposal_status_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_using_unique_proposal_status_id(cls, unique_proposal_status_id):
        return db.session.execute(
            select(cls).filter_by(unique_proposal_status_id=unique_proposal_status_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_proposal_status_id_using_unique_proposal_status_id_batch(cls, unique_proposal_status_ids: list[int]):
        return db.session.execute(
            select(cls.proposal_status_id).where(cls.unique_proposal_status_id.in_(unique_proposal_status_ids))
        ).scalars().all()

    @classmethod
    def seed(cls, resource: list[dict]):
        for item in resource:
            db.session.execute(
                insert(cls).values(
                    unique_proposal_status_id=item["unique_proposal_status_id"],
                    name=item["name"],
                    description=item["description"],
                )
            )
        db.session.commit()
