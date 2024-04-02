from flask import current_app as app

from app.extensions import db


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print("Initialized the database.")

    
@app.cli.command("sync-dp")
def sync_display_picture():
    from app.models.display_pictures import DisplayPictures
    from app.models import Resources
