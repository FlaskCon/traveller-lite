import os
import typing as t
from getpass import getpass

import click
from flask import current_app as app

from app.models import Resources
from app.models.accounts import Accounts
from app.models.conferences import Conferences
from app.models.display_pictures import DisplayPictures
from app.models.proposal_statuses import ProposalStatuses
from app.models.roles import Roles
from app.models.roles_membership import RolesMembership


@app.cli.command("seed")
def seed():
    from app.extensions import db

    with app.app_context():
        db.create_all()

    def set_admin_account(email_address: t.Optional[str] = None):
        if email_address is None:
            _email_address = input("Enter super admin email: ")
        else:
            _email_address = email_address

        if Accounts.exists(_email_address):
            print("Account already exists. Please enter another account.")
            set_admin_account()

        _password = getpass("Enter super admin password: ")
        _confirm_password = getpass("Confirm admin password: ")

        if _password != _confirm_password:
            print("Passwords do not match. Please try again.")
            set_admin_account(email_address=_email_address)

        return _email_address, _password

    if Roles.__is_empty__():
        print("Creating roles...")
        Roles.create_batch(Resources.roles)
    else:
        print("Roles table is not empty.")

    if DisplayPictures.__is_empty__():
        print("Creating display pictures...")
        DisplayPictures.seed(Resources.original_display_pictures)
    else:
        print("Display pictures table is not empty.")

    if ProposalStatuses.__is_empty__():
        print("Creating proposal statuses...")
        ProposalStatuses.seed(Resources.proposal_statuses)
    else:
        print("Proposal statuses table is not empty.")

    if Conferences.__is_empty__():
        print("Creating conferences...")
        Conferences.seed(Resources.conference)
    else:
        print("Conferences table is not empty.")

    if os.environ.get("SUPER_ADMIN_ACCOUNT", False) and os.environ.get("SUPER_ADMIN_PASSWORD", False):
        if Accounts.exists(os.environ.get("SUPER_ADMIN_ACCOUNT")):
            print("Super admin account already exists.")
            return

        account = Accounts.signup(
            email_address=os.environ.get("SUPER_ADMIN_ACCOUNT"),
            password=os.environ.get("SUPER_ADMIN_PASSWORD"),
            name_or_alias="Super Admin",
        )
    else:
        print("creating super admin account...")
        admin_email_address, admin_password = set_admin_account()
        account = Accounts.signup(
            email_address=admin_email_address,
            password=admin_password,
            name_or_alias="Super Admin",
        )

    account.confirm_account()

    admin_role_id = Roles.select_by_name("Super Administrator").role_id

    RolesMembership.set_roles(account.account_id, [admin_role_id])

    print("Super admin account created.")


@app.cli.command("does-account-exist")
@click.option("--email-address", "-ea")
def does_account_exist(email_address: str):
    if email_address is None:
        ea = input("Enter email address: ")
    else:
        ea = email_address

    print(True if Accounts.exists(ea) else False)


@app.cli.command("create-database")
def create_database():
    from app.extensions import db

    with app.app_context():
        db.create_all()


@app.cli.command("database-url")
def database_url():
    print(app.config["SQLALCHEMY_DATABASE_URI"])
