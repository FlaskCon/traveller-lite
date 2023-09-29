import functools

from flask import session
from flask_imp.security import login_check, pass_function_check

from app.models.roles_membership import RolesMembership
from .. import bp


def decorator_group(rule, **options):
    def decorator(func):
        @functools.wraps(func)
        @bp.route(rule, **options)
        @login_check("logged_in", True, "auth.login")
        @pass_function_check(
            RolesMembership.is_administrator,
            {"account_id": session},
            "account.update_feed",
            with_app_context=True,
        )
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


__all__ = ["decorator_group", "bp"]
