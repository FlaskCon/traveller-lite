import os
from datetime import datetime, date
from typing import Optional, Union

from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for, g
from werkzeug.routing import BuildError

from app.extensions import vite

load_dotenv()


def load_blueprints(app: Flask):
    from app.conf_2023 import conf_2023
    from app.conf_2024 import conf_2024

    app.register_blueprint(conf_2023)
    app.register_blueprint(conf_2024)


def create_app():
    app = Flask(__name__)

    vite.init_app(app)

    load_blueprints(app)

    @app.before_request
    def before_request():
        if "f" in request.args:
            try:
                g.go_back_to = url_for(f"{request.args.get('f')}.index")
            except BuildError:
                g.go_back_to = None
        else:
            g.go_back_to = None

    @app.get("/code-of-conduct")
    def code_of_conduct():
        return render_template("code-of-conduct.html")

    @app.get("/privacy-policy")
    def privacy_policy():
        return render_template("privacy-policy.html")

    @app.get("/speaking-experience")
    def speaking_experience():
        return render_template("speaking-experience.html")

    @app.get("/become-a-sponsor")
    def become_a_sponsor():
        return render_template("become-a-sponsor.html")

    #
    # FILTERS
    #

    @app.template_filter("https")
    def replace_http_for_https(value: str) -> str:
        """
        Replace http for https in the given string.
        """
        if os.getenv("ENV") == "development":
            return value

        if isinstance(value, str):
            return value.replace("http://", "https://")

        return value

    @app.template_filter("day_month")
    def day_month(date_or_datetime: Optional[Union[datetime, date]]) -> Optional[str]:
        """
        Returns the day and month of the given date or datetime.
        """

        def day_suffix(day: int) -> str:
            if 4 <= day <= 20 or 24 <= day <= 30:
                return "th"
            else:
                return ["st", "nd", "rd"][day % 10 - 1]

        if isinstance(date_or_datetime, date) or isinstance(date_or_datetime, datetime):
            return f"{date_or_datetime.day}{day_suffix(date_or_datetime.day)} {date_or_datetime.strftime('%b')}"

        return None

    @app.template_filter("day_month_year")
    def day_month_year(date_or_datetime: Optional[Union[datetime, date]]) -> Optional[str]:
        """
        Returns the day and month of the given date or datetime.
        """

        def day_suffix(day: int) -> str:
            if 4 <= day <= 20 or 24 <= day <= 30:
                return "th"
            else:
                return ["st", "nd", "rd"][day % 10 - 1]

        if isinstance(date_or_datetime, date) or isinstance(date_or_datetime, datetime):
            return (
                f"{date_or_datetime.day}{day_suffix(date_or_datetime.day)} "
                f"{date_or_datetime.strftime('%b')} "
                f"{date_or_datetime.strftime('%Y')}"
            )

        return None

    return app
