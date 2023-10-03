from datetime import datetime

from . import *


class Conferences(db.Model, MetaMixins):
    conference_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    index_endpoint = db.Column(db.String, nullable=False)

    latest = db.Column(db.Boolean, nullable=False, default=False)

    call_for_proposals_start_date = db.Column(db.Date, nullable=True)
    call_for_proposals_end_date = db.Column(db.Date, nullable=True)

    conference_start_date = db.Column(db.Date, nullable=False)
    conference_end_date = db.Column(db.Date, nullable=False)

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.year.desc())
        ).scalars().all()

    @classmethod
    def select_by_conference_id(cls, conference_id: int):
        return db.session.execute(
            select(cls).where(cls.conference_id == conference_id)
        ).scalar_one_or_none()

    @classmethod
    def update_by_conference_id(
            cls,
            conference_id: int,
            year: int,
            index_endpoint: str,
            latest: bool,
            call_for_proposals_start_date: str,
            call_for_proposals_end_date: str,
            conference_start_date: str,
            conference_end_date: str
    ):
        parse_cfpsd = datetime.strptime(
            call_for_proposals_start_date,
            "%Y-%m-%d"
        ).date()
        parse_cfped = datetime.strptime(
            call_for_proposals_end_date,
            "%Y-%m-%d"
        ).date()
        parse_csd = datetime.strptime(
            conference_start_date,
            "%Y-%m-%d"
        ).date()
        parse_ced = datetime.strptime(
            conference_end_date,
            "%Y-%m-%d"
        ).date()

        db.session.execute(
            update(cls).where(cls.conference_id == conference_id).values(
                year=year,
                index_endpoint=index_endpoint,
                latest=latest,
                call_for_proposals_start_date=parse_cfpsd,
                call_for_proposals_end_date=parse_cfped,
                conference_start_date=parse_csd,
                conference_end_date=parse_ced
            )
        )

        db.session.commit()

    @classmethod
    def delete_by_conference_id(cls, conference_id: int):
        db.session.execute(
            delete(cls).where(cls.conference_id == conference_id)
        )

        db.session.commit()
