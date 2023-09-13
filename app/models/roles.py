from . import *


# Roles are matched to Accounts in the RolesMembership model (roles_membership.py)

class Roles(db.Model, MetaMixins):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    @classmethod
    def get_by_id(cls, role_id):
        return db.session.execute(
            select(cls).filter_by(role_id=role_id).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def get_by_name(cls, name):
        return db.session.execute(
            select(cls).filter_by(name=name).limit(1)
        ).scalar_one_or_none()

    @classmethod
    def get_by_name_batch(cls, names: list[str]) -> dict[str, int]:
        return {name: role_id for name, role_id in [
            (row.name, row.role_id) for row in db.session.execute(
                select(cls).where(cls.name.in_(names))
            ).scalars().all()
        ]}

    @classmethod
    def get_all(cls):
        return db.session.execute(
            select(cls).order_by(cls.name)
        ).scalars().all()

    @classmethod
    def create(cls, name):
        db.session.execute(
            insert(cls).values(name=name)
        )
        db.session.commit()

    @classmethod
    def create_batch(cls, batch: list[dict]):
        for value in batch:
            db.session.execute(
                insert(cls).values(**value)
            )

        db.session.commit()
