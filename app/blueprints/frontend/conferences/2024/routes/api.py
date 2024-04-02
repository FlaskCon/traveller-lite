from flask import session

from .. import bp


@bp.route("/api/logged-in", methods=["GET"])
def is_logged_in():
    return {"logged_in": session.get("logged_in", False)}
