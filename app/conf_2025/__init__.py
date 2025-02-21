from flask import Blueprint, render_template, redirect, url_for

conf_2025 = Blueprint(
    "conf_2025",
    __name__,
    url_prefix="/2025",
    static_folder="static",
    template_folder="templates"
)


@conf_2025.route("/", methods=["GET"])
def index():
    return redirect(url_for("conf_2025.coming_soon"))


@conf_2025.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template("conf_2025/coming-soon.html")


@conf_2025.get("/code-of-conduct")
def code_of_conduct():
    return redirect(url_for("code_of_conduct", f="conf_2025"))


@conf_2025.get("/privacy-policy")
def privacy_policy():
    return redirect(url_for("privacy_policy", f="conf_2025"))


@conf_2025.get("/speaking-experience")
def speaking_experience():
    return redirect(url_for("speaking_experience", f="conf_2025"))


@conf_2025.get("/become-a-sponsor")
def become_a_sponsor():
    return redirect(url_for("become_a_sponsor", f="conf_2025"))
