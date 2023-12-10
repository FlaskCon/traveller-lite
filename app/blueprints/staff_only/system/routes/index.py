from flask import url_for, redirect

from .. import system_group


@system_group("/", methods=["GET"])
def index():
    return redirect(url_for("staff_only.system.dashboard"))
