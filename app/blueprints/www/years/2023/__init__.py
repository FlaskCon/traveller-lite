from flask_imp import Blueprint

bp = Blueprint(__name__)

bp.import_resources("routes")
