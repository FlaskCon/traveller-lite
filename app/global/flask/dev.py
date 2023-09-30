import click


def dev_cli(passed_app):
    import random
    from faker import Faker
    from flask import Flask
    from app.models import Resources
    from app.models.accounts import Accounts
    from app.models.roles import Roles
    from app.models.roles_membership import RolesMembership

    fake = Faker()
    app: Flask = passed_app

    @app.cli.command("dev-seed-test-data")
    def dev_seed_test_data():
        random_accounts = 100

        if Roles.__is_empty__():
            print("Creating roles from Resources.roles...")
            Roles.create_batch(Resources.roles)
        else:
            print("Roles already exist.")

        print("Generating {random_accounts} random accounts...")
        random_amount_of_attendees = []
        random_attendee_type = [["Attendee"], ["VIP", "Attendee"]]
        for i in range(1, random_accounts):
            roles = random.choice(random_attendee_type)
            random_amount_of_attendees.append(
                {
                    "email_address": fake.email(),
                    "name_or_alias": fake.name(),
                    "password": "password",
                    "roles": roles,
                }
            )

        defined_accounts = [
            {
                "email_address": "admin@sys.local",
                "name_or_alias": "Administrator",
                "password": "admin",
                "roles": ["Administrator"]
            },
            {
                "email_address": "cocofficial@sys.local",
                "name_or_alias": "Administrator",
                "password": "cocofficial",
                "roles": ["Code of Conduct Official"]
            },
            {
                "email_address": "reviewer@sys.local",
                "name_or_alias": "Administrator",
                "password": "reviewer",
                "roles": ["Proposal Reviewer"]
            },
            {
                "email_address": "speaker@sys.local",
                "name_or_alias": "Administrator",
                "password": "speaker",
                "roles": ["Speaker"]
            },
            {
                "email_address": "sponsor@sys.local",
                "name_or_alias": "Administrator",
                "password": "sponsor",
                "roles": ["Sponsor"]
            },
            {
                "email_address": "volunteer@sys.local",
                "name_or_alias": "Administrator",
                "password": "volunteer",
                "roles": ["Volunteer"]
            },
        ]

        Accounts.create_batch([*defined_accounts, *random_amount_of_attendees])

        for account in [*defined_accounts, *random_amount_of_attendees]:
            account_id = Accounts.select_account_id_using_email_address(account.get("email_address"))
            if account_id is None:
                raise Exception(f"Account not found: {account.get('email_address')}")

            list_of_roles = account.get("roles", [])
            role_ids: list[int] = list(Roles.select_names_batch(list_of_roles).values())
            RolesMembership.set_roles(account_id, role_ids)

    @app.cli.command("dev-show-accounts")
    def dev_show_accounts():
        from app.models.accounts import Accounts

        accounts = Accounts.select_all()

        for account in accounts:
            print(
                account.account_id,
                account.email_address,
                account.disabled,
                ", ".join([role.rel_role.name for role in account.rel_role_membership]),
                sep="\t"
            )

    @app.cli.command("get-account-roles")
    def dev_get_account_roles():
        from app.models.accounts import Accounts

        print("Class method: ", Accounts.get_roles_from_email_address_select("vipattendee@sys.local"))

        account = Accounts.select_using_email_address("vipattendee@sys.local")
        print("Instance method: ", account.get_roles_from_this())

    @app.cli.command("get-accounts-from-role")
    @click.option("--role", "-r")
    def dev_get_account_from_role(role: str):
        from app.models.roles import Roles

        this_role = role if role is not None else "Attendee"
        role_query = Roles.select_by_name(this_role)
        print(f"Role: {this_role}")
        if role_query is None:
            print("Role not found.")
            return
        print([role.rel_account.account_id for role in role_query.rel_role_membership])
