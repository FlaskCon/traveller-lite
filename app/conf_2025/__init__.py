from flask import Blueprint, render_template, redirect, url_for
from pyhead import Head

conf_2025 = Blueprint(
    "conf_2025",
    __name__,
    url_prefix="/2025",
    static_folder="static",
    template_folder="templates"
)


@conf_2025.route("/", methods=["GET"])
def index():
    head = Head(
        title="FlaskCon 2025",
        robots="index, follow",
        disable_detection_of_telephone_numbers=True,
        description="FlaskCon 2025",
        subject="A conference for the users of Flask.",
        rating="general",
    )
    head.set_google(
        no_sitelinks_search_box=True,
    )
    head.set_favicon(
        png_icon_16_href=url_for("static", filename="favicon-16x16.png"),
        png_icon_32_href=url_for("static", filename="favicon-32x32.png"),
        png_apple_touch_icon_120_href=url_for("static", filename="apple-touch-icon.png")
    )
    head.set_opengraph_website(
        url="https://flaskcon.com/2025",
        site_name="FlaskCon 2025",
        title="FlaskCon 2025",
        description="A conference for the users of Flask.",
        image=url_for('static', filename='2025-og-tag.jpg', _external=True, _scheme="https"),
        image_alt="FlaskCon 2025 logo",
        locale="en_US",
    )
    head.set_twitter_card(
        card="summary",
        title="FlaskCon 2025",
        description="A conference for the users of Flask.",
        image=url_for('static', filename='2025-twitter-tag.jpg', _external=True, _scheme="https"),
        image_alt="Sorted.iT logo with the slogan 'get it sorted' on top of a performance PC",
    )
    head.set_meta_tag(
        name="pinterest", content="nopin"
    )
    return render_template("conf_2025/index.html", head=head)


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
