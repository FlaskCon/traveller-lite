from flask import current_app as app

from app import DisplayPictures, Resources
from app.extensions import db


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")


@app.cli.command("syncdp")
def syncdp_command():
    udpids = [dp.unique_display_picture_id for dp in DisplayPictures.query.all()]

    for dp in Resources.original_display_pictures:
        if dp["unique_display_picture_id"] not in udpids:
            DisplayPictures.create(
                attribution=dp["attribution"],
                attribution_url=dp["attribution_url"],
                filename=dp["filename"],
                limited=dp["limited"],
                note=dp["note"],
                unique_display_picture_id=dp["unique_display_picture_id"],
            )
