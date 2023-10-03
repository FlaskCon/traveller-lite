from . import *


class Sponsors(db.Model, MetaMixins):
    sponsor_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    contact_information = db.Column(db.String, nullable=False)
    possible = db.Column(db.Boolean, nullable=False, default=False)
    requested = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    rejected = db.Column(db.Boolean, nullable=False, default=False)

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.year.desc())
        ).scalars().all()

    @classmethod
    def select_by_sponsor_id(cls, sponsor_id: int):
        return db.session.execute(
            select(cls).where(cls.sponsor_id == sponsor_id)
        ).scalar_one_or_none()

    @classmethod
    def select_by_year(cls, year: int):
        return db.session.execute(
            select(cls).where(cls.year == year)
        ).scalars().all()

    @classmethod
    def create_sponsor_request(
            cls,
            year: int,
            level: str,
            name: str,
            description: str,
            url: str,
            logo: str,
            contact_information: str,
    ):
        db.session.execute(
            insert(cls).values(
                year=year,
                level=level,
                name=name,
                description=description,
                url=url,
                logo=logo,
                contact_information=contact_information,
                requested=True,
            )
        )

        db.session.commit()

    @classmethod
    def create(
            cls,
            year: int,
            level: str,
            name: str,
            description: str,
            url: str,
            logo: str,
            contact_information: str,
    ):
        db.session.execute(
            insert(cls).values(
                year=year,
                level=level,
                name=name,
                description=description,
                url=url,
                logo=logo,
                contact_information=contact_information,
                possible=True,
            )
        )

        db.session.commit()

    @classmethod
    def update_by_sponsor_id(
            cls,
            sponsor_id: int,
            year: int,
            level: str,
            name: str,
            description: str,
            url: str,
            logo: str,
            contact_information: str,
    ):
        db.session.execute(
            update(cls).where(cls.sponsor_id == sponsor_id).values(
                year=year,
                level=level,
                name=name,
                description=description,
                url=url,
                logo=logo,
                contact_information=contact_information,
            )
        )

        db.session.commit()

    @classmethod
    def confirm(cls, sponsor_id: int):
        db.session.execute(
            update(cls).where(cls.sponsor_id == sponsor_id).values(
                possible=False,
                requested=False,
                confirmed=True,
                rejected=False,
            )
        )

        db.session.commit()

    @classmethod
    def reject(cls, sponsor_id: int):
        db.session.execute(
            update(cls).where(cls.sponsor_id == sponsor_id).values(
                possible=False,
                requested=False,
                confirmed=False,
                rejected=True,
            )
        )

        db.session.commit()
