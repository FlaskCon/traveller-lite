import functools

from flask import session
from flask_imp import Blueprint
from flask_imp.security import login_check, pass_function_check

from app.models.roles_membership import RolesMembership

bp = Blueprint(__name__)


def media_partners_group(rule, **options):
    def decorator(func):
        @functools.wraps(func)
        @bp.route(rule, **options)
        @login_check("logged_in", True, "auth.login")
        @pass_function_check(
            RolesMembership.has_roles,
            {"account_id": session, "urids": [100, 101, 102, 107, 103]},
            "account.update_feed",
            with_app_context=True,
        )
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator


bp.import_resources("routes")


@bp.before_app_request
def before_app_request():
    bp.init_session()
