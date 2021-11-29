from flask import request, Blueprint
from .items import items_bp
from .user import user_bp

init_bp = Blueprint("init_api", __name__, url_prefix="/api")


@init_bp.route("/")
def return_math_basics():
    return "2 + 2 = 4"


@init_bp.route("/", methods=["POST"])
def echo_a_message():
    request2 = request.get_json()
    try:
        return request2 + ""
    except TypeError:
        raise ValueError("User message cannot be None")
