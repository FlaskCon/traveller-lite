from flask import render_template

from .. import bp


@bp.get("/code-of-conduct")
def code_of_conduct():
    return render_template(bp.tmpl("code_of_conduct.html"))
