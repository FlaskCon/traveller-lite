from flask import render_template

from .. import bp


@bp.get("/about")
def about():
    return render_template(bp.tmpl("about.html"))
