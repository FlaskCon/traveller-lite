from flask import render_template, url_for, redirect

from . import decorator_group, bp


@decorator_group("/", methods=["GET"])
def index():
    return redirect(url_for("staff_only.system.dashboard"))
