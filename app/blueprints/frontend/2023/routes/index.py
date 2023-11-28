import json
from pathlib import Path

from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    staff = Path(bp.location, "staff_2023.json")
    reviewers = Path(bp.location, "reviewers_2023.json")
    media_partners = Path(bp.location, "media_partners_2023.json")

    talks = [
        {
            "title": "Flask SocketIO Load Balancing",
            "speaker": "Valentine Sean"
        },
        {
            "title": "Insights Building Sizable Flask Sites",
            "speaker": "Abdur-Rahmaan Janhangeer"
        },
        {
            "title": "Building a Scalable Machine Learning API with Flask and TensorFlow",
            "speaker": "Brayan Mwanyumba"
        },
        {
            "title": "How is a Request Processed in Flask?",
            "speaker": "Patrick Kennedy"
        },
        {
            "title": "Optimizing VS Code for Flask",
            "speaker": "Pamela Fox"
        },
        {
            "title": "Building Federated GraphQL APIs using Flask",
            "speaker": "Adarsh Devamritham"
        },
        {
            "title": "Secure by Design: Building one time secret share application based on ReadOnce objects",
            "speaker": "Shahriyar Rzayev"
        },
        {
            "title": "Building Web Applications with Flask and SQLAlchemy",
            "speaker": "Aman Singh"
        },
        {
            "title": "Configuring Flask-SQLAlchemy for Production Environments: Managing MultiDB Connections/Queries",
            "speaker": "Paul Asalu"
        },
        {
            "title": "Quart in Action: Async APIs for Model Front-Ends",
            "speaker": "Adam Englander"
        },
        {
            "title": "Don't think about settings, use Dynaconf",
            "speaker": "Bruno Rocha"
        },
        {
            "title": "End-to-End Flask App Testing with Playwright",
            "speaker": "Jay Miller"
        },
    ]

    return render_template(
        bp.tmpl("index.html"),
        staff=json.loads(staff.read_text()),
        reviewers=json.loads(reviewers.read_text()),
        media_partners=json.loads(media_partners.read_text()),
        talks=talks
    )


@bp.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template(bp.tmpl("coming-soon.html"))
