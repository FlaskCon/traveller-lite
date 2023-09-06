from flask import render_template

from .. import bp


@bp.get("/privacy-policy")
def privacy_policy():
    return render_template(bp.tmpl("privacy_policy.html"))
