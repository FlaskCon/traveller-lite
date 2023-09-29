from flask import redirect, url_for
from flask_imp.security import login_check

from .. import bp


@bp.get("/")
@login_check("logged_in", True, "auth.login")
def index():
    return redirect(url_for("account.update_feed"))
