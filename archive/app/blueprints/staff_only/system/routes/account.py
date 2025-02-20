from flask import render_template, session, request, url_for, redirect, flash
from flask_imp.security import include_csrf

from app.models.accounts import Accounts
from app.models.roles import Roles
from app.models.roles_membership import RolesMembership
from .. import system_group, bp


@system_group("/account/<int:account_id>", methods=["GET", "POST"])
@include_csrf()
def account(account_id):
    this_account = Accounts.select_using_account_id(account_id)

    if request.method == "POST":
        account_disabled = True if request.form.get("disabled") == "true" else False

        set_roles = []
        for key, value in request.form.items():
            if key.startswith("role_"):
                if value == "true":
                    set_roles.append(int(key.split("_")[1]))

        RolesMembership.set_roles(account_id, set_roles)

        if this_account.disabled != account_disabled:
            this_account.disabled = account_disabled
            this_account.save()

        flash("Account updated.")
        return redirect(url_for("staff_only.system.account", account_id=account_id))

    account_roles = [role.fk_role_id for role in this_account.rel_roles]
    all_roles = Roles.select_all()
    all_roles_as_json = {}
    for role in all_roles:
        if role.name == "Super Administrator":
            if role.role_id not in account_roles:
                continue
        all_roles_as_json[role.name] = {
            "role_id": role.role_id,
            "has": True if role.role_id in account_roles else False,
        }

    return render_template(
        bp.tmpl("account.html"),
        this_account=this_account,
        all_roles=all_roles,
        all_roles_as_json=all_roles_as_json,
        csrf=session.get("csrf"),
    )
