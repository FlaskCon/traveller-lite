import typing as t
from getpass import getpass

import click
from flask import current_app as app

from app.models import Resources
from app.models.accounts import Accounts
from app.models.roles import Roles
from app.models.roles_membership import RolesMembership
from app.models.profiles import Profiles
from app.models.display_pictures import DisplayPictures
from app.models.talk_statuses import TalkStatuses


@app.cli.command("seed")
def seed():
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

    if TalkStatuses.__is_empty__():
        print("Creating display pictures...")
        TalkStatuses.seed(Resources.talk_statuses)
    else:
        print("Display pictures table is not empty.")

    print("creating super admin account...")
    admin_email_address, admin_password = set_admin_account()
    account = Accounts.create(
        email_address=admin_email_address,
        password=admin_password
    )

    admin_role_id = Roles.select_by_name("Super Administrator").role_id

    RolesMembership.set_roles(account.account_id, [admin_role_id])

    print("Done.", account.account_id, admin_role_id)


@app.cli.command("does-account-exist")
@click.option("--email-address", "-ea")
def does_account_exist(email_address: str):
    if email_address is None:
        ea = input("Enter email address: ")
    else:
        ea = email_address

    print(True if Accounts.exists(ea) else False)


@app.cli.command("test-sql")
def test_sql():
    pass
