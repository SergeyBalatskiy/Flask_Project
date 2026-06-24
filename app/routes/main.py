from flask import Blueprint, render_template

main_bp = Blueprint("main_page", __name__)

@main_bp.route("/")
def main():
    return render_template("main.html")

@main_bp.route("/example_profile")
def example_profile():
    return render_template("example_profile.html")
