# app/routes/main.py
from flask import Blueprint, render_template

# from flask_login import login_required, current_user

from app.config import Config

bp = Blueprint("base", __name__)


@bp.route("/")
def index():
    ctx = {}
    if Config.DEBUG:
        ctx["debug"] = {
            "ENV": Config.ENV,
        }
    return render_template("index.html", ctx=ctx)


# @bp.route("/garden")
# @login_required
# def garden():
#     gardens = Garden.query.filter_by(user_id=current_user.id).all()
#     return render_template("garden.html", gardens=gardens)
#     # return render_template("garden.html", gardens=[])


@bp.route("/sandbox")
def sandbox():
    return render_template("sandbox.html")
