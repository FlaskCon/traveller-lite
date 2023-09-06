from flask_bigapp import Blueprint

bp = Blueprint(__name__)

bp.import_resources("routes")
