from flask import Blueprint, render_template, redirect, url_for

conf_2024 = Blueprint(
    "conf_2024",
    __name__,
    url_prefix="/2024",
    static_folder="static",
    template_folder="templates"
)


@conf_2024.route("/", methods=["GET"])
def index():
    return render_template("conf_2024/index.html")


@conf_2024.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template("conf_2024/coming-soon.html")


@conf_2024.get("/code-of-conduct")
def code_of_conduct():
    return redirect(url_for("code_of_conduct", f="conf_2024"))


@conf_2024.get("/privacy-policy")
def privacy_policy():
    return redirect(url_for("privacy_policy", f="conf_2024"))


@conf_2024.get("/speaking-experience")
def speaking_experience():
    return redirect(url_for("speaking_experience", f="conf_2024"))


@conf_2024.get("/become-a-sponsor")
def become_a_sponsor():
    return redirect(url_for("become_a_sponsor", f="conf_2024"))
