import json

from flask import render_template, redirect, url_for
from pathlib import Path
from .. import bp


@bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("2023.coming_soon"))

    # staff = Path(bp.location, "staff_2023.json")
    # reviewers = Path(bp.location, "reviewers_2023.json")
    # media_partners = Path(bp.location, "media_partners_2023.json")
    #
    # return render_template(
    #     bp.tmpl("index.html"),
    #     staff=json.loads(staff.read_text()),
    #     reviewers=json.loads(reviewers.read_text()),
    #     media_partners=json.loads(media_partners.read_text())
    # )


@bp.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template(bp.tmpl("coming-soon.html"))
