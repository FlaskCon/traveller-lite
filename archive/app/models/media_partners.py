from . import *


class MediaPartners(db.Model, MetaMixins):
    media_partner_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)

    @classmethod
    def select_all(cls):
        return db.session.execute(select(cls).order_by(cls.year.desc())).scalars().all()

    @classmethod
    def select_by_media_partner_id(cls, media_partner_id: int):
        return db.session.execute(
            select(cls).where(cls.media_partner_id == media_partner_id)
        ).scalar_one_or_none()

    @classmethod
    def select_by_year(cls, year: int):
        return db.session.execute(select(cls).where(cls.year == year)).scalars().all()

    @classmethod
    def create(
        cls,
        year: int,
        name: str,
        description: str,
        url: str,
        logo: str,
    ):
        db.session.execute(
            insert(cls).values(
                year=year,
                name=name,
                description=description,
                url=url,
                logo=logo,
            )
        )

        db.session.commit()

    @classmethod
    def update_by_media_partner_id(
        cls,
        media_partner_id: int,
        year: int,
        name: str,
        description: str,
        url: str,
        logo: str,
    ):
        db.session.execute(
            update(cls)
            .where(cls.media_partner_id == media_partner_id)
            .values(
                year=year,
                name=name,
                description=description,
                url=url,
                logo=logo,
            )
        )

        db.session.commit()

    @classmethod
    def delete_by_media_partner_id(cls, media_partner_id: int):
        db.session.execute(delete(cls).where(cls.media_partner_id == media_partner_id))

        db.session.commit()
