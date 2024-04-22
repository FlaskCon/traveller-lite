from . import *


class DisplayPictures(db.Model, MetaMixins):
    display_picture_id = db.Column(db.Integer, primary_key=True)
    unique_display_picture_id = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String, nullable=False)
    attribution = db.Column(db.String, nullable=False)
    attribution_url = db.Column(db.String, nullable=False)
    note = db.Column(db.String, nullable=True)
    limited = db.Column(db.Boolean, nullable=False, default=False)

    @classmethod
    def select_all(cls):
        return (
            db.session.execute(select(cls).order_by(cls.display_picture_id))
            .scalars()
            .all()
        )

    @classmethod
    def select_all_display_picture_id(cls):
        return (
            db.session.execute(
                select(cls.display_picture_id)
                .where(cls.unique_display_picture_id != 9999)
                .order_by(cls.display_picture_id)
            )
            .scalars()
            .all()
        )

    @classmethod
    def select_all_account_signup(cls):
        return (
            db.session.execute(
                select(cls.display_picture_id)
                .where(cls.unique_display_picture_id != 9999, cls.limited.is_(False))
                .order_by(cls.display_picture_id)
            )
            .scalars()
            .all()
        )

    @classmethod
    def select_using_display_picture_id(cls, display_picture_id):
        return db.session.execute(
            select(cls).filter_by(display_picture_id=display_picture_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_using_unique_display_picture_id(cls, unique_display_picture_id):
        return db.session.execute(
            select(cls)
            .filter_by(unique_display_picture_id=unique_display_picture_id)
            .limit(1)
        ).scalar_one_or_none()

    @classmethod
    def seed(cls, resource: list[dict]):
        for item in resource:
            db.session.execute(
                insert(cls).values(
                    unique_display_picture_id=item["unique_display_picture_id"],
                    filename=item["filename"],
                    attribution=item["attribution"],
                    attribution_url=item["attribution_url"],
                    note=item["note"],
                    limited=item["limited"],
                )
            )
        db.session.commit()

    @classmethod
    def create(
        cls,
        unique_display_picture_id,
        filename,
        attribution,
        attribution_url,
        limited,
        note,
    ):
        db.session.execute(
            insert(cls).values(
                unique_display_picture_id=unique_display_picture_id,
                filename=filename,
                attribution=attribution,
                attribution_url=attribution_url,
                limited=limited,
                note=note,
            )
        )
        db.session.commit()
