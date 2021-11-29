from flask import Blueprint, render_template

other_bp = Blueprint("other_template", __name__, url_prefix="/page")


@other_bp.route("/5")
def page_return1():
    return render_template("page5.html")


@other_bp.route("/6")
def page_return2():
    return render_template("page6.html")
