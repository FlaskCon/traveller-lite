from . import *


class Profile(db.Model, MetaMixins):
    profile_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"), nullable=False)

    first_name = db.Column(db.String(250), nullable=True)
    last_name = db.Column(db.String(250), nullable=True)
    pronouns = db.Column(db.String, nullable=True)
    bio = db.Column(db.String, nullable=True)
    avatar = db.Column(db.String, nullable=True)
    location = db.Column(db.String, nullable=True)
    website = db.Column(db.String, nullable=True)

    rel_account = relationship(
        "Accounts",
        order_by="Accounts.email_address",
        primaryjoin="Profile.fk_account_id==Accounts.account_id",
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
    def create(cls, account_id, user_handle):
        if cls.select_using_user_handle(user_handle):
            raise Exception(f"User handle '{user_handle}' already exists.")

        db.session.execute(
            insert(cls).values(
                fk_account_id=account_id,
                user_handle=user_handle
            )
        )
        db.session.commit()
