from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_babel import _, gettext

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html", title=_("Accueil"))


@main_bp.route("/change_language/<language>")
def change_language(language):
    session["language"] = language
    return redirect(request.referrer or url_for("main.index"))
