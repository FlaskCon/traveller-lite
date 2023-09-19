from flask import redirect, url_for
from flask_imp.security import login_check

from .. import bp


@bp.route("/", methods=["GET"])
@login_check("logged_in", True, "auth.login", message="You need to be logged to view that page")
def index():
    return redirect(url_for("account.your_account"))
