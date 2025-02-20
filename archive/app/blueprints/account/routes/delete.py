from flask_imp.security import login_check

from .. import bp


@bp.route("/delete", methods=["GET", "POST"])
@login_check("logged_in", True, "auth.login")
def delete():
    pass
