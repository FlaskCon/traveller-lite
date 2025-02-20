from flask import render_template

from app.models.media_partners import MediaPartners
from .. import bp, media_partners_group


@media_partners_group("/", methods=["GET"])
def index():
    media_partners = MediaPartners.select_all()
    return render_template(
        bp.tmpl("index.html"),
        media_partners=media_partners,
    )
