from flask import redirect, url_for
from datetime import datetime

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    year = datetime.now().year
    return redirect(url_for(f"www.{year}.index"))
