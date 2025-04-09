# app/routes/main.py
import urllib.parse
from flask import Blueprint, render_template
import urllib

# from flask_login import login_required, current_user

from app.config import Config

bp = Blueprint("base", __name__)


@bp.route("/")
def index():
    ctx = {}

    gmap_key = Config.GOOGLE_GMAP_KEY
    address_name = "Fromagerie du Baou"
    address = "ZA, Les Termes D908, 13124 Peypin"
    encoded_address = urllib.parse.quote(f"{address_name}, {address}")
    # google_maps_url = f"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d46304.56141799896!2d5.407556079101567!3d43.529742!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12c98da304b91259%3A0x5cb953bec8b688a3!2s{encoded_address}!5e0!3m2!1sfr!2sfr!4v1648222345678!5m2!1sfr!2sfr"
    # google map with no api
    google_maps_url = f"https://www.google.com/maps/embed/v1/place?key={gmap_key}&q={encoded_address}"
    ctx["contact"] = {
        "phone": "04 96 30 35 61",
        "address_name": address_name,
        "address": address,
        "email": "fromageriedubaou@gmail.com",
        "google_maps_url": google_maps_url,
    }
    print(google_maps_url)
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
