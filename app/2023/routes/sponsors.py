from flask import render_template

from .. import bp


@bp.get("/become-sponsor")
def become_sponsor():
    return render_template(bp.tmpl("become_sponsor.html"))
