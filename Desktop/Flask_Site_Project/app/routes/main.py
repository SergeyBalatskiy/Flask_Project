from flask import Blueprint, render_template

main_bp = Blueprint("main_page", __name__)


@main_bp.route("/main")
def main():
    return render_template("main.html")
