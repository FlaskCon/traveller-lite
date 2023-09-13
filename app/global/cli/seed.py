import random

from flask import current_app as app
from app.extensions import db


@app.cli.command("seed-test-data")
def seed_test_data():
    from app.models.accounts import Accounts
    from app.models.roles import Roles
    from app.models.roles_membership import RolesMembership

    accounts = [
        {"email_address": "admin@sys.local", "password": "admin"},
        {"email_address": "coc_person_one@sys.local", "password": "coc_person"},
        {"email_address": "coc_person_two@sys.local", "password": "coc_person"},
        {"email_address": "reviewer_one@sys.local", "password": "reviewer_one"},
        {"email_address": "reviewer_two@sys.local", "password": "reviewer_two"},
        {"email_address": "reviewer_three@sys.local", "password": "reviewer_three"},
    ]

    roles = [
        {"name": "Administrator"},
        {"name": "Code of Conduct Official"},
        {"name": "Proposal Reviewer"},
        {"name": "Speaker"},
        {"name": "Sponsor"},
        {"name": "Volunteer"},
        {"name": "VIP Attendee"},
        {"name": "Attendee"},
    ]

    if Accounts.__is_empty__():
        print("Creating test accounts...")
        Accounts.create_batch(accounts)
    else:
        print("Test accounts already exist.")

    if Roles.__is_empty__():
        print("Creating test roles...")
        Roles.create_batch(roles)
    else:
        print("Test roles already exist.")

    # if RolesMembership.__is_empty__():
    print("Assigning test roles...")
    names = [x for x in map(lambda x: x["name"], roles)]
    available_roles = Roles.get_by_name_batch(names)

    print("Available roles:", available_roles)
