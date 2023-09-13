from . import *


class Accounts(db.Model):
    account_id = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    salt = db.Column(db.String(4), nullable=False)
    disabled = db.Column(db.Boolean)

    @classmethod
    def get_by_id(cls, account_id):
        return db.session.execute(
            select(cls).filter_by(account_id=account_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def create(cls, email_address, password, disabled):
        from flask_imp.auth import Auth

        salt = Auth.generate_salt()
        salt_and_pepper_password = Auth.hash_password(password, salt)

        db.session.execute(
            insert(cls).values(
                email_address=email_address,
                password=salt_and_pepper_password,
                salt=salt,
                disabled=disabled,
            )
        )
        db.session.commit()

    @classmethod
    def update(
            cls,
            account_id: int,
            email_address: str,
            disabled: bool
    ):
        db.session.execute(
            update(cls).where(
                cls.account_id == account_id
            ).values(
                email_address=email_address,
                disabled=disabled,
            )
        )
        db.session.commit()

    @classmethod
    def reset_password(
            cls,
            account_id: int,
            new_password: str,
    ):
        from flask_imp.auth import Auth

        salt = Auth.generate_salt()
        salt_and_pepper_password = Auth.hash_password(new_password, salt)

        db.session.execute(
            update(cls).where(
                cls.account_id == account_id
            ).values(
                password=salt_and_pepper_password,
                salt=salt,
            )
        )
        db.session.commit()

    @classmethod
    def delete(cls, account_id: int):
        db.session.execute(
            delete(cls).where(
                cls.account_id == account_id
            )
        )
        db.session.commit()

    def get_roles(self):
        from .roles_membership import RolesMembership

        return RolesMembership.get_by_account_id(self.account_id)

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
                )
            )

        db.session.commit()
