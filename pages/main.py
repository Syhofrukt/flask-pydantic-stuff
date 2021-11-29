from flask import Blueprint, render_template

main_bp = Blueprint("main_template", __name__, url_prefix="/page")


@main_bp.route("/3")
def page_return1():
    return render_template("page3.html")


@main_bp.route("/4")
def page_return2():
    return render_template("page4.html")
