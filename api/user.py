from flask import request, Blueprint, jsonify
from typing import Optional
from pydantic import BaseModel, ValidationError


user_bp = Blueprint("user_api", __name__, url_prefix="/api")


class UserBaseModel(BaseModel):
    login: str
    password: str
    items: Optional[list[str]]


@user_bp.route("/user")
def return_something():
    username = request.get_json()
    try:
        return username + " is a good person"
    except TypeError:
        return "User is a good person"


@user_bp.route("/user", methods=["POST"])
def authorization():
    request1 = request.get_json()
    if request1 is None:
        return (
            jsonify(
                {
                    "error": "Auth fields can't be None. Try using: '{'login': 'your_login', 'password': 'your_password', 'items': 'items_is_optional' }'"
                }
            ),
            401,
        )
    else:
        try:
            new_user = UserBaseModel(**request1)
            return jsonify(new_user.login, new_user.password, new_user.items)
        except ValidationError:
            return (
                jsonify(
                    {
                        "error": "Auth fields are filled incorrectly. Try using: '{'login': 'your_login', 'password': 'your_password', 'items': 'items_is_optional' }'"
                    }
                ),
                400,
            )
