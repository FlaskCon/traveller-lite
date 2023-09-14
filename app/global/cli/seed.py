import typing as t
from getpass import getpass

import click
from flask import current_app as app

from app.models import Resources
from app.models.accounts import Accounts
from app.models.roles import Roles
from app.models.roles_membership import RolesMembership


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

    print("creating super admin account...")
    admin_email_address, admin_password = set_admin_account()
    account_id = Accounts.create(
        email_address=admin_email_address,
        password=admin_password,
        disabled=False,
    )

    admin_role_id = Roles.select_by_name("Super Administrator").role_id

    RolesMembership.set_roles(account_id, [admin_role_id])

    print("Done.", account_id, admin_role_id)


@app.cli.command("does-account-exist")
@click.option("--email-address", "-ea")
def does_account_exist(email_address: str):
    if email_address is None:
        ea = input("Enter email address: ")
    else:
        ea = email_address

    print(True if Accounts.exists(ea) else False)
