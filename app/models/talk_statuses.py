from . import *


class TalkStatuses(db.Model, MetaMixins):
    talk_status_id = db.Column(db.Integer, primary_key=True)
    unique_talk_status_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.talk_status_id)
        ).scalars().all()

    @classmethod
    def select_all_talk_status_id(cls):
        return db.session.execute(
            select(cls.talk_status_id).order_by(cls.talk_status_id)
        ).scalars().all()

    @classmethod
    def select_using_talk_status_id(cls, talk_status_id):
        return db.session.execute(
            select(cls).filter_by(talk_status_id=talk_status_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_using_unique_talk_status_id(cls, unique_talk_status_id):
        return db.session.execute(
            select(cls).filter_by(unique_talk_status_id=unique_talk_status_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def seed(cls, resource: list[dict]):
        for item in resource:
            db.session.execute(
                insert(cls).values(
                    unique_talk_status_id=item["unique_talk_status_id"],
                    name=item["name"],
                    description=item["description"],
                )
            )
        db.session.commit()
