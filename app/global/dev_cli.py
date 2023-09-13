from flask import current_app as app


@app.cli.command("perm")
def perm():
    from app.models.permissions import Permissions

    Permissions.create(
        name="admin",
        description="Admin",
    )
