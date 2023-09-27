from datetime import datetime

from . import *


class Accounts(db.Model, MetaMixins):
    account_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    salt = db.Column(db.String(4), nullable=False)
    disabled = db.Column(db.Boolean)
    confirmed = db.Column(db.Boolean, default=False)
    private_key = db.Column(db.String(256), nullable=True)

    # Tracking
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)

    rel_roles = relationship(
        "RolesMembership",
        primaryjoin="Accounts.account_id==RolesMembership.fk_account_id",
        viewonly=True,
    )

    rel_profile = relationship(
        "Profiles",
        primaryjoin="Accounts.account_id==Profiles.fk_account_id",
        viewonly=True,
    )

    rel_talks = relationship(
        "Talks",
        primaryjoin="Accounts.account_id==Talks.fk_account_id",
        viewonly=True,
    )

    @classmethod
    def exists(cls, email_address) -> bool:
        return True if db.session.execute(
            select(cls.account_id).filter_by(email_address=email_address).limit(1)
        ).scalar_one_or_none() else False

    @classmethod
    def get_roles_from_email_address_select(cls, email_address):
        result = db.session.execute(
            select(cls).filter_by(email_address=email_address).limit(1)
        ).scalar_one_or_none()
        return [role.rel_role.name for role in result.rel_roles]

    @classmethod
    def select_email_address_using_account_id(cls, account_id):
        return db.session.execute(
            select(cls.email_address).filter_by(account_id=account_id).limit(1)
        ).scalar_one_or_none()

    def get_roles_from_this(self):
        return [role.rel_role.name for role in self.rel_roles]

    @classmethod
    def select_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.email_address)
        ).scalars().all()

    @classmethod
    def select_using_account_id(cls, account_id):
        return db.session.execute(
            select(cls).filter_by(account_id=account_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_using_email_address(cls, email_address):
        return db.session.execute(
            select(cls).filter_by(email_address=email_address).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_account_id_using_email_address(cls, email_address):
        return db.session.execute(
            select(cls.account_id).filter_by(email_address=email_address).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def confirm_account_successful(cls, account_id: int, private_key: str):
        account = cls.select_using_account_id(account_id)
        if account.private_key == private_key:
            db.session.execute(
                update(cls).where(
                    cls.account_id == account_id
                ).values(
                    confirmed=True,
                    private_key=None,
                )
            )
            db.session.commit()
            return True
        return False

    def confirm_account(self):
        self.confirmed = True
        db.session.commit()

    def new_private_key(self):
        from flask_imp.auth import Auth

        self.private_key = Auth.generate_private_key(Auth.generate_password(length=1))
        db.session.commit()
        return self.private_key

    def remove_private_key(self):
        self.private_key = None
        db.session.commit()

    def create_profile(self):
        from app.models.profiles import Profiles
        from app.models.display_pictures import DisplayPictures
        import random

        Profiles.signup(self.account_id, random.choice(DisplayPictures.select_all_display_picture_id()))

    @classmethod
    def login(cls, email_address, password):
        from flask_imp.auth import Auth

        account = cls.select_using_email_address(email_address)
        if account:
            if Auth.auth_password(password, account.password, account.salt):
                return account
        return None

    @classmethod
    def signup(cls, email_address: str, password: str, name_or_alias: str):
        """
        Written for sqlite. Returns account after commit.
        """
        from flask_imp.auth import Auth
        from app.models.profiles import Profiles
        from app.models.display_pictures import DisplayPictures
        import random

        salt = Auth.generate_salt()
        salt_and_pepper_password = Auth.hash_password(password, salt)
        private_key = Auth.generate_private_key(Auth.generate_password(length=1))

        account = db.session.execute(
            insert(cls).values(
                email_address=email_address,
                password=salt_and_pepper_password,
                salt=salt,
                disabled=False,
                confirmed=False,
                private_key=private_key,
            )
        )
        db.session.flush()
        db.session.execute(
            insert(Profiles).values(
                fk_account_id=account.lastrowid,
                fk_display_picture_id=random.choice(DisplayPictures.select_all_display_picture_id()),
                name_or_alias=name_or_alias,
                earned_display_pictures={"earned": []}
            )
        )
        db.session.commit()

        return cls.select_using_account_id(account.lastrowid)

    @classmethod
    def update(
            cls,
            account_id: int,
            email_address: str,
            disabled: bool,
            confirmed: bool,
            private_key: str,
    ):
        db.session.execute(
            update(cls).where(
                cls.account_id == account_id
            ).values(
                email_address=email_address,
                disabled=disabled,
                confirmed=confirmed,
                private_key=private_key,
            )
        )
        db.session.commit()

    def reset_password(
            self,
            new_password: str,
    ):
        from flask_imp.auth import Auth

        salt = Auth.generate_salt()
        salt_and_pepper_password = Auth.hash_password(new_password, salt)

        self.salt = salt
        self.password = salt_and_pepper_password
        self.private_key = None

        db.session.commit()

    @classmethod
    def delete(cls, account_id: int):
        db.session.execute(
            delete(cls).where(
                cls.account_id == account_id
            )
        )
        db.session.commit()

    # batch actions:

    @classmethod
    def create_batch(cls, batch: list[dict]):
        """
        batch: [{"email_address": -, "password": -, "disabled": -}]
        :param batch:
        :return:
        """

        from flask_imp.auth import Auth

        for value in batch:
            salt = Auth.generate_salt()
            salt_and_pepper_password = Auth.hash_password(value.get("password", "password"), salt)

            db.session.execute(
                insert(cls).values(
                    email_address=value.get("email_address", "null@null.null"),
                    password=salt_and_pepper_password,
                    salt=salt,
                    disabled=value.get("disabled", False),
                    confirmed=value.get("confirmed", False),
                    private_key=value.get("private_key", None),
                )
            )

        db.session.commit()

    @classmethod
    def get_account_ids_from_email_address_select_batch(cls, email_addresses: list[str]) -> list[int]:
        return db.session.execute(
            select(cls.account_id).where(cls.email_address.in_(email_addresses))
        ).scalars().all()

    @classmethod
    def generate_page_account_data(cls, account_id: int):

        account = cls.select_using_account_id(account_id)

        return {
            "account_id": account.account_id,
            "email_address": account.email_address,
            "profile": account.rel_profile[0] if account.rel_profile else None,
        }
