from flask import Blueprint, render_template, redirect, url_for

conf_2023 = Blueprint(
    "conf_2023",
    __name__,
    url_prefix="/2023",
    static_folder="static",
    template_folder="templates",
)


@conf_2023.route("/", methods=["GET"])
def index():
    talks = [
        {
            "title": "Configuring Flask-SQLAlchemy for Production Environments: Managing MultiDB Connections/Queries",
            "speaker": "Paul Asalu",
            "time": "Unable to attend :(",
        },
        {
            "title": "Building a Scalable Machine Learning API with Flask and TensorFlow",
            "speaker": "Brayan Mwanyumba",
            "time": "Unable to attend :(",
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
        "conf_2023/index.html",
        talks=talks,
    )


@conf_2023.route("/coming-soon", methods=["GET"])
def coming_soon():
    return render_template("conf_2023/coming-soon.html")


@conf_2023.get("/code-of-conduct")
def code_of_conduct():
    return redirect(url_for("code_of_conduct", f="conf_2023"))


@conf_2023.get("/privacy-policy")
def privacy_policy():
    return redirect(url_for("privacy_policy", f="conf_2023"))


@conf_2023.get("/speaking-experience")
def speaking_experience():
    return redirect(url_for("speaking_experience", f="conf_2023"))


@conf_2023.get("/become-a-sponsor")
def become_a_sponsor():
    return redirect(url_for("become_a_sponsor", f="conf_2023"))
