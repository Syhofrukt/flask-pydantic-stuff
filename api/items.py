from flask import request, Blueprint

items_bp = Blueprint("items_api", __name__, url_prefix="/api")


@items_bp.route("/items")
def return_math_basics():
    return "3 * 3 = 9"


@items_bp.route("/items", methods=["POST"])
def return_a_message():
    request2 = request.get_json()
    try:
        return "user said: " + request2
    except TypeError:
        raise ValueError("User message cannot be None")
