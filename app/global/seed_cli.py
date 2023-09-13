from flask import current_app as app


@app.cli.command("seed-test-data")
def seed_test_data():
    from app.models.accounts import Accounts
    from app.models.roles import Roles

    Accounts.create_batch(
        [
            {"email_address": "admin@sys.local", "password": "admin"},
            {"email_address": "coc_person_one@sys.local", "password": "coc_person"},
            {"email_address": "coc_person_two@sys.local", "password": "coc_person"},
            {"email_address": "reviewer_one@sys.local", "password": "reviewer_one"},
            {"email_address": "reviewer_two@sys.local", "password": "reviewer_two"},
            {"email_address": "reviewer_three@sys.local", "password": "reviewer_three"},
        ]
    )

    Roles.create_batch(
        [
            {"name": "Administrator"},
            {"name": "Code of Conduct Official"},
            {"name": "Proposal Reviewer"}
        ]
    )


@app.cli.command("seed-test-memberships")
def seed_test_memberships():
    from app.models.accounts import Accounts
    from app.models.roles import Roles
    from app.models.roles_membership import RolesMembership

    role_ids = Roles.get_id_by_name_batch(
        [
            "Administrator",
            "Code of Conduct Official",
            "Proposal Reviewer"
        ]
    )

    print(role_ids)
