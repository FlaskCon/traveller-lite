from datetime import datetime

from . import *


def convert_date(date: str):
    try:
        cdate = datetime.strptime(
            date,
            "%Y-%m-%d"
        ).date()
    except ValueError:
        return None
    return cdate


class Conferences(db.Model, MetaMixins):
    conference_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    index_endpoint = db.Column(db.String, nullable=False)

    latest = db.Column(db.Boolean, nullable=False, default=False)

    call_for_proposals_start_date = db.Column(db.Date, nullable=True)
    call_for_proposals_end_date = db.Column(db.Date, nullable=True)

    conference_start_date = db.Column(db.Date, nullable=True)
    conference_end_date = db.Column(db.Date, nullable=True)

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.year.desc())
        ).scalars().all()

    @classmethod
    def select_latest(cls):
        return db.session.execute(
            select(cls).where(cls.latest).order_by(cls.year.desc())
        ).scalar_one_or_none()

    @classmethod
    def create(
            cls,
            year: int,
            index_endpoint: str,
            latest: bool,
            call_for_proposals_start_date: str,
            call_for_proposals_end_date: str,
            conference_start_date: str,
            conference_end_date: str
    ):
        db.session.execute(
            insert(cls).values(
                year=year,
                index_endpoint=index_endpoint,
                latest=latest,
                call_for_proposals_start_date=convert_date(call_for_proposals_start_date),
                call_for_proposals_end_date=convert_date(call_for_proposals_end_date),
                conference_start_date=convert_date(conference_start_date),
                conference_end_date=convert_date(conference_end_date)
            )
        )

        db.session.commit()

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
        db.session.execute(
            update(cls).where(cls.conference_id == conference_id).values(
                year=year,
                index_endpoint=index_endpoint,
                latest=latest,
                call_for_proposals_start_date=convert_date(call_for_proposals_start_date),
                call_for_proposals_end_date=convert_date(call_for_proposals_end_date),
                conference_start_date=convert_date(conference_start_date),
                conference_end_date=convert_date(conference_end_date)
            )
        )

        db.session.commit()

    @classmethod
    def delete_by_conference_id(cls, conference_id: int):
        db.session.execute(
            delete(cls).where(cls.conference_id == conference_id)
        )

        db.session.commit()

    @classmethod
    def seed(
            cls,
            conference: dict,
    ):
        db.session.execute(
            insert(cls).values(
                year=conference.get("year"),
                index_endpoint=conference.get("index_endpoint"),
                latest=conference.get("latest"),
                call_for_proposals_start_date=convert_date(conference.get("call_for_proposals_start_date")),
                call_for_proposals_end_date=convert_date(conference.get("call_for_proposals_end_date")),
                conference_start_date=convert_date(conference.get("conference_start_date")),
                conference_end_date=convert_date(conference.get("conference_end_date"))
            )
        )

        db.session.commit()
