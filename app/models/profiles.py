from . import *
from .update_feed import UpdateFeed


class Profiles(db.Model, MetaMixins):
    profile_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"), nullable=False)
    fk_display_picture_id = db.Column(db.Integer, db.ForeignKey("display_pictures.display_picture_id"), nullable=True)
    earned_display_pictures = db.Column(db.JSON, nullable=True)
    # {"earned": [unique_display_picture_id, ...]}

    company_name = db.Column(db.String(250), nullable=True)
    name_or_alias = db.Column(db.String(250), nullable=True)
    pronouns = db.Column(db.String, nullable=True)
    bio = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)

    rel_account = relationship(
        "Accounts",
        order_by="Accounts.email_address",
        primaryjoin="Profiles.fk_account_id==Accounts.account_id",
        viewonly=True,
    )

    rel_display_picture = relationship(
        "DisplayPictures",
        primaryjoin="Profiles.fk_display_picture_id==DisplayPictures.display_picture_id",
        viewonly=True,
    )

    @classmethod
    def select_using_account_id(cls, account_id):
        return db.session.execute(
            select(cls).filter_by(fk_account_id=account_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_using_profile_id(cls, profile_id):
        return db.session.execute(
            select(cls).filter_by(profile_id=profile_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def signup(cls, account_id, display_picture_id, name_or_alias):
        db.session.execute(
            insert(cls).values(
                fk_account_id=account_id,
                fk_display_picture_id=display_picture_id,
                name_or_alias=name_or_alias,
            )
        )
        db.session.commit()

    @classmethod
    def add_earned_display_picture(cls, account_id: int, unique_display_picture_id):
        profile = cls.select_using_account_id(account_id)

        if profile.earned_display_pictures:
            earned = profile.earned_display_pictures.get("earned", [])
        else:
            earned = []

        if earned:
            if unique_display_picture_id not in earned:
                earned.append(unique_display_picture_id)
            else:
                return
        else:
            earned.append(unique_display_picture_id)

        db.session.execute(
            update(cls).where(cls.fk_account_id == account_id).values(
                earned_display_pictures={"earned": earned}
            )
        )

        UpdateFeed.create(
            fk_account_id=account_id,
            title="You have earned a new display picture!",
            message="Check it out in your profile.",
            image="star.gif",
        )

        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

    @classmethod
    def delete_using_account_id(cls, account_id: int):
        from app.models.display_pictures import DisplayPictures

        deleted_display_picture = DisplayPictures.select_using_unique_display_picture_id(9999)

        db.session.execute(
            update(cls).where(cls.fk_account_id == account_id).values(
                fk_display_picture_id=deleted_display_picture.display_picture_id,
                company_name=None,
                name_or_alias="ACCOUNT DELETED",
                pronouns=None,
                bio=None,
                country=None,
                website=None,
            )
        )
        db.session.commit()
