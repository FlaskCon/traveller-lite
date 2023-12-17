from datetime import datetime

from . import *
from .roles import Roles


class RolesMembership(db.Model, MetaMixins):
    roles_membership_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(
        db.Integer, db.ForeignKey("accounts.account_id"), nullable=False
    )
    fk_role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)
    year = db.Column(db.Integer, nullable=False, default=datetime.now().year)

    rel_role = relationship(
        "Roles",
        order_by="Roles.name",
        primaryjoin="RolesMembership.fk_role_id==Roles.role_id",
        viewonly=True,
    )

    rel_account = relationship(
        "Accounts",
        order_by="Accounts.email_address",
        primaryjoin="RolesMembership.fk_account_id==Accounts.account_id",
        viewonly=True,
    )

    @classmethod
    def get_by_account_id(cls, fk_account_id: int):
        result = (
            db.session.execute(select(cls).filter_by(fk_account_id=fk_account_id))
            .scalars()
            .all()
        )
        return [
            (
                role_membership.fk_role_id,
                role_membership.rel_role.name,
                role_membership.year,
            )
            for role_membership in result
        ]

    @classmethod
    def has_roles(cls, account_id, urids: list):
        q = (
            db.session.execute(
                select(cls).where(
                    cls.fk_account_id == account_id,
                    cls.fk_role_id.in_(Roles.select_by_unique_role_ids(urids)),
                )
            )
            .scalars()
            .all()
        )
        return True if q else False

    @classmethod
    def set_roles(cls, account_id: int, role_ids: list[int]):
        current_roles = cls.get_by_account_id(account_id)

        already_has = [
            role_id
            for role_id, _, year in current_roles
            if role_id in role_ids and year == datetime.now().year
        ]
        to_add = [role_id for role_id in role_ids if role_id not in already_has]
        to_remove = [
            role_id
            for role_id, name, year in current_roles
            if role_id not in role_ids
            and name != "Super Administrator"
            and year == datetime.now().year
        ]

        db.session.execute(
            delete(cls).where(
                and_(cls.fk_account_id == account_id, cls.fk_role_id.in_(to_remove))
            )
        )

        for role_id in to_add:
            db.session.execute(
                insert(cls).values(
                    fk_account_id=account_id,
                    fk_role_id=role_id,
                )
            )

        db.session.commit()

    @classmethod
    def is_proposal_reviewer(cls, account_id: int):
        account_roles = cls.get_by_account_id(account_id)
        if "Proposal Reviewer" in [role for _, role, _ in account_roles]:
            return True
        return False

    @classmethod
    def is_administrator(cls, account_id: int):
        account_roles = cls.get_by_account_id(account_id)
        roles, year = [role for _, role, year in account_roles]
        if "Administrator" in roles:
            return True
        return False

    @classmethod
    def is_super_administrator(cls, account_id: int):
        account_roles = cls.get_by_account_id(account_id)
        roles = [role for _, role in account_roles]
        if "Super Administrator" in roles:
            return True
        return False

    @classmethod
    def delete_using_account_id(cls, account_id: int):
        db.session.execute(delete(cls).where(cls.fk_account_id == account_id))
        db.session.commit()
