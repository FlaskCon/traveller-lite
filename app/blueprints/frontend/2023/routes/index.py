from flask import render_template

from .. import bp


@bp.route("/", methods=["GET"])
def index():
    talks = [
        {
            "title": "Configuring Flask-SQLAlchemy for Production Environments: Managing MultiDB Connections/Queries",
            "speaker": "Paul Asalu",
            "time": "Saturday 16th - 07:00 UTC",
        },
        {
            "title": "Building a Scalable Machine Learning API with Flask and TensorFlow",
            "speaker": "Brayan Mwanyumba",
            "time": "Saturday 16th - 08:00 UTC",
        },
        {
            "title": "Building Federated GraphQL APIs using Flask",
            "speaker": "Adarsh Divakaran",
            "time": "Saturday 16th - 09:00 UTC",
        },
        {
            "title": "Don't think about settings, use Dynaconf",
            "speaker": "Bruno Rocha",
            "time": "Saturday 16th - 10:00 UTC",
        },
        {
            "title": "How is a Request Processed in Flask?",
            "speaker": "Patrick Kennedy",
            "time": "Saturday 16th - 15:00 UTC",
        },
        {
            "title": "End-to-End Flask App Testing with Playwright",
            "speaker": "Jay Miller",
            "time": "Saturday 16th - 16:00 UTC",
        },
        {
            "title": "Optimizing VS Code for Flask",
            "speaker": "Pamela Fox",
            "time": "Saturday 16th - 17:00 UTC",
        },
        {
            "title": "Flask SocketIO Load Balancing",
            "speaker": "Valentine Sean",
            "time": "Saturday 16th - 18:00 UTC",
        },
        {
            "title": "Quart in Action: Async APIs for Model Front-Ends",
            "speaker": "Adam Englander",
            "time": "Saturday 16th - 19:00 UTC",
        },
        {
            "title": "Insights Building Sizable Flask Sites",
            "speaker": "Abdur-Rahmaan Janhangeer",
            "time": "Saturday 16th - 21:00 UTC",
        },
    ]

    return render_template(
        bp.tmpl("index.html"),
        talks=talks,
    )


@bp.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template(bp.tmpl("coming-soon.html"))
