import random
from datetime import datetime

from flask_imp.auth import authenticate_password
from flask_imp.auth import encrypt_password
from flask_imp.auth import generate_password
from flask_imp.auth import generate_private_key
from flask_imp.auth import generate_salt
from flask_imp.auth import generate_email_validator
from sqlalchemy import func

from . import *
from .roles import Roles
from .update_feed import UpdateFeed


class Accounts(db.Model, MetaMixins):
    account_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    salt = db.Column(db.String(4), nullable=False)
    disabled = db.Column(db.Boolean, default=False)
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
        uselist=False,
    )

    rel_proposals = relationship(
        "Proposals",
        primaryjoin="Accounts.account_id==Proposals.fk_account_id",
        viewonly=True,
    )

    rel_update_feed = relationship(
        "UpdateFeed",
        primaryjoin="Accounts.account_id==UpdateFeed.fk_account_id",
        order_by="UpdateFeed.created.desc()",
        viewonly=True,
    )

    @classmethod
    def count_total_accounts(cls):
        return db.session.execute(
            select(func.count(cls.account_id))
        ).scalar_one_or_none()

    @staticmethod
    def save():
        db.session.commit()

    @classmethod
    def exists(cls, email_address) -> bool:
        """
        Returns True if email_address exists in database.
        :param email_address:
        :return:
        """
        return (
            True
            if db.session.execute(
                select(cls.account_id).filter_by(email_address=email_address).limit(1)
            ).scalar_one_or_none()
            else False
        )

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
        return (
            db.session.execute(select(cls).order_by(cls.created.desc())).scalars().all()
        )

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
                update(cls)
                .where(cls.account_id == account_id)
                .values(
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
        self.private_key = generate_private_key(generate_password(length=1))
        db.session.commit()
        return self.private_key

    def remove_private_key(self):
        self.private_key = None
        db.session.commit()

    def create_profile(self):
        from app.models.profiles import Profiles
        from app.models.display_pictures import DisplayPictures

        Profiles.signup(
            self.account_id,
            random.choice(DisplayPictures.select_all_display_picture_id()),
            self.name_or_alias,
        )

    def password_check(self, password) -> bool:
        if authenticate_password(
            password, self.password, self.salt, pepper_position="start"
        ):
            return True
        return False

    def set_new_password(self, new_password) -> None:
        self.salt = generate_salt()
        self.password = encrypt_password(
            new_password, self.salt, pepper_position="start"
        )

        db.session.commit()

    @classmethod
    def login(cls, email_address, password):
        account = cls.select_using_email_address(email_address)
        if account:
            if authenticate_password(
                password, account.password, account.salt, pepper_position="start"
            ):
                return account
        return None

    @classmethod
    def signup(
        cls,
        email_address: str,
        password: str,
        name_or_alias: str,
        confirmed: bool = False,
    ):
        """
        Written for sqlite. Returns account after commit.
        """

        from app.models.profiles import Profiles
        from app.models.display_pictures import DisplayPictures
        from .roles_membership import RolesMembership
        import random

        salt = generate_salt()
        encrypted_password = encrypt_password(password, salt, pepper_position="start")
        private_key = generate_email_validator()

        db.session.execute(
            insert(cls).values(
                email_address=email_address,
                password=encrypted_password,
                salt=salt,
                confirmed=confirmed,
                private_key=private_key,
            )
        )
        db.session.flush()

        account = cls.select_using_email_address(email_address)

        db.session.execute(
            insert(Profiles).values(
                fk_account_id=account.account_id,
                fk_display_picture_id=random.choice(
                    DisplayPictures.select_all_account_signup()
                ),
                name_or_alias=name_or_alias,
                earned_display_pictures={"earned": []},
            )
        )
        db.session.execute(
            insert(RolesMembership).values(
                fk_account_id=account.account_id,
                fk_role_id=Roles.select_by_unique_role_id(116).role_id,
            )
        )
        db.session.execute(
            insert(UpdateFeed).values(
                fk_account_id=account.account_id,
                title="Welcome to FlaskCon!",
                message="Thank you for signing up, we appreciate you joining us.",
                image="heart.gif",
                created=datetime.now(),
            )
        )
        db.session.commit()
        return account

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
            update(cls)
            .where(cls.account_id == account_id)
            .values(
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
        salt_and_pepper_password = encrypt_password(
            new_password, salt, pepper_position="start"
        )

        self.salt = salt
        self.password = salt_and_pepper_password
        self.private_key = None

        db.session.commit()

    @classmethod
    def delete(cls, account_id: int):
        db.session.execute(delete(cls).where(cls.account_id == account_id))
        db.session.commit()

    # batch actions:

    @classmethod
    def create_batch(cls, batch: list[dict], confirm_accounts: bool = False):
        """
        batch: [{"email_address": -, "password": -, "disabled": -}]
        :param batch:
        :param confirm_accounts:
        :return:
        """

        for value in batch:
            if cls.exists(value.get("email_address")):
                print(f"Account already exists: {value.get('email_address')}")
                continue

            cls.signup(
                email_address=value.get("email_address"),
                password=value.get("password", "password"),
                name_or_alias=value.get("name_or_alias"),
                confirmed=confirm_accounts,
            )

    @classmethod
    def get_account_ids_from_email_address_select_batch(
        cls, email_addresses: list[str]
    ) -> list[int]:
        return (
            db.session.execute(
                select(cls.account_id).where(cls.email_address.in_(email_addresses))
            )
            .scalars()
            .all()
        )

    @classmethod
    def generate_page_account_data(cls, account_id: int):
        account = cls.select_using_account_id(account_id)

        return {
            "account_id": account.account_id,
            "email_address": account.email_address,
            "profile": account.rel_profile[0] if account.rel_profile else None,
        }

    @classmethod
    def delete_account(cls, account_id: int):
        from app.models.profiles import Profiles
        from app.models.roles_membership import RolesMembership
        from app.models.update_feed import UpdateFeed
        from flask_imp.auth import Auth

        Profiles.delete_using_account_id(account_id)
        RolesMembership.delete_using_account_id(account_id)
        UpdateFeed.delete_using_account_id(account_id)

        db.session.execute(
            update(cls)
            .where(cls.account_id == account_id)
            .values(
                email_address="ACCOUNT DELETED",
                password="ACCOUNT DELETED",
                salt=Auth.generate_salt(),
                disabled=True,
                confirmed=False,
                private_key=None,
            )
        )

        db.session.commit()
