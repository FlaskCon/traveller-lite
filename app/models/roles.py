from . import *


# Roles are matched to Accounts in the RolesMembership model (roles_membership.py)


class Roles(db.Model, MetaMixins):
    role_id = db.Column(db.Integer, primary_key=True)
    unique_role_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(128), nullable=False)

    rel_role_membership = relationship(
        "RolesMembership",
        order_by="RolesMembership.fk_account_id",
        primaryjoin="Roles.role_id==RolesMembership.fk_role_id",
        viewonly=True,
    )

    @classmethod
    def select_by_unique_role_ids(cls, unique_role_ids):
        return (
            db.session.execute(
                select(cls.role_id).where(cls.unique_role_id.in_(unique_role_ids))
            )
            .scalars()
            .all()
        )

    @classmethod
    def select_by_id(cls, role_id):
        return db.session.execute(
            select(cls).filter_by(role_id=role_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_by_unique_role_id(cls, unique_role_id):
        return db.session.execute(
            select(cls).filter_by(unique_role_id=unique_role_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_by_name(cls, name):
        return db.session.execute(
            select(cls).filter_by(name=name).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def select_names_batch(cls, names: list[str]) -> dict[str, int]:
        """
        Reutrns {name: role_id, name: role_id, ...}
        """

        return {
            name: role_id
            for name, role_id in [
                (row.name, row.role_id)
                for row in db.session.execute(select(cls).where(cls.name.in_(names)))
                .scalars()
                .all()
            ]
        }

    @classmethod
    def select_all(cls):
        return db.session.execute(select(cls).order_by(cls.name)).scalars().all()

    @classmethod
    def create(cls, name):
        db.session.execute(insert(cls).values(name=name))
        db.session.commit()

    @classmethod
    def create_batch(cls, batch: list[dict]):
        for value in batch:
            db.session.execute(insert(cls).values(**value))

        db.session.commit()
