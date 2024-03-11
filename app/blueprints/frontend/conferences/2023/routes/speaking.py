from flask import render_template

from .. import bp


@bp.get("/speaking-experience")
def speaking_experience():
    return render_template(bp.tmpl("speaking_experience.html"))
