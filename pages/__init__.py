from flask import Blueprint, render_template
from .main import main_bp
from .other import other_bp

pages_bp = Blueprint("pages_template", __name__, url_prefix="/page")


@pages_bp.route("/1")
def page_return1():
    return render_template("page1.html")


@pages_bp.route("/2")
def page_return2():
    return render_template("page2.html")
