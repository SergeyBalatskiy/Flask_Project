from flask import Blueprint, render_template

about_site_info = Blueprint("about_site", __name__)

@about_site_info.route("/about_site")
def about_site():
    return render_template("about_site.html")