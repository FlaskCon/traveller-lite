from flask import redirect, url_for
from flask_imp import Blueprint

bp = Blueprint(__name__)

bp.import_nested_blueprint("conferences")
bp.import_nested_blueprint("media_partners")
bp.import_nested_blueprint("proposals")
bp.import_nested_blueprint("sponsors")
bp.import_nested_blueprint("system")


@bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("auth.login"))


@bp.before_app_request
def before_app_request():
    bp.init_session()
