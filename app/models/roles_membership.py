from . import *


class RolesMembership(db.Model, MetaMixins):
    roles_membership_id = db.Column(db.Integer, primary_key=True)
    fk_account_id = db.Column(db.Integer, db.ForeignKey("accounts.account_id"), nullable=False)
    fk_role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"), nullable=False)

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
        result = db.session.execute(
            select(cls.fk_role_id, cls.rel_role.name).filter_by(fk_account_id=fk_account_id)
        ).scalars().all()
        return result

    @classmethod
    def set_roles(cls, account_id: int, role_ids: list[int]):
        db.session.execute(
            delete(cls).where(cls.fk_account_id == account_id)
        )

        for role_id in role_ids:
            db.session.execute(
                insert(cls).values(
                    fk_account_id=account_id,
                    fk_role_id=role_id
                )
            )

        db.session.commit()
