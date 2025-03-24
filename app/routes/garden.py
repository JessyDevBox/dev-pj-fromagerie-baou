# app/routes/main.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models import Garden

bp = Blueprint("garden", __name__)


@bp.route("/")
@login_required
def list():
    gardens = Garden.query.filter_by(user_id=current_user.id).all()
    return render_template("garden_list.html", gardens=gardens)
    # return render_template("garden.html", gardens=[])


@bp.route("/<int:garden_id>")
@login_required
def details(garden_id):
    garden = None
    gardens = Garden.query.filter_by(user_id=current_user.id, id=garden_id).all()
    if gardens:
        garden = gardens[0]
    return render_template("garden_details.html", garden=garden)
    # return render_template("garden.html", gardens=[])
