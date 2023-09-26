from . import *


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
    def add_earned_display_picture(cls, account_id, unique_display_picture_id):
        profile = cls.select_using_account_id(account_id)
        if profile.earned_display_pictures:
            earned = profile.earned_display_pictures.get("earned", [])
        else:
            earned = []

        if earned:
            if unique_display_picture_id not in earned:
                earned.append(unique_display_picture_id)
        else:
            earned.append(unique_display_picture_id)

        profile.earned_display_pictures = {"earned": [*earned]}

        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()
