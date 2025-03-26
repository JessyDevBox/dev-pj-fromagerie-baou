# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import Garden
from app.config import ConfigEnv

bp = Blueprint("route", __name__)


@bp.route("/")
def index():
    ctx = {}
    if not ConfigEnv.is_prod:
        ctx["debug"] = {
            "isProd": ConfigEnv.is_prod,
            "platform": ConfigEnv.platform,
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
