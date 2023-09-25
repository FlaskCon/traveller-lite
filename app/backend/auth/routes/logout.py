from flask import (
    session,
    url_for,
    redirect
)
from app.extensions import imp

from .. import bp


@bp.route("/logout", methods=["GET"])
def logout():
    session.clear()
    imp.init_session()
    return redirect(url_for("auth.login"))
